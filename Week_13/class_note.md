## Face Verification

### How to find 张三 in the group
	1. One VS all: not very practical when the number of class is huge。 Solution: 通过比对来verify
	2. CNN 分类的各种不变性
			- 光照不变
			- 尺度不变
			- 旋转不变
			- 年龄不变
		在提取feature之后，做对比，基于各种不变性。提取特征的方式，通过训练分类器，实质是得到一个好的特征提取器。
		虽然有各种的不变性，但是data augumentation还会提供value，因为他给模型提供了更多的场景，可以更好的保留各种不变性。（In other words, 各种不变性 does not comes for free）
	3. 分类问题和比对问题之间的差异


### 构造FaceID - FaceNet 
	1. Image -> align -> face vector
		- 分类器的基本架构：
			cbrp64 -> cbrp256 -> cbrp64 -> fc -> fc -> softmax
	2. Normalization is important before measuring the similarity
		- L1 norm and L2 norm and Lm norm 
		- The range of Eculidean distance is between (0, sqrt(n))
		- Cosine distance
		- Histogram similarity
	3. When training the verificaiton for human face.
		- MSE is better than cross entropy. 
			- This is because: cross entropy 
	4. How to improve
		- 对于分类问题 cross entropy is good，对于特征提取问题，MSE is better
		- 同一样本的不同image之间的距离 应该小于 不同样本之间的距离: cross entrophy 的组间距离很小
		- Triplet loss: max(0, d_s - d_ns + 1)
			- anchor, pos, neg
			- 考虑极端情况 triplet loss = 0 -> d_s = 0, d_ns = 1 which is the ideal
			- d_s - d_ns < alpha: alpha is the margin. 
	5. Challenge: 样本选取的时候随机性很大，导致triplet loss的variation会很大，导致训练相对不稳定
		- OHEM: Online hard example mining
			- 一次loss计算，涉及三次forward calculation
			- MSE and Cross Entrophy 结合
		- OHNM: Online hard negative mining
			- Negative samples: twins
			- 本质是增加难以区分样本的比例，从而增强模型的学习能力
			- 10 people, 3 image from each person. 30 * 2 * 27, 在此基础上应用OHEM和OHNM

### LFW and vggface2
	- LFW

### EER and ROC	
	- Threshold
	- ROC 的计算




###
Question:
1, 如何决定哪一些weight可以去掉（Experimentation？Or theory?）
2, 是否有风险mute掉重要的weights
3, 决定哪一个channel剪裁掉的时候，为什么要归一化， 归一化本身不改变顺序啊？




