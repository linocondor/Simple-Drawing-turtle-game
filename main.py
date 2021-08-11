from  turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


#move functions
def move_forwards(): 
    tim.forward(10)
def move_backward(): 
    tim.backward(10)
def rotate_right(): 
    tim.right(10)
def rotate_left(): 
    tim.left(10)
def clear_screen(): 
    screen.reset()


screen.listen()
screen.onkeypress(key="Up", fun=move_forwards)
screen.onkeypress(key="Down", fun=move_backward)
screen.onkeypress(key="Right", fun=rotate_right)
screen.onkeypress(key="Left", fun=rotate_left)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()