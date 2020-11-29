## Code 
### Code Structure
1. yolov3.cfg define the hyper parameter and the model structure
2. Model structure is loaded into the Module structure. Instead of bulid the model with code, it is due to legacy to directly read in the model architecture from config file. 
3. Route and shortcut layer, the first one is concatenate the later one is add.
4. Yolo Layer. 
	- Network output the offset: tx and tx which should be between 0 and 1. 
	- Compute grid offset gives us the coordinate of the cell of the final feature map and the normalized width and height. 
	- Decode: Combine the offset and the grid coordinate to generate the shape of bbox on the feature map.
	- Map the bbox from feature map to the original image. Direct multiplication the stride. 
	- Encode: 
5. obj_mask = ByteTensor(nB, nA, nG, nG).fill_(0) and noobj_mask describe which anchor box in the cell is compared with groud positive and negative bboxes.
6. build_targets generates masks & tx, ty, tw, th(encoding)· After we could calclualte the loss and use optimize to find the tx, ty, tw, th betweeen the prediction and anchor. In the end, deconde to may the prediction to the raw image.  
7. Understand the darkNet forward and yolo forward calculation. The esssence for forward calculation is to compute the loss, the yolo forward calls build_target in step (6).
8. Train.py details the forward and backward calculation, followed by logging the metrics for each batch/epoch. Entry point model(imgs, targets)

### Package structure
1. Config
	- Coco data
	- Yolo config
2. Data
	- Image
	- Label
	- Classes.names
	- Train.txt
	- Test.txt
3. Util


### Four major component
1. Input: Data augmentation
	- Mixup: Mix within batch, two image is good enough. 
	- Cutout: size is more important than shape. Normalize first before cut. GridMask avoid cutout useful part. 
	- CutMix: Mix the label and feature of different images. Two option: use lambda to control the balance of two lables or take two labels both into account. 
	- Mosaic: Enhance the background complex, increase the batch size. The final loss will also need to be adjusted with the ratio parameter. 
2. Network itself: Relu, Swish, Mish
3. Related with training: 
	- Regularization
		1. label smoothing(soft label) is adding an disturbation to serve as regularization. 
		2. dropBlock: drop out performance is random and is not effective for convolution layer. 
	- Loss: L1, L2, smooth L1 loss, IoU loss, GIoU, DIoU, CIoU
4. Output

### Running on custom dataset


### Understand the output
1. mAP
2. Interpolated Precision: It is simply the highest precision value for a certain recall level. 
3. IoU helps us in determining whether a predicted box is a true positive, false positive or false negative.
	- If IoU > 0.5 then it is a true positive.
	- If IoU< 0.5 it is a false positive and.
	- If IoU > 0.5 but object is miss classified then it will be a false negative.
4. To calculate AP we will take the sum of the interpolated precision at 11 different recall levels starting from 0 to 1(like 0.0, 0.1, 0.2, …..)
5. for mAP: average over each class.


### Key concept
1. Bbox is the prediciton output which can be used to compare with the ground truth. 
2. Anchor is the input initial guess. 


Question: 
1. What is the DarkNet in Yolo?
2. Multi-scale training 如何适应每张图片的size不一致？如何使得最后Yolo层的output都是13x13？






