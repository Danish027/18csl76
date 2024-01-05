import numpy as np

# Input data - X and target output - y
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([.92], [.86], [.89]), dtype=float)

# Normalize the input data
X = X/np.amax(X, axis=0)

# Sigmoid activation function
def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid function for backpropagation
def der_sigmoid(x):
    return x * (1 - x)

# Hyperparameters
epoch = 5000  # Number of training iterations
lr = 0.01     # Learning rate
neurons_i = 2 # Number of neurons in input layer
neurons_h = 3 # Number of neurons in hidden layer
neurons_o = 1 # Number of neurons in output layer

# Weight and bias initialization
weight_h = np.random.uniform(size=(neurons_i, neurons_h))
bias_h = np.random.uniform(size=(1, neurons_h))
weight_o = np.random.uniform(size=(neurons_h, neurons_o))
bias_o = np.random.uniform(size=(1, neurons_o))

# Training the model
for i in range(epoch):
    # Forward Propagation
    inp_h = np.dot(X, weight_h) + bias_h
    out_h = sigmoid(inp_h)
    inp_o = np.dot(out_h, weight_o) + bias_o
    out_o = sigmoid(inp_o)

    # Calculating error
    err_o = y - out_o
    grad_o = der_sigmoid(out_o)
    delta_o = err_o * grad_o

    # Backpropagating the error
    err_h = delta_o.dot(weight_o.T)
    grad_h = der_sigmoid(out_h)
    delta_h = err_h * grad_h

    # Updating weights and biases
    weight_o += out_h.T.dot(delta_o) * lr
    weight_h += X.T.dot(delta_h) * lr

# Printing the results
print('Inputl: ', y)
print('Predi: ', X)
print('Actuacted: ', out_o)
