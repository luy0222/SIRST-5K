# SIRST-5K

### SIRST-5K: Exploring Massive Negatives Synthesis with Self-supervised Learning for Robust Infrared Small Target Detection



## Contents
- [Introduction](#introduction)
  - [Overview](#overview)
  - [Visual](#visual)
- [Dependencies and Installation](#dependencies-and-installation)
- [Quick Inference](#quick-inference)
- [Codes Demos](#codes-demos)
- [Image Quality Assessment](#image-quality-assessment)
- [Inference Dataset](#inference-dataset)
- [Citation](#citation)
- [Acknowledgement](#acknowledgement)



## Introduction

We propose a method based on real-world noise modeling and transfer. By extracting the unique noise distribution of infrared sensors, our model adds different types of noise to the original data to generate new samples, ensuring theauthenticity and diversity of the synthesised data. Without requiring additional manual labeling, our model generates challenging massive samples through the use of negative sample augmentation strategies. Utilizing the Synthetic SIRST-5K dataset significantly improves the performance and convergence speed of infrared small target detection models. Furthermore,
our proposed negative sample augmentation strategies can be directly applied to most existing infrared small target detectors, demonstrating strong versatility.


### Overview
<img src="./datas/framework.jpg" width=100%>

### Visual

<img src="./datas/Quantitative result1 .jpg" width=100%>
<img src="./datas/Quantitative result2 .jpg" width=100%>

## Dependencies and Installation
- Following [DNANet](https://github.com/YeRen123455/Infrared-Small-Target-Detection)
- Python == 3.7
- pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
- pip install scikit-image
- pip install tqdm
- pip install matplotlib
- pip install tensorboard==2.14.0
- Pip install opencv-python==4.8.0.76



## Quick Inference

Download the dataset download dir models [[Baidu Drive](https://pan.baidu.com/s/1WV1ytntgvxaBqetYIuBAYw ) (code:1234). Currently, the available dataset are:

- `SIRST-5K`: The dataset synthesized using negatives generation strategies (Fig 2).
- `NUDT-SIRST`:An open-sourced dataset with rich targets.  
- `3_NUDT-SIRST0.1`: finetune use our strategies (The bast visualization).


## Codes Demos

**Noise Sampling**

```bash
# Run Noise_Sampling.py directly
python codes/Noise_Sampling/Noise Sampling.py
```

**Noise  displacement**

```bash
# Run add_noise.py directly
python codes/Mix_Rot/add_noise.py
```

**Negative augmentation**

```bash
# Run rot_patch.py directly
python codes/Mix_Rot/rot_patch.py
```
```bash
# Run rot_mask.py directly
python codes/Mix_Rot/rot_mask.py
```

## Usage

#### 1. Train.

```bash
python train.py --base_size 256 --crop_size 256 --epochs 1500 --dataset [dataset-name] --split_method 50_50 --model [model name]   --deep_supervision True --train_batch_size 16 --test_batch_size 16 --mode TXT

```
#### 2. Test.

```bash
python test.py --base_size 256 --crop_size 256 --st_model [trained model path] --model_dir [model_dir] --dataset [dataset-name] --split_method 50_50 --model [model name]   --deep_supervision True --test_batch_size 1 --mode TXT 
```

#### 3. Visulize your predicts.
```bash
python visulization.py --base_size 256 --crop_size 256 --st_model [trained model path] --model_dir [model_dir] --dataset [dataset-name] --split_method 50_50 --model [model name]   --deep_supervision True --test_batch_size 1 --mode TXT 
```

## Quantative Results 

| dataset    | mIoU (x10(-2)) | Pd (x10(-2))|  Fa (x10(-6)) |code:1234|
| ------------- |:-------------:|:-----:|:-----:|:-----:|
|  NUDT-SIRST | 86.87 | 97.98 | 3.71| [[Weights]](https://pan.baidu.com/s/1xeV4IPpmJCYzzwMmWrzeYQ) |
| NUDT-SIRST0.1_3 | 92.78 | 98.84 | 2.74 |
| SIRST-5k | 88.61 | 99.15 | 5.15 |[[Weights]](https://pan.baidu.com/s/1xeV4IPpmJCYzzwMmWrzeYQ) |


## Acknowledgement
*This code is highly borrowed from [DNA](https://github.com/YeRen123455/Infrared-Small-Target-Detection). Thanks to Boyang Li.

