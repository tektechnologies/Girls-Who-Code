# Starter Code
# import turtle

# parent = turtle.Turtle()
# kid = turtle.Turtle()

# kid.shape('turtle')

# parent.up()
# parent.setx(100)
# parent.sety(200)
# parent.down()

# parent.color('red')

# parent.right(90)
# parent.forward(300)
# parent.up()
# parent.forward(50)
# parent.down()
# parent.forward(50)

# kid.right(90)
# kid.forward(120)
# kid.left(90)
# kid.forward(200)
# importing turtle allows us to use code that we didnt write to excute the code we
# are going to write. This code lives else where and 'import' allows our code to
# call that code 
import turtle

# Turtle with a capitol T is a Constructor function that will create us a
# 'turtle object'
# Then we can 'assign' that turtle we created to the variable called parent
parent = turtle.Turtle()
# we do the same thing for this turtle we created and called 'kid'
kid = turtle.Turtle()
# using a variable allows us to store some information in memeory that we can access
# later in this case we are going to want to use our new turtles called parent and kid

# using our kid turtle we can use the '.' or dot operator to access a method
# called 'shape' which gives our kid the shape of a turtle
kid.shape('turtle')
parent.shape('turtle')


parent.up()

parent.setx(100)
parent.sety(200)

parent.down()

parent.color('blue')
kid.color('green')

parent.right(90)
parent.forward(300)
parent.up()
parent.forward(50)
parent.down()
parent.forward(50)

parent.back(50)
parent.up()
parent.back(50)
parent.down()
parent.back(300)
parent.left(90)

parent.up()
parent.setx(0)
parent.sety(0)
parent.down()

kid.right(90)
kid.forward(120)
kid.left(90)
kid.forward(200)



