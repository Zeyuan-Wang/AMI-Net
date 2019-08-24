# AMI-Net

This is the source code of our IJCNN 2019 submitted paper: "[Attention-based Multi-instance Neural Network for Medical
Diagnosis from Incomplete and Low Quality Data](https://arxiv.org/abs/1904.04460)". Please cite it if you use AMI-Net for 
your research.

## Introduction

* AMI-Net is developed for resolving the problems of *incomplete data, label and feature noise existing, redundant and highly correlated features*, in medical outcome prediction.
* It mainly consists of *word embedding, multi-head attention, attention-based pooling*, and uses the **multi-instance neural network** to integrate all computational modules. The overall architecture shows here.

<div align="middle"><img src="https://github.com/Zeyuan-Wang/img/AMI-Net.png"width="80%"></div>

## Data Description

* **sample_data.xlsx**: There are 3182 sample cases from the whole "Western Medicine" dataset. The column "y" is the binary prediction target. The other 88 columns are all binary features, i.e., whether the patient has this symptom. And for each case, there exist at most 21 features and 5 at least, representing the individual patient condition.

## File Description

* **main.py**:  The main code for running the model.
* **config.py**:  Contains the hyper-parameters of AMI-Net.
* **load_data.py**:  The script for data transformation.
* **model.py**:  The script for AMI-Net construction.
* **utils.py**:  Contains the computational modules of the AMI-Net.

## Dependencies

* Python  3.6.8
* numpy  1.16.0
* sklearn  0.18.1
* tensorflow  2.0.0-beta1
```shell
$ pip install tensorflow==2.0.0-beta1
```
