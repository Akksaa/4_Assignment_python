import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        
        self.cells = []  

        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
                self.cells.append(cell)

        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")
        
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def move_eraser(self, event):
        """Moves eraser and erases overlapping cells."""
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        
        overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for item in overlapping:
            if item in self.cells: 
                self.canvas.itemconfig(item, fill="white")

root = tk.Tk()
root.title("Eraser on Canvas")
EraserCanvas(root)
root.mainloop()
