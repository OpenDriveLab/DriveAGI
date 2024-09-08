"""
This script is used for preprocessing OpenDV-YouTube meta data, from raw video files to image files.
The script is a part of the [`GenAD`](https://arxiv.org/abs/2403.09630) project.
"""

import json
import os, sys
import time
import argparse
from multiprocessing import Pool

from tqdm import tqdm

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from utils.easydict import EasyDict
from utils.frame_extraction import extract_frames
from utils.download import POSSIBLE_EXTS, youtuber_formatize, get_mini_opendv


def collect_unfinished_videos(config, mini=False):
    configs = EasyDict(json.load(open(config, "r")))
    root = {
        "train": configs.train_img_root,
        "val": configs.val_img_root
    }

    meta_infos = json.load(open(configs.meta_info, "r"))
    if mini:
        meta_infos = get_mini_opendv(meta_infos)
    if os.path.exists(configs.finish_log):
        finish_log = set(open(configs.finish_log, "r").readlines())
        finish_log = {x.strip() for x in finish_log}
    else:
        finish_log = set()
    
    unfinished_videos = []
    print("collecting unfinished videos...")
    for video_meta in tqdm(meta_infos):
        if video_meta["videoid"] in finish_log:
            continue
        if video_meta["split"] == "Train":
            continue
        video_path = os.path.join(configs.video_root, youtuber_formatize(video_meta["youtuber"]), video_meta['videoid'])
        for ext in POSSIBLE_EXTS:
            if os.path.exists(f"{video_path}.{ext}"):
                break
        if not os.path.exists(f"{video_path}.{ext}"):
            raise ValueError(f"Video {video_meta['videoid']} not found. maybe something wrong in the download process?")
        
        video_info = {
            "video_id": video_meta["videoid"],
            "video_path": f"{video_path}.{ext}",
            "output_dir": os.path.join(root[video_meta["split"].lower()], youtuber_formatize(video_meta["youtuber"]), video_meta['videoid']),
            "freq": configs.frame_rate,
            "start_discard": video_meta["start_discard"],
            "end_discard": video_meta["end_discard"],
            "exception_file": configs.exception_file,
            "finish_log": configs.finish_log
        }
        unfinished_videos.append(video_info)

    return unfinished_videos, EasyDict(configs)


def convert_multiprocess(video_lists, configs):
    video_count = len(video_lists)    
    with Pool(configs.num_workers) as p:
        current_time = time.perf_counter()
        for _ in tqdm(p.imap(extract_frames, video_lists), total=video_count):
            pass
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='configs/video2img.json')
    parser.add_argument('--mini', action='store_true', default=False, help='Convert mini dataset only.')
    # parser.add_argument('--start_id', type=int, default=0)
    # parser.add_argument('--end_id', type=int, default=-1)
    # parser.add_argument('--test_video', type=str, default=None)

    args = parser.parse_args()
    video_lists, meta_configs = collect_unfinished_videos(args.config, args.mini)
    
    # if args.end_id == -1:
    #     args.end_id = len(video_lists)
    # video_lists = video_lists[args.start_id:args.end_id]
    # if args.test_video is not None:
    #     convert_multiprocess([{**video_lists[0], "video_path": args.test_video}], meta_config)
    #     exit(0)

    convert_multiprocess(video_lists, meta_configs)