import os
import torch
from torch.utils.ffi import create_extension

#this_file = os.path.dirname(__file__)

sources = ['src/my_lib_nd.c']
headers = ['src/my_lib_nd.h']
defines = []
with_cuda = False

if torch.cuda.is_available():
    raise ValueError( 'There is currently no CUDA support. Please adapt the stn.pytorch CUDA code appropriately.')

    print('Including CUDA code.')
    sources += ['src/my_lib_cuda_nd.c']
    headers += ['src/my_lib_cuda_nd.h']
    defines += [('WITH_CUDA', None)]
    with_cuda = True

this_file = os.path.dirname(os.path.realpath(__file__))
print(this_file)
if torch.cuda.is_available():
    raise ValueError( 'There is currently no CUDA support. Please adapt the stn.pytorch CUDA code appropriately.')
    extra_objects = ['src/my_lib_cuda_kernel_nd.cu.o']
else:
    extra_objects = []

extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

ffi = create_extension(
    '_ext.my_lib_nd',
    headers=headers,
    sources=sources,
    define_macros=defines,
    relative_to=__file__,
    with_cuda=with_cuda,
    extra_objects=extra_objects
)

if __name__ == '__main__':
    ffi.build()