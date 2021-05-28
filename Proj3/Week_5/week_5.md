## Week 5

### 感受野的计算
ASPP， Resnet_astrous
感受野就是输入图像对这一层输出的神经元的影响有多大。

### 数据处理
1. 裁剪
2. 旋转
3. 拉伸
4. 透视
5. 剪切


### 数据加载
一、建立自定义数据处理方法类：如随机擦除，随机裁剪等

class RandomErasing(object):
    def __init__(self,probability=0.5)
    
    def __call__(self, img)
        ...
        return img

二、建立数据预处理组合类实例：如图像翻转，归一化，向量化，擦除等

train_transform = transforms.Compose([
            transforms.Resize((384, 128), interpolation=3),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            RandomErasing(probability=0.5, mean=[0.0, 0.0, 0.0])
        ])

三、建立数据读取类：从本地路径进行数据加载，形成列表等
四、生成torch数据流类实例：


### 数据闭环与主动学习
在机器学习的建模过程中，通常包括样本选择，模型训练，模型预测，模型更新这几个步骤。在主动学习这个领域则需要把标注候选集提取和人工标注这两个步骤加入整体流程，也就是：

机器学习模型：包括机器学习模型的训练和预测两部分；
待标注的数据候选集提取：依赖主动学习中的查询函数（Query Function）；
人工标注：专家经验或者业务经验的提炼；
获得候选集的标注数据：获得更有价值的样本数据；
机器学习模型的更新：通过增量学习或者重新学习的方式更新模型，从而将人工标注的数据融入机器学习模型中，提升模型效果。






 

