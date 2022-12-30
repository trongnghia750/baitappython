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
           if __name__=='__main__':
                main()
