# Cloths Virtual Try On
![GitHub stars](https://img.shields.io/github/stars/practice404/clothes-virtual-try-on.svg)
[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SwayamInSync/clothes-virtual-try-on/blob/main/setup.ipynb)

## Table of contents
- [Cloths Virtual Try On](#cloths-virtual-try-on)
  - [Table of contents](#table-of-contents)
  - [General info](#general-info)
  - [Demo](#demo)
  - [Block Diagram](#block-diagram)
  - [Methodology](#methodology)
  - [Setup](#setup)
  - [Citation](#citation)

## Updates

- [19/12/2023] Fixed the `openpose` installation and missing model weights issue
- [19/12/2023] Replaced the `remove.bg` dependecy with `rembg`
- [26/04/2023] Fixed the GAN generation issue

## General info

This project is a part of a crework community project. While buying clothes online, it is difficult for a customer to select a desirable outfit in the first attempt because they can’t try on clothes. This project aims to solve this problem.

<img width="383" alt="general_info" src="https://user-images.githubusercontent.com/63489382/163923011-c2898812-2491-4ec2-beb7-dcaaaf680e4f.png">


## Demo

https://user-images.githubusercontent.com/63489382/163922795-5dbb0f52-95e4-42c6-95d7-2d965abeba6d.mp4



## Block Diagram
![block_diagram_whole](https://user-images.githubusercontent.com/63489382/163922947-c1677f79-ad6f-4550-affc-7d4e80f0d247.png)


## Methodology
![block_diagram_detailed](https://user-images.githubusercontent.com/63489382/163922991-86d148c2-1a97-48a5-b4ec-d8c16819374a.png)


## Setup
- Make an account on [ngrok](https://ngrok.com/) and apply for an API key.
- Replace the API key inside `setup.ipynb` inside `!ngrok authtoken <your_token>`
- Run the `setup.ipynb` and you'll get the link of your server. Make a post request or use our `client-side` folder


## Citation
**Work in progress**
