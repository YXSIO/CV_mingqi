## FaceBadgetNet
### The major difference with objection detection
	1. Facial detection has more uniformed feature, compared with objection detection, where there are many classes with its own characters. 
	2. 关键点检测在精读上take a step further，所以在训练的时候对数据集需要更加specific的要求。
	3. 对Precision 和 recall的要求比较高： 非活体检测为活体penalty较高。

### 基本模型
	1. 分类器模型: ResNet based model
		- Chanllenge
			1. 当人脸倾斜的时候检测的效果有所下降。
			2. 样本不均衡
			3. 样本的相似度很高
			4. 细粒度分类问题: 整体上差别较小，细节上差别较大

	2. Patch-based Feature
		- Focus on the patches(detials) rather than the whole image. 
		- How to get the patches, which, how many
			- Randomly choose the patch, since the spoof-specific discriminative information exists in the whole face area.
		- Multi-mode, RGB, Depth, IR to stack these channel wise and feed into a CNN. 
			- For each mode, build a separate CNN and then fuse them together.

	3. Multi-stream fusion with MFE（random Modality Feature Erasing）
		- 融合方式：add/concat;两者对于整体网络参数辆的影响不同
			- Since the feature distributions of different modalities are different, the author choose to concate instead of add of the feature maps. 
		- 参数过多容易造成过拟合：dropout -》 dropblock -〉dropmode: MFE.
		- Flight overfitting: Skip connection provide different model structures

	4. Training:
		- Original image： 112 x 112: 跟模型匹配
		- 32 x 32 as input size. 剪切，对齐 
		- SGD: weight decay 0.0005, momentum: 0.9
		- 学习率的调整：cosine annealing learning rate schedule

	5. Evaluation
		- 不同的patch大小对于ACER有较大影响
		- Whether fusion or not 也有影响



### CASIA-SURF dataset
	1. RGB, Depth, IR

Question: 
1. Multi-scale training in yolo: 通过去除了FC layer，使得模型可以accept any size of input. 但是如何保证输出的图像仍然是13 x 13的呢？
2. Yolo中的reorg操作，将浅层信息和深层信息融合。由于深层和浅层的dimension不一致，所以需要reorg来缩减浅层的dimension，但可以增加channel的数量。


