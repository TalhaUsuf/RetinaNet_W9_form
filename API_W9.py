from pymongo import MongoClient
from pydantic import BaseModel,FilePath
from pathlib import Path
from typing import List
from fastapi import FastAPI, status
import random
import uvicorn
import pandas as pd
import sqlite3



app = FastAPI()

conn = sqlite3.connect(database="W9_logs.sqlite")





class output_model(BaseModel):

      """Used to validate the datatypes and structures to ensure data-integrity

      fpath will be used to store the input file path
      b64_imgs will save the input images as a list of b64 strings
      scores will save list of scores
      bboxes will store a list of lists containing bboxes coordinates
      classes will store a list of integers corresponding to classes indices
      w9_images will save list of string paths corresponding to W9 images
      other_images will save a list of string paths corresponding to other images
      """

      fpath : str
      b64_imgs : List[str]
      scores : List[float]
      bboxes : List[List[float]]
      classes : List[int]
      w9_images : List[str]
      other_images : List[str]
      detections : List[int]



@app.get('/status')
async def status_(status_code=status.HTTP_200_OK):
      return {
      "status" : f"ALIVE"
      }


@app.post('/insert/{fpath}', response_model=output_model, status_code=status.HTTP_201_CREATED)
async def insert_to_db(fpath : str):
      # insert somethinmg to database
      # with MongoClient() as client:
      #       logs = client["W9"]["API_LOGS"]

      #       dummy = {
      #             "fpath" : "dummy_path",
      #             "b64_imgs" : ["this", "is", "a", "dummy", "string"],
      #             "scores" : [1.2,561.5, 2.5,6.5,5.5],
      #             "bboxes" : [[1.2, 55, 56, 560], [54, 564, 56, 584]],
      #             "classes" : [1, 52 , 5, 54],
      #             "w9_images" : ["sdgdfsgdf", "dsgdfsgdfgdf0"],
      #             "other_images" : ["dsgfdsgdf", "dsgdsg"],
      #             }
            # logs.insert_one(dummy)
      # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      #
      #                 recognize the file extension
      #                 read the file
      #                 save images in separate dirs and make list
      #                 convert them into base64 strings and make list
      #                 loop over images and apply detection
      #                 make a list 'detections' and [1,0,0,1,1,1,0] 0 for not W9 image and 1 for W9 image
      #                 save those images to a separate directory.
      #
      # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


      # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      #                  do recognition here
      # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

      # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      dummy = {
                  "fpath" : f"{fpath}",
                  "b64_imgs" : ["this", "is", "a", "dummy", "string"],
                  "scores" : [1.2,561.5, 2.5,6.5,5.5],
                  "bboxes" : [[1.2, 55, 56, 560], [54, 564, 56, 584]],
                  "classes" : [1, 52 , 5, 54],
                  "w9_images" : ["sdgdfsgdf", "dsgdfsgdfgdf0"],
                  "other_images" : ["dsgfdsgdf", "dsgdsg"],
                  "detections" : [1,0,0,1,1,0],
                  }

      return dummy





# @app.get('/recognize', response_model=output_model)
# async def recognition(file_input : input_model):

#       with MongoClient() as client:
#             logs = client["W9"]["API_LOGS"]
#             logs.insert_one(file_input.dict())
#       return {

#       }


if __name__=='__main__':
      # uvicorn.run("API_W9:app", port=8080, limit_concurrency=4, workers=4)
      uvicorn.run("API_W9:app", port=8080, limit_concurrency=4, reload=True)
