# Lesson 1 summary

## State of art Detection
### Two Stage Detection
### One Stage Detection
### Anchor free Detection
- Trend
- CenterNet
- FCos

## RCNN: AlexNet as backbone
1. Region proposal: Selection search
	- Resize all region into same size
2. Feature extration: CNN with proposed region
	- Training: transfer learning
		1. Pretrain on ILSVRC2012 dataset
		2. Finetune on real dataset
		3. Batch size 128: 1:3 pos vs neg sample.
3. Classification and detection: SVM + Regression

## NMS
- Soft NMS fix the problem of two targets share high IOU with each other.

## Problem
- SVM and regressor are post-hoc: CNN features not updated in response to SVM and regressors

## Fast RCNN: VGG as backbone
Make each part of the process to be more modular.
### Improvement
1. Replace SVM and regressor with FC layers 
2. First SS then feed the entire image into the CNN to generate feature map. 
3. ROIPooling layer to resize all the extract feature map.
	- Grid each ROI in feature map to fixed size, and do max pooling within each grid
	- So different size of feature maps can transfer into feature maps with same size
4. Multi-task loss: multi-class cross entropy and location smooth L1 loss.

 
