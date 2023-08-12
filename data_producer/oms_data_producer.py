__all__ = ["create_moving_background", "apply_object_to_path", "encode_to_video"]

import cv2
import numpy as np
from tqdm import tqdm
import skvideo.io


# discreet path along circle of radius 10
# all these extra numbers are for transformations that make the circle centered and line up and such
#     path_indices = (
#         np.rint(np.linspace(156, 356, 300)).astype(int),
#         np.rint(np.sqrt(100**2 - (np.linspace(156, 356, 300) -256)**2) + 256).astype(int)
#     )
#     path_indices_2 = (
#         np.rint(np.linspace(156, 356, 300)).astype(int),
#         (-1 * np.rint(np.sqrt(100**2 - ((np.linspace(156, 356, 300)) -256)**2)).astype(int)) + 256
#     )


def create_moving_background(
        canvas: np.ndarray,
        fps: int,
        seconds: int
) -> np.ndarray:
    """
    Create a moving background for the object to move on.
    :param canvas: 3d NumPy array of shape (frames, height, width)
    :param fps: frames per second
    :param seconds: number of seconds to run the video for
    :return: modified canvas with moving background
    """
    frames, height, width = canvas.shape
    # TODO: make sure that the shape should be width + frames (just a guess right now)
    placeholder = np.zeros(shape=(width + frames, height, width), dtype=np.int32)

    populated = False  # set to true when the first column reaches the other side

    counter = 0
    # 512 is to account for the time for the first column to reach other side
    for i in range(width + fps * seconds):

        # set counter to 0 every 16 frames
        if i % 8 == 0 and counter != 8 and counter != 0:
            counter = 0

        # every 16 frames create a column
        if counter < 8:
            placeholder[i, :, 0] = 255

        # for each column of 255, move it over 1 frame
        if i > 0:
            # video_frames[i-1] is the previous frame
            indices = np.where(placeholder[i - 1] == 255)

            # indices[1] is the column indices there are 265 repeats for each column,
            # therefore we use a set to remove duplicates
            cols = set(indices[1])
            # cols.remove(height)
            cols = sorted(list(cols))

            # j is the column
            for j in range(len(cols)):
                col = cols[j]

                # erases from the tail end of the column
                # if the column, 8 to the left of the current column, is also a white column, remove it
                if col - 7 in cols and col - 6 in cols:
                    placeholder[i, :, col - 7] = 0

                # re-add the intermediate parts of the column
                placeholder[i, :, col] = 255

                # as long as the column is not the last one, add another column next to it
                if col < width - 1:
                    placeholder[i, :, col + 1] = 255
                else:
                    if not populated:
                        populated = True
                        # print(i)

        counter += 1

    # TODO: Again, confirm that width is supposed to be here
    canvas = placeholder[width:fps * seconds + width]
    return canvas


def apply_object_to_path(
        canvas: np.ndarray, path: tuple[np.ndarray, np.ndarray], object_radius: int, fill: bool = True,
) -> np.ndarray:
    """
    Apply the object to the path.
    :param canvas: 3d NumPy array of shape (frames, height, width)
    :param path: tuple of two 1d NumPy arrays of shape (frames,) representing the x and y coordinates of the object
    :param object_radius: radius/size of the object
    :param fill: Optional whether to fill the object or not
    :return: an updated canvas with the object applied along the path given
    """
    frames, height, width = canvas.shape
    if fill:
        mode = -1
    else:
        mode = None  # if you just want the outline of the object

    for x, y, frame in zip(path[0], path[1], range(frames)):
        # creates a rectangle at the current position
        canvas[frame] = cv2.rectangle(
            canvas[frame],
            (x - object_radius, int(y + object_radius)),
            (x + object_radius, int(y - object_radius)),
            (128, 128, 128),
            mode  # fill the rectangle
        )

    return canvas


def encode_to_video(canvas: np.ndarray, fps: int, output_dir: str) -> bool:
    """
    Encode the frames to a video.
    :return: True if successful, False otherwise
    """

    # skvideo.setFFmpegPath("~/opt/homebrew/Cellar/ffmpeg/6.0/bin/")

    try:
        writer = skvideo.io.FFmpegWriter(output_dir, inputdict={"-r": str(fps), '-pix_fmt': "gray"},
                                         outputdict={'-vcodec': 'libx264', '-pix_fmt': "gray", '-r': str(fps)},
                                         verbosity=1)
        for i in tqdm(range(canvas.shape[0]), desc="writing video"):
            writer.writeFrame(canvas[i])
        writer.close()
    except Exception as e:
        print(e)
        return False

    return True
