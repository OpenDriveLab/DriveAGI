# DriveAGI
This is **"The One"** project that [**`OpenDriveLab`**](https://opendrivelab.com/) is committed to contribute to the community, providing some thought and general picture of how to embrace `foundation models` into autonomous driving.

## At A Glance

Here are some key components to construct a large foundation model curated for an autonomous system.

![overview](assets/overview.png "overview")

## DriveData


With the continuous maturation and application of autonomous driving technology, a systematic examination of open-source autonomous driving datasets becomes instrumental in fostering the robust evolution of the industry ecosystem. In this survey, we provide a comprehensive analysis of more than 70 papers on the timeline, impact, challenges, and future trends in autonomous driving dataset. More details can be found in our [Autonomous Driving Datasets Survey Page](./Drivedata.md).

> **Open-sourced Data Ecosystem in Autonomous Driving: the Present and Future**
> - [Research Gate](https://www.researchgate.net/publication/375331218_Open-sourced_Data_Ecosystem_in_Autonomous_Driving_the_Present_and_Future?channel=doi)
> - [PDF version](https://opendrivelab.com/Dataset_Survey_Chinese.pdf)
>
> ```bib
> @article{li2023datasetsurvey,
>   title={Open-sourced Data Ecosystem in Autonomous Driving: the Present and Future},
>   author={Hongyang Li, Yang Li, Huijie Wang, Jia Zeng, Pinlong Cai, Dahua Lin, Junchi Yan, Feng Xu, Lu Xiong, Jingdong Wang, Futang Zhu, Kai Yan, Chunjing Xu, Tiancai Wang, Beipeng Mu, Shaoqing Ren, Zhihui Peng, Yu Qiao},
>   doi={10.13140/RG.2.2.10945.74088},
>   year={2023}
> }
> ```
<!-- > [Hongyang Li](https://lihongyang.info/)<sup>1</sup>, Yang Li<sup>1</sup>, [Huijie Wang](https://faikit.github.io/)<sup>1</sup>, [Jia Zeng](https://scholar.google.com/citations?user=kYrUfMoAAAAJ)<sup>1</sup>, Pinlong Cai<sup>1</sup>, Dahua Lin<sup>1</sup>, Junchi Yan<sup>2</sup>, Feng Xu<sup>3</sup>, Lu Xiong<sup>4</sup>, Jingdong Wang<sup>5</sup>, Futang Zhu<sup>6</sup>, Kai Yan<sup>7</sup>, Chunjing Xu<sup>8</sup>, Tiancai Wang<sup>9</sup>, Beipeng Mu<sup>10</sup>, Shaoqing Ren<sup>11</sup>, Zhihui Peng<sup>12</sup>, Yu Qiao<sup>1</sup>
> 
> <sup>1</sup> Shanghai AI Lab, <sup>2</sup> Shanghai Jiao Tong University, <sup>3</sup> Fudan University, <sup>4</sup> Tongji University, <sup>5</sup> Baidu, <sup>6</sup> BYD, <sup>7</sup> Changan, <sup>8</sup> Huawei, <sup>9</sup> Megvii Technology, <sup>10</sup> Meituan, <sup>11</sup> Nio Automotive, <sup>12</sup> Agibot
> -->

![overview](assets/Drivedata_overview.jpg "Drivedata_overview")
>Current autonomous driving datasets can broadly be categorized into two generations since the 2010s. We define the Impact (y-axis) of a dataset based on sensor configuration, input modality, task category, data scale, ecosystem, etc.


![overview](assets/Drivedata_timeline.jpg "Drivedata_timeline")

---
Below we would like to share the latest update from our team on the **`DriveData`** side. We will release the detail of the **`DriveEngine`** and the **`DriveAGI`** in the future.

## DriveLM
Introducing the First benchmark on **Language Prompt for Driving**.

**Quick facts:**
- Task: given the language prompts as input, predict the trajectory in the scene
- Origin dataset: `nuScenes`
- Repo: https://github.com/OpenDriveLab/DriveLM

## OpenScene
The Largest up-to-date **3D Occupancy Forecasting** dataset for visual pre-training.

**Quick facts:**
- Task: given the large amount of data, predict the 3D occupancy in the environment. 
- Origin dataset: `nuPlan`
- Repo: https://github.com/OpenDriveLab/OpenScene
- Related work: [OccNet](https://github.com/OpenDriveLab/OccNet), [3D Occupancy Prediction Challenge 2023](https://opendrivelab.com/AD23Challenge.html#Track3) 

## OpenLane-V2 Update
Flourishing [OpenLane-V2](https://github.com/OpenDriveLab/OpenLane-V2) with **Standard Definition (SD) Map and Scene Elements**.

**Quick facts:**
- Task: given SD-map (also known as ADAS map) and scene elements as input, build the driving scene on the fly _without_ aid of HD-map. 
- Repo: https://github.com/OpenDriveLab/OpenLane-V2
- Related work: [TopoNet](https://github.com/OpenDriveLab/TopoNet), [Lane Topology Challenge 2023](https://opendrivelab.com/AD23Challenge.html#openlane_topology) 

