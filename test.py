import tkinter as tk
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
import cv2

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Crea dos botones para reproducir el video y mostrar imágenes de la webcam
        self.button1 = tk.Button(self, text='Reproducir vídeo', command=self.play_video)
        self.button1.pack()
        self.button2 = tk.Button(self, text='Mostrar webcam', command=self.show_webcam)
        self.button2.pack()

        # Crea un widget para mostrar el video o las imágenes de la webcam
        self.view = QtMultimediaWidgets.QVideoWidget(self)
        self.view.show()

    def play_video(self):
        # Crea un reproductor de vídeo y establece la ruta del archivo de vídeo a reproducir
        self.player = QtMultimedia.QMediaPlayer(self.view)
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile('ruta/del/video.mp4')))
        self.player.play()

    def show_webcam(self):
        # Abre la webcam y crea un reproductor de vídeo
        self.cap = cv2.VideoCapture(0)
        self.player = QtMultimedia.QMediaPlayer(self.view)

        # Crea un bucle para mostrar imágenes de la webcam
        def show_frame():
            # Lee una imagen de la webcam
            ret, frame = self.cap.read()
            if ret:
                # Convierte la imagen a formato QImage y establece como contenido del reproductor de vídeo
                image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                self.player.setMedia(QtMultimedia.QMediaContent(QtMultimedia.QMediaContent.fromImage(image)))
                self.player.play()
                # Vuelve a llamar a la función para seguir mostrando imágenes
                QtCore.QTimer.singleShot(1, show_frame)
        show_frame()

if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()