import sys
from tkinter import *
from Model import Model
from flask import Flask

class MainWindow():

    def __init__(self):
        self.master = Tk()
        self.master.title("KogniteLab")
        self.master.geometry("500x500")
        self.model = Model(16)
        self.LayerButton = Button(self.master, text="Add Layer", command=self.build)
        self.SummaryButton = Button(self.master, text="Summary", command=self.summary)
        self.SaveButoon = Button(self.master, text="Save the model", command=self.save_model)
        self.LayerButton.pack()
        self.SummaryButton.pack()
        self.SaveButoon.pack()
        mainloop()
        


    def build(self):
        self.model.AddLayer(10)
        print("layer added")

    def summary(self):
        self.model.ModelDefinition()

    def save_model(self):
        self.model.SaveModel()

    

if __name__ == '__main__':
    window = MainWindow()
    