## Tricks
### Activation function
	1. Relu
		- Non-differentiable at 0: easy to trapped in local minimum which more steep valley, since it is non-differentiable.
		- Non-zero centered, zipzag when back propagation. All w_i moves along same direction. Use the w_1 and  diagram. As a result, more distance will be travelled until reaching to the target. Also, more likely to encounter the local minimum. 
		- 0 when x < 0. Lose infomationwhen x < 0.
	2. Swish: originate from LSTM's gate.
		- Self-gate: a*sigma(a)
		- Unbounded above: avoid saturation
		- Bounded below: Strong regularization for large negative numbers. It limited the number of parameters, therefore, has the effect of regularization. 
		- Non-monotonicity: no died neuron for small negative
		- Smoothness: less sensitive to init and LR. 
	3. Mish
		- More robust than swish, but not beat Relu 100% times. 


2. Loss: detection loss
	1. L1, L2, smooth L1 loss
		- L1's gradient is constant at negative and positive segment, therefore, it is hard to converge to high accuracy.
		- L2: Early stage is not very stable since the loss is very big.
		- Smooth L1 is a specific case of huber loss. 
			* Coordinates participate in computing separately: should consider lx, ly, lw,lh together. 
			* Different predicted boxes have same loss, therefore, it is impossible to distinguish which bbox is better, given the same loss. 
	2. IoU loss
		- When no interception, no distinguish between cases.
		- When the IoU is the same, no distinguish between cases.
	3. GIoU(General): 在没有相交的情况下也产生出对应的数值。IoU - Ac/Square
	4. DIoU(Distance): 解决了相交情况下： d^2 / c^2
	5. CIoU(Complete): So far we consider the location/distance, but we have not consider the shape. 
		* Overlap area
		* Center distance
		* Shape as aspect ratio: alpha dynamically adjust the importance of the shape


### Acceration
	1. Platform, pre-training and post-training
		- Mathematical operation: addition and multiplication

	2. Networking slimming

	3. Knowledge Distillation







