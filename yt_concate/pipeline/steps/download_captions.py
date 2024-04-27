import os
# import yt_dlp
import json
from youtube_transcript_api import YouTubeTranscriptApi
from .step import Step
from .step import StepException
import time
class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        # ydl_opts = {
        #     'writesubtitles': True,
        #     'writeautomaticsub': True,
        #     'skip_download': True,
        #     'subtitleslangs': ['en'],
        # }
        start = time.time()
        for url in data:   #data = video_links
            print("downloading caption for", url)
            if utils.caption_file_exists(url):
                print("found existing caption file")
                continue
            try:
                # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                #     ydl.download([url])
                # srt = YouTubeTranscriptApi.get_transcript("SW14tOda_kI")
                id = url.split("watch?v=")[-1]
                # print(id)
                srt = YouTubeTranscriptApi.get_transcript(id)  #這裡的srt為list
                # prints the result
                print(srt)
                text = []
                for i in srt:  # i ={}, dict # srt = [{}, {}, ...]
                    print(i)
                    print(type(i))
            except (KeyError, AttributeError):
                print("Error when downloading caption for", url)
                continue

            # source = YoutubeDL(url)
            # en_caption = source.captions.get_by_language_code('a.en')
            # en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            # print(en_caption_convert_to_srt)

            # # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_filepath(url), "w", encoding="utf-8")
            # with open("subtitles.txt", "w") as f:
            # srt_str = ",".join(str(element) for element in srt)
            # text_file.write(str(srt))     #.write()只能對str作用
            text_file.write(json.dumps(srt))
            # for i in srt:
            #     text_file.write(json.dumps(i))
                # text_file.write(i["start"])
                # text_file.write(i["duration"])

                # text_file.write("{}\n".format(i))
            # for i in srt:
            #     f.write("{}\n".format(i))
            text_file.close()
            # break
        end = time.time()
        print("took", end - start, "second")
        # return srt
