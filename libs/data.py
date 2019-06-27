"""
Create synthetic data, pre-process, etc.
----
matias di martino (c) 2019, matias.di.martino.uy@gmail.com
"""
import numpy as np
import matplotlib.pyplot as plt


def toy_data1(n0=1000, n1=3000):
    """
    Create toy data 1 which consists of two 1-d Gaussian distributions with mean and std:
    N0(-.5, .4**2) N1(.5, .3**2). Inputs n0 and n1 set the number of samples from class 0 
    and 1, respectively. The output contain the samples feature values X.shape = (n0+n1, 1) 
    and the samples labels y (shape (n0+n1, 1))
    """
    X0 = -.5 + .4*np.random.randn(n0,1)  # Gaussian dist with mean -.5 and std .4**2
    X1 = +.5 + .3*np.random.randn(n1,1)  # Gaussian dist with mean +.5 and std .3**2
    y0 = np.zeros((n0,1))
    y1 = np.ones((n1,1))

    X = np.vstack((X0,X1))
    y = np.vstack((y0,y1)).squeeze()

    # Shuffle data
    i = np.arange(len(y))
    np.random.shuffle(i)
    X = X[i,:]
    y = y[i]
return X,y
