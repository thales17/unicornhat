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

pixels = [
    {'x': 0, 'y': 0,  'color': 'red'},
    {'x': 1, 'y': 0,  'color': 'green'},
    {'x': 2, 'y': 0,  'color': 'blue'},
    {'x': 3, 'y': 0,  'color': 'yellow'},
    {'x': 4, 'y': 0,  'color': 'orange'},
    {'x': 5, 'y': 0,  'color': 'purple'},
    {'x': 6, 'y': 0,  'color': 'cyan'},
    {'x': 7, 'y': 0,  'color': 'gray'},
    
]

for pixel in pixels:
    unicorn.set_pixel(
        pixel['x'],
        pixel['y'],
        colors[pixel['color']]['r'],
        colors[pixel['color']]['g'],
        colors[pixel['color']]['b']
    )

unicorn.show()
time.sleep(1)
