import argparse

def main():
    parser = argparse.ArgumentParser(
        description="YT-views: Execute tasks with provided video_id and api_key."
    )
    parser.add_argument(
        "--video_id",
        type=str,
        required=True,
        help="The YouTube video ID."
    )
    parser.add_argument(
        "--api_key",
        type=str,
        required=True,
        help="Your YouTube Data API key."
    )

    args = parser.parse_args()

    print(f"Video ID received: {args.video_id}")
    print(f"API Key received: {args.api_key}")

    # Place your main logic here, for example:
    # fetch_views(args.video_id, args.api_key)

if __name__ == "__main__":
    main()

#python main.py --video_id YOUR_VIDEO_ID --api_key YOUR_API_KEY
