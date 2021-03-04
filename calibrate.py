import winsound
import time
import pyautogui as auto
import data_handler
from classes import *

DELAY = 7


def main():
    print("First we need to make sure the camera is set up properly."
          "Please zoom completely our (and have it stay that way throughout the calibration process)."
          "The next step is to tell the program where the compass icon is located."
          "After you press enter, you have " + str(DELAY + 3)
          + " seconds to hover your mouse over the compass icon."
            "Three short beeps followed by a longer beep indicate that the position of the mouse has been saved.")
    input()
    screen_resolution = auto.size()
    compass = get_position(click_before_done=True)
    data_handler.set_compass_pos(compass[0], compass[1])
    auto.moveTo(screen_resolution[0] // 2 - 15, screen_resolution[1] // 2 - 5, 0.5)
    auto.drag(0, 500, 1, button="middle")
    print("Compass location has been saved.")

    print("Now we need to know which course you are calibrating.")
    available_courses = data_handler.get_available_courses()
    print("You can choose between the following courses: ")
    for course_name in available_courses:
        print(course_name + ", ", end="")
    print("\n")
    chosen_course_name = input("Please type the name of the course you want to calibrate: ")
    chosen_course = Course(chosen_course_name, data_handler.get_course_data(chosen_course_name))
    print("You have chosen " + chosen_course.name)

    print("Please move to the tile in front of the last obstacle."
          "Then input anything in this program to confirm that you are in position.")
    print("Make sure you are zoomed out completely")
    print("We are ready to start calibrating the course. At each obstacle you will hear a single beep."
          "This indicates that the software is waiting for your input."
          "All you have to do then is to press enter into this console."
          "Then, " + str(DELAY + 3)
          + " seconds will pass, and you will hear the same beeps as when you calibrated the compass."
            "By then you should have your mouse cursor hovering over the current obstacle."
            "Do not make any movement between obstacles unless explicitly told so."
            "Usually you are expected to just click on the next obstacle."
            "After the program has acknowledged the mouse position of the current obstacle"
            ", you should click on the obstacle. The program will again notify you when ready for the next obstacle."
            "This will continue until you have completed the entire course."
            "If you fall during the course, exit the software and try again.")

    for obstacle_index in range(chosen_course.amount_of_obstacles):
        for sub_step_index in range(chosen_course.obstacles[obstacle_index].amount_of_sub_steps):
            print(chosen_course.obstacles[obstacle_index].sub_steps[sub_step_index].description)
            input()
            if obstacle_index == 0 and sub_step_index == 0:
                new_position = get_position(click_before_done=True, initial_delay=True)
            else:
                new_position = get_position(click_before_done=True, initial_delay=False)
            data_handler.update_course_obstacle(chosen_course.name, new_position[0], new_position[1], obstacle_index,
                                                sub_step_index)
            time.sleep(chosen_course.obstacles[obstacle_index].sub_steps[sub_step_index].time_to_complete)
        if chosen_course.obstacles[obstacle_index].description:
            print(chosen_course.obstacles[obstacle_index].description)
            input()
        if obstacle_index == 0 and chosen_course.obstacles[obstacle_index].amount_of_sub_steps == 0:
            new_position = get_position(click_before_done=True, initial_delay=True)
        else:
            new_position = get_position(click_before_done=True, initial_delay=False)
        data_handler.update_course_obstacle(chosen_course.name, new_position[0], new_position[1], obstacle_index, -1)
        time.sleep(chosen_course.obstacles[obstacle_index].time_to_complete)

    winsound.Beep(2000, 1000)
    print("Calibration complete. Exiting...")


def get_position(click_before_done=False, initial_delay=True):
    if initial_delay:
        time.sleep(DELAY)
    winsound.Beep(1500, 100)
    time.sleep(0.9)
    winsound.Beep(1500, 100)
    time.sleep(0.9)
    winsound.Beep(1500, 100)
    time.sleep(0.9)
    position = auto.position()
    if click_before_done:
        auto.click()
    winsound.Beep(2000, 1000)
    return position


if __name__ == "__main__":
    main()
