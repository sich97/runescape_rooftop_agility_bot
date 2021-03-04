import pyautogui as auto
import time
import data_handler
from classes import *
from anti_bot_detection import *


START_DELAY = 5
MAX_DURATION = 4

ANTI_BOT_DETECTION_CHANCE = 0.1
ANTI_BOT_DETECTION_MIN_PAUSE = 10
ANTI_BOT_DETECTION_MAX_PAUSE = 60 * 4
ANTI_BOT_DETECTION_MIN_DRAG_TIME = 1
ANTI_BOT_DETECTION_MAX_DRAG_TIME = 3


def main():
    available_courses = data_handler.get_available_courses()
    print("You can choose between the following courses: ")
    for course_name in available_courses:
        print(course_name + ", ", end="")
    print("\n")
    chosen_course_name = input("Please type the name of the course you want automated: ")
    chosen_course = Course(chosen_course_name, data_handler.get_course_data(chosen_course_name))
    screen_resolution = auto.size()

    print("You have chosen " + chosen_course.name)
    desired_amount_of_loops = int(input("And how many times would you like to do this course?"))
    print("Please move to the tile in front of the last obstacle and scroll out completely."
          "Then input anything in this program which will start the course in 10 seconds...")
    input()
    time.sleep(START_DELAY)

    # Set camera position
    compass = data_handler.get_compass_pos()
    auto.moveTo(compass[0], compass[1], 1)
    auto.click()
    auto.moveTo(screen_resolution[0] // 2 - 15, screen_resolution[1] // 2 - 5, 0.5)
    auto.drag(0, 100, 1, button="middle")

    completed_loops = 0
    start = time.time()
    while (completed_loops < desired_amount_of_loops) and (time.time() - start < MAX_DURATION * 60 * 60):
        do_course(chosen_course, compass, screen_resolution, ANTI_BOT_DETECTION_MIN_DRAG_TIME,
                  ANTI_BOT_DETECTION_MAX_DRAG_TIME)
        completed_loops += 1


def do_course(course, compass, screen_resolution, anti_bot_detection_min_drag_time, anti_bot_detection_max_drag_time):
    """
    :param course:
    :type course: classes.Course
    :param compass:
    :type compass: list of int
    :param screen_resolution:
    :type screen_resolution: tuple of int
    :param anti_bot_detection_min_drag_time:
    :type anti_bot_detection_min_drag_time: int
    :param anti_bot_detection_max_drag_time:
    :type anti_bot_detection_max_drag_time: int
    :return:
    """
    for obstacle in course.obstacles:
        for sub_step in obstacle.sub_steps:
            auto.moveTo(sub_step.x_pos, sub_step.y_pos, 0.5)
            auto.click()
            time.sleep(sub_step.time_to_complete)
        anti_bot_detection(1 - ANTI_BOT_DETECTION_CHANCE, ANTI_BOT_DETECTION_MIN_PAUSE, ANTI_BOT_DETECTION_MAX_PAUSE,
                           compass, screen_resolution, anti_bot_detection_min_drag_time,
                           anti_bot_detection_max_drag_time)
        auto.moveTo(obstacle.x_pos, obstacle.y_pos, 1)
        auto.click()
        time.sleep(obstacle.time_to_complete)


if __name__ == "__main__":
    main()
