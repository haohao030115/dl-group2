# G1 MuJoCo Simulation Environment

**Unitree G1 MuJoCo 仿真环境**。

## 1. 环境版本

  Component              Version

  ---------------------- ----------------------------------

  Python                 **3.9**
  Conda                 25.5.1
  MuJoCo Python          3.3.2
  Unitree G1 Model       GitHub项目中/models/g1下载即可

> G1 Menagerie 官方要求 MuJoCo 2.3.4 或更高版本。

## 2. 创建 Conda 环境

    conda create -n robot（自己设置环境名字） python=3.9
    conda activate robot

## 3. 安装 MuJoCo

    pip install mujoco
    如果报错可以在conda环境下运行：conda install -c conda-forge mujoco

检查：

    python -c "import mujoco; print(mujoco.__version__)"

## 3. 下载 Unitree G1 模型

本项目使用 Google DeepMind 的 MuJoCo Menagerie 中的 Unitree G1：

直接下载项目内/models/g1内所有文件，最好保留原有目录层级。

即：

    models/g1/
    ├── assets/
    ├── g1.xml
    ├── g1_with_hands.xml
    ├── g1_mjx.xml
    ├── grasp.xml
    ├── scene.xml
    ├── scene_with_hands.xml
    └── scene_mjx.xml

## 4. 测试官方 G1

本项目需要 G1 双手，因此主要使用：

    scene_with_hands.xml

为了满足项目环境需求，搭建了桌子和小木块，因此主要只使用：

    grasp.xml

如果能正常看到 G1，说明 MuJoCo 和 G1 模型安装成功。

## 5.大致项目结构

```
g1_grasp_project/
├── models/
│   └── g1/
│       ├── assets/
│       ├── ...
├── scripts/

```
