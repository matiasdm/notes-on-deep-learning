"""
Define functions on random variables (such as the mutual information).
----
Matias Di Martino (c) 2019, matias.di.martino.uy@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt


def MI(x1=x1, x2=x2, n_bins=(n1,n2)):
    """
    Compute the mutual information between the RV X1 and X2. x1 and x2 are arrays containing the samples x1[i] and x2[i] (xi are arrays of size num_samples x dimension). n_bins sets the number of partitions for the axis associated with each RV. 

    notes: 
    - this implementation may not be robust to outliers (I use the minimum and maximum values), consider removing the outliers on x1 and x2 prior calling this functions. 
    ---- 
    examples: let assume we have features X (X[i] in R^d) and labels y (y[i] in {0,1}).
        mi = MI(x1=X, x2=y, n_bins=(100,2)) 
        (The labels is binary so doesn't make sense to split y axis in more than two slots.)
    """
    
    # (1) set the discrete domain
    x_min = x1.min(axis=0)
    x_max = x1.max(axis=0)

    


    return mi


if __name__=='__main__':
    # Use this for debugging

