import torch
import copy

a = {"a":torch.Tensor([1,2,3]),\
    "b":torch.Tensor([4,5,6])}

b = copy.copy(a)

print(a)
print(b)

a["a"][1] = 7

print(a)
print(b)