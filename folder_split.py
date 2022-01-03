from random import seed
import splitfolders
splitfolders.ratio('./VOC2012_7', output='./VOC2012_7_dataset',
                   seed=42, ratio=(0.6, 0.2, 0.2))
