#Challange Link
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json



def turnRight():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()
    

for step in range (1,7):
    move()
    turn_left()
    jump()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
