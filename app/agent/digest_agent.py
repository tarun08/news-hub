import os
from typing import Optional
from pydantic import BaseModel
import google.genai as genai
import time


PROMPT = """You are an expert AI news analyst specializing in summarizing technical articles, research papers, and video content about artificial intelligence.
    Your role is to create concise, informative digests that help readers quickly understand the key points and significance of AI-related content.
    Guidelines:
    - Create a compelling title (5-10 words) that captures the essence of the content
    - Write a 2-3 sentence summary that highlights the main points and why they matter
    - Focus on actionable insights and implications
    - Use clear, accessible language while maintaining technical accuracy
    - Avoid marketing fluff - focus on substance
    """

class DigestOutput(BaseModel):
    title: str
    summary: str

    
class DigestAgent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set. Please configure it in .env file.")
        
        # Initialize Gemini client
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.5-flash"
        self.system_prompt = PROMPT

    def generate_digest(self, title: str, content: str, article_type: str) -> Optional[DigestOutput]:
        try:
            user_prompt = f"Create a digest for this {article_type}:\nTitle: {title}\nContent: {content[:8000]}"

            for attempt in range(3):
                try:
                    response = self.client.models.generate_content(
                        model=self.model,
                        contents=[self.system_prompt, user_prompt]
                    )
                    return DigestOutput.parse_raw(response.text)
                except Exception as e:
                    print(f"Attempt {attempt+1} failed: {e}")
                    time.sleep(2 ** attempt)  # wait 2, 4, 8 seconds


            return DigestOutput.parse_raw(response.text)
        except Exception as e:
            print(f"Error generating digest: {e}")
            return None