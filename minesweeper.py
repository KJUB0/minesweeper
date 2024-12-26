from tkinter import *
import time

width = 7
height = 7
policka = width*height
half = int(height/2)

mapa = []
for i in range(0,height*width):
    mapa.append(0)

print(len(mapa))

window = Tk()
window.title("Moje prve okno")
window.geometry("640x280")

canvas = Canvas(window, bg='white')
canvas.pack(anchor=CENTER, expand=True, fill=BOTH)

###################################
### CODE TO FILL MAPA GOES HERE ###



### CODE TO FILL MAPA ENDS HERE ###
###################################

def drawMap():
    global mapa

    # compute tile width/height based on the total canvas width/height
    tw = canvas.winfo_width() / width
    th = canvas.winfo_height() / height

    # go through all policka
    for index in range(0,policka):
        # vyplnenie policok
        if mapa[index] == 1:
            color = 'black'
        elif mapa[index] == 2:
            
        elif mapa[index] == 3:
            
        elif mapa[index] == 0:
            

        # compute position
        x = index % width
        y = index // width

        # render
        canvas.create_rectangle(x*tw, y*th, (x+1)*tw, (y+1)*th, fill='white', outline="black")

while True:
    drawMap()
    window.update()