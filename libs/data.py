"""
Create synthetic data, process, etc.
----
Matias Di Martino (c) 2019, matias.di.martino.uy@gmail.com
"""
import numpy as np
import matplotlib.pyplot as plt


def toy_data1(n0=1000, n1=3000, verbose=0):
    """
    Create toy data 1 which consists of two 1-d Gaussian distributions with mean and std:
    # N0(-.5, .4**2) N1(.5, .3**2). Inputs n0 and n1 set the number of samples from class 0 and 1, respectively. The output contain the samples feature values X.shape = (n0+n1, 1) and the samples labels y (shape (n0+n1, 1))
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

    if verbose>0:
        plt.hist(X[y==0,:], 20, alpha = .5)
        plt.hist(X[y==1,:], 20, alpha = .5)   
        plt.legend(['class 0', 'class 1'])
        plt.title('Empirical distribution of class 0 and class 1')
        # plt.show()

    return X,y


def toy_data2(n0=100, n1=300, verbose=0):
    """
    Create toy data 2 which consists of two 2d segments of circumference.
    """
    # Samples of the class 0
    theta = np.random.uniform(low=0,high=np.pi, size=(n0,1))
    c = [.6,.45]; r0 = .23; dr = .04
    r = np.random.normal(loc=r0, scale=dr, size=(n0,1))
    X0 = np.hstack((c[0]+r*np.cos(theta),c[1]+r*np.sin(theta)))
    # Samples of the class 1
    c = [.4,.55]
    theta = np.random.uniform(low=0,high=np.pi, size=(n1,1))
    r = np.random.normal(loc=r0, scale=dr, size=(n1,1))
    X1 = np.hstack((c[0]+r*np.cos(-theta),c[1]+r*np.sin(-theta)))

    # Labels
    y0 = np.zeros((n0,1))
    y1 = np.ones((n1,1))

    X = np.vstack((X0,X1))
    y = np.vstack((y0,y1)).squeeze()

    # Shuffle data
    i = np.arange(len(y))
    np.random.shuffle(i)
    X = X[i,:]
    y = y[i]

    if verbose>0:
        plt.scatter(X[y==0,0], X[y==0,1])
        plt.scatter(X[y==1,0], X[y==1,1])
        plt.legend(['class 0', 'class 1'])
        plt.xlabel('x'); plt.ylabel('y')
        plt.xlim([0,1]); plt.ylim([0,1])
        plt.axis('equal')
        plt.title('Empirical distribution of class 0 and class 1')
        # plt.show()
    return X, y


def toy_data3(n=(100,200,300), d=10, verbose=0):
    """
    Creates d-dimensional samples of N multivariate Gaussian distributions. n is a N-tuple with the number of samples from each class (e.g. n=(20, 30, 15)). Each distribution is a random gaussian with random mean and covariance matrix.  
    """
    sigma_0 = .5  # Sets an order of magnitude for the std of the samples. 
    k = 5  # Number of N(0,1) variables combined (this avoid overlapping of dist when d --> inf)


    X = np.empty((0,d))
    y = np.empty((0,1))

    for (c,nci) in enumerate(n):  # for each class
        X0 = np.random.normal(loc=0, scale=1, size=(d,nci))  # N(0,1) n random vectors dim d
        # X0 has components iid with mu=0 and sigma=Id
        A = np.random.uniform(low=0, high=sigma_0, size=(d,d))  # A random dxd matrix 
        # X0 are nci iid d-dimensional vectors N(0,1), now we are creating a new random variable
        # X1 = mu + A*X0 with both mu and A random. (This sets a random mean and a random variance, because A is random there is going to be correlation between the dimensions.) If we leave A like this, as d --> inf we will be combining infinite random variables and so all the classes are going to tend to be more overlapped. To avoid this, only k elements of each row of A will be kept active. This way, we ensure that only an average of k variables is performed (independently of d), this is going to produce a more stable distribution across d. 
        A[A>sigma_0*k/d] = 0

        Xi = np.dot(A,X0)  # Xi has mu = A*"0"=0 and var = A A^t
        mu = np.random.uniform(size=(d,1)) / np.sqrt(d) # random mean
        # mu = np.random.uniform(size=(d,1)) 
        Xi = Xi + np.dot(mu, np.ones((1,nci)))  # add a random mean
        # See Larry Wasserman "All of Statistics", pg 54. 
        # Now Xi has random mean mu ~ U[0,1]^d and var = A A^t (A ~ U[0,1]^(dxd))
        Xi = np.transpose(Xi)

        yi = c*np.ones((nci,1))  # Define the labels. 
        
        X = np.vstack((X,Xi))
        y = np.vstack((y,yi))

    return X, y.squeeze()


if __name__=='__main__':
    # Debug and test stuffs 
    X,y = toy_data3(n=(2,5,3), d=2)
    print(y)

    