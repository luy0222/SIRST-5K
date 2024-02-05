# SIRST-5K

### SIRST-5K: Exploring Massive Negatives Synthesis with Self-supervised Learning for Robust Infrared Small Target Detection



## Contents
- [Introduction](#introduction)
  - [Overview](#overview)
  - [Visual](#visual)
- [Dependencies and Installation](#dependencies-and-installation)
- [Dataset](#dataset )
- [Codes Demos](#codes-demos)
- [Usage](#usage)
- [Quantative Results ](#quantative-results)




## Introduction
<img src="./datas/5k.jpg" width=100%>

### Overview
<img src="./datas/framework.jpg" width=100%>



### Visual
<img src="./datas/Quantitative result1 .jpg" width=100%>


## Dependencies and Installation
- Following [DNANet](https://github.com/YeRen123455/Infrared-Small-Target-Detection)
- Python == 3.7
- pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
- pip install scikit-image
- pip install tqdm
- pip install matplotlib
- pip install tensorboard==2.14.0
- pip install opencv-python==4.8.0.76



## Dataset 

Download the dataset download dir models[[Baidu Drive](https://pan.baidu.com/s/1EG-loK86aWJL7M6bPQjivA?pwd=1234)]. Currently, the available dataset are:
- `SIRST-5K`: The dataset synthesized using negatives generation strategies (Fig 2).


## Codes Demos

**Noise Sampling**

```bash
# Run Noise_Sampling.py directly
python codes/Noise_Sampling/Noise_Sampling.py
```

**Noise  displacement**

```bash
# Run add_noise.py directly
python codes/Mix_Rot/add_noise.py
```

**Negative**

```bash
# Run rot_patch.py directly
python codes/Mix_Rot/rot_patch.py
```
```bash
# Run rot_mask.py directly
python codes/Mix_Rot/rot_mask.py
```

Our negative augmentation strategies can produce large amounts of challenging image data. You can download the [SIRST-5K](https://pan.baidu.com/s/1EG-loK86aWJL7M6bPQjivA?pwd=1234) directly for training.

## Usage

#### 1. Train.

```bash
python train.py --base_size 256 --crop_size 256 --epochs 1500 --dataset [dataset-name] --split_method 50_50  --deep_supervision True --train_batch_size 16 --test_batch_size 16 --mode TXT

```
#### 2. Test.

```bash
python test.py --base_size 256 --crop_size 256 --st_model [trained model path] --model_dir [model_dir] --dataset [dataset-name] --split_method 50_50    --deep_supervision True --test_batch_size 1 --mode TXT 
```

#### 3. Visulize your predicts.
```bash
python visulization.py --base_size 256 --crop_size 256 --st_model [trained model path] --model_dir [model_dir] --dataset [dataset-name] --split_method 50_50 --model [model name]   --deep_supervision True --test_batch_size 1 --mode TXT 
```

## Quantative Results 

| Model    | mIoU (x10(-2)) | Pd (x10(-6))|  Fa (x10(-6)) ||
| ------------- |:-------------:|:-----:|:-----:|:-----:| 
|  Ours | 92.78|98.84  |2.735 |[[Weights]](https://pan.baidu.com/s/1s0x0-IJsPwiKymP-MEaOKA?pwd=1234)|





