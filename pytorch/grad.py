## In this we will learn about Gradient calculation with auto gurad

## diff b/w torch.randn() and torch.rand() is 
## torch.randn() is normal distribution while torch.rand() is uniorm distribution

import torch

x = torch.randn(3, requires_grad=True)

# print(x)
# ## add backword
# y = 2+x
# print(y)
# ## mul backword
# z = y*x*3
# print(z)

# ## to add mean function in it

# m = y.mean()
# # #above value makes an scaller value to vector value 
# m.backward()
# print(x.grad) # it will give us value like dm/dx means derrivative related
# ## backword function is only used in vector

# vector_value = torch.tensor([0.12, 0.2, 0.001], dtype=torch.float32)
# ## above is again vector value
# z.backward(vector_value) ## dx/dx

# print(x.grad)



## prevent from tracking the gradient
## we hav three methods for it
## 1-
# x.requires_grad_(False) 
## we have to mention _ with end of function name it will modify variable in place of first otherwise you might get error  
print(x)
## 2-
## detech metthod create a new vector with same values 
d = x.detach()
print(d)
## 3-
with torch.no_grad():
    t = x* 3
    print(t)


