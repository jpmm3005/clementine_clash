import torch
import torchvision
from torchvision import transforms, datasets
import ssl
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
ssl._create_default_https_context = ssl._create_unverified_context
data_path = "./data" # You can change this path training = datasets.MNIST( root=data_path, # Specify the directory train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]) )
# import torch from torchvision import datasets, transforms

from torchvision import transforms, datasets

training = datasets.MNIST("", train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
testing = datasets.MNIST("", train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
batch_size=100
trainset = torch.utils.data.DataLoader(training, batch_size, shuffle=True)
testset = torch.utils.data.DataLoader(testing, batch_size, shuffle=True)

for tensor in trainset:
    print(tensor)
    break

x, y = tensor[0][0], tensor[1][0]

print(x)
print(y)

print(x.shape) # notice it's not just 28x28 for the image, but a 1 as well

import matplotlib.pyplot as plt

plt.imshow(x.view(28,28)) # need to use .view(28, 28) to reshape access the image
plt.show()

def hello_world():
    print("print")

hello_world()

class Net(nn.Module):
    def __init__(self):
        super().__init__()

        # 3 hidden layers
        # input, output
        self.fully_connected_1 = nn.Linear(28*28, 64)
        self.fully_connected_2 = nn.Linear(64, 64)
        self.fully_connected_3 = nn.Linear(64, 64)

        # output layer
        self.fully_connected_4 = nn.Linear(64, 10)

        # have defined the layers but no path for the data to take yet

        # Feedforward neural network

    def forward(self, x):
        x = F.relu(self.fully_connected_1(x))
        x = F.relu(self.fully_connected_2(x))
        x = F.relu(self.fully_connected_3(x))
        # we dont want relu on the output layer, instead we want a probability distribution on the model
        x = self.fully_connected_4(x)

        # distributing across the classes of numbers and not the batches
        # dim = 0 will distribute probability across the batch instead of the classes
        return F.log_softmax(x, dim=1)


net = Net()
print(net)

# passing the data in the distribution
X = torch.rand((28,28))
X = X.view(1, 28*28) # need to do .view(-1 or 1) to flatten and avoid dimention error

output = net(X)
print(output)

# output is the actual predictions of the random data, without having weights and biases


# everything that is adjustable in our model
optimizer = optim.Adam(net.parameters(), lr=0.001) # lr = learning rate, size of the step optimizer will take to get to the best place to lower the loss

EPOCHS = 3


class Neuron:

    def __init__(self, weights: int, biases: int, relu):
        self.weights = np.random.rand(batch_size)
        self.biases = np.random.rand()


    def relu(self, tensor) -> int: # need to declare a variable tensor so we can run this in the for loop
        relu_lyr = nn.RelU()
        output_lyr = relu_lyr(tensor)

    def forward(self, tensor):
        sum = np.dot(tensor, self.weights) + self.biases
# in progress