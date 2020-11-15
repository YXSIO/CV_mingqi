## One stage:
	1. YOLO V1: 
		-Confidence = probability * IOU: 1, if it is an object, 2, how good it is in terms of IOU
		-The output for V1 is 7 X 7 X (5 X B + C): 5 = probability + coorinate
		-The loss function is consisted of three parts: bounding box regresssion + confidence + 
		-Pros: fast
		-Cons: 
			1. not very good at small objects: only 7 x 7 feature map. To improve, we can have finer cells or have more points in the feature map for RCNN. 
			2. Bad for crowed objects, since each cell only predict one object.
			3. The regression is for x, y, sqrt(w), sqrt(h) which is not good.
			4. Deform convolution to solve the problem of 可形变物体
	2. YOLO V2:
		-Add BN
		-Finer grids: 13 X 13
		-Structure perspective: V2 add short cut to combine the physical info(edge and corner) and semantic info together. For a detection problem, it can be decomposed into regression(location) and cls(semantics). 
		-Use reorgnation to merge shallow layers with deep layers, since they are in different size. It is crutial for detection tasks, which consist of regression and classificaiton. 
		-Multi-scale training: to accommodate image with different sizes. 
		-The usage of Anchor. 
	3. YOLO V3:
		-Modularize the NN structure: Each modual contains a Bottle-nect in Resnet. Due to the bottle nect structure, it also helps with back propagation.
		-Multi scale structure for the Network, not only the input has multi scale. e.g. Assuming the input image is 416 x 416. The output can be 13 x 13(Large obj: 32 x 32) or 26 x 26(Mid size: 16 x 16) or 52 x 52 feature map(small size obj: 8 x 8). As a result, the detection of large and small object is separated. 
		-Upper sampling: 
			a. Transpose convolution/de-convolution. Inverse matrix multiplication. 
			b. Interpolate
		-FPN: Feature Pyramid Network. Pros: improve the performance a lot. Cons: computationally expensive. 
	4. YOLO V4:
		Original:
			-Data autmentation: Mosaic to help with the regularization. Increase the batch size in some sense.
			-Self-Adversarial Training: 
				1. Alter input: freeze the weight update during back propagation and let the loss propagation to the input. 
			-CBN -> CmBN: mini-batch is not a constrain any more
			-Modified SAM: Spatial attention model. 
				- Maxpooling and averge pooling -> convolution -> sigmoid. Modified version: directly apply sigmond to the whole feature maps. When combining the attention part with the original featuer map, some part is retained and some part is muted. 
			-Modified PAN: addition -> concatenation.
			-Bag of specials and bag of freebies. 

## RetinaNet
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
	7. Why up sampling: The backbone outputted feature map is too small. 
	8. 又说少需求，就加Other heads



Question: 
1. In RetinaNet, what is FCN?
2. How FPN is used as an architecture in RetinaNet? Output prediction for different feature maps? How the output is compared with the ground truth?
3. Why we need to up-sample on FPN?
4. One class one channel? How is it different from NMIST one nural one class? 







