import numpy as np
import torch
import torch.nn.functional as F

dtype = torch.float
device = torch.device("cpu")
# N is batch size; D_in is input dimension;
N, D_out = 4, 6

# Version without pytorch
output = np.random.randn(N, D_out)

def my_softmax(nums):
    rst = np.exp(nums) / np.sum(np.exp(nums), axis=1).reshape(4,1)
    return rst

print(my_softmax(output))


# Version with pytorch
output = torch.randn(N, D_out, device=device, dtype=dtype)

print(output)
print(F.softmax(output, dim=1))
print(F.softmax(output, dim=1).sum(axis=1))  # Sums to 1 because it is a distribution!