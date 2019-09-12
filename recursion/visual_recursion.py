import turtle


MY_TURTLE = turtle.Turtle()
MY_WIN = turtle.Screen()


# Function which draw a spiral recursively
def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


draw_spiral(MY_TURTLE, 100)
MY_WIN.exitonclick()


# Function draw tree recursively (some kind of fractal)
def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-15, t)
        t.left(40)
        tree(branch_len-15,t)
        t.right(20)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75, t)
    my_win.exitonclick()


main()

