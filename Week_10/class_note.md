## Multi-mode anti-spooty face recogonition
### 


Question: 
1. Multi-scale training in yolo: 通过去除了FC layer，使得模型可以accept any size of input. 但是如何保证输出的图像仍然是13 x 13的呢？
2. Yolo中的reorg操作，将浅层信息和深层信息融合。由于深层和浅层的dimension不一致，所以需要reorg来缩减浅层的dimension，但可以增加channel的数量。


