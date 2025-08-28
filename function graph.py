import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x): return x**x

a=2
b=0.1

res,_=quad(f,b,a)
print("integral:",res)

xx=np.linspace(b,a,500)
yy=f(xx)

plt.figure(figsize=(8,6),facecolor="black")
plt.plot(xx,yy,"w",lw=2,label="f(x)=x^x")
plt.fill_between(xx,yy,color="w",alpha=.2)
plt.title("x^x integral from "+str(b)+" to "+str(a),color="w")
plt.xlabel("x",color="w")
plt.ylabel("f(x)",color="w")
plt.grid(True,ls="--",lw=.5,c="gray")
plt.legend()
plt.gca().set_facecolor("black")
plt.tick_params(colors="w")
plt.show()
