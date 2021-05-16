from tkinter import *
from tkinter import filedialog


def visualizations(main_screen):
    global visualizations_screen
    visualizations_screen = Toplevel(main_screen)

    visualizations_screen.geometry("300x450")
    visualizations_screen.title("Wizualizacje")

    Label(visualizations_screen, text="Wybierz wizualizacje", bg="#49A", width="300", height="2",
          font=("Arial", 13)).pack()

    Checkbutton(visualizations_screen, text="Nazwa wizualizacji").pack()
    Checkbutton(visualizations_screen, text="Nazwa wizualizacji").pack()
    Checkbutton(visualizations_screen, text="Nazwa wizualizacji").pack()
    Checkbutton(visualizations_screen, text="Nazwa wizualizacji").pack()

    Button(visualizations_screen, text='cofnij', height="1", width="4",
           command=lambda: visualizations_screen.destroy()).pack()
