import os
from .step import Step
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip

class EditVideo(Step):
    def process(self, data, inputs, utils):   # data = {[caption_file, {}], [caption_file, {}], }
        dirPath = r"C:\Users\USER\Desktop\coding_Allen_advanced\yt-concate\downloads\videos"
        clips = []
        for file in os.listdir(dirPath):
            # print(file)
            for found in data:         # found = [caption_file, {}]
                caption_file = found[0]
                if file.split(".")[0] == caption_file.split(".")[0]:
                    content = found[1]
                    start_time = float(content["start"])
                    d_time = float(content["duration"])
                    end_time = start_time + d_time
                    print(caption_file, content, start_time, end_time)

                    video = VideoFileClip(os.path.join(dirPath, file)).subclip(start_time, end_time)
                    video.reader.close()
                    video.audio.reader.close_proc()

                    clips.append(video)
                    if len(clips) >= inputs["limit"]:
                        break
        print(clips)
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile("outputs_1.mp4")

