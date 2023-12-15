<img src="image/UoN_logo.svg" alt="UON" style="zoom: 150%;" />



# Scale Optimization Using Evolutionary Reinforcement Learning for Object Detection on Drone Imagery

### Coming Soon ...

###  [Paper]() | [🤗Demo🔥]( )   

Jialu Zhang<sup>1,3</sup>, Xiaoying Yang<sup>1</sup>, Wentao He<sup>1</sup>, Jianfeng Ren<sup>1,2</sup> (Corresponding author), Qian Zhang<sup>1,2</sup>, Yitian Zhao<sup>3</sup>, Ruibin Bai<sup>1,2</sup>, Xiangjian He<sup>1,2</sup>, Jiang Liu<sup>3,4</sup>

- <sup>1</sup>The Digital Port Technologies Lab, School of Computer Science, University of Nottingham Ningbo China
- <sup>2</sup>Nottingham Ningbo China Beacons of Excellence Research and Innovation Institute, University of Nottingham Ningbo China
- <sup>3</sup>Cixi Institute of Biomedical Engineering, Chinese Academy of Sciences
- <sup>4</sup>Department of Computer Science and Engineering, Southern University of Science and Technology

Emails:

- {sgxjz1, scxxy1, scxwh1, jianfeng.ren, qian.zhang, ruibin.bai, sean.he}@nottingham.edu.cn
- yitian.zhao@nimte.ac.cn
- liuj@sustech.edu.cn

### ![framework](./image/framework.png)

Abstract

Object detection in aerial imagery presents a significant challenge due to large scale variations among objects. This paper proposes an evolutionary reinforcement learning agent, integrated within a coarse-to-fine object detection framework, to optimize the scale for more effective detection of objects in such images. Specifically, a set of patches potentially containing objects are first generated. A set of rewards measuring the localization accuracy, the accuracy of predicted labels, and the scale consistency among nearby patches are designed in the agent to guide the scale optimization. The proposed scale-consistency reward ensures similar scales for neighboring objects of the same category. 
Furthermore, a spatial-semantic attention mechanism is designed to exploit the spatial semantic relations between patches. The agent employs the proximal policy optimization strategy in conjunction with the evolutionary strategy, effectively utilizing both the current patch status and historical experience embedded in the agent.  The proposed model is compared with state-of-the-art methods on two benchmark datasets for object detection on drone imagery. It significantly outperforms all the compared methods. 
