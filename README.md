# VSim Differential Motion Simulator

## Overview

VSim is a differential motion simulator designed to create simple toy videos to 
test with potential solutions for the ego-motion problem. Using VSim you can 
create videos of a square moving in a custom path created by your mouse on a 
constantly moving background.

https://github.com/a-lohia/VSim/assets/96156566/d1a0867c-7e8e-48cd-800c-aa66963e6d9d

https://github.com/a-lohia/VSim/assets/96156566/e021065f-a8fe-42bd-a9ec-d2e0fb214380

## Installation

Clone this repository. Then run `pip install -r requirements.txt` to install. 
If you want to convert these videos to DVS, install v2e sim by cloning the 
[v2e repository](https://github.com/SensorsINI/v2e) as well

> [!IMPORTANT]  
> VSim requires ffmpeg to be installed on your system

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

1. Add the parameters to your `params.yaml` file
    - `save_dir` is the path to where you want to save the test data **USE .mp4 or it will not work**
    - `ref_save_dir` is the path to where you want to save the reference test data (for use as "ground truth" in the future) **USE .mp4 or it will not work**
    - `height` is the height of the test data (in pixels) 
    - `width` is the width of the test data (in pixels)
    - `fps` is the frames per second of the test data
    - `col_width` is the width of the columns in the moving background (in pixels)
    - `object_radius` is the radius of the moving object (in pixels)
    - `fill` is the amount of fill (-1 is filled, 0 is border) > 0 is thickness
2. call `create_data.create_data("path_to_params.yaml")` to create the test data (This is in manual path mode, 
so you will have to manually create the path with your mouse)
   - You can enter a discrete path instead of the create-your-own by assembling your own function and following the steps in `test.py`

## Credits

Written by Arya Lohia for the IRIS project at [Parsa Research Lab at GMU](https://mason.gmu.edu/~mparsa/)

## License
MIT License
