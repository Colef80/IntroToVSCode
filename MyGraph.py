#need to import module from library
#import into a virtual environment, or copy (too many 3rd parties in route env is bad)
#what to do to create a virtual envirnonemnt (VE)
#1: Create a VE
    #type in terminal: python3-m venv myvenv <<<this can change
#2: Activate the virtual environement
    #source myvenv/bin/activate
#3: Install the 3rd party libraries
    #pip3 install mathplotlib <<<this can change

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello there!")

print("Hi again!")


#always check bottom right to see what env you are in
#Ensure that the env with libraries installed (ve) is being used