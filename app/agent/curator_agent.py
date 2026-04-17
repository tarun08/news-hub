import os
import google.genai as genai
from typing import Optional

class CuratorAgent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set. Please configure it in .env file.")
        
        # Initialize Gemini client
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.5-pro"

        self.system_prompt = """You are a curator agent. 
        Your role is to filter, rank, and summarize raw data 
        to best answer a given query. 
        Focus on relevance, quality, and conciseness."""

    def curate(self, query: str, raw_data: list[str]) -> Optional[str]:
        """
        Curates raw data based on the query using Gemini.
        """
        combined_data = "\n".join(raw_data)

        user_prompt = f"""
        Query: {query}
        
        Data:
        {combined_data}
        
        Task: Provide only the most relevant, high-quality, and concise information.
        """

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=[self.system_prompt, user_prompt]
            )
            return response.text.strip()
        except Exception as e:
            print(f"Error generating curation: {e}")
            return None
