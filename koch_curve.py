import matplotlib.pyplot as plt
import numpy as np


# The following is an attempt at a recursive solution, which is similar to the one in the book but has some issues here
# which are due to either the book code itself, GOTO and GOSUB in BASIC, or incorrect memory allocation for the arrays

# # max iterations
# max_lvl = 1

# # parameter
# r = 0.29

# xL = [item for sublist in [[0]*(max_lvl-1),[30]] for item in sublist]
# xR = [item for sublist in [[0]*(max_lvl-1),[330]] for item in sublist]
# yL = [item for sublist in [[0]*(max_lvl-1),[190]] for item in sublist]
# yR = [item for sublist in [[0]*(max_lvl-1),[190]] for item in sublist]


# # Draw line at lowest level of recursion
# def subroutine_1(level):
#     if level > 0:
#         subroutine_2(level)
#     plt.plot([xL[0], xR[0]], [yL[0], yR[0]])
#     subroutine_3()
    
# # Branch into lower levels
# def subroutine_2(level):
#     level-=1
    
#     # Left Branch
#     xL[level-1] = xL[level]
#     xR[level-1] = 0.333*xR[level] + 0.667*xL[level]
#     yL[level-1] = yL[level]
#     yR[level-1] = 0.333*yR[level] + 0.667*yL[level]
#     subroutine_1(level) #back to subroutine 1
    
#     # Middle Left Branch
#     xR[level-1] = 0.5*xR[level] + 0.5*xL[level] - r*(yL[level]-yR[level])
#     xL[level-1] = xR[level-1]
#     yR[level-1] = 0.5*yR[level] + 0.5*yL[level] + r*(xL[level]-xR[level])
#     yL[level-1] = yR[level-1]
#     subroutine_1(level) #back to subroutine 1
    
#     # Middle Right Branch
#     xR[level-1] = 0.667*xR[level] + 0.333*xL[level]
#     yR[level-1] = 0.667*yR[level] + 0.333*yL[level]
#     xL[level-1] = xR[level-1]
#     yL[level-1] = yR[level-1]
#     subroutine_1(level) #back to subroutine 1
    
#     # Right Branch
#     xR[level-1] = xR[level]
#     yR[level-1] = yR[level]
#     xL[level-1] = xR[level-1]
#     yL[level-1] = yR[level-1]
#     subroutine_1(level) #back to subroutine 1
    
#     level += 1
    

# # Finish and plot
# def subroutine_3():
#     plt.xlim([0, 360])
#     plt.ylim([0, 200])
#     plt.show()
    
# # Main
# def main():
#     subroutine_1(max_lvl)
    
# main()


###############################################################################################################

# The following is a solution using matrices and linear algebra

# settings  cols: scale s, rotation thta, translation x Tx, translation y Ty
iterations = 3
settings = np.array([[1/3, 0, 0, 0],
            [1/3, np.pi/3, 1/3, 0],
            [1/3, -np.pi/3, 1/2, np.sqrt(3)],
            [1/3, 0, 2/3, 0]])
initiator = [[0,1],[0,0]]

def rotation_mat(thta):
    return np.array([[np.cos(thta), -np.sin(thta)],
                     [np.sin(thta), np.cos(thta)]])

def Hutch_w1(v):
    w1 = settings[0]
    s = w1[0]
    thta = w1[1]
    tx = w1[2]
    ty = w1[3]
    
    rot = rotation_mat(thta)
    trans = np.array([tx, ty])
    
    operator = s*(rot @ v) + trans
    return operator

def Hutch_w2(v):
    w2 = settings[1]
    s = w2[0]
    thta = w2[1]
    tx = w2[2]
    ty = w2[3]
    
    rot = rotation_mat(thta)
    trans = np.array([tx, ty])
    
    operator = s*(rot @ v) + trans
    return operator

def Hutch_w3(v):
    w3 = settings[2]
    s = w3[0]
    thta = w3[1]
    tx = w3[2]
    ty = w3[3]
    
    rot = rotation_mat(thta)
    trans = np.array([tx, ty])
    
    operator = s*(rot @ v) + trans
    return operator

def Hutch_w4(v):
    w4 = settings[3]
    s = w4[0]
    thta = w4[1]
    tx = w4[2]
    ty = w4[3]
    
    rot = rotation_mat(thta)
    trans = np.array([tx, ty])
    
    operator = s*(rot @ v) + trans
    return operator


# this is not right but its presence shows something
def iterate_wk(initiator, iterations, wk):
    if iterations = 1:
        return initiator
    else:
        initiator = [wk(initiator[0]), wk(initiator[1])]
        return compute_new_line_segment(initiator, iterations-1, wk)


    
