import keras
import numpy as np
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import Adam
from keras.models import Sequential

class Model:
    def __init__(self, input_shape):
        self.model = Sequential()
        self.model.add(Dense(64, input_dim=input_shape))
        self.problem = ""

    def SetProblem(self, problem):
        self.problem = problem

    def ModelDefinition(self):
        self.model.summary()

    def Train(self, X, y, batch_size, epochs, learning_rate):
        if self.problem == "classification":
            self.model.compile(loss = "categorical_crossentropy", optimizer = Adam(lr = learning_rate))
        elif self.problem == "regression":
            self.model.compile(loss = "mae", optimizer = Adam(lr = learning_rate))
        self.model.fit(X,y, batch_size, epochs)

    def Predict(self, X):
        self.model.predict(X)

    def AddLayer(self, n):
        self.model.add(Dense(n))
        self.model.add(Activation("relu"))

    def SaveModel(self):
        self.model.save("model.h5")
