from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(name='pybind_torch_cuda',
      ext_modules=[
          CUDAExtension('pybind_torch_cuda',
                        ['pybind_torch_cuda/pybind_torch.cu'])
      ],
      cmdclass={'build_ext': BuildExtension})
