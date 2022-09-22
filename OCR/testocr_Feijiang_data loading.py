import paddle
print(paddle.__version__)




# 我们使用飞桨框架自带的 paddle.vision.datasets.MNIST 完成mnist数据集的加载。
from paddle.vision.transforms import Compose, Normalize
transform = Compose([Normalize(mean=[127.5],
                                std=[127.5],
                                data_format='CHW')])
# 使用transform对数据集归一化
print('download training data and load training data')
train_dataset = paddle.vision.datasets.MNIST(mode='train', transform=transform)
test_dataset = paddle.vision.datasets.MNIST(mode='test', transform=transform)
print('load finished')

