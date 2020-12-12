## Tricks
### Acceration
	1. Platform, pre-training and post-training
		- Mathematical operation: addition and multiplication
		- Network design
		  1. MobileNets
			-  V1
				- Step 1: Depthwise convolution: Dk * Dk * M * Df * Df
				- Step 2: 1 x 1 convolution
				- Step 3: Dep / Ori = 1/D_k^2
			-  V2
				- Inverted residuals: expand -> transfer -> reduce
				- Linear bottleneck: element wise add without relu
			- V3 SENet: squeeze excitation Net
				- Squeeze: global average pooling
				- Excitation: Sigmoid - FC - Relu - FC - Sigmoid
				- Scale: channel wise multiplicaiton
				- h-swish is a function of Relu6
		  2. Shuffle Net
				- Group convolution is the general case of depth-wise convolution.
				- Shuffle to make the each subgroup has the global info.
		  3. Efficient Net
				- Compound model scaling: figure out the network structure by the computer. 
				- Channel number, layer number, resolution. 
				- Use memory, flops to contrain the grid search. 

	2. Networking slimming
		- Model quantization: on the hardware level, change the float bit from 32 to int 8 bit. The compression is through mapping.
		- Relu6 is designed to reduce the info lose duirng quantization. It contrain the weights distribution to not to be long-tail distributed. 
		- Model pruning
			- Too flexiable
		- Network slimming
			- Channel pruning: light weight channel could be removed. 
			- Pipeline: train origianl model -> load trained model + prune layers -> finetune pruned model.
			- How to decide which channel to choose: select operation followed by batch normalization operation. BN will give weight to each channel through gamma. 


	3. Knowledge Distillation

	Question: 
	1. What is the meanning of Gamma for BN?
	2. Why it is associated with each channel?







