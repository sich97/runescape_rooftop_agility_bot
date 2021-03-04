class Course:
    def __init__(self, name, course_data):
        """
        :param name:
        :type name: str
        :param course_data:
        :type course_data: dict of str
        """
        self.name = name
        self.obstacles = []

        for obstacle_index in range(int(course_data["amount_of_obstacles"])):
            x_option = str(obstacle_index) + "_x"
            y_option = str(obstacle_index) + "_y"
            time_option = str(obstacle_index) + "_time"
            description_option = str(obstacle_index) + "_description"

            sub_steps = []
            amount_of_sub_steps_option = str(obstacle_index) + "_amount_of_sub_steps"
            for step_index in range(int(course_data[amount_of_sub_steps_option])):
                sub_step_x_option = str(obstacle_index) + "_sub_step_" + str(step_index) + "_x"
                sub_step_y_option = str(obstacle_index) + "_sub_step_" + str(step_index) + "_y"
                sub_step_time_option = str(obstacle_index) + "_sub_step_" + str(step_index) + "_time"
                sub_step_description_option = str(obstacle_index) + "_sub_step_" + str(step_index) + "_description"
                sub_steps.append(Obstacle(int(course_data[sub_step_x_option]), int(course_data[sub_step_y_option]),
                                          int(course_data[sub_step_time_option]),
                                          course_data[sub_step_description_option], []))

            self.obstacles.append(Obstacle(int(course_data[x_option]), int(course_data[y_option]),
                                           int(course_data[time_option]), course_data[description_option], sub_steps))

        self.amount_of_obstacles = len(self.obstacles)


class Obstacle:
    def __init__(self, x_pos, y_pos, time_to_complete, description, sub_steps):
        """
        :param x_pos:
        :type x_pos: int
        :param y_pos:
        :type y_pos: int
        :param time_to_complete:
        :type time_to_complete: int
        :param description:
        :type description: str
        :param sub_steps:
        :type sub_steps: list of Obstacle
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.time_to_complete = time_to_complete
        if description and description != "None":
            self.description = description
        else:
            self.description = ""
        self.sub_steps = sub_steps
        self.amount_of_sub_steps = len(self.sub_steps)
