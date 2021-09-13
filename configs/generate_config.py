from detectron2.model_zoo import model_zoo
from detectron2.config import get_cfg
from rich.console import Console
import json
import yaml




def main():

    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/retinanet_R_101_FPN_3x.yaml"))
    cfg.MODEL.WEIGHTS = "https://dl.fbaipublicfiles.com/detectron2/COCO-Detection/retinanet_R_101_FPN_3x/190397697/model_final_971ab9.pkl"
    cfg.MODEL.ROI_HEADS.NUM_CLASSES=6
    cfg.MODEL.RETINANET.NUM_CLASSES=6
    cfg.MODEL.SEM_SEG_HEAD.NUM_CLASSES=6
    cfg.INPUT.MIN_SIZE_TRAIN= [
               640,
               672,
               704,
               736,
               768,
               800,
               1000,
          ]
    
    cfg.INPUT.MAX_SIZE_TRAIN= 1000


    cfg.INPUT.MIN_SIZE_TEST= 800
    cfg.INPUT.MAX_SIZE_TEST= 1000


    cfg.DATASETS.TRAIN=["w9train"]
    cfg.DATASETS.TEST=["w9test"]
    
    cfg.DATALOADER.NUM_WORKERS=12


    ITER = 17000
    cfg.SOLVER.MAX_ITER=ITER
    cfg.SOLVER.BASE_LR=0.0001
    cfg.SOLVER.GAMMA=0.10
    cfg.SOLVER.STEPS=[int(0.8 * ITER), int(0.9 * ITER)]

    cfg.SOLVER.WARMUP_ITERS=1000
    cfg.SOLVER.CHECKPOINT_PERIOD=200 # save checkpoints after every 200 iterations
    
    # %%%%%%%%%%%%%%%%%%%%%%%  set BATCH SIZE HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    cfg.SOLVER.IMS_PER_BATCH = 6     # batch-size across all gpus 

    cfg.TEST.EVAL_PERIOD=500 # evaluate results after every 500 iterations

    cfg.OUTPUT_DIR = "./output"
    with open("custom.yaml", "w") as f:
        f.write(cfg.dump())


    Console().rule(f"{type(cfg.dump())}", characters="=")
    Console().print(json.dumps(cfg, indent=5))

if __name__ == '__main__':
    main()
