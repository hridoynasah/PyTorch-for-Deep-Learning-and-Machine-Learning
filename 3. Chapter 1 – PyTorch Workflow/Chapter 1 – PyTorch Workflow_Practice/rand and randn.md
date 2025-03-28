In PyTorch, `torch.rand()` and `torch.randn()` both generate random numbers, but they differ in their distribution.

---

### **1️⃣ `torch.rand()` – Uniform Distribution**  
```python
torch.rand(size)
```
- Generates **random numbers between `0` and `1`**.
- Follows a **Uniform Distribution** (each number has an equal chance of being picked).
- No negative numbers.

#### **Example:**
```python
import torch

x = torch.rand(3)  # Generates 3 random numbers
print(x)
```
🔹 **Output (example, varies every time)**  
```
tensor([0.6724, 0.1352, 0.9845])
```
- All values are **between `0` and `1`**.

---

### **2️⃣ `torch.randn()` – Normal (Gaussian) Distribution**  
```python
torch.randn(size)
```
- Generates **random numbers centered around `0`**, with both **positive and negative values**.
- Follows a **Standard Normal Distribution** (mean = `0`, standard deviation = `1`).
- Values spread out in a bell-shaped curve.

#### **Example:**
```python
y = torch.randn(3)  # Generates 3 random numbers
print(y)
```
🔹 **Output (example, varies every time)**  
```
tensor([-1.2453, 0.3471, 2.1938])
```
- Values **can be negative or positive**.
- Most numbers are **close to `0`**, but some can be far away.

---

### **📌 Key Differences**
| Feature         | `torch.rand()` | `torch.randn()` |
|---------------|---------------|---------------|
| **Range** | `[0, 1]` (Only positive) | `(-∞, +∞)` (Can be negative) |
| **Distribution** | Uniform | Normal (Gaussian) |
| **Mean (avg value)** | `0.5` (since 0 to 1) | `0` (centered around 0) |
| **Common Use** | Random probabilities, dropout, noise | Initializing neural network weights |

---

### **🎯 When to Use Which?**
- ✅ **Use `torch.rand()`** when you need **random probabilities** (e.g., dropout, random mask).  
- ✅ **Use `torch.randn()`** when initializing **neural network weights**, as many deep learning models assume a normal distribution.  
