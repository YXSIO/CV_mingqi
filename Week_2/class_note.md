## Two stage detection: Fast RCNN
### Components:
	0. Selective search -> ROI
	1. Deep convNet(B1): Generate the feature map
		- Training: 1:3 ration to prepare the positive and negative samples. 
	2. **ROI projection**(B2): map all the ROI(proposed regions) onto the feature map of the entire image. 
		- Mapping is intuitively find the corner points.
		- Take the int function to the division result.
	3. **ROI pooling**(B3): Convert all the features of each ROI to the same size. 
		- Evenly divide each feature map of ROI into M X M
		- Apply maxpooling to each cell within the M X M.
		- If some feature map is smaller than M X M, then we have to disgard that ROI. 
		- As a result, smaller region's performance is not good. Another reason for this bad performance is due to the twice rounding. (Small rounding on the ROI pooling got amplified on the raw image)
			1. Increase the resolution of feature map
			2. Increase the number of anchor boxes

	3'. **ROI align**: The result is a 7 by 7 matrix. 
		- Pros: 
				1. there is no rounding
				2. Bi-linear interpolation
		- Cons: 
				1. N is hyper parameter
				2. Not all the feature points contributes
	3". **Precise ROI pooling**: 
		1. Find the locaiton of red points with bi-linear interpolation.
		2. Find the average pooling using integration / area. 
		- Pros: solve the cons of ROI align. 
	4. FCs(B4): FC layers cost a lot. 
	5. Milti-task loss: Softmax + regressor (B5)

## Two stage detection: Faster RCNN - end 2 end 
### Improvement
	1. RPN: replace the selective search to generate ROI.
		-Classification:  38 * 50 * 18 (2*9)
			1. Anchor serves as the initial candidate for ROI, similar with the way how we get the bounding box from ROI. 
			2. 9 achors: small, mid, large objects with 3 aspect ratio.
			3. 38 * 50: each point is the center of the anchors. 
			4. 2 is the indicator of background or foreground. 
		-Regression:  1 * 36 (9*4) * 38 * 50 
			1. x, y, w, h
			2. x1, y1, x2, y2
			3. Offset regression: p-a -> g-a; normalize over different anchor sizes so that the regression loss will not be dominated by bigger anchor boxes. 

### Components
	1. Backbone: VGG16/ZFnet
	2. Link/nect 
	3. Heads


Question: 
1. why 38 * 50
2. soft max back propagation interview







