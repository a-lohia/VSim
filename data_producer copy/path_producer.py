__all__ = ["create_path", "manually_create_path"]

import cv2
import numpy as np
import pygame
import pygame.gfxdraw


def create_path(
        height: int, width: int, frames: int, construction_function: callable, x_0=None
) -> tuple[np.ndarray, np.ndarray]:
    """
    Creates a path made by a discrete set of coordinates for the object to follow.
    :param height: canvas height
    :param width: canvas width
    :param frames:
    :param construction_function:
    :param x_0: Optional if you want to give a set of x coordinates to evaluate on
    :return: coordinates of the path as a tuple of numpy arrays
    """

    if x_0 is None:
        x = np.rint(np.linspace(0, width, frames)).astype(int)
    else:
        x = x_0
    y = np.rint(construction_function(x)).astype(int)

    return x, y


def manually_create_path(
        height: int, width: int, frames: int
) -> tuple[np.ndarray, np.ndarray]:
    """
    Create a path for the object to follow manually. When run correctly, it opens a pygame window and tracks your
    mouse movements and samples coordinates.
    :param height: canvas height
    :param width: canvas width
    :param frames:
    :return: coordinates of the path as a tuple of numpy arrays
    """

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((height, width))
    clock = pygame.time.Clock()
    running = True
    i = 0
    dt = 0

    x, y = np.zeros(frames, dtype=np.int32), np.zeros(frames, dtype=np.int32)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_x, current_y = pygame.mouse.get_pos()
        x[i], y[i] = current_x, current_y

        pygame.gfxdraw.pixel(
            screen,
            current_x,
            current_y,
            (255, 255, 255),
        )

        pygame.display.flip()
        dt = clock.tick(120) / 1000

        if i == frames - 1:
            running = False

        i += 1

    pygame.quit()

    return x, y
