## Deep Learning 类的 coding

1. 写一个简单的 CNN

```py

import torch.nn.functional as F     # 包括了一些激活函数, 池化, padding
import torch.nn as nn               # nn = neural network, 一些神经网络的基本模块, 如卷积之类的

# 基于图像分类写一个 SimpleCNN
class SimpleCNN(nn.module):
    def __init__(self, num_class = 10, dropout_rate = 0.5):
        super(SimpleCNN, self).__init__()   # 让子类能够调用父类的方法, 这里调用初始化

        self.conv1 = nn.Conv2D(in_channels=1, out_channels=16, kernel_size=3, padding=1, stride=1)
        self.conv2 = nn.Conv2D(in_channels=16, out_channels=32, kernel_size=3, padding=1, stride=1)
        self.conv3 = nn.Conv2D(in_channels=32, out_channels=64, kernel_size=3, padding=1, stride=1)

        # 连续过了三次卷积, feature 直接喂到 MLP 当中
        # 输入是 28x28 -> 784 维度向量
        # 中间 channel 数翻倍, 所以, 使用 maxpooling 来降采样
        self.dropout = nn.Dropout(dropout_rate)

        # MLP 输入的维度是 28 / 2 / 2 / 2 = 3.5 向下取整数是 3x3
        self.fc1 = nn.Linear(64*3*3, 128)   # 这里需要把 feature map 展开成 vector
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.linear(64, num_class)
    
    def forward(self, x):
        # 卷积, 激活, 池化 - conv, relu, pooling - conv1
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, kernel_size = 2, stride = 2)

        # 卷积, 激活, 池化 - conv, relu, pooling - conv2
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, kernel_size = 2, stride = 2)

        # 卷积, 激活, 池化 - conv, relu, pooling - conv3
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(x, kernel_size = 2, stride = 2)

        # 使用 view 函数来转换维度
        # (b, c, h, w) -> (b, chw)
        x = x.view(x.size[0], -1)

        # 如果加 dropout 的话, 就是在输入的 feature 上加
        x = self.dropout(x)

        x = F.relu(self.fc1(x))

        x = self.dropout(x)

        x = F.relu(self.fc2(x))

        return x
```




2. 写一个 sparse convolution - 仅对非零元素进行卷积运算


```py
import torch.nn.functional as F
import torch.nn as nn


class SparseConv2D(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0, bias=False):
        super(SparseConv2D, self).__init__()

        # 准备一些属性和一个卷积的操作, 留到后边使用
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.conv = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel_size, stride=stride, padding=padding, bias=False)

    def forward(self, x):
```




3. 写一个 Transformer 的 self-attention

```py
