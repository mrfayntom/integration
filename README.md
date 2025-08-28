# integration

## Overview  
I was solving some integration problems in physics, and it made me think about how we solve integrals by hand versus how a computer solves them. At first, finding out that libraries exist made it feel too easy, but then I discovered another approach: using computers to explore integrals through visualization and finding values under the curve—something that’s hard for humans but natural for machines.  

---

## Create a funtion Graph
I started searching for tricky integrals to solve, and one interesting case I found was the integral of ∫ x^x with limits from `b` to `a`. To explore this, I wrote a script called **`function_graph.py`** that calculates the integral and represents it visually with a graph.  

<p align="center">
  <img width="691" height="547" alt="image" src="https://github.com/user-attachments/assets/eec7c1c7-38a1-4730-841b-71def9a5066c" />
</p>

---

## Create Imaginary Rectangle 
I wrote a script to prove the value of an integral using the **Mean Value Theorem for Integrals**. The method states that there exists an imaginary rectangle with height `f(c)` and width `(a - b)` whose area is equal to the area under the curve. This is demonstrated in my code by finding such a `c` and drawing the rectangle along with the curve.  

<p align="center">
  <img width="846" height="547" alt="image" src="https://github.com/user-attachments/assets/4a6f0a63-63f5-4528-aea2-cbf1233c724a" />
</p>

---

## Integration solver
At last, I created an **integration solver** just for fun. It can handle both definite and indefinite integrals, showing symbolic results or visualizing the area under the curve.  

### Libraries Used  
- **NumPy** – numerical operations  
- **SciPy** – numerical integration (`quad`)  
- **SymPy** – symbolic mathematics  
- **Matplotlib** – plotting and visualization  

---

### Installation  

To install the required libraries, run:  

```bash
pip install numpy scipy sympy matplotlib
