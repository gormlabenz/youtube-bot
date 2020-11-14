from pprint import pprint
from youtube_search import YoutubeSearch
import json
from pytube import YouTube

class YouTubeBot:
    def __init__(self, search_term, max_results=None):
        self.max_results = max_results
        self.search_term = search_term
        self.search_results = self.search()
        self.downloaded_videos = self.download()

    def search(self):
        search_results = YoutubeSearch(self.search_term, max_results=self.max_results).to_dict()
        self.save_search(search_results)
        return search_results

    def save_search(self, search_results):
        with open("youtube_search.json", "r") as json_file:
            data = json.load(json_file)

        [search_results.remove(result) for result in search_results if result in data]

        data.append(search_results)

        with open("youtube_search.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    def download(self):
        downloaded_videos = []
        for result in self.search_results:
            url = f"""https://youtube.com{result['url_suffix']}"""
            YouTube(url).streams.first().download(output_path='./videos')
            print(f"""donwloaded: {result['title']}""")
        return downloaded_videos
