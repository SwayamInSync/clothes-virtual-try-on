# Cloths Virtual Try On

## Table of contents
- [Cloths Virtual Try On](#cloths-virtual-try-on)
  - [Table of contents](#table-of-contents)
  - [General info](#general-info)
  - [Demo](#demo)
  - [Block Diagram](#block-diagram)
  - [Methodology](#methodology)
  - [Setup](#setup)
  - [Citation](#citation)


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
- Replace the API key inside `C_A_MARK_2.ipynb` inside `!ngrok authtoken <you api>`
- Make an account on [remove.bg](https://www.remove.bg/) and aply for API key
- Replace the remove.bg api with yours inside `remove_bg.py` where `api = <your api>` inside the function `remove_bg`
- Run the `C_A_MARK_2.ipynb` and you'll get the link of your server. Make a post request or use our `client-side` folder


## Citation
**Work in progress**
