## Face Verification

### Face embedding 的提升之路
	1. Triplet的写法
		- 可以完成组内距离小，组间距离大


	2. L2 constrained softmax loss
		- 尽量使得各个weight之间相互正交
		- softmax is for classificaiton, the purpose is to have high value of Y^*
		- embedding requires the disance between sample within the same category close.


### FaceNet
	1. Challenge: 样本选取的时候随机性很大，导致triplet loss的variation会很大，导致训练相对不稳定
		- OHEM: Online hard example mining
			- 一次loss计算，涉及三次forward calculation
			- MSE and Cross Entrophy 结合
		- OHNM: Online hard negative mining
			- Negative samples: twins
			- 本质是增加难以区分样本的比例，从而增强模型的学习能力
			- 10 people, 3 image from each person. 30 * 2 * 27, 在此基础上应用OHEM和OHNM

### VGGFace
	1. Metric learning
	2. 先用softmax，在用triplet loss 做训练（先后做）

### Centor Loss
	1. softmax 进行分类
	2. Centerloss 进行类内的压缩 （辅助：同时做，把两个loss一起定义到总体的loss中）
	3. 类中心点是不断update的
		两种方式得到中心点
			- 统计的方法：求组内各个样本的均值。 但是中心点不是真实的中心点
			- 把center参数化：通过梯度的优化去求解ceter

### Large Margin Cosine Loss - LMCL
	1. 调节w 使得w 和 x 之间的夹角更小
	

### Arc Face
	1. 把margin放到cosine函数的内部计算里面
	2. Geodesic Distance





###
Question:
1, VGGFace中先后用两个loss做训练，所以算是two stage的算法吗？
2, 两个stage 的模型架构是不一样的吗？相当于model了两个问题？
3, 上节课中的课后的代码中triplet的选取是完全随机，并没有应用Online hard example training 对吗？




