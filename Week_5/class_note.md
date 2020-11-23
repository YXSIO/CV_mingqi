## Two stages
	1. NMS and soft-NMS 
	2. ROI pooling: Grid each ROI in feature map to fixed size, and do max pooling within each grid. It has quantilization error twice. 
	3. ROI align: no quantilization error, but not all points contributes to the pooled results. Bi-linear interpolation has been used here. 
	4. Precise ROI pooling: bi-linear interpolation to find the red dots. Then using integration to calcuate the average for each grid. 
	5. Faster RCNN: backbone is ZF, Resnet, VGG16; output is B x C x H/16 x W/16 (1 x 256 x 38 x 50)
	6. RPN: region proposal network: binary cls + bbox regression + NMS + anchor box + Conv Layers. There are 9 bbox on each of the 38 x 50 points. One each pixel, the channel is 256, there for 256-d vector is responsible for the cls and regression for the 9 anchors within each pixel. 
	7. *Take-away*: after convolution and pooling, each pixel on the feature map corresponding to certain regions on the original input image. 
	8. After RPN, 128 candidate is selected for each image. Much less than the results from SS. 
	9. Smooth L1 loss when regress for the proposal region from anchor. (fit the offset and normalized by the width and height to balance large and small objects)
		- Encoding -> fit the encoding and generate the output by Net -> decoding to get the predicted proposal. 
	10. How to select the 128 proposal: based on IOU with ground truth. (1:3) 


## One stage
### Yolo - V1
	1. Confidence: P(obj) * IOU
	2. Final output: 7 x 7 x (5*2 + 20) -- two bbox and 20 cls.
	3. What is the reorg layer
	4. Multi-scale training: remove the FC layers. Can accept any input sizes. 

	V2:
	1. Anchor: 10 numbers correspond to 5 anchors
	2. a_wi / a_ori = 13 / W: original bbox -> normalized bbox -> transfer to 13x13 -> to each cell. 
	3. Predict offset and follow the encoding and decoding steps to get the location of the bounding box. 

	V3:
	1. Skip connection like Resnet
	2. Multi-scales, 13 x 13, 26 x 26, 52 x 52. 
	3. 80 Classes from softmax -> logistic (Each class will not supress each other)
	4. FPN: feature pyramid network enable the multi-scales training. Semantic and localization info is combined. 
	
	V4: 
	1. Spacial attention model figures out where to mute to generate the mask. 
	2. Label smoothing
	3. Mish as activation function

### RetinaNet
	1. Structure: Resnet + FPN + FCN
	2. Answer the question on why One stage is not as good as two stage. 
		- Pos VS neg sample is very skewed for one stage. (i.e. 3 VS 49 + 46 = 95)
		- Gradient is dominated by easy samples. 
	3. Focal loss: 
		- 解决多少的问题：add alpha as weight to the loss for both pos and neg samples. 
		- 解决难易的问题：(1-p(t))^2 as weight to the loss for both pos and neg samples. (Modelating factor, and focusing parameters)


## Anchor free method: CenterNet - points as objects
	Overview: each target object is represented by a center point. When training, the target is not to find such center point directly, but to find a good fit for its points cloud.
	1. Backbone: Model architecture is not important, since you can just plug in any NN module. There are four NN structures in centerNet which can be used based on different computation/performance trade off. Hourglass for up sampling. 
	2. Link/Nect: Change the number of channel. 
		- 3 x 3 conv to 承上 backbone
		- Relu to add non-linearity.
		- 1 x 1 to change the number of channel - 启下: The purpose of 1 x 1 is to coordinate with the downstream functional head. 
		- Center Heatmap: 128 x 128 x 80
			- Depict object using their center points.
			- Describe center point by heatmap: points cloud distribution described by probability distribution. 
			- One class one channel
			- Regress focal loss: alpha = 2, beta = 4
			- Using 3 x 3 max pool as a way to NMS
		- Cons: too expensive for cases which has many classes.
	3. Functional head
	4. Offset: 128 x 128 x 2 -> (512 -> 128, if the regression is on 128 x 128, then the error will be amplified on the raw input. The solution is compensaing discretization.) Predict the error/offset and put it back.
	5. Size: 128 x 128 x 2 -> W and H
	6. Other heads: 128 x 128 x n
	7. The loss function is consisted of three parts: center heatmap, offset, size. 


Question: 
1. In Line 664 of the yolo.cfg, randomly 320-608 is enabled/implemented by image resizing?
2. The anchor height is fixed, but the image size is flexiable, would it be problem?
3. Route layer to look back, why is that? Do they use the previous layer's results as one of the NN's output? What is the purpose for Route layer?
4. What is the relation structural among yolo layers?






