## Multi-mode anti-spooty face recogonition
### 人脸识别的一般过程
	1. 人脸检测: 去除背景的干扰
		- OpenCV
		- dlib: key point, bbox
		- mtcnn
	2. 人脸对齐: 位置的归一化 -> Key point detection (landmark) -> 拉伸对齐
	2. 提取特征: CNN feature extration
	3. 相似度比对: 1 - Eucidean distance. 

### 活体检测技术回顾 - Anti-spoofing
	1. Image distortion analysis
		- Design the features
			- Specular relection feature
			- Blurriness feature
			- Chromatic moment
			- Color diversity feature
		- Concate the feature together and make final decision
	2. Colour texture
		- 在RGB空间活体和非活体不是很好区分，但是在其他空间HSV更容易区分
		- 这里用传统的方法，因为CNN需要大量的数据集，活体检测的数据集不容易采集。
		- Generate the histogram from HSV, IR and different color space
	3. Detect 心率
	4. Facebagnet Multi-mode


### 数据集预评价方法
	1. RGB, Depth, IR

	2. CASIA-SURF dataset

### face verificaiton
	1. DeepFace


	Question: 
	1. Multi mode 多模态是怎样的概念
	2. Multi mode 和 Multi label, Meta Learning 的联系与区别
	



