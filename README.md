# cube-scrambl3r
Rubik's cube program for Lego Mindstorms EV3
based off [David Gilday's MindCub3r](https://www.mindcuber.com/mindcub3r/mindcub3r.html).

Written in [MicroPython, running on ev3dev](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3).

If the links above have become stale, and essential files cannot be located (structure build file, 
MicroPython manual, and SD card image for EV3), you may contact me for backup copies.
<!-- copies at https://drive.google.com/drive/u/0/folders/1jUdjHS22F1zwnxoQA3R3IfTaT3J7NjvH -->

## Current Status
As of January 2020, this program can scramble the cube, and read its scrambled state; it cannot yet
resolve the cube.

- [x] rotate, and flip the cube
- [x] twist a layer
- [x] scan the entire cube
- [x] scan a cube face (_in progress_)
- [ ] reliably read facelet colors
- [ ] verify a valid cube was scanned
- [ ] integrate http://github.com/muodov/kociemba for solving
- [ ] solve the cube

## Cube Scanning and Color Detection

The stock `ColorSensor` can return a `Color` constant, but it does not work well with my cube.
(It may be optimized for Lego brick colors.) Reading RGB instead, returns raw colors
that then need to be categorized.

Idea: collect RGB samples, and run a clustering algorithm to group them into groups, by color. 
White is the color farthest from (0,0,0), and can be used to anchor one cluster. 

Cube color logic helps color detection:
* 6 colors total: Red Blue Green White Yellow Orange
* There are 9 facelets of each color
* Each center facelet is of a distinct color
    * White is opposite Yellow
    * Orange is opposite Red
    * Green is opposite Blue
* The 8 corner pieces are: R-W-G, etc.
* 12 edge pieces are: ...
