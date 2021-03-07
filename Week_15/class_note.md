## Face Verification

### 人脸遮挡时attention机制
	1. Triplet online hard data mining (OHEM, OHDM)
		- hard data: loss 比较大的
		- online: 在训练的时候动态更新hard data: 按照epoch还是batch更新，需要进行消融实验
	2. SENET and CBAM
		- 本质上是一个信息的筛选：提取出有用的信息
		- 在一个代表图片信息的矩阵上面选取信息，在不同位置产生权重alpha，不同文章的不同点在于alpha的生成方式不同
		- alpha = f(weight, bias) where f is a simple net work
		- Convolution block attention model
		- SENet: Squeeze and excitation -> Channel wise attention: 48*48*96 -> alpha 1*96
		- 消融实验： resnet -> resNet + SENet -> resNet + CMBA
		- Global pooling -> FC -> ReLU -> FC -> sigmond (convert the range of alpha to be 0 and 1)
		- CMBA 增加 global average and max pooling 之后共同进入 shared MLP, 之后对应位置权重相加，最后在进入sigmoid: CAM
		- SAM: Spatial attention Module: Instead of using MLP, apply Conv layer to both maxPool and AvgPool, then add, then feed into sigmoid
		- CMBA: Channel wise attention(What) + Spatial wise attention(where) = volumn wise attention
		- What and where mechanism
		- SAM和CAM顺序，以及Convolution的大小都是通过实验对比来得到

### Center loss 与 Prone
		- Proning is about 去除上一层的卷积核，导致下一层的所有卷积核都要被删除
		- 核心思路时压缩channel的围度

### Data augumentation - 通过landmark detection
		- 通过facial key points的检测，勾画出口罩的位置，然后mute掉数据




###
Question:
1. 如何驱使模型的attentin放到非遮挡的部分
2. Adjust learning rate 在实践中一般都会优于固定的学习率吗
3. 先用不带口罩训练，再去用带口罩的数据fine tune，这样和一起用两类数据直接一起训练的优劣的对比？




