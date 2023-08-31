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


def create_data(params_dir: str) -> None:
    """
    This method is used to simulate differential motion. params dir is a path to a .yaml file in the format of
    `template.yaml,` or shown below:

    > save_dir: path to save the video (MUST HAVE .mp4 extension, or it will not work)
    > ref_save_dir: path to save the reference video (ground truth) (MUST HAVE .mp4 extension, or it will not work)
    > height: e.g., 180
    > width: e.g., 240
    > frames: e.g., 600
    > fps: e.g., 120
    > col_width: e.g., 20
    > object_radius: e.g., 25
    > fill: int; if fill = -1, it will fill, if int >= 0, it will be the thickness of the outline (0 is border)

    REQUIRED: FFMPEG must be installed on your machine and added to path to compile the video.

    Running this method will open a Pygame window where the user can draw a path with the mouse for the time in
    params.yaml
    The user inputs a pathway using mouse input
    :param params_dir: path to a .yaml file in the format of `template.yaml`
    :return: None (saves an .mp4 video to save_dir and ref_save_dir)
    """

    # -----------------------
    # --- Params / Setup ----
    # -----------------------

    with open(params_dir) as f:
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

    seconds = np.ceil(frames / fps).astype(int)  # calculate duration of the video produced

    canvas = np.zeros(shape=(frames, height, width), dtype=np.int32)  # initialize canvas (will be filled for the video)
    ref_canvas = np.zeros(shape=(frames, height, width), dtype=np.int32)  # initialize reference canvas (placeholder)

    # -----------------------
    # -- Paths / Creation ---
    # -----------------------

    # change to a path creation function of your choice if preferred
    x, y = manually_create_path(width, height, frames)

    canvas = create_moving_background(canvas, fps, seconds)

    canvas = apply_object_to_path(canvas, (x, y), object_radius)
    ref_canvas = apply_object_to_path(ref_canvas, (x, y), object_radius, fill=fill)

    # -----------------------
    # ------- Render --------
    # -----------------------

    result = encode_to_video(canvas, fps, save_dir)
    ref_result = encode_to_video(ref_canvas, fps, ref_save_dir)

    if result:
        print("Video saved successfully!")
    else:
        print("Error saving video.")
