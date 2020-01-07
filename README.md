# cube-scrambl3r
Rubik's cube program for Lego Mindstorms EV3
based off [David Gilday's MindCub3r](https://www.mindcuber.com/mindcub3r/mindcub3r.html).

Written in [MicroPython, running on ev3dev](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3).

If the links above have become stale, and essential files cannot be located (structure build file, 
MicroPython manual, and SD card image for EV3), you may contact me for backup copies.

<!-- https://drive.google.com/drive/u/0/folders/1jUdjHS22F1zwnxoQA3R3IfTaT3J7NjvH -->

## Current Status
As of January 2020, this program can scramble the cube, and read its scrambled state; it cannot yet
resolve the cube.

- [x] rotate, and flip the cube
- [x] twist a layer
- [ ] scan a cube face (_in progress_)
- [x] scan the entire cube
- [ ] verify a valid cube was scanned
- [ ] integrate [/muodov/kociemba]() for solving
- [ ] solve the cube
