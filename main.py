import pyautogui as auto
import time
import data_handler
from classes import *


START_DELAY = 5
MAX_DURATION = 4


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
        do_course(chosen_course)
        completed_loops += 1


def do_course(course):
    """
    :param course:
    :type course: classes.Course
    :return:
    """
    for obstacle in course.obstacles:
        for sub_step in obstacle.sub_steps:
            auto.moveTo(sub_step.x_pos, sub_step.y_pos, 0.5)
            auto.click()
            time.sleep(sub_step.time_to_complete)
        auto.moveTo(obstacle.x_pos, obstacle.y_pos, 1)
        auto.click()
        time.sleep(obstacle.time_to_complete)


if __name__ == "__main__":
    main()
