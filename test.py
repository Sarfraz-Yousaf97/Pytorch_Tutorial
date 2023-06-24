import torch

# torch rand 
# x= torch.rand(3)
# print(x)
# torch empty
# y = torch.empty(1,2,3,4)
# print(y)
# to make all value zeros and ones in 1D, 2D, 3D, ...
# z = torch.zeros(2,2)
# o = torch.ones(2,2)
# print(z, '\n', o)
# we can also add datatype in it 
o = torch.ones(2,2)
print(o.dtype)
# you can chnage by default datatype with this
o = torch.ones(2,2, dtype=torch.int)
print(o.dtype)