from tkinter import *
from tkinter import ttk
import random
import time

root=Tk()
root.title('Sorting Vizualizer')
root.config(bg='black')

selected_alg=StringVar()
data=[]

def drawData(data):
    canvas.delete('all')
    c_height=380
    c_width=1200
    x_width=c_width/(len(data)+1)
    offset =30
    normdata=[i / max(data)for i in data]
    for i, height in enumerate(normdata):
        x0=i*x_width+offset+10
        y0=c_height - height *340
        x1=(i+1)*x_width+offset
        y1=c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill="#BB2CD9")
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))
    root.update_idletasks()

def BubbleSort():
    global data
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                drawData(data)
                time.sleep(0.0002)
    
def Selectionsort():
    global data
    for i in range(len(data)): 
        min_idx = i 
        for j in range(i+1, len(data)): 
            if data[min_idx] > data[j]: 
                min_idx = j        
        data[i], data[min_idx] = data[min_idx], data[i] 
        drawData(data)
        time.sleep(0.02)


def Generate():
    global data
    minvalue=int(minentry.get())
    maxvalue=int(maxentry.get())
    size=int(sizeentry.get())
    data=[]
    for _ in range(size):
        data.append(random.randrange(minvalue,maxvalue+1))
    drawData(data)




UI_frame=Frame(root,width=1330,height=200,bg='#25ccf7')
UI_frame.grid(row=0,column=0,padx=10,pady=5)

canvas=Canvas(root, width=1330,height=450,bg='#0A79DF')
canvas.grid(row=1,column=0,padx=10,pady=5)



Button(UI_frame,text='Selection sort',command=Selectionsort,bg='#4834DF').grid(row=0,column=4,padx=5,pady=5)
Button(UI_frame,text='Bubble Sort',command=BubbleSort,bg='#4834DF').grid(row=0,column=3,padx=5,pady=5)

Label(UI_frame,text='size : ',bg='#25ccf7').grid(row=1,column=0,padx=5,pady=5,sticky=W)
sizeentry=Entry(UI_frame)
sizeentry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

Label(UI_frame,text='Min value : ',bg='#25ccf7').grid(row=1,column=2,padx=5,pady=5,sticky=W)
minentry=Entry(UI_frame)
minentry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

Label(UI_frame,text='Max value : ',bg='#25ccf7').grid(row=1,column=4,padx=5,pady=5,sticky=W)
maxentry=Entry(UI_frame)
maxentry.grid(row=1,column=5,padx=5,pady=5,sticky=W)

Button(UI_frame,text='Generate',command=Generate,bg='#4834DF').grid(row=0,column=2,padx=5,pady=5)


root.mainloop()