from .step import Step
from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR
class DownloadVideos(Step):
    def process(self, data, inputs, utils):   # caption_file = xxxxxx.json  # data = {[caption_file, {}], [caption_file, {}], }
        # ===移除重複的檔名==========================================
        # print(len(data))
        # file_set = set([found[0] for found in data])   # found = [caption_file, {}]
        # print(len(file_set))
        # =========================================================
        file_set = set([found[0] for found in data])     # found = [caption_file, {}]
        print("video to download=", len(file_set))
        for found in file_set:      # found = caption_file = xxxxxx.json
            # print(found)
            url = 'https://www.youtube.com/watch?v=' + found.split(".")[0]
        #     # ========寫不出來========================
        #     # if utils.video_file_exists():     #不會重複下載影片
        #     #     print(f"found existing video file for {url}, skipping")
        #     #     continue
        #
            print("downloading", url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=found.split(".")[0] + ".mp4")

        return data   # data = {[caption_file, {}], [caption_file, {}], }



