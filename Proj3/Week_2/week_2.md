## Basic concept review

### Transpose convolution network
	1. 卷积到矩阵乘法的过度: 把输入矩阵拉成一维，把kernal变换成矩阵，输出为一维
	2. transpose卷积同样可以转化为矩阵乘法
	3. 反向传播和tranpose的关系：
		- tranpose的output维度大于input的维度
		- backpropgation: dx = K^T * dy
		- 结论: 转置卷积和反向传播之间可以相互转化实现
	4. Diluted convolution
	5. 转置卷积可以被用作上采样和反向传播
	6. 转置卷积的stride对应原来卷积的stride，因为转置卷积的stride都为1.


### FCN: Full convolution network: no fully connection layers
	1. Semantic segmentation: pixel-wise classification
	2. The motivation to have down-sampling is to decrase the amount of computation VS having all the layer to be FCN
	3. VGG -》 FCN: output m x n x 21
		- VGG只有3X3的卷积核
		- 去掉fc， 从最后一个layer开始做上采样
		- Padding 100: 确保卷积的输出至少大于1
		- Crop与padding相互对应：确保输出部分对应padding之前的信息
		- 上采样的时候：双线性上采样的精度相对较差。bilinear interpolation的矩阵实现
		- In-network upper sampling：通过Bilinear initialization， 可以保证学习的效率更快。
		- Pooling 5， pooling 4结合起来做上采样可以提高segmentation效果




 

