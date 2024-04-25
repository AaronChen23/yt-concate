from .step import Step
from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR
class DownloadVideos(Step):
    def process(self, data, inputs, utils):   # data = [[caption_file, captions], [caption_file, captions],...]
        # ===因為目前樣本數太少，所以底下兩行程式的len會相同==============
        # print(len(data))
        # file_set = set([found[0] for found in data])
        # print(len(file_set))
        # =========================================================
        file_set = set([found[0] for found in data])
        print("video to download=", len(file_set))
        for found in data:  #這裡的data不能用file_set來替代
            # print(found[0])
            # print(found[0].split(".")[0])
            # print('https://www.youtube.com/watch?v=' + found[0].split(".")[0])
            url = 'https://www.youtube.com/watch?v=' + found[0].split(".")[0]

            # ========寫不出來========================
            # if utils.video_file_exists():     #不會重複下載影片
            #     print(f"found existing video file for {url}, skipping")
            #     continue

            print("downloading", url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=found[0].split(".")[0] + ".mp4")

        return data



