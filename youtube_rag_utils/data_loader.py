# utils/data_loader.py

from googleapiclient.discovery import build
import pandas as pd
from pathlib import Path

def get_youtube_service(api_key):
    return build("youtube", "v3", developerKey=api_key)

def fetch_video_metadata(youtube, query, max_results=25):
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results
    )
    response = request.execute()

    videos = []
    for item in response["items"]:
        snippet = item["snippet"]
        video_id = item["id"]["videoId"]
        videos.append({
            "video_id": video_id,
            "title": snippet["title"],
            "description": snippet["description"],
            "published_at": snippet["publishedAt"],
            "thumbnail_url": snippet["thumbnails"]["high"]["url"],
            "channel_title": snippet["channelTitle"],
            "video_url": f"https://www.youtube.com/watch?v={video_id}"
        })

    return pd.DataFrame(videos)

def save_metadata_to_csv(df, save_path="data/videos.csv"):
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"✅ Saved {len(df)} videos to {save_path}")
