#!/usr/bin/env python

import time

import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(0.5)
width, height = unicorn.get_shape()


colors = {
    'red': {'r': 255, 'g': 0, 'b': 0},
    'green': {'r': 0, 'g': 255, 'b': 0}
}

pixels = [
    {'x': 0, 'y': 0,  'color': 'red'},
    {'x': 1, 'y': 0,  'color': 'green'},
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
