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
- Recommend mmedit version == 0.15.1



## Quick Inference

Download the dataset download dir models [[Baidu Drive](https://pan.baidu.com/s/1cb-l62cusv8anPwvtfvR7Q )] (code:1234), and put them into the [weights](weights/) folder. Currently, the available dataset are:

- `SIRST-5K`: The dataset synthesized using negatives generation strategies (Fig 2).
- `NUDT-SIRST`:An open-sourced dataset with rich targets.  
- `3_NUDT-SIRST0.1`: finetune use our strategies (The bast visualization).


## Codes Demos

**Noise Sampling**

```bash
# Run Noise Sampling.py directly
python codes/Noise Sampling/Noise Sampling.py
```

**Negative augmentation**

```bash
# Run rot_p.py directly
python codes/rot_PM/rot_p.py
```

We have migrated the negative augmentation code to [basicvsr_net.py](codes/basicvsr_net.py).

## **Image Quality Assessment**

**Selecting samples for evaluation**

```bash
# For FLIR
python codes/flir_sub.py
# For VideoLQ
python codes/videolq_sub.py 
```

**No-reference metrics calculation**

Recommended for using [IQA-PyTorch](https://github.com/chaofengc/IQA-PyTorch). Our paper results can be found in [Results](/results).

## Inference Dataset
1. You can download the VideoLQ and our FLIR testing dataset from [[Baidu Drive](https://pan.baidu.com/s/1cb-l62cusv8anPwvtfvR7Q )] (code:1234).
2. Click on the [FLIR](https://www.flir.com/oem/adas/adas-dataset-form) for the full FLIR dataset.

##  Citation
If you find this project useful for your research, please consider citing our paper. :smiley:
```bibtex
@article{song2023negvsr,
  title={NegVSR: Augmenting Negatives for Generalized Noise Modeling in Real-World Video Super-Resolution},
  author={Song, Yexing and Wang, Meilin and Xian, Xiaoyu and Yang, Zhijing and Fan, Yuming and Shi, Yukai},
  journal={arXiv preprint arXiv:2305.14669},
  year={2023}
}
```
## Acknowledgement
This project is build based on [RealBasicVSR](https://github.com/ckkelvinchan/RealBasicVSR) and [VQD-SR](https://github.com/researchmm/VQD-SR). We thank the authors for sharing their code.
