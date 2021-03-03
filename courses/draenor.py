from courses import course


def create():
    obstacles = [
        course.Obstacle(-5, -300, 6),
        course.Obstacle(-20, -300, 9),
        course.Obstacle(-200, 60, 10),
        course.Obstacle(60, 0, 10),
        course.Obstacle(-120, 100, 8),
        course.Obstacle(0, 250, 7),
        course.Obstacle(270, 0, 8),
        course.Obstacle(200, -200, 9)
    ]

    draenor = course.Course("draenor", obstacles)
    return draenor
