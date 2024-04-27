import os
from pprint import pprint
from .step import Step
from yt_concate.settings import CAPTIONS_DIR
import json

class ReadCaption(Step):
    def process(self, data, inputs, utils):
# ================youtube_transcript_api下載字幕(資料為list):自己寫的===========================================================================
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):     # caption_file = xxxxxx.txt
        #     captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), "r") as f:   # caption_file = xxxxxx.txt
                # text = []
                text = f.read()
                print(text)
                print(type(text))
                print(json.loads(text))
                print(type(json.loads(text)))
                lines = json.loads(text)
                data[caption_file] = lines
                # for line in lines:  # lines = [{}, {}, ...]  # line={}
                #     data[caption_file] = line

            #         text.append(line.strip())        # text=[{},{}...]
            # data[caption_file] = text
# ===========================================================================================================================================
        pprint(data)  # data = {caption_file:{}, caption_file:{}, caption_file:{}, ...}
        # print(type(data))
        # print(text)
        # print(type(text))
        return data

# #================pytube下載字幕(影片老師用的)===================================================================================================
#             captions = {}
#             with open(yt.caption_filepath, "r") as f:
#                 time_line = False
#                 time = None
#                 caption = None
#                 for line in f:
#                     line = line.strip()     #.strip()-->去除首尾空格
#                     if "-->" in line:
#                         time_line = True
#                         time = line
#                         continue
#                     if time_line:
#                         caption = line
#                         captions[caption] = time   #captions{}字典裡的內容為{caption: time}
#                         time_line = False
#             yt.captions = captions                 #修改後的字典,回傳到yt的captions
# #=========================================================================================================================================

