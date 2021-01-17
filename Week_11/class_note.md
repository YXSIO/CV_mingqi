## FaceBadgetNet
### Code Structre
	- Train.py
		1. data preparation: FDDataset
			- Key method: __getitem__
				- 切片程序: augumentor
		2. Dataloader: key argument train_dataset
		3. Model class: FusionNet - Net
			- encoder: resNet 18
			- res1, res2, res3
				- forward
					- self.conv1 = nn.Sequential(self.e
                          self.e
                          self.e
                          self.p
						self.conv2 = self.encoder.layer1
						self.conv3 = self.encoder.layer2

			- Res4: self._make_layer(BasicBlock,  128*3, 256, 2, stride=2)
			- Res5: self._make_layer(BasicBlock,  256, 512,  2, stride=2)
				- BasicBlock

### Improvement: SE-Net
	- Attention: Create a new set of weights and let NN to get the attention.
		1. Pixel wise weight
		2. Channel wise weight
			- Global average pooling.
				- 1 x 1 x c -> FC -> ReLU -> FC -> Sigmoid: very similar to the bottle neck. 
		3. SE ResNet model. 
			- The skip connect provides the weights to the Feature map. 

### Acyclic cosine annealing learing rate schedule
	- Snapshot ensemble training. 




