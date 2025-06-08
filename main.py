import argparse
import requests

def get_video_stats(video_id, api_key):
    url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            stats = data['items'][0]['statistics']
            return {
                "viewCount": stats.get("viewCount"),
                "likeCount": stats.get("likeCount"),
                "favoriteCount": stats.get("favoriteCount"),
                "commentCount": stats.get("commentCount")
            }
        else:
            print("No data found for this video.")
            return None
    else:
        print(f'Error {response.status_code}: {response.text}')
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch YouTube video statistics.")
    parser.add_argument("video_id", type=str, help="YouTube video ID")
    parser.add_argument("api_key", type=str, help="YouTube API key")

    args = parser.parse_args()

    stats = get_video_stats(args.video_id, args.api_key)
    if stats is not None:
        print(f"View count: {stats['viewCount']}")
        print(f"Like count: {stats['likeCount']}")
        print(f"Favorite count: {stats['favoriteCount']}")
        print(f"Comment count: {stats['commentCount']}")



#python main.py --video_id YOUR_VIDEO_ID --api_key YOUR_API_KEY
