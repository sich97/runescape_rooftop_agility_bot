import pyautogui as auto
import courses
import time


START_DELAY = 5


def main():
    available_courses = courses.courses_list.keys()
    print("You can choose between the following courses: ")
    for course_name in available_courses:
        print(course_name + ", ", end="")
    print("\n")
    chosen_course_name = input("Please type the name of the course you want automated: ")
    chosen_course = courses.courses_list[chosen_course_name]
    screen_resolution = auto.size()

    print("You have chosen " + chosen_course.name)
    print("Please move to the tile in front of the last obstacle, then click the compass by the minjimap, then input anything in this program which will start the course in 10 seconds...")
    input()
    time.sleep(START_DELAY)
    set_camera_position(screen_resolution)

    while True:
        do_course(chosen_course, screen_resolution)


def do_course(course, screen_resolution):
    """
    :param course:
    :type course: courses.course.Course
    :param screen_resolution:
    :type screen_resolution: tuple of int
    :return:
    """
    for obstacle in course.obstacles:
        move_mouse_to_centre(screen_resolution)
        auto.move(obstacle.x_from_centre, obstacle.y_from_centre, 0.5)
        auto.click()
        time.sleep(obstacle.time_to_complete)


def move_mouse_to_centre(screen_resolution):
    """
    :param screen_resolution:
    :type screen_resolution: tuple of int
    :return:
    """
    auto.moveTo(screen_resolution[0] // 2 - 15, screen_resolution[1] // 2 - 5, 0.5)


def set_camera_position(screen_resolution):
    """
    :param screen_resolution:
    :type screen_resolution: tuple of int
    :return:
    """
    auto.scroll(-4000)
    move_mouse_to_centre(screen_resolution)
    auto.drag(0, 100, 1, button="middle")


if __name__ == "__main__":
    main()
