# Introduction

This repository uses [Detectron2](https://detectron2.readthedocs.io/en/latest/modules/index.html) platform to train (fine-tune) RetinaNet Model for detection of specific fields in W9 form. Highly indebted to excellent [Detectron2](https://detectron2.readthedocs.io/en/latest/modules/index.html) library by FaceBook which made things easy.



# Dataset

Dataset has been partially hand annotated and partially been produced using augmentation scripts, annotations are almost balanced.

--------

 - Mosaic Augmentations
 - Copy Paste Region Augmentations
 - Augmentations supported by Albumentations Library
 

 - [dataset is here in COCO form](https://drive.google.com/drive/folders/16Wt2dNprEnNHSOfmTz4oLTYndy1EPH4a?usp=sharing)

 - Training Data Stats.

|  category  | #instances   |  category  | #instances   |  category  | #instances   |
|:----------:|:-------------|:----------:|:-------------|:----------:|:-------------|
|    tl1     | 21951        |    tl2     | 16716        |     c1     | 24892        |
|     c2     | 23733        |    p11     | 14005        |    p12     | 4541         |
|            |              |            |              |            |              |
|   total    | 105838       |            |              |            |              |


 - Testing Data Stats.

|  category  | #instances   |  category  | #instances   |  category  | #instances   |
|:----------:|:-------------|:----------:|:-------------|:----------:|:-------------|
|    tl1     | 1726         |    tl2     | 1408         |     c1     | 1932         |
|     c2     | 1938         |    p11     | 290          |    p12     | 292          |
|            |              |            |              |            |              |
|   total    | 7586         |            |              |            |              |

:::note
 - See following file in the given [google drive link](https://drive.google.com/drive/folders/16Wt2dNprEnNHSOfmTz4oLTYndy1EPH4a?usp=sharing) to see **config file used in training**
:::
 
```
custom.yaml
```



# ANNOTATIONS DISTRIBUTION

| Train | Test |
|:-------: | :---------: |
|![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/814d69199694a6f01d668e69ac95e456234f70743ca442e75d12aa377076db10-image.png) | ![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/e0a8ba43b5b4ae80dfe0d1b0011037980b6825d35420ac912db1b4c3d7327288-image.png)
 |



# Annotation Fields


 - p11
 - p12
 - tl1
 - tl2
 - c1
 - c2
 
| | |
| :----: | :------: |
|![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/14b9f757003e0b941c993b24b133b19ce738107758c8e0577754411880c66b2f-image.png) | ![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/1822367545ed5cbc184ef76e672c85a5f0cd100b2dc977f97be10b6ec9fa294d-image.png) |
| ![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/11f89eeb807834367f88f59727a229f8bfcf38bce1cb2b14d68ef635e617fc37-image.png) | ![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/88466e4afb88b0d7ccfff30349cc83036fa86d3aee25b67b101128ee317c9b4a-image.png) |




# Drive Link

 - [Dataset Exists on the Google Drive](https://drive.google.com/drive/folders/16Wt2dNprEnNHSOfmTz4oLTYndy1EPH4a?usp=sharing)



# Config File Used In Training

This file was used to train RetinaNet

|**Model**|
|--|
|retinanet_R_101_FPN_3x.yaml|||

:::important
Config File used to train
:::


# Predict on a dir. containing images
To do prediction on images pressent inside a dir. **Weights must be present at demo/model_0012999.pth**, find weights [here].(https://drive.google.com/drive/folders/1QV1juDKtOj_U_SkWQTnuf804y3gkEe4D?usp=sharing)
```
python w9_predict.py  --input /home/talha/Downloads/W9_copy_paste_augmentation/data/*.png --output /home/talha/Downloads/W9_copy_paste_augmentation/predictions
```


For help type:

```
python w9_predict.py  --help
```


# Database 

Database must have following fields - see[[1]](#1), [[2]](#2):
 - 'fpath' (gets by request)
 - 'inp-images' list of base64 images given in input
 - 'pred_boxes'
 - 'scores'
 - 'pred_classes'
 - 'decision' a list of `[1, 0]` showing if corresponding image is W9 form or not, like `[1,0,0,0,1,1,1 ...]`
 - 'w9-pages-path' path of the folder containing w9 pages
 - 'other-pages-path' path of the folder containing other i.e. non-W9 pages
----

<a index="1">[1] E. Cerami, “Integrating FastAPI and MongoDB,” FastAPI Tutorials, Mar. 28, 2021. https://medium.com/fastapi-tutorials/integrating-fastapi-and-mongodb-8ef4f2ca68ad (accessed Sep. 10, 2021).
</a>

<a index="2"> [2] N. Jayatilake, “How to get started with MongoDB in 10 minutes,” We’ve moved to freeCodeCamp.org/news, Feb. 11, 2019. https://medium.com/free-code-camp/learn-mongodb-a4ce205e7739 (accessed Sep. 10, 2021).
</a>


# API

:::important
API must be made on Django
:::

 
 - **Input**  ---> file path (can be .tiff or .pdf file)
 - **Output JSON response** ---> 
 
```
{
    "detected" : path of folder containing W9 images,
    "filtered file" : path of pdf file excluding the W9 images.
}

```
# Dataset link on google drive

 - [dataset is here in COCO form](https://drive.google.com/drive/folders/16Wt2dNprEnNHSOfmTz4oLTYndy1EPH4a?usp=sharing)

 - Training Data Stats.

|  category  | #instances   |  category  | #instances   |  category  | #instances   |
|:----------:|:-------------|:----------:|:-------------|:----------:|:-------------|
|    tl1     | 21951        |    tl2     | 16716        |     c1     | 24892        |
|     c2     | 23733        |    p11     | 14005        |    p12     | 4541         |
|            |              |            |              |            |              |
|   total    | 105838       |            |              |            |              |


 - Testing Data Stats.

|  category  | #instances   |  category  | #instances   |  category  | #instances   |
|:----------:|:-------------|:----------:|:-------------|:----------:|:-------------|
|    tl1     | 1726         |    tl2     | 1408         |     c1     | 1932         |
|     c2     | 1938         |    p11     | 290          |    p12     | 292          |
|            |              |            |              |            |              |
|   total    | 7586         |            |              |            |              |

:::note
 - See following file in the given [google drive link](https://drive.google.com/drive/folders/16Wt2dNprEnNHSOfmTz4oLTYndy1EPH4a?usp=sharing) to see **config file used in training**
:::
 
 
```
custom.yaml
```


# ANNOTATIONS DISTRIBUTION

| Train | Test |
|:-------: | :---------: |
|![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/814d69199694a6f01d668e69ac95e456234f70743ca442e75d12aa377076db10-image.png) | ![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/e0a8ba43b5b4ae80dfe0d1b0011037980b6825d35420ac912db1b4c3d7327288-image.png)
 |



# Annotation Fields

Class | Index
----: | :----
|tl1|0|
|tl2|1|
|c1|2|
|c2|3|
|p11|4|
|p12|5|

# Sample Annotations

| | |
| :----: | :------: |
|![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/14b9f757003e0b941c993b24b133b19ce738107758c8e0577754411880c66b2f-image.png) | ![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/1822367545ed5cbc184ef76e672c85a5f0cd100b2dc977f97be10b6ec9fa294d-image.png) |
| ![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/11f89eeb807834367f88f59727a229f8bfcf38bce1cb2b14d68ef635e617fc37-image.png) | ![image.png](https://boostnote.io/api/teams/QCauNH2r-/files/88466e4afb88b0d7ccfff30349cc83036fa86d3aee25b67b101128ee317c9b4a-image.png) |



|*Prediction Results*|    
|:-----:|
|![W9_form_page1_0_0.jpg](https://boostnote.io/api/teams/QCauNH2r-/files/d38297dd6c985e2b7bc7a7913235145fc9427a471c25a23b16c9b655c9b5497b-W9_form_page1_0_0.jpg)| 
![W9_form_page1_0_9.jpg](https://boostnote.io/api/teams/QCauNH2r-/files/774fb279ac9e493cf30fa2ca6cc5c5764b000e9bda5de982377474b901a8b416-W9_form_page1_0_9.jpg)|
|![W9_form_page1_9_0.jpg](https://boostnote.io/api/teams/QCauNH2r-/files/d2c6ae0174cbeaefdd62d450f86e3b19c19a8bc37c5feaef101e052d0c255d37-W9_form_page1_9_0.jpg)|







# 500 iterations

Overall results

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 48.416 | 69.689 | 53.142 | 37.033 | 41.933 | 41.572 |


per category results


| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 39.936 | tl2        | 57.220 | c1         | 55.080 |
| c2         | 51.838 | p11        | 52.111 | p12        | 34.310 |


# 2500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 73.710 | 92.110 | 81.979 | 29.023 | 53.815 | 72.342 |


[09/03 01:05:45] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 


| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 50.443 | tl2        | 53.794 | c1         | 86.973 |
| c2         | 90.413 | p11        | 75.683 | p12        | 84.953 |


# 3000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 48.787 | 62.968 | 49.542 | 11.503 | 26.016 | 53.167 |


[09/03 01:15:40] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 


| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 2.544  | tl2        | 42.928 | c1         | 84.759 |
| c2         | 90.215 | p11        | 7.537  | p12        | 64.738 |


# 3500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 68.923 | 81.849 | 74.011 | 19.126 | 53.957 | 73.425 |


[09/03 01:25:42] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 


| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 47.957 | tl2        | 29.618 | c1         | 92.648 |
| c2         | 93.358 | p11        | 78.756 | p12        | 71.201 |


# 4000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 79.750 | 95.559 | 85.715 | 21.176 | 67.645 | 75.620 |


[09/03 01:35:45] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 


| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 49.556 | tl2        | 66.380 | c1         | 95.368 |
| c2         | 96.179 | p11        | 88.727 | p12        | 82.290 |

# 4500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 83.887 | 96.951 | 87.387 | 39.652 | 72.214 | 77.103 |


[09/03 01:45:47] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 61.999 | tl2        | 69.970 | c1         | 95.393 |
| c2         | 96.687 | p11        | 91.123 | p12        | 88.149 |


# 5000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 85.138 | 97.271 | 89.461 | 32.393 | 76.257 | 77.099 |


[09/03 01:55:48] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 


| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 63.704 | tl2        | 73.525 | c1         | 94.464 |
| c2         | 96.686 | p11        | 92.185 | p12        | 90.263 |

# 5500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 83.802 | 96.684 | 89.444 | 37.552 | 69.773 | 77.086 |


[09/03 02:05:55] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 61.262 | tl2        | 71.607 | c1         | 96.202 |
| c2         | 96.914 | p11        | 89.616 | p12        | 87.214 |




# 6000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 84.931 | 97.629 | 89.487 | 31.463 | 75.815 | 77.245 |



[09/03 02:15:52] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 


| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 62.994 | tl2        | 72.876 | c1         | 96.274 |
| c2         | 97.022 | p11        | 93.523 | p12        | 86.897 |


# 6500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 80.088 | 98.045 | 89.224 | 25.720 | 74.150 | 73.093 |


[09/03 02:25:54] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 59.565 | tl2        | 63.277 | c1         | 89.889 |
| c2         | 92.955 | p11        | 92.367 | p12        | 82.477 |

# 7000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 87.328 | 98.074 | 90.596 | 39.225 | 79.205 | 78.182 |


[09/03 02:35:50] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 


| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 70.848 | tl2        | 73.286 | c1         | 96.422 |
| c2         | 97.097 | p11        | 94.552 | p12        | 91.762 |

# 7500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 83.164 | 98.064 | 90.222 | 43.492 | 75.035 | 74.011 |


[09/03 02:45:51] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 66.516 | tl2        | 71.630 | c1         | 94.330 |
| c2         | 96.872 | p11        | 86.054 | p12        | 83.579 |



# 8000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 83.583 | 97.597 | 90.437 | 36.568 | 71.631 | 77.778 |


[09/03 02:55:51] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 58.237 | tl2        | 66.758 | c1         | 96.113 |
| c2         | 96.903 | p11        | 91.382 | p12        | 92.106 |


# 8500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 85.801 | 98.336 | 89.906 | 33.465 | 74.865 | 78.071 |


[09/03 03:05:52] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 61.878 | tl2        | 75.452 | c1         | 96.340 |
| c2         | 97.401 | p11        | 93.644 | p12        | 90.093 |


# 9000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 77.488 | 90.238 | 85.948 | 17.307 | 70.846 | 72.837 |



[09/03 03:15:53] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 


| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 68.771 | tl2        | 46.769 | c1         | 88.296 |
| c2         | 91.334 | p11        | 87.617 | p12        | 82.143 |



# 9500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 86.401 | 97.536 | 90.057 | 27.146 | 78.367 | 78.157 |


[09/03 03:25:52] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 67.402 | tl2        | 71.458 | c1         | 96.444 |
| c2         | 97.157 | p11        | 93.912 | p12        | 92.033 |


# 10000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 88.848 | 98.499 | 93.154 | 41.298 | 79.843 | 78.402 |
[09/03 03:35:53] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 
| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 71.099 | tl2        | 80.730 | c1         | 97.119 |
| c2         | 97.782 | p11        | 92.908 | p12        | 93.449 |

# 10500 iterations


|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 86.621 | 98.240 | 91.875 | 34.277 | 73.947 | 78.496 |
[09/03 03:45:51] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 

| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 67.587 | tl2        | 74.905 | c1         | 96.882 |
| c2         | 97.627 | p11        | 91.495 | p12        | 91.232 |


# 11000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 85.947 | 98.537 | 90.385 | 26.244 | 76.227 | 78.579 |
[09/03 03:55:48] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 

| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 71.286 | tl2        | 63.150 | c1         | 97.332 |
| c2         | 97.955 | p11        | 94.163 | p12        | 91.796 |


# 11500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 87.385 | 97.402 | 91.805 | 22.385 | 78.622 | 78.421 |

[09/03 04:05:54] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 

| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 69.951 | tl2        | 75.462 | c1         | 97.174 |
| c2         | 97.473 | p11        | 92.010 | p12        | 92.241 |



# 12000 iterations


|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 87.452 | 97.781 | 93.421 | 27.175 | 79.503 | 76.642 |
[09/03 04:15:47] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 

| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 73.464 | tl2        | 77.634 | c1         | 97.282 |
| c2         | 97.656 | p11        | 94.618 | p12        | 84.059 |






# 12500 iterations


|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 90.165 | 98.820 | 93.037 | 33.875 | 82.872 | 78.905 |
[09/03 04:25:48] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 

| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 76.249 | tl2        | 80.774 | c1         | 97.687 |
| c2         | 98.103 | p11        | 95.024 | p12        | 93.150 |



# 13000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 90.367 | 98.829 | 92.924 | 33.947 | 83.006 | 78.833 |


[09/03 04:35:48] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 77.536 | tl2        | 80.999 | c1         | 97.604 |
| c2         | 98.110 | p11        | 94.855 | p12        | 93.100 |



# 13500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 90.418 | 98.498 | 92.802 | 32.782 | 83.325 | 78.858 |


[09/03 04:45:53] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 77.694 | tl2        | 80.883 | c1         | 97.620 |
| c2         | 98.109 | p11        | 95.240 | p12        | 92.963 |


# 14000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 90.294 | 98.455 | 92.802 | 29.610 | 83.141 | 78.893 |


[09/03 04:55:59] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 




| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 77.355 | tl2        | 80.659 | c1         | 97.693 |
| c2         | 98.106 | p11        | 94.994 | p12        | 92.957 |


# 14500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 90.296 | 98.449 | 92.762 | 30.148 | 83.150 | 78.885 |


[09/03 05:05:55] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 77.138 | tl2        | 80.908 | c1         | 97.662 |
| c2         | 98.110 | p11        | 94.992 | p12        | 92.966 |


# 15000 iterations


|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 90.303 | 98.449 | 92.669 | 30.000 | 83.277 | 78.856 |


[09/03 05:15:53] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 77.368 | tl2        | 80.733 | c1         | 97.608 |
| c2         | 98.110 | p11        | 95.036 | p12        | 92.962 |


# 15500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 90.203 | 98.375 | 92.497 | 30.159 | 83.221 | 78.845 |


[09/03 14:59:51] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 76.337 | tl2        | 81.055 | c1         | 97.657 |
| c2         | 98.099 | p11        | 95.127 | p12        | 92.943 |


# 16000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 90.201 | 98.411 | 92.589 | 30.121 | 83.192 | 78.876 |


[09/03 15:09:56] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 76.493 | tl2        | 80.922 | c1         | 97.617 |
| c2         | 98.101 | p11        | 95.119 | p12        | 92.953 |



# 16500 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 90.187 | 98.418 | 92.630 | 29.738 | 83.239 | 78.876 |


[09/03 15:20:06] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 


| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 76.685 | tl2        | 80.662 | c1         | 97.614 |
| c2         | 98.096 | p11        | 95.126 | p12        | 92.942 |


# 17000 iterations

|   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 90.376 | 98.428 | 92.668 | 30.909 | 83.403 | 78.892 |


[09/03 15:30:09] d2.evaluation.coco_evaluation INFO: Per-category bbox AP: 



| category   | AP     | category   | AP     | category   | AP     |
|:-----------|:-------|:-----------|:-------|:-----------|:-------|
| tl1        | 77.095 | tl2        | 81.289 | c1         | 97.679 |
| c2         | 98.104 | p11        | 95.132 | p12        | 92.959 |



# Drive Link

 - [Dataset Exists on the Google Drive](https://drive.google.com/drive/folders/16Wt2dNprEnNHSOfmTz4oLTYndy1EPH4a?usp=sharing)


# All trained Weights (from all projects)
 - [All weights are here](https://drive.google.com/drive/folders/1QV1juDKtOj_U_SkWQTnuf804y3gkEe4D?usp=sharing)
 
 
 




```
CUDNN_BENCHMARK: false
DATALOADER:
  ASPECT_RATIO_GROUPING: true
  FILTER_EMPTY_ANNOTATIONS: true
  NUM_WORKERS: 12
  REPEAT_THRESHOLD: 0.0
  SAMPLER_TRAIN: TrainingSampler
DATASETS:
  PRECOMPUTED_PROPOSAL_TOPK_TEST: 1000
  PRECOMPUTED_PROPOSAL_TOPK_TRAIN: 2000
  PROPOSAL_FILES_TEST: []
  PROPOSAL_FILES_TRAIN: []
  TEST:
  - w9test
  TRAIN:
  - w9train
GLOBAL:
  HACK: 1.0
INPUT:
  CROP:
    ENABLED: false
    SIZE:
    - 0.9
    - 0.9
    TYPE: relative_range
  FORMAT: BGR
  MASK_FORMAT: polygon
  MAX_SIZE_TEST: 1000
  MAX_SIZE_TRAIN: 1000
  MIN_SIZE_TEST: 800
  MIN_SIZE_TRAIN:
  - 640
  - 672
  - 704
  - 736
  - 768
  - 800
  - 1000
  MIN_SIZE_TRAIN_SAMPLING: choice
  RANDOM_FLIP: horizontal
MODEL:
  ANCHOR_GENERATOR:
    ANGLES:
    - - -90
      - 0
      - 90
    ASPECT_RATIOS:
    - - 0.5
      - 1.0
      - 2.0
    NAME: DefaultAnchorGenerator
    OFFSET: 0.0
    SIZES:
    - - 32
      - 40.31747359663594
      - 50.79683366298238
    - - 64
      - 80.63494719327188
      - 101.59366732596476
    - - 128
      - 161.26989438654377
      - 203.18733465192952
    - - 256
      - 322.53978877308754
      - 406.37466930385904
    - - 512
      - 645.0795775461751
      - 812.7493386077181
  BACKBONE:
    FREEZE_AT: 2
    NAME: build_retinanet_resnet_fpn_backbone
  DEVICE: cuda
  FPN:
    FUSE_TYPE: sum
    IN_FEATURES:
    - res3
    - res4
    - res5
    NORM: ''
    OUT_CHANNELS: 256
  KEYPOINT_ON: false
  LOAD_PROPOSALS: false
  MASK_ON: false
  META_ARCHITECTURE: RetinaNet
  PANOPTIC_FPN:
    COMBINE:
      ENABLED: true
      INSTANCES_CONFIDENCE_THRESH: 0.5
      OVERLAP_THRESH: 0.5
      STUFF_AREA_LIMIT: 4096
    INSTANCE_LOSS_WEIGHT: 1.0
  PIXEL_MEAN:
  - 103.53
  - 116.28
  - 123.675
  PIXEL_STD:
  - 1.0
  - 1.0
  - 1.0
  PROPOSAL_GENERATOR:
    MIN_SIZE: 0
    NAME: RPN
  RESNETS:
    DEFORM_MODULATED: false
    DEFORM_NUM_GROUPS: 1
    DEFORM_ON_PER_STAGE:
    - false
    - false
    - false
    - false
    DEPTH: 101
    NORM: FrozenBN
    NUM_GROUPS: 1
    OUT_FEATURES:
    - res3
    - res4
    - res5
    RES2_OUT_CHANNELS: 256
    RES5_DILATION: 1
    STEM_OUT_CHANNELS: 64
    STRIDE_IN_1X1: true
    WIDTH_PER_GROUP: 64
  RETINANET:
    BBOX_REG_LOSS_TYPE: smooth_l1
    BBOX_REG_WEIGHTS:
    - 1.0
    - 1.0
    - 1.0
    - 1.0
    FOCAL_LOSS_ALPHA: 0.25
    FOCAL_LOSS_GAMMA: 2.0
    IN_FEATURES:
    - p3
    - p4
    - p5
    - p6
    - p7
    IOU_LABELS:
    - 0
    - -1
    - 1
    IOU_THRESHOLDS:
    - 0.4
    - 0.5
    NMS_THRESH_TEST: 0.5
    NORM: ''
    NUM_CLASSES: 6
    NUM_CONVS: 4
    PRIOR_PROB: 0.01
    SCORE_THRESH_TEST: 0.05
    SMOOTH_L1_LOSS_BETA: 0.0
    TOPK_CANDIDATES_TEST: 1000
  ROI_BOX_CASCADE_HEAD:
    BBOX_REG_WEIGHTS:
    - - 10.0
      - 10.0
      - 5.0
      - 5.0
    - - 20.0
      - 20.0
      - 10.0
      - 10.0
    - - 30.0
      - 30.0
      - 15.0
      - 15.0
    IOUS:
    - 0.5
    - 0.6
    - 0.7
  ROI_BOX_HEAD:
    BBOX_REG_LOSS_TYPE: smooth_l1
    BBOX_REG_LOSS_WEIGHT: 1.0
    BBOX_REG_WEIGHTS:
    - 10.0
    - 10.0
    - 5.0
    - 5.0
    CLS_AGNOSTIC_BBOX_REG: false
    CONV_DIM: 256
    FC_DIM: 1024
    NAME: ''
    NORM: ''
    NUM_CONV: 0
    NUM_FC: 0
    POOLER_RESOLUTION: 14
    POOLER_SAMPLING_RATIO: 0
    POOLER_TYPE: ROIAlignV2
    SMOOTH_L1_BETA: 0.0
    TRAIN_ON_PRED_BOXES: false
  ROI_HEADS:
    BATCH_SIZE_PER_IMAGE: 512
    IN_FEATURES:
    - res4
    IOU_LABELS:
    - 0
    - 1
    IOU_THRESHOLDS:
    - 0.5
    NAME: Res5ROIHeads
    NMS_THRESH_TEST: 0.5
    NUM_CLASSES: 6
    POSITIVE_FRACTION: 0.25
    PROPOSAL_APPEND_GT: true
    SCORE_THRESH_TEST: 0.05
  ROI_KEYPOINT_HEAD:
    CONV_DIMS:
    - 512
    - 512
    - 512
    - 512
    - 512
    - 512
    - 512
    - 512
    LOSS_WEIGHT: 1.0
    MIN_KEYPOINTS_PER_IMAGE: 1
    NAME: KRCNNConvDeconvUpsampleHead
    NORMALIZE_LOSS_BY_VISIBLE_KEYPOINTS: true
    NUM_KEYPOINTS: 17
    POOLER_RESOLUTION: 14
    POOLER_SAMPLING_RATIO: 0
    POOLER_TYPE: ROIAlignV2
  ROI_MASK_HEAD:
    CLS_AGNOSTIC_MASK: false
    CONV_DIM: 256
    NAME: MaskRCNNConvUpsampleHead
    NORM: ''
    NUM_CONV: 0
    POOLER_RESOLUTION: 14
    POOLER_SAMPLING_RATIO: 0
    POOLER_TYPE: ROIAlignV2
  RPN:
    BATCH_SIZE_PER_IMAGE: 256
    BBOX_REG_LOSS_TYPE: smooth_l1
    BBOX_REG_LOSS_WEIGHT: 1.0
    BBOX_REG_WEIGHTS:
    - 1.0
    - 1.0
    - 1.0
    - 1.0
    BOUNDARY_THRESH: -1
    CONV_DIMS:
    - -1
    HEAD_NAME: StandardRPNHead
    IN_FEATURES:
    - res4
    IOU_LABELS:
    - 0
    - -1
    - 1
    IOU_THRESHOLDS:
    - 0.3
    - 0.7
    LOSS_WEIGHT: 1.0
    NMS_THRESH: 0.7
    POSITIVE_FRACTION: 0.5
    POST_NMS_TOPK_TEST: 1000
    POST_NMS_TOPK_TRAIN: 2000
    PRE_NMS_TOPK_TEST: 6000
    PRE_NMS_TOPK_TRAIN: 12000
    SMOOTH_L1_BETA: 0.0
  SEM_SEG_HEAD:
    COMMON_STRIDE: 4
    CONVS_DIM: 128
    IGNORE_VALUE: 255
    IN_FEATURES:
    - p2
    - p3
    - p4
    - p5
    LOSS_WEIGHT: 1.0
    NAME: SemSegFPNHead
    NORM: GN
    NUM_CLASSES: 6
  WEIGHTS: https://dl.fbaipublicfiles.com/detectron2/COCO-Detection/retinanet_R_101_FPN_3x/190397697/model_final_971ab9.pkl
OUTPUT_DIR: ./output
SEED: -1
SOLVER:
  AMP:
    ENABLED: false
  BASE_LR: 0.0001
  BIAS_LR_FACTOR: 1.0
  CHECKPOINT_PERIOD: 200
  CLIP_GRADIENTS:
    CLIP_TYPE: value
    CLIP_VALUE: 1.0
    ENABLED: false
    NORM_TYPE: 2.0
  GAMMA: 0.1
  IMS_PER_BATCH: 6
  LR_SCHEDULER_NAME: WarmupMultiStepLR
  MAX_ITER: 17000
  MOMENTUM: 0.9
  NESTEROV: false
  REFERENCE_WORLD_SIZE: 0
  STEPS:
  - 13600
  - 15300
  WARMUP_FACTOR: 0.001
  WARMUP_ITERS: 1000
  WARMUP_METHOD: linear
  WEIGHT_DECAY: 0.0001
  WEIGHT_DECAY_BIAS: 0.0001
  WEIGHT_DECAY_NORM: 0.0
TEST:
  AUG:
    ENABLED: false
    FLIP: true
    MAX_SIZE: 4000
    MIN_SIZES:
    - 400
    - 500
    - 600
    - 700
    - 800
    - 900
    - 1000
    - 1100
    - 1200
  DETECTIONS_PER_IMAGE: 100
  EVAL_PERIOD: 500
  EXPECTED_RESULTS: []
  KEYPOINT_OKS_SIGMAS: []
  PRECISE_BN:
    ENABLED: false
    NUM_ITER: 200
VERSION: 2
VIS_PERIOD: 0
```