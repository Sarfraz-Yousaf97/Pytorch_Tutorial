import numpy
import torch
# x = torch.rand(5, 3) , # here this examle 5 is shows total rows and 3 shows is coulmns
# print(x)
# We can also can rand only rows or coulmns following is example
# x = torch.rand(5,3)
# print(x)
# print(x[:, 0]) # all rows, column 0
# print(x[1, :]) # row 1, all columns
# print(x[1,1]) # element at 1, 1
# print(x[1,1].item()) # for getting actual value onlu use when we have only one value
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
# o = torch.ones(2,2)
# print(o.dtype)
# # you can chnage by default datatype with this
# o = torch.ones(2,2, dtype=torch.int)
# print(o.dtype)

# you can also addition with mathematical operation

# a = torch.rand(2, 2)
# b = torch.rand(2, 2)

# print(a)
# print(b)

# add = a + b
# mull = a * b
# sub = a - b
# div = a / b

# print(add, 'add \n ', mull, 'mull \n ', sub, ' sub \n', div, 'div')



# Size and reshape

# x = torch.rand(4, 4)
# print(x)
# y = x.view(-1, 8)
# print(y)
# # we can also print size on it
# print(y.size())

# converting pytorhc array to numpy array
s = torch.ones(6)
print(s)
d = s.numpy()
print(d)
# print(type(d))
# for addittion in complete array you can 
s.add_(1) # function will be written with _ otherwise it will not work
print(s) # pytorch array
print(d) # numpy array
