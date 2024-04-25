from .step import Step
from yt_concate.model.found import Found
from pprint import pprint
class Search(Step):
    def process(self, data, inputs, utils):
        found = []
        search_word = inputs["search_word"]
        for caption_file in data:           # caption_file = xxxxxx.txt  # data = {caption_file: [],...}
            captions = data[caption_file]   #captions = []
            for caption in captions:        #caption = {}
                # print(caption)
                # print(type(caption))
                if search_word in caption:
                    # print(caption_file, "found word")
                    f = [caption_file, captions]
                    # print(f)
                    found.append(f)
        print(found)
        print(len(found))
        return found


# ================pytube下載字幕(影片老師用的)===================================================================================================
#         found = []
#         for yt in data:
#             captions = yt.captions    #yt.captions為一個字典{caption: time} #yt.captions為一個list[{}, {}, {}...]
#             for caption in captions:  #caption={}
#                 if search_word in caption.value():
                    # time = caption["start"]
                    # text = caption["text"]
                    # f = Found(yt, text, time)  #instance
                    # found.append((yt, text, time))    #因為每次執行append只能append一個東西，所以用()tuple
                    # found.append(caption)     # found=[{}, {}, {}...]
#================pytube下載字幕(影片老師用的)===================================================================================================