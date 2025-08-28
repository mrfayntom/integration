import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import quad
import time

mode=input("definite or indefinite: ").strip().lower()
x=sp.Symbol("x")
expr_in=input("f(x)=")
try: expr=sp.sympify(expr_in)
except: print("bad func"); exit()

if mode=="indefinite":
    try:
        I=sp.integrate(expr,x)
        print("indef int of",expr_in,":")
        sp.pprint(I)
    except: print("cant integrate")

elif mode=="definite":
    try: a=float(input("a=")); b=float(input("b="))
    except: print("bad lim"); exit()
    try: f=sp.lambdify(x,expr,modules=["numpy"])
    except: print("cant num"); exit()
    try: area,_=quad(f,a,b); print("area:",area)
    except: print("fail num"); exit()
    st=time.time(); dur=10; w=b-a; avg=area/w
    md=float("inf"); bc=None; t=0
    xx=np.linspace(a,b,10_000_000)
    for xi in xx:
        try: yi=f(xi)
        except: continue
        d=abs(yi-avg)
        if d<md: md=d; bc=xi
        t+=1
        if time.time()-st>dur: break
    if bc is None: print("no c"); exit()
    fc=f(bc); r=fc*w
    print("c≈",bc,"tries:",t)
    print("f(c)≈",fc)
    print("avg≈",avg)
    print("rect area:",r)
    print("integral:",area)
    print("diff:",abs(r-area))
    xp=np.linspace(a,b,1000)
    try: yp=f(xp)
    except: print("cant plot"); exit()
    plt.figure(figsize=(10,6),facecolor="black")
    plt.plot(xp,yp,"w",lw=2,label="f(x)="+expr_in)
    plt.fill_between(xp,yp,color="w",alpha=.15)
    plt.bar(bc,avg,width=w,align="center",color="cyan",alpha=.3,ec="cyan",label="rect")
    plt.plot(bc,fc,"ro",ms=8,label="c≈"+str(round(bc,5)))
    plt.title("mvt",color="w")
    plt.xlabel("x",color="w"); plt.ylabel("f(x)",color="w")
    plt.grid(True,ls="--",c="gray")
    plt.gca().set_facecolor("black")
    plt.tick_params(colors="w")
    plt.legend(facecolor="black",edgecolor="w")
    plt.show()
else: print("bad mode")
