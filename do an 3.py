from sympy import symbols, Eq, solve
           from sympy import *
           import matplotlib.pyplot as plt
           import numpy as np

           flg, ax=plt.subplots()
           x = np.linspace(start=-10.0,stop=10.0, num=200)
           y = x**4-2*x**2-3
           y1 = 4*x**3-4*x
           y2 = 12*x**2-4
           y3 = 24*x
           ax.plot(x,y,label=r'$y = x^{4}-2x^{2}-3$')
           ax.plot(x,y1,label=r'$y = 4x^{3}-4x$')
           ax.plot(x,y2,label=r'$y = 12x^{2}-4$')
           ax.plot(x,y3,label=r'$y = 24x$')
           ax.set_xlabel('truc hoanh')
           ax.set_ylabel('truc tung')
           ax.legend()
           plt.show()


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

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def do_thi_mat_cau(ax):
    x = np.linspace(start=-10.0, stop=10.0, num=200)
    y = np.linspace(start=-10.0, stop=10.0, num=200)
    X, Y = np.meshgrid(x, y)
    Z = (4 - (X + 2)** 2 - (Y - 1) ** 2)
    ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.set_title('Đồ thị mặt cầu')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.show()
def main():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(133, projection='3d')
    do_thi_mat_cau(ax)
    ax.set_title('Đồ thị mặt cầu')
if __name__=='__main__':
    main()




