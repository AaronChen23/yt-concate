from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"

def main():
    inputs = {
        "channel_id" : CHANNEL_ID
    }
    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)

#=====底下這樣寫不好。可以寫一個清單，把底下的class裝起來==================
# g = GetVideoList()
# g.process()
# d = DownCaption()
# d.process()
# d = DownloadVideo()
# d.process()

if __name__ == "__main__":
    main()

# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(video_list))