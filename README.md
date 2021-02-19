# Minimum Viable PyTorch CUDA - Python Binding

**NOTE:** This is basically a clone of
[pybind_pytorch_cuda](https://github.com/nachovizzo/pybind_pytorch)
but using `CUDA` as example. For a full explanaion on the code go check that
repository.

- [Minimum Viable PyTorch CUDA - Python Binding](#minimum-viable-pytorch-cuda---python-binding)
  - [How to build and run this](#how-to-build-and-run-this)
  - [Is this CUDA](#is-this-cuda)

This is a very minimalistic project that aims to build a C++/Python module,
leveraging on the power of PyTorch tools.

## How to build and run this

This is the **most** exciting part. Just run this command:

```shell
pip3 install git+https://github.com/nachovizzo/pybind_pytorch_cuda
```

If you are not that lazy to ask pip to clone the repo for you, you could do
instead:

```sh
pip3 install -e . -r requirements.txt
```

```python
from pybind_torch_cuda import greet; greet()
```

If everything is ok you should get this on your shell:

```shell
Hello Pytorch from CUDA
```

## Is this CUDA

Not really. Not that the only thing that makes this "really" a CUDA program
is the `__global__` tag before the `void Greet()` function. If it wasn't for
that, this source file could be through to any normal `C++` compiler. But the
idea here is not to write `CUDA` code but rather show how to easily bind it
to Python. So this trick serve it purpose.
