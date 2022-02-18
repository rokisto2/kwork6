from functools import partial
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd


class window:

    def __init__(self):
        # Bottom window
        self.old_window = Tk()
        self.old_window.title("Converter")
        self.old_window.minsize(width=560, height=420)
        self.old_window.config(bg='black')

        # Label
        image = Image.open("im.jpg")
        image = ImageTk.PhotoImage(image)
        my_label = Label(image=image)
        my_label.config(bg='black')
        my_label.place(x=17, y=0)

        # Button
        button = Button(text="Start",command=partial(self.button_clicked, self))
        button.place(x=275, y=350)

        self.old_window.mainloop()

    class button_clicked:
        # Singleton
        def __init__(self, window):
            self.file_path = filedialog.askopenfilename(title="Please, choose the initial file")
            self.file = open(self.file_path)
            self.new_window = Tk()
            window.old_window.destroy()
            self.new_window.config(bg="black")
            self.new_window.title("Converter")
            self.new_window.minsize(width=500, height=300)
            self.transfotm()
            self.my_label1 = Label(self.new_window)
            self.my_label1.config(text="Choose the output format of your file", fg="light green", bg="black", font=24)
            self.my_label1.place(x=100, y=20)

            button1 = Button(self.new_window, text="CSV", command=self.button_clicked1)
            button1.place(x=200, y=100)
            button2 = Button(self.new_window, text="XML", command=self.button_clicked2)
            button2.place(x=300, y=100)

        # Facade
        def transfotm(self):
            new_columns = ['Date', 'Time', 'Speed', 'Distance', 'Description']
            data = pd.read_table(self.file, names=new_columns, thousands=',')

            col1 = pd.to_datetime(data["Date"], format='%Y/%d/%m')
            result1 = col1.dt.strftime('%d.%m.%Y')

            col2 = pd.to_datetime(data["Time"])
            result2 = col2.dt.strftime('%H:%M:%S')

            result3 = data["Speed"] * 1.943844

            result4 = data["Distance"] * 0.006214

            result5 = data["Description"]

            self.df = pd.concat([result1, result2, result3, result4, result5], axis=1)

        def button_clicked1(self):
            self.df.to_csv(filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[("CSV file", ".csv")]))
            self.new_window.destroy()

        def button_clicked2(self):
            self.df.to_xml(filedialog.asksaveasfilename(defaultextension='.xml', filetypes=[("XML file", ".xml")]))
            self.new_window.destroy()


window()