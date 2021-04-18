## Basic concept review


### Convolution
	1. how to calculation the parameter of the convolution layer: C_in * C_out * w * h 
	2. The computation involved: output dimension * (C_in * C_out * w * h )
	3. Pooling is a specific case of convolution with fixed parameter

### Activation function
	1. Sigmoid	
	2. Relu
	3. Elu
	4. Global average pooling


### Upper sampling: 
	1. unpooling: zero and max unpooling
	2. interpolation: Nearest interpolation, bilinear interpolation, bicubic interpolation
	3. transposed convolution: only recover the shape, not the value.

### Batch normalization: Normalizaiton and transoformation steps
	Training Deep Neural Networks is complicated by the fact that the distribution of each layer’s inputs changes during training, as the parameters of the previous layers change. This slows down the training by requiring lower learning rates and careful parameter initialization, and makes it notoriously hard to train models with saturating nonlinearities.
	We refer to the change in the distributions of internal nodes of a deep network, in the course of training, as Internal Covariate Shift.
	Batch normalization provides an elegant way of reparametrizing almost any deep network. The reparametrization significantly reduces the problem of coordinating updates across many layers.

	1. The motivatin for BN is two folds: 
	2. Two parameter to learn


 

