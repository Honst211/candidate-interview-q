"""
通常，神经网络以“线性变换->激活函数->线性变换->激活函数->线性变化...”的形式进行一系列的变换。

一个2层的神经网络如何实现？
随着层数的增加，参数的管理会变得复杂。请创建一个简化参数管理机制。
"""


import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 生成假数据
np.random.seed(42)
num_samples = 10
num_features = 5
X = np.random.rand(num_samples, num_features)
y = np.random.randint(0, 2, size=(num_samples,))

# 1. 权重的初始化
input_size = X.shape[1]
hidden_size = 64  # 假设隐藏层大小为64
output_size = 1  # 假设输出大小为1（二分类问题）

model = nn.Sequential(
    nn.Linear(input_size, hidden_size),
    nn.ReLU(),
    nn.Linear(hidden_size, output_size),
    nn.Sigmoid()  # 使用 Sigmoid 函数作为输出层的激活函数，用于二分类问题
)


# 2. 神经网络的推理
def predict(x):
    # 将模型设为评估模式，不进行梯度计算
    model.eval()
    with torch.no_grad():
        # 将输入数据转为 Tensor 类型
        x_tensor = torch.tensor(x, dtype=torch.float32)
        # 使用模型进行推理
        output = model(x_tensor)
        # 返回预测结果
        return output.item()  # 假设输出是一个标量，使用 item() 获取其值


# 3. 神经网络的训练
criterion = nn.BCELoss()  # 二分类问题使用二元交叉熵损失函数
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 使用随机梯度下降优化器

# 将训练数据转为 Tensor 类型
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32).view(-1, 1)  # 将标签 reshape 成列向量

# 训练神经网络
num_epochs = 100
for epoch in range(num_epochs):
    # 将模型设为训练模式，开启梯度计算
    model.train()

    # 前向传播
    outputs = model(X_tensor)
    loss = criterion(outputs, y_tensor)

    # 反向传播及优化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 打印训练过程中的损失
    print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')
