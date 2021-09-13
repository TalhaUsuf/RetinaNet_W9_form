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