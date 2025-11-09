import matplotlib.pyplot as plt
import numpy as np

class JuliaSet:
    """
    Class to generate and plot Julia sets, for a given function (complex).
    Parameters:
    f: function - the complex function to generate the Julia set.
    x_left, x_right: float - the range of x values.
    y_top, y_bottom: float - the range of y values.
    prec: float - the precision of the grid.
    max_iter: int - maximum number of iterations to determine set membership.
    threshold: float - the escape radius.
    """
    def __init__(self, f, x_left=-1, x_right=1, y_top=1, y_bottom=-1, prec=0.001, max_iter=50, threshold=10):
        self.f = f
        self.x_left = x_left
        self.x_right = x_right
        self.y_top = y_top
        self.y_bottom = y_bottom
        self.prec = prec
        self.max_iter = max_iter
        self.threshold = threshold
    def evaluate(self):
        #grid initizialization
        x_val = np.arange(self.x_left, self.x_right, self.prec)
        y_val = np.arange(self.y_bottom, self.y_top, self.prec)
        #julia set init
        julia_set = np.zeros((len(y_val), len(x_val)))
        for x in range(len(x_val)):
            for y in range(len(y_val)):
                z = complex(x_val[x], y_val[y])
                iteration = 0
                while abs(z) < self.threshold and iteration < self.max_iter:
                    z = self.f(z)
                    iteration += 1
                julia_set[y, x] = iteration
        self.julia_set = julia_set
        return julia_set
    def plot(self, save=None):
        plt.imshow(self.julia_set)
        plt.axis('off')

        if save is not None:
            plt.imsave(save, self.julia_set)