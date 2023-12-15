<img src="image/UoN_logo.svg" alt="UON" style="zoom: 150%;" />


# Scale Optimization Using Evolutionary Reinforcement Learning for Object Detection on Drone Imagery

### Coming Soon ...

###  [Paper]() | [🤗Demo🔥]( )   

Jialu Zhang<sup>1,3</sup>, Xiaoying Yang<sup>1</sup>, Wentao He<sup>1</sup>, Jianfeng Ren<sup>1,2</sup> (Corresponding author), Qian Zhang<sup>1,2</sup>, Yitian Zhao<sup>3</sup>, Ruibin Bai<sup>1,2</sup>, Xiangjian He<sup>1,2</sup>, Jiang Liu<sup>3,4</sup>

- <sup>1</sup>The Digital Port Technologies Lab, School of Computer Science, University of Nottingham Ningbo China
- <sup>2</sup>Nottingham Ningbo China Beacons of Excellence Research and Innovation Institute, University of Nottingham Ningbo China
- <sup>3</sup>Cixi Institute of Biomedical Engineering, Chinese Academy of Sciences
- <sup>4</sup>Department of Computer Science and Engineering, Southern University of Science and Technology


## Framework

![framework](./image/framework.png)

## Abstract

Object detection in aerial imagery presents a significant challenge due to large scale variations among objects. This paper proposes an evolutionary reinforcement learning agent, integrated within a coarse-to-fine object detection framework, to optimize the scale for more effective detection of objects in such images. Specifically, a set of patches potentially containing objects are first generated. A set of rewards measuring the localization accuracy, the accuracy of predicted labels, and the scale consistency among nearby patches are designed in the agent to guide the scale optimization. The proposed scale-consistency reward ensures similar scales for neighboring objects of the same category. 
Furthermore, a spatial-semantic attention mechanism is designed to exploit the spatial semantic relations between patches. The agent employs the proximal policy optimization strategy in conjunction with the evolutionary strategy, effectively utilizing both the current patch status and historical experience embedded in the agent.  The proposed model is compared with state-of-the-art methods on two benchmark datasets for object detection on drone imagery. It significantly outperforms all the compared methods. 

## Results

![visual1](./image/visual1.png)

![visual2](./image/visual2.png)



UAVDT dataset

| Method                         | AP       | AP50     | AP75     |
| ------------------------------ | -------- | -------- | -------- |
| Faster R-CNN (TPAMI, 2017)     | 12.1     | 23.5     | 10.8     |
| ClusDet (ICCV, 2019)           | 13.7     | 26.5     | 12.5     |
| DMNet (CVPR Workshop, 2020)    | 14.7     | 24.6     | 16.3     |
| GLSAN (TIP, 2021)              | 17.0     | 28.1     | 18.8     |
| AdaZoom (TMM, 2022)            | 20.1     | 34.5     | 21.5     |
| Zoom&Reasoning Det (SPL, 2022) | 21.8     | 34.9     | 24.8     |
| UFPMP-Det (AAAI, 2022)         | 24.6     | 38.7     | 28.0     |
| **Proposed Method**            | **28.0** | **43.8** | **31.5** |

VisDrone dataset

| Method                          | AP       | AP50     | AP75     |
| ------------------------------- | -------- | -------- | -------- |
| Faster R-CNN (TPAMI, 2017)      | 21.8     | 41.8     | 20.1     |
| SAIC-FPN (Neurocomputing, 2019) | 35.7     | 62.3     | 35.1     |
| ClusDet (ICCV, 2019)            | 32.4     | 56.2     | 31.6     |
| DMNet (CVPR Workshop, 2020)     | 29.4     | 49.3     | 30.6     |
| GLSAN (TIP, 2021)               | 32.5     | 55.8     | 33.0     |
| HRDNet (ICME, 2021)             | 35.5     | 62.0     | 35.1     |
| Zoom&Reasoning Det (SPL, 2022)  | 39.0     | 66.5     | 39.7     |
| UFPMP-Det (AAAI, 2022)          | 39.2     | 65.3     | 40.2     |
| UFPMP-Det+MS (AAAI, 2022)       | 40.1     | 66.8     | 41.3     |
| AdaZoom (TMM, 2022)             | 40.3     | **66.9** | 41.8     |
| **Proposed Method**             | **42.2** | 66.0     | **44.5** |
