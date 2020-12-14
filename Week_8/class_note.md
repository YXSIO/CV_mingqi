## Tricks
### Training flow chart
    - ArgumentParser: data cfg and model cfg parser. 
        - Initial model: model = Darknet(opt.model_def).to(device) 
            * Create module_list = create_modules(self.module_defs): modules = nn.Sequential() Define stage
                - "convolutional": bn, relu, conv2D
                - "maxpool", "uppersample", "route", "shortcut"
                - "yolo": calculate the output, loss and the encoding/decoding
        - Load the dataset
        	- torch.utils.data.DataLoader(dataset, batch_size=opt.batch_size, ...)
        - Initialize the optimizer
        	- torch.optim.Adam(model.parameters() 
        - For each epoch:
            - model.train()
            - for batch_i, (_, imgs, targets) in enumerate(dataloader):
                - Forward: loss, outputs = model(imgs, targets)    # 对应darknet中的forward: execuate stage
                    - targets is from the dataloader
                	- Darknet layers: 
                		- "convolutional", "upsample", "maxpool", "route", "shortcut" :  x = module(x)  
                		- "yolo" layers: x, layer_loss = module[0](x, targets, img_dim) 
                    		- x.shape: b x 255 x 13 x 13 (anchor 6, 7, 8)
                    		- compute_grid_offsets
                       	 		- 1. 针对不同size的feature map (13x13, 26x26, 52x52), 求出不同grid的左上角坐标
                       	 		- 2. 将(0, 416)范围的anchor scale到(0, 13)的范围
                    		- 将prediction的x,y,w,h放到grid中: decoding - the original predicted result is between [0,1]
                    			- Test: 进一步把prediction从grid level放到原图的尺寸
                    			- Train: encode the loss between anchor and the ground truth.
                    				- build target: On the grid level, for each ground truth box, find its corresponding best anchor and fill the obj_mask and non_obj_mask. encoding and using the IOU to compute the cls mask, obj mask and onn-obj mask using anchor, prediction and ground truth. 
                    				- loss: three parts: 
                        				- regression loss only consider the obj_mask
                        				- conf loss consider both obj_mask and non_obj_mask
                        				- cls loss consider only obj_mask
                    		- Add the loss from yolo layer
                    		- yolo_outputs.append(x)
                    	- layer_outputs.append(x)
                - Backward: loss.backward()
                - Log training metrics
            - Log validation metrics

   - Notes: 
   		- Decoding: going from [0,1] -> grid level -> image level
   		- Encoding: imge level (image, target) -> grid level

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
	3. Forward within each class can be called implicitly? 
	x, layer_loss = module[0](x, targets, img_dim) 

	forward(self, x, targets=None, img_dim=None): The x in the forward is the input x of module or the output? And why?







