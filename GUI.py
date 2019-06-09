import sys
from tkinter import *
from Model import Model

def main():

    master = Tk()
    master.title("KogniteLab")
    model = Model(16)

    def build():
        model.AddLayer(10)
        print("layer added")

    def summary():
        model.ModelDefinition()

    LayerButton = Button(master, text="Add Layer", command=build)
    SummaryButton = Button(master, text="Summary", command=summary)


    LayerButton.pack()
    SummaryButton.pack()

    mainloop()


if __name__ == '__main__':
    main()
