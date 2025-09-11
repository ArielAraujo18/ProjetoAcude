import tkinter as tk
import math

def draw_heart(canvas, center_x, center_y, size, color):
    points = []
    for angle in range(0, 360, 2):
        rad = math.radians(angle)
        x = center_x + size * (16 * math.sin(rad)**3)
        y = center_y - size * (13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad))
        points.extend([x, y])
    canvas.create_polygon(points, fill=color, outline=color, smooth=True)

def main():
    window = tk.Tk()
    window.title("Heart Drawing")
    canvas = tk.Canvas(window, width=400, height=300, bg='white')
    canvas.pack()

    center_x = 200
    center_y = 150
    size = 15
    color = 'red'
    draw_heart(canvas, center_x, center_y, size, color)

    window.mainloop()

if __name__ == "__main__":
    main()