import configparser

DATA_FILE = "data.ini"


def get_available_courses():
    config = open_config()
    return config.sections()


def get_course_data(course_name):
    """
    :param course_name:
    :type course_name: str
    :return:
    """
    config = open_config()
    course = config[course_name]
    resulting_course = {}
    for key, value in course.items():
        if "description" in key:
            resulting_course[key] = value
        else:
            resulting_course[key] = int(value)
    return resulting_course


def get_compass_pos():
    config = open_config()
    compass_pos = [int(config["DEFAULT"]["compass_x"]), int(config["DEFAULT"]["compass_y"])]
    return compass_pos


def set_compass_pos(x, y):
    """
    :param x:
    :type x: int
    :param y:
    :type y: int
    :return:
    """
    config = open_config()
    config.set("DEFAULT", "compass_x", str(x))
    config.set("DEFAULT", "compass_y", str(y))

    with open(DATA_FILE, "w") as configfile:
        config.write(configfile)


def update_course_obstacle(course_name, x, y, obstacle_number, obstacle_sub_step):
    """
    :param course_name:
    :type course_name: str
    :param x:
    :type x: int
    :param y:
    :type y: int
    :param obstacle_number:
    :type obstacle_number: int
    :param obstacle_sub_step:
    :type obstacle_sub_step: int
    :return:
    """
    config = open_config()

    if obstacle_sub_step != -1:
        x_option = str(obstacle_number) + "_sub_step_" + str(obstacle_sub_step) + "_x"
        y_option = str(obstacle_number) + "_sub_step_" + str(obstacle_sub_step) + "_y"
    else:
        x_option = str(obstacle_number) + "_x"
        y_option = str(obstacle_number) + "_y"

    config.set(course_name, str(x_option), str(x))
    config.set(course_name, str(y_option), str(y))

    with open(DATA_FILE, "w") as configfile:
        config.write(configfile)


def open_config():
    config = configparser.ConfigParser()
    config.read(DATA_FILE)
    return config
