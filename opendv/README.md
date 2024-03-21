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

## Data Preprocessing (Video-to-Image)

When the download is finished, you can first set the configures in `configs/video2img.json` to those you expect. The script also **supports multi-threading processing**, so you can set the `num_workers` to a proper value according to your hardware condition.

Note that if you want to align with the annotations we provide, `frame_rate` **should not be changed.**

Then, you can run the following command to preprocess the raw video data.

```cmd
python scripts/video2img.py >> vid2img_output.txt
```