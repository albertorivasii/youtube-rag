import os
import sys
from youtube_rag_utils.data_loader import *
from dotenv import load_dotenv

	
load_dotenv()  # Load environment variables from .env file

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")  # Recommended: store your key in an .env file

def main(query, max_results):
	if not YOUTUBE_API_KEY:
		raise ValueError("Please set the YOUTUBE_API_KEY environment variable.")
	youtube = get_youtube_service(YOUTUBE_API_KEY)
	df = fetch_video_metadata(youtube, query, max_results)
	save_metadata_to_csv(df, save_path="data/metadata.csv")

if __name__ == "__main__":
	query= sys.argv[1]
	max_results= sys.argv[2]
	main()

