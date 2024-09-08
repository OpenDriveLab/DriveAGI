"""
This script is used for preprocessing OpenDV-YouTube meta data, from Google sheet (as csv file) to json file.
The script is a part of the [`GenAD`](https://arxiv.org/abs/2403.09630) project.
"""

import json
import pandas as pd
import numpy as np
import argparse
from tqdm import tqdm

KEY_MAP = {
    'train / val': 'split',
    'mini / full set': 'subset',
    'nation or area (inferred by gpt)': 'area',
    'state, province, or city (inferred by gpt and refined by human)': 'state',
    'discarded length at the begininning (second)': 'start_discard',
    'discarded length at the ending (second)': 'end_discard'
}

SPECIFIC_TYPE_MAP = {
    'state': str
}

def duration2length(duration):
    """
        duration: HH:MM:SS, or MM:SS
        length: int (seconds)
    """
    duration = duration.split(":")
    length = int(duration[0]) * 60 + int(duration[1])
    if len(duration) == 3:
        length = length * 60 + int(duration[2])
    return length


def csv2json(csv_path, json_path):
    df = pd.read_csv(csv_path)
    vid_list = []
    keys = df.keys()
    for vid_id in tqdm(range(len(df["ID"]))):
        vid_info = dict()
        for key in keys:
            value = df[key][vid_id]
            assigned_key = KEY_MAP.get(key.lower(), key.lower())
            if assigned_key in SPECIFIC_TYPE_MAP:
                value = SPECIFIC_TYPE_MAP[assigned_key](value)
            if isinstance(value, np.int64):
                value = int(value)
            elif value == "nan":
                value = "N/A"
            vid_info[assigned_key] = value
            
        vid_info["length"] = duration2length(vid_info["duration"])
        vid_list.append(vid_info)
        
    with open(json_path, "w") as f:
        json.dump(vid_list, f, indent=4, ensure_ascii=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert OpenDV-YouTube meta data from csv to json')
    parser.add_argument('--csv_path', '-i', type=str, default="meta/OpenDV-YouTube.csv", help='path to the csv file')
    parser.add_argument('--json_path', '-o', type=str, default="meta/OpenDV-YouTube.json", help='path to the json file')
    args = parser.parse_args()

    csv2json(args.csv_path, args.json_path)