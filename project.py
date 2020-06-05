
import tkinter
import time

WIDTH = 700
HEIGHT = 700

stop = True
last_func = None

def main():
    window = tkinter.Tk()
    window.title("Start Drawing")
    window.minsize(width=WIDTH, height=HEIGHT)

    frame = tkinter.Frame(window, bg="#abb8cf", bd=5)
    frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.1, anchor="n")

    frame_bottom = tkinter.Frame(window, bg="#abb8cf", bd=5)
    frame_bottom.place(relx=0.5, rely=0.85, relwidth=0.9, relheight=0.1, anchor="n")

    canvas = tkinter.Canvas(window, bg="white", height=500, width=800)
    canvas.place(relx=0.5, rely=0.15, relwidth=1, relheight=0.7, anchor="n")

    btn_comp = tkinter.Button(frame, text="Doodle Symmetry", fg='black', command=lambda: set_func(canvas, 'comp'))
    btn_comp.place(relx=0.2, relwidth=0.25, relheight=1)

    btn_solo = tkinter.Button(frame, text="Doodle", fg='black', command=lambda: set_func(canvas, 'solo'))
    btn_solo.place(relx=0.55, relwidth=0.25, relheight=1)

    btn_stop = tkinter.Button(frame_bottom, text="Stop", fg='black', command= watch_dog)
    btn_stop.place(relx=0.2, relwidth=0.25, relheight=1)

    btn_clear = tkinter.Button(frame_bottom, text="Clear", fg='black', command=lambda: canvas.delete("all"))
    btn_clear.place(relx=0.55, relwidth=0.25, relheight=1)
    canvas.bind("<Button-3>", left_click)

    window.mainloop()

def left_click(event):
    global stop
    stop = not stop
    if last_func and (not stop):
        last_func()

def set_func(canvas, type):
    # make the drawing start only after the user click the left button of the mouse
    global last_func
    if type == 'solo':
        last_func = lambda: doodle_solo(canvas)
    elif type == 'comp':
        last_func = lambda: doodle_comp(canvas)

def watch_dog():
    # make the stop button stop the drawing
    global stop
    stop = True

def doodle_solo(canvas):
    global stop
    global last_func
    old_mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    old_mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    while not stop:
        mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
        mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
        canvas.create_line(mouse_x, mouse_y, old_mouse_x, old_mouse_y, fill="black", width=2)
        old_mouse_x, old_mouse_y = mouse_x, mouse_y
        canvas.update()
    last_func = lambda: doodle_solo(canvas)


def doodle_comp(canvas):
    global  stop
    global  last_func
    stop = False

    old_mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    old_mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    while not stop:
        mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
        mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
        canvas.create_line(mouse_x, mouse_y, old_mouse_x, old_mouse_y, fill= "black", width=2)
        canvas.create_line(WIDTH - mouse_x, mouse_y, WIDTH - old_mouse_x, old_mouse_y, fill= "grey", width=1)
        old_mouse_x, old_mouse_y = mouse_x, mouse_y
        canvas.update()
    last_func = lambda: doodle_comp(canvas)


def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas

if __name__ == '__main__':
    main()
