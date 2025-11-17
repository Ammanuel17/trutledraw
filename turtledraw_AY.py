
import turtle
import math
import sys

def main():
    # Ask user for input filename
    filename = input("Enter the input filename (e.g., turtle-draw.txt): ").strip()
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print("Error opening file:", e)
        sys.exit(1)

    
    screen = turtle.Screen()
    screen.setup(width=450, height=450)
    screen.title("Turtle Draw - by TurtleDraw_xx")
    screen.tracer(0)  

    draw_turtle = turtle.Turtle()
    draw_turtle.hideturtle()
    draw_turtle.speed(0)   # maximum speed
    draw_turtle.penup()    
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()

    
    current_point = None  
    total_distance = 0.0

    
    for raw_line in f:
        line = raw_line.strip()
        if not line:
            continue  

        parts = line.split()
        if len(parts) == 0:
            continue

        key = parts[0].lower()

        # Handle "stop" lines
        if key == "stop":
            draw_turtle.penup()
            current_point = None
            continue

        
        if len(parts) < 3:
            print(f"Ignoring malformed line: {line}")
            continue

        color = parts[0].lower()
        try:
            x = int(parts[1])
            y = int(parts[2])
        except ValueError:
            print(f"Ignoring line with non-integer coords: {line}")
            continue

        try:
            draw_turtle.color(color)
        except turtle.TurtleGraphicsError:
            draw_turtle.color("black")

        if current_point is None:

            
            draw_turtle.penup()
            draw_turtle.goto(x, y)
            draw_turtle.pendown()
            current_point = (x, y)
        else:
            prev_x, prev_y = current_point
            dx = x - prev_x
            dy = y - prev_y
            dist = math.hypot(dx, dy)
            total_distance += dist

            # draw to the new point
            draw_turtle.pendown()
            draw_turtle.goto(x, y)

            current_point = (x, y)

    f.close()

    screen.update()

    w = screen.window_width()
    h = screen.window_height()
    margin_x = 20
    margin_y = 20
    write_x = w/2 - margin_x - 120   
    write_y = -h/2 + margin_y

    writer.goto(write_x, write_y)
    writer.write(f"Total distance: {total_distance:.2f}", align="left", font=("Arial", 12, "normal"))

    print(f"Total distance = {total_distance:.2f}")

    input("Press Enter to close the window...")
    turtle.bye()

if __name__ == "__main__":
    main()
