from distutils.core import setup
from Cython.Build import cythonize

setup(name='Mandelbrot renderer',
      ext_modules=cythonize("mandelbrot.pyx"))
