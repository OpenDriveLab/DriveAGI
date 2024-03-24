# OpenDV-YouTube
Due to YouTube License, we could not directly offer our processed data. However, you can follow the steps below to download the raw data and process it by yourself.

## Environment Setup

Install the required packages by running the following command:

```cmd
pip install -r requirements.txt
```

## Meta Data Preparation
First, download the <a href="https://docs.google.com/spreadsheets/d/1bHWWP_VXeEe5UzIG-QgKFBdH7mNlSC4GFSJkEhFnt2I" target="_blank">OpenDV-YouTube Google Sheet</a> as a `csv` file. For default setting, you should save the file as `meta/OpenDV-YouTube.csv`. You could change it to whatever path you want as long as you change the `csv_path` in the command in the next step.

Then, run the following command to preprocess the meta data. The default value for `--csv_path` (or `-i`) and `--json_path` (or `-o`) are `meta/OpenDV-YouTube.csv` and `meta/OpenDV-YouTube.json` respectively. 

```cmd
python scripts/meta_preprocess.py -i CSV_PATH -o JSON_PATH
```

## Raw Data Download

To download the raw data from YouTube, you should first change the configures in `configs/download.json`. 

Note that the script **supports multi-threading download**, so please set the `num_workers` to a proper value according to your hardware and network condition.

Also, the `format` key in the config file **should strictly obey** the format selection rules of the `youtube-dl` package. We do not recommend changing it unless you are familiar with the package.

Now you can run the following command to download the raw video data.

```cmd
python scripts/youtube_download.py >> download_output.txt
```

The download will take about $2000/\mathrm{NUM_{WORKERS}}$ hours, also depending on your network condition. The data will take about **3TB** of disk space.

## Data Preprocessing (Video-to-Image)

When the download is finished, you can first set the configures in `configs/video2img.json` to those you expect. The script also **supports multi-threading processing**, so you can set the `num_workers` to a proper value according to your hardware condition.

Note that if you want to align with the annotations we provide, `frame_rate` **should not be changed.**

Then, you can run the following command to preprocess the raw video data.

```cmd
python scripts/video2img.py >> vid2img_output.txt
```

The preprocessing will take about $8000/\mathrm{NUM_{WORKERS}}$ hours, resulting in about **25TB** of images.

## Annotation Preparation

The full annotation data, including **commands** and **contexts** of video clips, is available at <a href="https://huggingface.co/datasets/OpenDriveLab/OpenDV-YouTube-Language" target="_blank">OpenDV-YouTube-Language</a>. The files are in `json` format, with total size of about **14GB**.

The annotation data is aligned with the structure of the preprocessed data. You can use the following code to load in annotations respectively.

```python
import json

# for train
full_annos = []
for split_id in range(10):
  split = json.load(open("10hz_YouTube_train_split{}.json".format(str(split_id)), "r"))
  full_annos.extend(split)

# for val
val_annos = json.load(open("10hz_YouTube_val.json", "r"))
```

Annotations will be loaded in `full_annos` as a list where each element contains annotations for one video clip. All elements in the list are dictionaries of the following structure.

```
{
  "cmd": <int> -- command, i.e. the command of the ego vehicle in the video clip.
  "blip": <str> -- context, i.e. the BLIP description of the center frame in the video clip.
  "folder": <str> -- the relative path from the processed OpenDV-YouTube dataset root to the image folder of the video clip.
  "first_frame": <str> -- the filename of the first frame in the clip. Note that this file is included in the video clip.
  "last_frame": <str> -- the filename of the last frame in the clip. Note that this file is included in the video clip.
}
```