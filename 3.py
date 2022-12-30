import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def do_thi_mat_cau(ax):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = (np.outer(np.cos(u), np.sin(v)) * 2) - 2
    y = (np.outer(np.sin(u), np.sin(v)) * 2) + 1
    z = (np.outer(np.ones(np.size(u)), np.cos(v)) * 2) + 4
    ax.plot_surface(x, y, z, cmap='plasma')
    ax.set_title('Đồ thị mặt cầu')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
def main():
    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot(133, projection='3d')
    do_thi_mat_cau(ax)
    ax.set_title('Đồ thị mặt cầu')
    plt.show()
if __name__=='__main__':
    main()