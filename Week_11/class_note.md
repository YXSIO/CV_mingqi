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





