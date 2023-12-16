from turtle import *


def koch_snowflake_side(side_length, levels):
    if levels == 0:
        forward(side_length)
        return

    side_length /= 3
    koch_snowflake_side(side_length, levels - 1)
    left(60)
    koch_snowflake_side(side_length, levels - 1)
    right(120)
    koch_snowflake_side(side_length, levels - 1)
    left(60)
    koch_snowflake_side(side_length, levels - 1)


def koch_snowflake(side_length, levels):
    for i in range(3):
        koch_snowflake_side(side_length, levels)
        right(120)


if __name__ == "__main__":
    levels = int(input("Enter Koch Snowflake level: "))

    if levels > 7:
        print("Too high level, level will be set to 7")
        levels = 7

    if levels < 0:
        print("Level can't be negative, level will be set to 0")
        levels = 0

    side_length = 300

    speed(0)
    hideturtle()

    penup()
    tracer(False)
    backward(side_length / 2.0)
    pendown()

    koch_snowflake(side_length, levels)

    tracer(True)
    done()
