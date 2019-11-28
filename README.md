# DLCV_hw3
## Retinanet with svhn dataset

refrence from https://github.com/penny4860/retinanet-digit-detector  
and using https://github.com/fizyr/keras-retinanet for package in repository

Model : Retinanet with ResNet152

## environment
  python 3.6  
  tensorflow-gpu 1.5.0  
  keras 2.2.4  
  keras-retinanet 0.5.0  

## folder: 
  ##### snapshots  :  for saving weights  
  ##### train_all  :   all training image  
  ##### train_all_anno  :  all training annotation with pascal voc annotation xml format  
  ##### valid: for valid  : 3*.png for valid   #####it's unuse  
  ##### valid_annot  : 3*.png annotation with pascal voc annotation xml format #####it's unuse  
  
## python:
  ##### main.py : use python main.py for training  
  ##### convert2xml.py : change to xml format  
  ##### construct_dataset.py : use it to find the trainning data's label, bounding box,....(with digitstructure.mat)  
  ##### eval.py : it can show the predict result  
  ##### Demo_eval.ipynb : demo for predict image  
  
my training weight store in : https://drive.google.com/open?id=1OuttuIFpE4uCxyvC5ID0jmVXryu4Z9gl
