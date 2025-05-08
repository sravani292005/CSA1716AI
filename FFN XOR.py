import numpy as np
import tensorflow as tf
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Define XOR input and output
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Create the Feedforward Neural Network model
model = Sequential([
    Input(shape=(2,)),  # Define input layer explicitly
    Dense(4, activation='relu'),  # Hidden layer with 4 neurons
    Dense(1, activation='sigmoid')  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Evaluate and test the model
predictions = model.predict(X)
print("Predictions:")
print(np.round(predictions))
