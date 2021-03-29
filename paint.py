from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename as saveAs
from PIL import Image, ImageTk, ImageGrab

color = 'black'
size = 5
oldx = None
oldy = None
btn1 = 'up'
bg_color = 'white'
rgb_list = (255, 255, 255)

def color_btn():
    global color
    color = askcolor(title='COLOR', color=color)[1]

def bgcolor_btn():
    global bg_color, rgb_list
    rgb_list = []

    bg_color_all = askcolor(title='COLOR', color=bg_color)
    
    bg_color_rgb = bg_color_all[0]
    bg_color = bg_color_all[1]

    canvas.configure(bg=bg_color)

    for i in bg_color_rgb:
        i = int(i)
        rgb_list.append(i)
    rgb_list = tuple(rgb_list)

def eraser_btn():
    global color
    color = bg_color

def size_btn(val):
    global size
    size = val

def reset_btn():
    canvas.delete('all')

def btn1down(event):
    global btn1
    btn1 = 'down'

def btn1up(event):
    global btn1, oldx, oldy
    btn1 = 'up'
    oldx, oldy = None, None


def motion(event):
    if btn1 == 'down':
        global oldx, oldy, line, size

        if oldx is not None and oldy is not None:
            event.widget.create_line(oldx, oldy, event.x, event.y, 
                                    width=size, fill=color,
                                    capstyle=ROUND, smooth=True, splinesteps=36)
        
        oldx = event.x
        oldy = event.y

def save_btn():
    try:
        filename = saveAs(defaultextension='.jpg',filetypes=(("PNG images","*.png"),("JPEG images","*.jpg"),("GIF images","*.gif")))
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + root.winfo_width() 
        y1 = y + root.winfo_height() - 50

        ImageGrab.grab().crop((x, y, x1, y1)).save(filename)

        messagebox.showinfo('Save As', 'image save as...' + str(filename))
    except:
        messagebox.showinfo('Save As', 'failed image save as...' )


def main():
    
    global brush_btn, eraser_btn, color_btn, save_btn, reset_btn, size_btn, bgcolor_btn, paint_btn, open_btn
    global root, canvas

    root = Tk()
    root.configure(bg='#c0c0c0')

    bgcolor_btn = Button(root, text='BACKGROUND', command=bgcolor_btn)
    bgcolor_btn.grid(row=0, column=0)

    eraser_btn = Button(root, text='ERASER', command=eraser_btn)
    eraser_btn.grid(row=0, column=1)

    color_btn = Button(root, text='COLOR', command=color_btn)
    color_btn.grid(row=0, column=2)

    save_btn = Button(root, text='SAVE', command=save_btn)
    save_btn.grid(row=0, column=3)

    reset_btn = Button(root, text='RESET', command=reset_btn)
    reset_btn.grid(row=0, column=4)

    size_btn = Scale(root, from_=1, to=20, orient=HORIZONTAL, command=size_btn)
    size_btn.grid(row=0, column=5)

    canvas = Canvas(root, bg=bg_color, width=800, height=800)
    canvas.grid(row=1, columnspan=6)

    canvas.bind('<Motion>', motion)
    canvas.bind('<ButtonPress-1>', btn1down)
    canvas.bind('<ButtonRelease-1>', btn1up)

    root.mainloop()


if __name__ == '__main__':
    main()