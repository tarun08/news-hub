from app.scrapper.antropic import AnthropicScraper
from app.scrapper.openai import OpenAiScrapper
from app.scrapper.youtube import YoutubeScrapper


def run_scraper(hours: int = 24):
    youtube_scraper = YoutubeScrapper()
    openai_scraper = OpenAiScrapper()
    anthropic_scraper = AnthropicScraper()

    openai_articles = openai_scraper.scrap(hours)
    anthropic_articles = anthropic_scraper.scrap(hours)

    if openai_articles:
        article_dicts = [
            {
                "guid": a.guid,
                "title": a.title,
                "url": a.url,
                "published_at": a.published_at,
                "description": a.description,
                "category": a.category
            }
            for a in openai_articles["articles"]
        ]
    
    
    if anthropic_articles:
        article_dicts = [
            {
                "guid": a.guid,
                "title": a.title,
                "url": a.url,
                "published_at": a.published_at,
                "description": a.description,
                "category": a.category
            }
            for a in anthropic_articles["articles"]
        ]

    
    return {
        "success": bool(openai_articles or anthropic_articles),
        "openai": openai_articles,
        "anthropic": anthropic_articles,
    }
