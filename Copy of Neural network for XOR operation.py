# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:22:57 2025

@author: DELL
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases with small random values
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_hidden = np.random.rand(hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_output = np.random.rand(output_size)
    
    def forward(self, X):
        # Compute activations for hidden layer
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)
        
        # Compute activations for output layer
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = sigmoid(self.final_input)
        
        return self.final_output
    
    def train(self, X, y, epochs=10000, learning_rate=0.1):
        for _ in range(epochs):
            # Forward pass
            output = self.forward(X)
            
            # Compute error
            error = y - output
            
            # Backpropagation
            output_gradient = error * sigmoid_derivative(output)
            hidden_error = np.dot(output_gradient, self.weights_hidden_output.T)
            hidden_gradient = hidden_error * sigmoid_derivative(self.hidden_output)
            
            # Update weights and biases
            self.weights_hidden_output += np.dot(self.hidden_output.T, output_gradient) * learning_rate
            self.bias_output += np.sum(output_gradient, axis=0) * learning_rate
            self.weights_input_hidden += np.dot(X.T, hidden_gradient) * learning_rate
            self.bias_hidden += np.sum(hidden_gradient, axis=0) * learning_rate

# Example usage
if __name__ == "__main__":
    # Define dataset (XOR problem)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    
    # Create neural network
    nn = FeedForwardNN(input_size=2, hidden_size=4, output_size=1)
    
    # Train neural network
    nn.train(X, y)
    
    # Test neural network
    predictions = nn.forward(X)
    print("Predictions after training:")
    print(predictions)
