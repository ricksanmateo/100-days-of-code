def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_left():
    turn_left()

while not at_goal():
    if wall_in_front():
       jump()
    else:
        move()