import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import time

def f(x): return x**x

a=2.0; b=0.1
w=a-b

area,_=quad(f,b,a)
avg=area/w

st=time.time()
dur=10
md=float("inf")
bc=None
t=0

xx=np.linspace(b,a,10_000_000)

for x in xx:
    fx=f(x)
    d=abs(fx-avg)
    if d<md:
        md=d; bc=x
    t+=1
    if time.time()-st>dur: break

r_area=f(bc)*w

xp=np.linspace(b,a,1000)
yp=f(xp)

plt.figure(figsize=(10,6),facecolor="black")
plt.plot(xp,yp,"w",lw=2,label="f(x)=x^x")
plt.fill_between(xp,yp,color="w",alpha=.15)
plt.bar(bc,avg,width=w,align="center",color="cyan",alpha=.3,ec="cyan",label="rect")
plt.plot(bc,f(bc),"ro",ms=8,label="c≈"+str(round(bc,5)))
plt.title("mean value after 10s",color="w")
plt.xlabel("x",color="w"); plt.ylabel("f(x)",color="w")
plt.grid(True,ls="--",c="gray")
plt.gca().set_facecolor("black")
plt.tick_params(colors="w")
plt.legend(facecolor="black",edgecolor="w")
plt.show()

print("c≈",bc,"tries:",t)
print("f(c)≈",f(bc))
print("avg≈",avg)
print("integral:",area)
print("rect area:",r_area)
print("diff:",abs(r_area-area))
