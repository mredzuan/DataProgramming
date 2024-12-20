import torch
print(torch.__version__)

torch.get_default_dtype()



#Attempt to change dtype-----

#torch.set_default_dtype(torch.int)

#torch.set_default_dtype(torch.float64)

tensor_arr = torch.Tensor([[1,2,3], [1,2,3]])


torch.is_tensor(tensor_arr)


torch.numel(tensor_arr)


tensor_uninitialized = torch.Tensor(2, 2)


tensor_initialized_rand = torch.rand(2,2)


tensor_int = torch.tensor([5,3]).type(torch.IntTensor)


tensor_short = torch.ShortTensor([1.0, 2.0, 3.0])

tensor_float = torch.tensor([1.0, 2.0, 3.0]).type(torch.half)


tensor_fill = torch.full((2,6), fill_value=10)


tensor_of_one = torch.ones([2,4], dtype=torch.int32)


tensor_of_zeroes = torch.zeros_like(tensor_of_one)


tensor_eye = torch.eye(5)


non_zero = torch.nonzero(tensor_eye)


#Sparse tensor------------

i = torch.tensor([[0, 1, 1], 
                  [2, 2, 0]])


v = torch.tensor([3, 4, 5], dtype=torch.float32)

sparse_tensor = torch.sparse_coo_tensor(i, v, size=[2,5])
