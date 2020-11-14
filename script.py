import pprint
from Bot import YouTubeBot

downloaded_videos = YouTubeBot('reddit videos', 2)
pprint.pprint(downloaded_videos)