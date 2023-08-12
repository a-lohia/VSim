# VSim Differential Motion Simulator

## Overview

VSim is a differential motion simulator designed to create simple toy videos to 
test with potential solutions for the ego-motion problem. Using VSim you can 
create videos of a square moving in a custom path created by your mouse on a 
constantly moving background.

https://github.com/a-lohia/VSim/assets/96156566/e67944f1-5f7d-455b-870f-8d6913689d9a

https://github.com/a-lohia/VSim/assets/96156566/22ff62f1-6dcd-4f0b-8776-85418b54da09

## Installation

Clone this repository. Then run `pip install -r requirements.txt` to install. 
If you want to convert these videos to DVS, install v2e sim by cloning the 
[v2e repository](https://github.com/SensorsINI/v2e) as well

## Instructions

### Parameters 

|    Parameter    |                        Description                        | Implemented |
|:---------------:|:---------------------------------------------------------:|:-----------:|
|   `save_dir`    |       Path to where you want to save the test data        |     Yes     |
| `ref_save_dir`  |  Path to where you want to save the reference test data   |     Yes     |
|    `height`     |            Height of the test data (in pixels)            |     Yes     |
|     `width`     |            Width of the test data (in pixels)             |     Yes     |
|    `frames`     |                     Number of frames                      |     Yes     |
|      `fps`      |            Frames per second of the test data             |     Yes     |
|   `col_width`   | Width of the columns in the moving background (in pixels) |     Yes     |
| `object_radius` |          Radius of the moving object (in pixels)          |     Yes     |

### Instructions to use

1. Add the parameters to the `test_data_params.yaml` file
    - `save_dir` is the path to where you want to save the test data
    - `height` is the height of the test data (in pixels)
    - `width` is the width of the test data (in pixels)
    - `fps` is the frames per second of the test data
    - `col_width` is the width of the columns in the moving background (in pixels)
    - `object_radius` is the radius of the moving object (in pixels)
2. run `main.py` to create the test data (This is in manual path mode, 
so you will have to manually create the path with your mouse)
   - You can enter a discrete path instead of the create-your-own in the `main.py` file

## Credits

Written by Arya Lohia for the IRIS project at [Parsa Research Lab at GMU](https://mason.gmu.edu/~mparsa/)

## License
MIT License
