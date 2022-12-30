import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def do_thi_hyperbolic(ax):
    x = np.linspace(start=-10.0, stop=10.0, num=200)
    y = np.linspace(start=-10.0, stop=10.0, num=200)
    X, Y = np.meshgrid(x, y)
    Z = ((X / 3) ** 2 + (Y / 5) ** 2 - (2 ** 2))
    ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.set_title('Đồ thị mặt hyperbolic 1 tầng')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.show()
def main():
    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot(132, projection='3d')
    do_thi_hyperbolic(ax)
    ax.set_title('Đồ thị hyperbolic')
if __name__=='__main__':
    main()