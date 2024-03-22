"""
This script is used for downloading OpenDV-YouTube raw data.
The script is a part of the [`GenAD`](https://arxiv.org/abs/2403.09630) project.
"""

from multiprocessing import Pool
from tqdm import tqdm
import os, sys
import time
import json

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from utils.easydict import EasyDict
from utils.download import youtuber_formatize, POSSIBLE_EXTS

DEFAULT_FORMAT_SELECTION = 'bestvideo[height>=720,height<=1080]/best[height>=720,height<=1080]/bestvideo[height>=720]/best[height>=720]'
CONFIGS = dict()

def single_download(vid_info):
    url = vid_info["link"]
    filename = vid_info["videoid"]
    folder = youtuber_formatize(vid_info["youtuber"])
    path = os.path.join(CONFIGS.root, folder)

    for ext in POSSIBLE_EXTS:
        if os.path.exists(f"{path}/{filename}.{ext}"):
            print(f"Video {filename} already exists in {path}. Skipping...")
            return
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    os.system(f"youtube-dl -f '{CONFIGS.format}' -o '{path}/{filename}.%(ext)s' {url}")
    

def multiple_download(video_list, configs):
    global CONFIGS

    video_count = len(video_list)
    CONFIGS["format"] = configs.get("format", DEFAULT_FORMAT_SELECTION)
    CONFIGS["root"] = configs.root
    CONFIGS = EasyDict(configs)
    finished = 0
    with Pool(configs.num_workers) as p:
        current_time = time.perf_counter()
        for _ in tqdm(p.imap(single_download, video_list), total=video_count):
            finished += 1
            working_time = time.perf_counter() - current_time
            eta = working_time / finished * (video_count - finished)
            eta = time.strftime("%H:%M:%S", time.gmtime(eta))
            print("Finished {}/{} videos. ETA: {}.".format(finished, video_count, eta))


def check_status(video_list, configs):
    if "exception_file" not in configs:
        print("No exception file specified. Skipping...")
        return

    print("Checking download status...")
    with open(configs.exception_file, "w") as f:
        f.write("Checking download status...\n")
    for vid_info in tqdm(video_list):
        exists = False
        path = os.path.join(configs.root, youtuber_formatize(vid_info["youtuber"]))
        for ext in POSSIBLE_EXTS:
            if os.path.exists("{}/{}.{}".format(path, vid_info["videoid"], ext)):
                exists = True
                break
        if not exists:
            with open(configs.exception_file, "a") as f:
                f.write(f"Video [{vid_info['videoid']}] not found in [{path}].\n")

    with open(configs.exception_file, "a") as f:
        f.write("\nChecking download status finished.")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/download.json", help="Path to the config file. should be a `json` file.")
    args = parser.parse_args()
    
    configs = EasyDict(json.load(open(args.config, "r")))
    video_list = json.load(open(configs.pop("video_list"), "r"))
    if not os.path.exists(configs.root):
        os.makedirs(configs.root, exist_ok=True)

    multiple_download(video_list, configs)
    check_status(video_list, configs)