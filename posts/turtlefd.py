import turtle

def draw_3d_text(text, font_size):
    turtle.speed(1)
    turtle.color("black")

    for char in text:
        turtle.write(char, font=("Arial", font_size, "bold"))
        turtle.penup()
        turtle.forward(15)  # Move forward to create spacing
        turtle.pendown()

    turtle.done()

def main():
    text_to_write = "Southeast chodnar University"
    font_size = 20

    turtle.penup()
    turtle.goto(-200, 0)  # Starting position on the left
    turtle.pendown()

    draw_3d_text(text_to_write, font_size)

if __name__ == "__main__":
    main()
