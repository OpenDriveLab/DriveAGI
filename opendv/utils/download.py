import os
import cv2

POSSIBLE_EXTS = ["mp4", "webm", "mkv"]

def youtuber_formatize(youtuber):
    return youtuber.replace(" ", "_")


def get_video_with_meta(video_path, need_metas=["fps", "duration", "num_frames"]):
    if not os.path.exists(video_path):
        video = None
        fps = -1
        duration = -1
        num_frames = -1
    else:
        try:
            video = cv2.VideoCapture(video_path)
            fps = video.get(cv2.CAP_PROP_FPS)
            if fps == 0:
                cmd = "ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries stream=r_frame_rate {}".format(video_path)
                precise_fps = os.popen(cmd).read().split("/")
                fps = float(precise_fps[0]) / float(precise_fps[1])
                if ("num_frames" in need_metas) or ("duration" in need_metas):
                    cmd = "ffprobe -show_entries format=duration -v quiet -of csv=\"p=0\" {}".format(video_path)
                    precise_duration = os.popen(cmd).read()
                    duration = int(float(precise_duration))
                if "num_frames" in need_metas:
                    num_frames = int(duration * fps)
            else:
                if "num_frames" in need_metas:
                    num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
                if "duration" in need_metas:
                    duration = video.get(cv2.CAP_PROP_FRAME_COUNT) / fps            
                    
        except Exception as e:
            print("Error: ", e)
            video = None
            fps = -1
            duration = -1
            num_frames = -1
        
    return_params = (video,)
    if "fps" in need_metas:
        return_params += (fps,)
    if "duration" in need_metas:
        return_params += (duration,)
    if "num_frames" in need_metas:
        return_params += (num_frames,)

    return return_params

def get_mini_opendv(full_video_list):
    mini_list = []
    for vid_info in full_video_list:
        if vid_info["subset"] != "Mini":
            continue
        mini_list.append(vid_info)

    return mini_list