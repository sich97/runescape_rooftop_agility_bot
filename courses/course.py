class Course:
    def __init__(self, name, obstacles):
        """
        :param name:
        :type name: str
        :param obstacles:
        :type obstacles: list of Obstacle
        """
        self.name = name
        self.obstacles = obstacles


class Obstacle:
    def __init__(self, x_from_centre, y_from_centre, time_to_complete):
        """
        :param x_from_centre:
        :type x_from_centre: int
        :param y_from_centre:
        :type y_from_centre: int
        :param time_to_complete:
        :type time_to_complete: int
        """
        self.x_from_centre = x_from_centre
        self.y_from_centre = y_from_centre
        self.time_to_complete = time_to_complete
