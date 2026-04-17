from datetime import datetime, timezone, timedelta
from typing import Optional

import feedparser
from pydantic import BaseModel


class OpenAiArticle( BaseModel):
    title: str
    description: str
    url: str
    guid: str
    published_at: datetime
    category: Optional[str] = None
    
class OpenAiScrapper():
    def __init__(self):
        pass


    def _fetch_recent_articles(self, tillHoursAgo):
        # OpenAI blog RSS feed
        url = "https://openai.com/blog/rss.xml"
        feed = feedparser.parse(url)

        # Calculate cutoff time (2 hours ago)
        cutoff = datetime.now(timezone.utc) - timedelta(hours=tillHoursAgo)

        articles = []

        print(f"\nChecking for articles published after {cutoff}...\n")

        for entry in feed.entries:

            published_parsed = getattr(entry, "published_parsed", None)
            if not published_parsed:
                continue

            # Convert published time to datetime
            published_time = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)

            if published_time > cutoff:
                print(entry.get("title", ""))
                articles.append(OpenAiArticle(
                    title=entry.get("title", ""),
                    description=entry.get("description", ""),
                    url=entry.get("link", ""),
                    guid=entry.get("id", entry.get("link", "")),
                    published_at=published_time,
                    category=entry.get("tags", [{}])[0].get("term") if entry.get("tags") else None
                ))

            return articles


    def scrap(self, tillHoursAgo: int = 24):
        return {
            "articles": self._fetch_recent_articles(tillHoursAgo),
        }
