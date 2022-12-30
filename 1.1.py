import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def do_thi_yen_ngua(ax):
    x = np.linspace(start=-10.0, stop=10.0, num=200)
    y = np.linspace(start=-10.0, stop=10.0, num=200)
    X, Y = np.meshgrid(x, y)
    Z = (X/3)**2 - (Y/2)**2
    ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.set_title('Đồ thị mặt yên ngựa')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.show()
def main():
    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot(131, projection='3d')
    do_thi_yen_ngua(ax)
    ax.set_title('Đồ thị mặt yên ngựa')
if __name__=='__main__':
    main()
