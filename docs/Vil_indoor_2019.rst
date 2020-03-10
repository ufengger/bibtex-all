Notes on: Carrera Villacres, J. L. et al. (2019): A particle filter-based reinforcement learning approach for reliable wireless indoor positioning
==================================================================================================================================================

.. code-block:: bibtex

   @article{Vil_indoor_2019,
     author    = {Carrera Villacres, Jose Luis and Zhao, Zhongliang and Braun, Torsten and Li, Zan},
     title     = {A Particle Filter-Based Reinforcement Learning Approach for Reliable Wireless Indoor Positioning},
     journal   = {IEEE Journal on Selected Areas in Communications},
     volume    = {37},
     number    = {11},
     pages     = {2457–2473},
     year      = {2019},
     doi       = {10.1109/jsac.2019.2933886},
     url       = {http://dx.doi.org/10.1109/JSAC.2019.2933886},
     issn      = {1558-0008},
     month     = {Nov},
     publisher = {Institute of Electrical and Electronics Engineers (IEEE)},
   }

简介
----

基于指纹的室内定位系统通常由两个阶段组成：

- off-line (training) phase. 这一阶段的主要目的是为了建立数据库。

- on-line (localization) phase. 定位。

由于无线信号不稳定，室内定位通常面临两个问题：

- global localization problem. 初始定位。

- kidnapped-robot problem. 文章里定义不清楚。

PFRL
   Particle filter-based reinforcement learning.

PFRL 包含两部分：

- 粒子滤波用于精确的室内定位；

- RL 用于保证系统的可靠性（Robustness）。

粒子滤波融合下述信息：

- indoor zone prediction. The zone prediction method is designed with an
  ensemble learning algorithm by combining different individual predictors in a
  HMM. 室内区域预测可以提供准确的测距模型，例如我们如果知道终端和 AN 在一个区域，
  那么就采用 LOS 的测距模型，否则，采用 NLOS 的测距模型。

- range radio information.

- IMUs.

- floor plan information. 地图？

RL:

- propose an efficient reinforcement learning-based resampling method to assure
  the placement of samples (i.e. particles) over areas where the desired
  distribution is large (i.e., areas with high probability of containing the
  ground truth position).

分布式的架构：

- 室内区域预测在定位终端上做（计算量小）；

- PFRL 在服务端做（需要大量计算）。
