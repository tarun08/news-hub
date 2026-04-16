
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

class YoutubeScrapper():
    def __init__(self):
        pass
        
    def scrap(self, video_id):
        return  {
            "info" : self.get_video_info(video_id),
            "transcript": self.get_video_transcript(video_id)
        }
    
    def _get_video_info(video_id):
        """Fetch video title and description using pytube."""
        url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(url)
        return {
            "title": yt.title,
            "description": yt.description,
            "channel": yt.author,
            "publish_date": yt.publish_date
        }
    
    def _get_video_transcript(video_id):
        """Fetch transcript if available using youtube-transcript-api."""
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_text = " ".join([entry["text"] for entry in transcript])
            return transcript_text
        except Exception as e:
            return f"No transcript available: {e}"