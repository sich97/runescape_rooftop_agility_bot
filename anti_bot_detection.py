import random
import time
import pyautogui as auto


SCREEN_RESOLUTION_MARGIN = 50
MAX_CAMERA_ROTATIONS = 5


def anti_bot_detection(fire_chance, min_pause, max_pause, compass, screen_resolution, min_drag_time, max_drag_time):
    """
    :param fire_chance:
    :type fire_chance: float
    :param min_pause:
    :type min_pause: int
    :param max_pause:
    :type max_pause: int
    :param compass:
    :type compass: list of int
    :param screen_resolution:
    :type screen_resolution: tuple of int
    :param min_drag_time:
    :type min_drag_time: int
    :param max_drag_time:
    :type max_drag_time: int
    :return:
    """
    if random.random() > fire_chance:
        function_index = random.randint(0, 2)
        if function_index == 0:
            pause(min_pause, max_pause)
        elif function_index == 1:
            camera(compass, screen_resolution, min_drag_time, max_drag_time)
        elif function_index == 2:
            movement()


def pause(min_pause, max_pause):
    """
    :param min_pause:
    :type min_pause: int
    :param max_pause:
    :type max_pause: int
    :return:
    """
    pause_duration = random.randint(min_pause, max_pause)
    time.sleep(pause_duration)


def camera(compass, screen_resolution, min_drag_time, max_drag_time):
    """
    :param compass:
    :type compass: list of int
    :param screen_resolution:
    :type screen_resolution: tuple of int
    :param min_drag_time:
    :type min_drag_time: int
    :param max_drag_time:
    :type max_drag_time: int
    :return:
    """
    amount_of_movements = random.randint(1, MAX_CAMERA_ROTATIONS)
    for i in range(amount_of_movements):
        if bool(random.randint(0, 1)):
            x_drag_destination = random.randint(SCREEN_RESOLUTION_MARGIN, screen_resolution[0] // 2 - 15)
        else:
            x_drag_destination = random.randint(screen_resolution[0] // 2 - 15,
                                                screen_resolution[0] - SCREEN_RESOLUTION_MARGIN)

        y_drag_destination = random.randint(SCREEN_RESOLUTION_MARGIN, screen_resolution[1] // 2 - 5)

        drag_time = random.randint(min_drag_time, max_drag_time)

        auto.moveTo(screen_resolution[0] // 2 - 15, screen_resolution[1] // 2 - 5, 0.5)
        auto.dragTo(x_drag_destination, y_drag_destination, drag_time, button="middle")

    auto.moveTo(compass[0], compass[1], 1)
    auto.click()
    auto.moveTo(screen_resolution[0] // 2 - 15, screen_resolution[1] // 2 - 5, 0.5)
    auto.drag(0, 100, 1, button="middle")


def movement():
    print("Anti bot detection function 'movement' not yet defined")
