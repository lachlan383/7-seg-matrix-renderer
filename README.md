# 7-seg-matrix-renderer
A prototype image renderer for an arbitrary matrix of 7-segment displays. All source code is contained in [7seg.py](https://github.com/lachlan383/7-seg-matrix-renderer/blob/main/7seg.py) (requires Python 3.x and the Python pygame module).

### Sample Input:
<p align="center"><img src="https://raw.githubusercontent.com/lachlan383/7-seg-matrix-renderer/main/sample.png" width="250"/></p>

### Sample Output (20x8 digits):
<p align="center"><img src="https://raw.githubusercontent.com/lachlan383/7-seg-matrix-renderer/main/out1.png" width="250"/></p>

### Sample Output (32x12 array):
<p align="center"><img src="https://raw.githubusercontent.com/lachlan383/7-seg-matrix-renderer/main/out2.png" width="400"/></p>

## Explanation
I have long been planning to build a large digital display made entirely from 7-segment LED modules. The first step I took was to create a prototype renderer to understand how to map a normal digital image into individual brightness levels for each LED in a typical 4-digit module. This Python program uses the pygame module for it's graphics utilities, and is designed to visualize and test one method of taking an ordinary digital image constructed of square pixels and mapping this onto an arbitrary matrix of red LED 7-seg displays.

I have completed this initial stages of the required hardware:

<img src="https://raw.githubusercontent.com/lachlan383/7-seg-matrix-renderer/main/hardware%20prototype.jpg" width="300"/>

This image shows an 8x4 (8 sets of 4 digits with 7-segments each) composite module I have built, with independent control over every single LED segment.
