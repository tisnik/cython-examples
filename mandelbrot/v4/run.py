#!/usr/bin/env python
# vim: set fileencoding=utf-8

from sys import argv, exit
from mandelbrot import calc_mandelbrot


if __name__ == "__main__":

    if len(argv) < 4:
        print("usage: python mandelbrot width height maxiter")
        exit(1)

    width = int(argv[1])
    height = int(argv[2])
    maxiter = int(argv[3])
    calc_mandelbrot(width, height, maxiter)
