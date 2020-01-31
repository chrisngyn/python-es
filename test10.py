# Math plot lib module - an EXTERNAL Python module, meaning we need to install it first before we import it in our program
# In terminal:
# 1. brew install python3 - comes with pip3, a package manager for Python
# 2. pip3 install matplotlib
# 3. now we can import

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [1500, 1100, 1400, 1200]
plt.plot(x, y)
months = ["January", "February", "March", "April"]
plt.xticks(x, months)
plt.plot(x, y)
plt.show()
plt.bar(x, y)
plt.title("test")
plt.ylabel("test2")