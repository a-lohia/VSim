# Import create_data.create_data from data_producer/create_data.py to actually use this package.

# This file is used to simulate differential motion. The user inputs a pathway using mouse input
# and the program will generate a video of the pathway with a moving square that follows the path
# and a constant moving background. The program will also generate a reference video of the same
# path with just the outline of the moving square for comparison later.

# go to data_producer folder to adjust the parameters of the produced video (size, length, etc...)

from data_producer.diff_data_producer import *
from data_producer.path_producer import *
import numpy as np
import yaml
from pathlib import Path
import skvideo.io


# -----------------------
# --- Params / Setup ----
# -----------------------

fn = Path(r"data_producer/data_producer_params.yaml")

PARAMS_DIR = fn

with open(PARAMS_DIR) as f:
    params = yaml.safe_load(f)

    save_dir = params["save_dir"]
    ref_save_dir = params["ref_save_dir"]
    fps = params["fps"]
    height = params["height"]
    width = params["width"]
    frames = params["frames"]
    col_width = params["col_width"]
    object_radius = params["object_radius"]
    fill = params["fill"]  # either True or int

seconds = np.ceil(frames / fps).astype(int)

canvas = np.zeros(shape=(frames, height, width), dtype=np.int32)
ref_canvas = np.zeros(shape=(frames, height, width), dtype=np.int32)

# -----------------------
# -- Paths / Creation ---
# -----------------------

# change to a path creation function of your choice if preferred
x, y = manually_create_path(width, height, frames)

canvas = create_moving_background(canvas, fps, seconds)

canvas = apply_object_to_path(canvas, (x, y), object_radius)
ref_canvas = apply_object_to_path(ref_canvas, (x, y), object_radius, fill=fill)


# RENDER

result = encode_to_video(canvas, fps, save_dir)
ref_result = encode_to_video(ref_canvas, fps, ref_save_dir)

if result:
    print("Video saved successfully!")
else:
    print("Error saving video.")
