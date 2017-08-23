#!/usr/bin/env python

import time

import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(0.5)
width, height = unicorn.get_shape()


colors = {
    'red': {'r': 255, 'g': 0, 'b': 0},
    'green': {'r': 0, 'g': 255, 'b': 0},
    'blue': {'r': 0, 'g': 0, 'b': 255},
    'yellow': {'r': 255, 'g': 255, 'b': 0},
    'orange': {'r': 255, 'g': 128, 'b': 0},
    'purple': {'r': 255, 'g': 0, 'b': 255},
    'cyan': {'r': 0, 'g': 255, 'b': 255},
    'gray': {'r': 128, 'g': 128, 'b': 128},
}

patterns = [
    [
        {'x': 0, 'y': 7,  'color': 'blue'},
        {'x': 1, 'y': 5,  'color': 'blue'},
        {'x': 1, 'y': 6,  'color': 'blue'},
        {'x': 2, 'y': 5,  'color': 'blue'},
        {'x': 3, 'y': 5,  'color': 'blue'},
        {'x': 4, 'y': 5,  'color': 'blue'},
        {'x': 5, 'y': 5,  'color': 'blue'},
        {'x': 6, 'y': 5,  'color': 'blue'},
        {'x': 6, 'y': 6,  'color': 'blue'},
        {'x': 7, 'y': 7,  'color': 'blue'},
        {'x': 5, 'y': 4,  'color': 'blue'},
        {'x': 5, 'y': 3,  'color': 'blue'},
        {'x': 4, 'y': 2,  'color': 'blue'},
        {'x': 3, 'y': 2,  'color': 'blue'},
        {'x': 2, 'y': 3,  'color': 'blue'},
        {'x': 2, 'y': 4,  'color': 'blue'},
    ]
]

for pixels in patterns:
    for pixel in pixels:
        unicorn.set_pixel(
            pixel['x'],
            pixel['y'],
            colors[pixel['color']]['r'],
            colors[pixel['color']]['g'],
            colors[pixel['color']]['b']
        )

unicorn.show()
time.sleep(5)
