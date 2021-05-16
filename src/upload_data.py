from tkinter import *
from tkinter import filedialog
from typing import TextIO

from DataSets import *


def browse_file():  # Browse and upload file from explorer, to use in future

    file = filedialog.askopenfile(initialdir="/", title="Select a File",
                                  filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))


def open_file(path, mode):
    global selection
    selection = "DataSets/" + path + ', ' + mode
    print(selection)


def upload_data(main_screen):
    global data_screen

    data_screen = Toplevel(main_screen)
    data_screen.geometry("300x450")
    data_screen.title("Uplad danych")

    Label(data_screen, text="Wybierz Upload albo Usunięcie danych", bg="#49A", width="300", height="2",
          font=("Arial", 13)).pack()
    Label(data_screen, text="").pack()

    Button(data_screen, text="Uplad", height="2", width="30", command=lambda: browse_file()).pack()
    Label(data_screen, text="").pack()

    Button(data_screen, text="Iris", height="2", width="30", command=lambda: open_file('iris.tab', 'r')).pack()
    Button(data_screen, text="Heart_disease", height="2", width="30",
           command=lambda: open_file('heart_disease.tab', 'r')).pack()
    Button(data_screen, text="Titanic", height="2", width="30", command=lambda: open_file('titanic.tab', 'r')).pack()
    Button(data_screen, text="ZOO", height="2", width="30", command=lambda: open_file('zoo.tab', 'r')).pack()

   # Button(data_screen, text='cofnij', height="1", width="4", command=lambda: data_screen.destroy()).pack()
