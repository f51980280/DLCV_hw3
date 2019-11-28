#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import cv2
import h5py
import construct_datasets #if use this, construct "train_data_processed.h5" with digitStruct.mat


# In[42]:


root_dir = os.getcwd()

train_data = pd.read_hdf(os.path.join(root_dir, 'train', 'train_data_processed.h5'), 'table')
train = train_data.to_numpy()


# In[83]:


from lxml import etree, objectify

#training data path for covert to xml
f = h5py.File(os.path.join(root_dir, 'train', 'digitStruct.mat'), 'r')

for i in range(train.shape[0]):
    E = objectify.ElementMaker(annotate=False)
    
    ID = int(train[i,2].split('.')[0])
    box = construct_datasets.get_bbox(int(train[i,2].split('.')[0])-1,f)

    anno_tree = E.annotation(
        E.filename(construct_datasets.get_name(ID-1,f)),
        E.size(
            E.width(train[i,12]),
            E.height(train[i,11]),
            E.depth(3)
        ),
    )
    
    for j in range(len(box['left'])):
        E2 = objectify.ElementMaker(annotate=False)
        anno_tree2 = E2.object(
            E.name(int(box['label'][j])),
            E.bndbox(
                E.xmin(int(box['left'][j])),
                E.ymin(int(box['top'][j])),
                E.xmax(int(box['width'][j]+box['left'][j])),
                E.ymax(int(box['height'][j]+box['top'][j]))
            ),
        )
        anno_tree.append(anno_tree2)

    etree.ElementTree(anno_tree).write("annotation_test2/"+str(ID).split('.')[0]+".xml", pretty_print=True)


# In[ ]:




