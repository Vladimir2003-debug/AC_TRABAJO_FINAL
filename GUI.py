from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

def visualizarUsuario():   
    global cap

    if cap is not None:
        ret,frame = cap.read()
    
        if ret == True:

            frame = imutils.resize(frame,width=640)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lblVideoUsuario.configure(image=img)
            lblVideoUsuario.image=img
            lblVideoUsuario.after(10,visualizarUsuario)
        else:
            lblinfoVideoPath1.configure(text="Aun no se ha prendido la camara")
            lblVideoUsuario.image = ""
            cap.release()

def visualizarInstructor():   
    global cap

    if cap is not None:
        ret,frame = cap.read()
    
        if ret == True:

            frame = imutils.resize(frame,width=640)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lblVideoInstructor.configure(image=img)
            lblVideoInstructor.image=img
            lblVideoInstructor.after(10,visualizarInstructor)
        else:
            lblinfoVideoPath2.configure(text="Aun no se ha seleccionado un video")
            lblVideoInstructor.image = ""
            cap.release()

def iniciarUsuario():
    global cap

    cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)

    visualizarUsuario()

def iniciarInstructor():
    global cap

    video_path = filedialog.askopenfilename(filetypes=[
        ("all video format",".mp4"),
        ("all video format",".avi"),
        ])
    if len(video_path) > 0:
        lblinfoVideoPath2.configure(text=video_path)
        cap = cv2.VideoCapture(video_path)
        visualizarInstructor()
    else:
        lblinfoVideoPath2.configure(text="No se ha seleccionado un video")
        lblVideoInstructor.image=""
        cap.release()

cap = None
root = Tk()

btnvisualizarUsuario = Button(root,text="Prender Camara",command=iniciarUsuario)
btnvisualizarUsuario.grid(column=1, row=0, padx=5,pady=5,columnspan=1)

btnvisualizarinstructor = Button(root,text="Elegir video Instructor",command=iniciarInstructor)
btnvisualizarinstructor.grid(column=2, row=0, padx=5,pady=5,columnspan=2)

lblinfo2 = Label(root,text="Aun no se ha prendido la camara")
lblinfo2.grid(column=1, row=1)

lblinfoVideoPath1 = Label(root,text="Aun no se ha prendido la camara")
lblinfoVideoPath1.grid(column=1, row=1)

lblinfoVideoPath2 = Label(root,text="Aun no se ha seleccionado un video")
lblinfoVideoPath2.grid(column=2, row=1)

lblVideoUsuario = Label(root)
lblVideoUsuario.grid(column=1, row=2,columnspan=1)

lblVideoInstructor = Label(root)
lblVideoInstructor.grid(column=2, row=2,columnspan=2)

root.mainloop()