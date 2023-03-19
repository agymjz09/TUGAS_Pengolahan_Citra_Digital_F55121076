# Nama  : Agym Mahaputra Romy Barlianta
# Nim   : F55121076
# Kelas : B

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2


class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.pic = None
        self.canvas = None
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Citra", menu=file_menu)
        file_menu.add_command(label="Input Citra", command=self.open_image)

        edit_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Perbaikan Citra", menu=edit_menu)
        edit_menu.add_command(label="Penajaman Citra", command=self.sharpen_image)
        edit_menu.add_command(label="Penghalusan Citra", command=self.smooth_image)
        edit_menu.add_command(label="Normal Gambar", command=self.show_original_image)

    def create_widgets(self):
        self.canvas = Canvas(self.root, width=400, height=400, bg='gray')
        self.canvas.pack()

        Label(self.root, text="Agym Mahaputra Romy Barlianta", font=("Times New Roman", 12), pady=7).pack()
        Label(self.root, text="F55121076", font=("Times New Roman", 12), pady=7).pack()
        Label(self.root, text="Kelas B", font=("Times New Roman", 12), pady=7).pack()

    def open_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.pic = cv2.imread(path)
            self.show_image(self.pic)

    def show_image(self, image_data):
        image_tk = ImageTk.PhotoImage(Image.fromarray(image_data))
        self.canvas.create_image(0, 0, anchor=NW, image=image_tk)
        self.canvas.image = image_tk

    def show_original_image(self):
        if self.pic is not None:
            self.show_image(self.pic)

    def sharpen_image(self):
        if self.pic is not None:
            gray = cv2.cvtColor(self.pic, cv2.COLOR_BGR2GRAY)
            sharp = cv2.Laplacian(gray, cv2.CV_64F)
            self.show_image(sharp)

    def smooth_image(self):
        if self.pic is not None:
            gray = cv2.cvtColor(self.pic, cv2.COLOR_BGR2GRAY)
            smooth = cv2.GaussianBlur(gray, (5, 5), 0)
            self.show_image(smooth)


if __name__ == '__main__':
    root = Tk()
    root.title("Aplikasi Perbaikan Citra Agym Mahaputra Romy Barlianta F55121076")
    root.configure(pady=35)
    editor = ImageEditor(root)
    root.mainloop()
