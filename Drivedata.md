<div id="top">

# Open-sourced Data Ecosystem in Autonomous Driving: the Present and Future

> **This repo is all you need for Open-sourced Data Ecosystem in Autonomous Driving.** We present comprehensive paper collections, leaderboards, and challenges.

<!-- ![](https://img.shields.io/badge/Record-137-673ab7.svg)
![](https://img.shields.io/badge/License-MIT-lightgrey.svg) -->

## Table of Contents

- [Challenges and Leaderboards](#challenges-and-leaderboards)
- [Dataset Collection](#Dataset-collection)
    + [Perception](#perception)
    + [Mapping](#mapping)
    + [Prediction and Planning](#prediction-and-planning)
- [Data Engine](#Dataset-collection)
    + [Commercial Platforms](#commercial-platforms)
    + [Label Tools](#label-tools)
- [License](#license)
- [Citation](#citation)
- [Contact](#contact)


<p align="right">(<a href="#top">back to top</a>)</p>

## Challenges and Leaderboards

<table>
<capital></capital>

<tr>
    <td >Title</td>
    <td >Host</td>
    <td >Year</td>
    <td >Task</td>
    <td >Entry</td>
</tr>

<tr>
      <td rowspan=4 ><a href="https://opendrivelab.com/AD23Challenge.html" target="_blank" title="Autonomous Driving Challenge">Autonomous Driving Challenge</a></td>
  	  <td rowspan=4 > OpenDriveLab</td>
      <td rowspan=4 >CVPR2023</td>
       <td>Perception / OpenLane Topology</td>
    	<td rowspan=4> 111 </td>
</tr>
<tr>
       <td>Perception / Online HD Map Construction</td>
</tr>
<tr>
       <td>Perception / 3D Occupancy Prediction</td>
</tr>

<tr>
<td>Prediction & Planning / nuPlan Planning</td>
</tr>

<tr>
      <td rowspan=12 ><a href="https://waymo.com/open/challenges/" target="_blank" title="Waymo Open Dataset
Challenges">Waymo Open Dataset Challenges</a></td>
  	  <td rowspan=12 > Waymo</td>
      <td rowspan=4>CVPR2023</td>
       <td>Perception / 2D Video Panoptic Segmentation</td>
    	<td rowspan=4> 35 </td>
</tr>
<tr>
       <td>Perception / Pose Estimation</td>
</tr>
<tr>
       <td>Prediction / Motion Prediction</td>
</tr>

<tr>
    <td>Prediction / Sim Agents</td>
</tr>
      <td rowspan=4>CVPR2022</td>
       <td>Prediction / Motion Prediction</td>
    	<td rowspan=4> 128 </td>
</table>

<p align="right">(<a href="#top">back to top</a>)</p>

## Dataset Collection



### Perception 

<!-- 
<table>
<capital>感知类数据集：</capital>
<tr>
<th>普通表头</th>
<th align="right"><i>斜体表头而且居右</th>
<th colspan=2>表头横向合并单元格</th>
<td width="80px">限制列宽为80px超出会自动换行</td>
</tr>

<tr>
<th>左边也可以有表头</th>
<td bgcolor=#ffffcc>涂个颜色</td>
<td><mark>高亮文本</mark>但不全高亮</td>
<td><b>有时候加粗</b><i>有时候斜体</i></td>
<td width="20px">20px小于80px服从80px列宽命令无效</td>
</tr>

<tr>
<td>表头不一定是一整行或者一整列的</td>
<td rowspan=2>纵向合并单元格要注意<br>下一行少一个单元格<br>字太多必要时我会换行</td>
<td rowspan=2 colspan=2>单元格也可以从两个方向合并</td>
<td rowspan=2 width="10%">百分比和像素是可以混用的具体服从哪个取决于哪个大</td>
</tr>
<td align="left"> 简单做个居左 </td>
</tr>
</table> -->

<table>
<capital></capital>

<tr>
    <td rowspan=2 colspan=1>Dataset</td>
    <td rowspan=2 >Year</td>
    <td  align="middle" colspan=3 >Diversity</td>
    <td  align="middle" colspan=3 >Sensor</td>
    <td rowspan=2 colspan=1>Annotation</td>
    <td rowspan=2 colspan=1>Paper</td>
</tr>
<tr>
  	  <td> Scenes</td>
    	<td> Hours </td>
    	<td> Region </td>
  	  <td> Camera</td>
    	<td> Lidar </td>
    	<td> Other </td>
</tr>
<tr>
      <td><a href="https://www.cvlibs.net/datasets/kitti/" target="_blank" title="Homepage">KITTI</a></td>  	  <td> 2012</td>
    	<td> 50 </td>
    	<td> 6 </td>
  	  <td> EU</td>
    	<td> Font-view </td>
      <td> ✗</td>
    	<td> GPS&IMU </td>
      <td>2D BBox & 3D BBox</td>
      <td><a href="https://www.cvlibs.net/publications/Geiger2012CVPR.pdf" target="_blank" title="Homepage">Info</a></td>
</tr>
<tr>
      <td><a href="https://www.cityscapes-dataset.com/" target="_blank" title="Homepage">Cityscapes</a></td>  	  <td> 2016</td>
    	<td> - </td>
    	<td> - </td>
  	  <td> EU</td>
    	<td> Font-view </td>
      <td> ✗ </td>
    	<td> </td>
      <td>2D Seg</td>
      <td><a href="https://arxiv.org/abs/1604.01685" target="_blank" title="Homepage">Info</a></td>
</tr>
<tr>
<tr>
</table>




### Mapping Dataset

<table>
<capital></capital>

<tr>
    <td rowspan=2 colspan=1>Dataset</td>
    <td rowspan=2 >Year</td>
    <td  align="middle" colspan=2 >Diversity</td>
    <td  align="middle" colspan=2 >Sensor</td>
    <td  align="middle" colspan=4 >Annotation</td>
    <td rowspan=2 colspan=1>Paper</td>
</tr>
<tr>
  	  <td> Scenes</td>
    	<td> Frames </td>
  	  <td> Camera</td>
    	<td> Lidar </td>
    	<td> Type </td>
    	<td> Space </td>
    	<td> Inst. </td>
    	<td> Track </td>
</tr>
<tr>
      <td>Caltech Lanes</td>
  	  <td> 2008</td>
      <td>4</td>
    	<td> 1224/1224 </td>
    	<td>  </td>
  	  <td> ✗</td>
    	<td>  </td>
      <td>  PV  </td>
    	<td>✓</td>
      <td>x</td>
      <td><a href="https://www.cvlibs.net/datasets/kitti/" target="_blank" title="Homepage">Link</a></td>
</tr>
<tr>
</tr>

<tr>
<tr>
</table>


<p align="right">(<a href="#top">back to top</a>)</p>

## Data Engine
### Commercial Platforms

### Label Tools

<p align="right">(<a href="#top">back to top</a>)</p>

## License
Open-sourced Data Ecosystem in Autonomous Driving is released under the [MIT license](./LICENSE).

<p align="right">(<a href="#top">back to top</a>)</p>

## Citation
If you find this project useful in your research, please consider citing:
```BibTeX
@article{hongyang2023datasetsurvey,
  title={Open-sourced Data Ecosystem in Autonomous Driving: the Present and Future},
  author={Hongyang Li, Yang Li, Huijie Wang, Jia Zeng, Pinlong Cai,Dahua Lin, Junchi Yan, Feng Xu, Lu Xiong, Jingdong Wang, Futang Zhu, Kai Yan, Qian Zhang, Chunjing Xu, Tiancai Wang, Beipeng Mu, Shaoqing Ren, Zhihui Peng, Yu Qiao},
  journal = ResearchGate,
  doi={10.13140/RG.2.2.10945.74088},
  year={2023}
}
```

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact
Primary contact: `lihongyang@pjlab.org.cn`. You can also contact: `liyang@pjlab.org.cn`.

<p align="right">(<a href="#top">back to top</a>)</p>