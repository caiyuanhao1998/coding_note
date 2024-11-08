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
import torch
import torch.nn as nn
import torch.nn.functional as F
from einops import rearrange

class SelfAttention(nn.Module):
    def __init__(self, dim=64, head_num=8):
        super(SelfAttention, self).__init__()

        self.dim = dim
        self.head_num = head_num
        self.dim_head = self.dim // self.head_num

        # to_q, to_k, to_v 的计算是在外部计算
        # 即对某一个 feature embedding 来完全计算
        self.to_q = nn.Linear(dim, dim)
        self.to_k = nn.Linear(dim, dim)
        self.to_v = nn.Linear(dim, dim)

        self.proj_out = nn.Linear(dim, dim)
        self.positional_encoding = nn.Parameter(torch.zeros(1,1,dim))
        self.layernorm = nn.LayerNorm(dim)
    
    def forward(self, x):
        '''
            input - x: [b, n, c]
            return - out: [b, n, c]
        '''
        x = x + self.positional_encoding
        q_inp = self.to_q(x)
        k_inp = self.to_k(x)
        v_inp = self.to_v(x)

        # split q, k, v into different heads in channel dimension
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> b h n d', h=self.head_num), 
                        (q_inp, k_inp, v_inp))

        attn = (q @ k.transpose(-2, -1)) / torch.sqrt(self.dim_head)
        attn = attn.softmax(dim=-1)
        x = attn @ v
        x = rearrange(x, 'b h n d -> b n (hd)')
        out = self.proj_out(x)
        out = self.layernorm(x + out)

        return out
```


4. 写一个 ImageTokenizer - 将图像分成一系列的小块, 然后将每个小块编码为一系列的向量表示

```py

import torch
import torch.nn as nn
import torch.nn.functional as F
from einops import rearrange

class ImageTokenizer(nn.Module):
    def __init__(self, image_size, patch_size, dim, in_channels=3, patch_dropout_p = 0):
        super().__init__()
        
        assert image_size % patch_size == 0

        num_patches = (image_size // patch_size) ** 2
        self.image_size = image_size
        self.patch_size = patch_size
        self.dim = dim

        # use conv to patchify and embed the image
        self.conv = nn.Conv2d(in_channels = in_channels, out_channels = dim, kernel_size = patch_size, stride = patch_size)
        
        # positional embedding
        self.pos_embed = nn.Parameter(torch.zeros(1, num_patches, dim))
        nn.init.trunc_normal_(self.pos_embed, std=0.02)

        # dropout
        self.patch_dropout = nn.Dropout(patch_dropout_p)

    def forward(self, x):
        '''
            input: (b, c, h, w)
            output: [b, num_patches, patch_dim]
        '''
        x = self.conv(x) # b, c, h, w -> b, c, num_patches.sqrt(), num_patches.sqrt()
        x = rearrange(x, 'b c m m -> b c (mm)') 
        x = x.transpose(1, 2) # b, num_patches, c
        x = self.patch_dropout(x + self.pos_embed)

        return x
```



5. 写一个简单的 diffusion 模块 - 主要是记清楚前向的公式和后向的公式

```py
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

# diffusion 一般是设置 beta 参数
class SimpleDiffusion(nn.Module):
    def __init__(self, sampling_steps=1000, beta_start=1e-4, beta_end=0.02):
        super().__init__()
        self.sampling_steps = sampling_steps

        # setting the series of betas and alphas linearly
        self.betas = torch.linspace(betas_start, betas_end, sampling_steps)
        self.alphas = 1 - self.betas
        self.alphas_bar = torch.cumprod(self.alphas, dim=0)
    
    # forward noising process
    def forward_diffusion(self, x0, t):
        noise = torch.randn_like(x0)
        xt = torch.sqrt(self.alphas_bar[t]) * x0 + torch.sqrt(1-self.alphas_bar[t]) * noise
        return xt, noise

    
    # reverse denoising process
    def reverse_diffusion(self, xt, t, denoiser):
        noise_pred = denoiser(xt,t)
        xo_pred = (xt - torch.sqrt(1-self.alpha_bar[t]) * noise_pred) / torch.sqrt(self.alpha_bar[t])
        xt_prev = torch.sqrt(self.alpha_bar[t]) * x0_pred + torch.sqrt(1-self.alpha_bar[t]) * noise_pred
        return xt_prev
```








6. 写一个空洞卷积 - 把卷积核内部参数之间的距离扩大以增大感受野

```py
import torch
import torch.nn as nn
import torch.nn.functional as F

class DilatedConv2D(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding=0, dilation=1):
        super().__init__()
        self.conv = nn.Conv2D(in_channels=in_channels, out_channels=out_channels, stride=stride, padding=padding, dilation=dilation)
    
    def forward(self, x):
        x = self.conv(x)
        return x
```