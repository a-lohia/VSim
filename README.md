# VSim Differential Motion Simulator

## Overview

VSim is a differential motion simulator designed to create simple toy videos to 
test with potential solutions for the ego-motion problem. Using VSim you can 
create videos of a square moving in a custom path created by your mouse on a 
constantly moving background.

## Installation

## Instructions

### Parameters 

|    Parameter    |                        Description                        | Implemented |
|:---------------:|:---------------------------------------------------------:|:-----------:|
|   `save_dir`    |       Path to where you want to save the test data        |     Yes     |
|    `height`     |            Height of the test data (in pixels)            |     Yes     |
|     `width`     |            Width of the test data (in pixels)             |     Yes     |
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



## License
MIT License
