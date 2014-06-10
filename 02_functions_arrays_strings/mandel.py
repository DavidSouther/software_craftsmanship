#!/usr/bin/env python

import sys
from colorsys import hls_to_rgb
from array import array

w = 1024 * 4
h = 768 * 4

header = [
        0, # id_length
        0, # color_map_type
        2, # image_type
        0, # first_entry_index
        0, #
        0, # color_map_length
        0, #
        0, # color_map_entry_size
        0, # x_origin
        0, #
        h % 256, # y_origin
        h / 256, #
        w % 256, # image_width
        w / 256, #
        h % 256, # image_height
        h / 256, #
        24, # pixel_depth
        32, # image_descriptor
        ]

def mandelbrot(c):
    z = c

    for i in xrange(127, -1, -1):
        if abs(z) > 3:
            return i

        z = z ** 2 + c

    return 0

p = []
for y in xrange(h):
    b = 1 - 2. * y / h

    for x in xrange(w):
        a = -2.5 + 3.5 * x / w
        i = mandelbrot(a + b * 1j)
        color = hls_to_rgb((i / 255.0), 0.5, 0.5)
        p.append(int(color[0] * 255))
        p.append(int(color[1] * 255))
        p.append(int(color[2] * 255))

array('B', header + p).tofile(sys.stdout)
