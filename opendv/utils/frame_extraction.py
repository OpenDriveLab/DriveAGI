"""
This script is used for preprocessing OpenDV-YouTube raw data.
The script is a part of the [`GenAD`](https://arxiv.org/abs/2403.09630) project.
"""

import os
import time
import traceback
import json

import numpy as np
import decord
import cv2
from tqdm import tqdm

from utils.download import get_video_with_meta

DECORD_ACCEPTABLE_TYPES = ['mp4']
FORCE_USE_CV2 = True

IDX_WIDTH = 9
# set [IDX_WIDTH] to [None] if you want to use the default format, i.e. zero padding to the maximal index of a video
INFO_INTERVAL = 1000
DEFAULT_FPS = 10


def extract_frames(video_info):
    video_path = video_info.get("video_path", None)
    output_dir = video_info.get("output_dir", None)
    fps = video_info.get("freq", DEFAULT_FPS)
    discard_begin = video_info.get("start_discard", 90)
    discard_end = video_info.get("end_discard", 60)
    exception_file = video_info.get("exception_file", None)
    finish_log = video_info.get("finish_log", None)

    if video_path is None or output_dir is None:
        print("skipping invalid video info...")
        return

    try:
        if (FORCE_USE_CV2) or (video_path.split('.')[-1] not in DECORD_ACCEPTABLE_TYPES):
            print("[opencv] extracting frames from video [{}]...".format(video_path))
            cv2_extract_frames(video_path, output_dir, fps, discard_begin, discard_end, exception_file)
        else:
            print("[decord] extracting frames from video [{}]...".format(video_path))
            decord_extract_frames(video_path, output_dir, fps, discard_begin, discard_end, exception_file)

        if finish_log is not None:
            with open(finish_log, "a") as f:
                f.write(video_info.get("video_id", video_path.split("/")[-1]))
                f.write("\n")
        
    except Exception as e:
        exceptions = dict()
        exceptions["video_path"] = video_path
        exceptions["problem"] = str(e)
        exceptions["action"] = "skipped"
        exceptions["details"] = traceback.format_exc()
        json.dump(exceptions, open(exception_file, "a"), indent=4)
        with open(exception_file, "a") as f:
            f.write(",\n")

        traceback.print_exc()


def count_done_frames(save_path):
    return len(os.listdir(save_path))

def special_video_setting_log(video_path, exception_file, height=None, width=None, video_reader=None):
    skipped = False

    exception = None
    if video_reader is None:
        exception = {
            "video_path": video_path,
            "problem": "video not found or corrupted",
            "action": "skipped",
            "details": "video not found or corrupted"
        }
        return True
    
    if (height is None) or (width is None):
        height = video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = video_reader.get(cv2.CAP_PROP_FRAME_WIDTH)

    if (width < 1280) and (height < 720):
        exception = {
            "video_path": video_path,
            "problem": "< 720p",
            "action": "skipped",
            "details": "{} x {}".format(width, height)
        }
        skipped = True

    elif (width / height != 16 / 9):
        exception = {
            "video_path": video_path,
            "problem": "not 16:9",
            "action": "as normal",
            "details": "{} x {}".format(width, height)
        }

    if exception is not None:
        json.dump(exception, open(exception_file, "a"), indent=4)
        with open(exception_file, "a") as f:
            f.write(",\n")
    
    return skipped


def decord_extract_frames(video_path, save_path, fps=10, discard_begin=90, discard_end=60, msg_file=None):
    start_index = 0
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    else:
        start_index = count_done_frames(save_path) -1
        # so that we could rewrite the last frame, in case the last frame is corrupted

    video = decord.VideoReader(video_path, ctx=decord.cpu(), num_threads=1)
    video_fps = video.get_avg_fps()
    num_frames = int( fps * (len(video) // video_fps - discard_begin - discard_end) )
    idx_width = len(str(num_frames)) if IDX_WIDTH is None else IDX_WIDTH
    interval = video_fps / fps

    img = video[0].asnumpy()
    frame_height, frame_width, _ = img.shape
    if special_video_setting_log(video_path,  msg_file, frame_height, frame_width):
        return
    del img
    first_log = True

    indices = np.array([ int(discard_begin * video_fps) + int(np.round(i * interval)) for i in range(num_frames)])
    start_time = time.perf_counter()
    ids = list(range(num_frames))
    for id in ids[start_index:]:
        frame = video[indices[id]].asnumpy()
        file_path = os.path.join(save_path, str(id).zfill(idx_width) + ".jpg")
        cv2.imwrite(file_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

        if (first_log) or ((id+1) % INFO_INTERVAL == 0):
            first_log = False
            elapsed_time = time.perf_counter() - start_time
            eta = elapsed_time / (id+1) * (len(indices) - id - 1)
            elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            eta = time.strftime("%H:%M:%S", time.gmtime(eta))
            progress_bar = "\u2588" * int((id+1) / len(indices) * 20) + " " * (20 - int((id+1) / len(indices) * 20))
            print("{} {}/{} Elapsed: {}\t ETA: {}".format(progress_bar, id+1, len(indices), elapsed_time, eta))


def cv2_extract_frames(video_path, save_path, fps=10, discard_begin=90, discard_end=60, msg_file=None):
    start_index = 0
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    else:
        start_index = count_done_frames(save_path) -1
        # so that we could rewrite the last frame, in case the last frame is corrupted

    video, video_fps, total_frames = get_video_with_meta(video_path, need_metas=["fps", "num_frames"])
    if video is not None:
        num_frames = int( fps * (total_frames // video_fps - discard_begin - discard_end) )
        idx_width = len(str(num_frames)) if IDX_WIDTH is None else IDX_WIDTH
        interval = video_fps / fps

    if special_video_setting_log(video_path, msg_file, video_reader=video):
        return
    first_log = True
    
    indices = np.array([ int(discard_begin * video_fps) + int(np.round(i * interval)) for i in range(num_frames)])
    start_time = time.perf_counter()
    ids = list(range(num_frames))
    for id in ids[start_index:]:
        video.set(cv2.CAP_PROP_POS_FRAMES, indices[id])
        _, frame = video.read()
        file_path = os.path.join(save_path, str(id).zfill(idx_width) + ".jpg")
        cv2.imwrite(file_path, frame)

        if (first_log) or ((id+1) % INFO_INTERVAL == 0):
            first_log = False
            elapsed_time = time.perf_counter() - start_time
            eta = elapsed_time / (id+1) * (len(indices) - id - 1)
            elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            eta = time.strftime("%H:%M:%S", time.gmtime(eta))
            progress_bar = "\u2588" * int((id+1) / len(indices) * 20) + " " * (20 - int((id+1) / len(indices) * 20))
            print("{} {}/{} Elapsed: {}\t ETA: {}".format(progress_bar, id+1, len(indices), elapsed_time, eta))