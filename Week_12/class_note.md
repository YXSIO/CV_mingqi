## FaceBadgetNet
### How to apply to production
	- Two stages:
		1. First anti-spoofing detection
		2. Face verification

### Model compression
	- Pre Training
		1. Mobile net, shuffle net

	- Post Training
		1. 减少某些weights的情况下，尽量保留acc
			- 通过消融实验来决定mute谁
			- Weights level: select theh weight by its absolute value
				- First train, then delete
				- Delete, training EM iteration.
			- Per kernel level
				- Use the L1 and L2 norm 加和排序然后归一化，从而决定删谁，
				- 删除之后，在训练性能又会提升
			- Kernel by group
				- 组间选择删除
			- Pruning the input will also reduce the computation for the following layers. 


###
Question:
1, 如何决定哪一些weight可以去掉（Experimentation？Or theory?）
2, 是否有风险mute掉重要的weights
3, 决定哪一个channel剪裁掉的时候，为什么要归一化， 归一化本身不改变顺序啊？



How to change the number of channels duirng convolution?

What is the bottle neck structure?




