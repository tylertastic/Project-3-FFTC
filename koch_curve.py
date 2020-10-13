import matplotlib.pyplot as plt
import numpy as np

# max iterations
max_lvl = 1

# parameter
r = 0.29

xL = [item for sublist in [[0]*(max_lvl-1),[30]] for item in sublist]
xR = [item for sublist in [[0]*(max_lvl-1),[330]] for item in sublist]
yL = [item for sublist in [[0]*(max_lvl-1),[190]] for item in sublist]
yR = [item for sublist in [[0]*(max_lvl-1),[190]] for item in sublist]


# Draw line at lowest level of recursion
def subroutine_1(level):
    if level > 0:
        subroutine_2(level)
    plt.plot([xL[0], xR[0]], [yL[0], yR[0]])
    subroutine_3()
    
# Branch into lower levels
def subroutine_2(level):
    level-=1
    
    # Left Branch
    xL[level-1] = xL[level]
    xR[level-1] = 0.333*xR[level] + 0.667*xL[level]
    yL[level-1] = yL[level]
    yR[level-1] = 0.333*yR[level] + 0.667*yL[level]
    subroutine_1(level) #back to subroutine 1
    
    # Middle Left Branch
    xR[level-1] = 0.5*xR[level] + 0.5*xL[level] - r*(yL[level]-yR[level])
    xL[level-1] = xR[level-1]
    yR[level-1] = 0.5*yR[level] + 0.5*yL[level] + r*(xL[level]-xR[level])
    yL[level-1] = yR[level-1]
    subroutine_1(level) #back to subroutine 1
    
    # Middle Right Branch
    xR[level-1] = 0.667*xR[level] + 0.333*xL[level]
    yR[level-1] = 0.667*yR[level] + 0.333*yL[level]
    xL[level-1] = xR[level-1]
    yL[level-1] = yR[level-1]
    subroutine_1(level) #back to subroutine 1
    
    # Right Branch
    xR[level-1] = xR[level]
    yR[level-1] = yR[level]
    xL[level-1] = xR[level-1]
    yL[level-1] = yR[level-1]
    subroutine_1(level) #back to subroutine 1
    
    level += 1
    

# Finish and plot
def subroutine_3():
    plt.xlim([0, 360])
    plt.ylim([0, 200])
    plt.show()
    
# Main
def main():
    subroutine_1(max_lvl)
    
main()
    
  