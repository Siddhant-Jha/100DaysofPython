#Challange Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json


def turnRight():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
