import numpy as np
from Grid_show_actions import plot_actions
import matplotlib.pyplot as plt


r = -1
gamma = 0.95

action_policy = [['Nothing', 'RLUD', 'RLUD', 'RLUD','RLUD'],
                 ['RLUD', 'RLUD', 'RLUD', 'RLUD','RLUD'],
                 ['RLUD', 'RLUD', 'RLUD', 'RLUD','RLUD'],
                 ['RLUD', 'RLUD', 'RLUD', 'RLUD','RLUD'],
                 ['RLUD', 'RLUD', 'RLUD','RLUD', 'Nothing']]

P_dict = {"R": (1, 0, 0, 0), "L": (0, 1, 0, 0), "U": (0, 0, 1, 0), "D": (0, 0, 0, 1), "RD": (0.5, 0, 0, 0.5),
     "RU": (0.5, 0, 0.5, 0),"RL": (0.5, 0.5, 0, 0), "LD": (0, 0.5, 0, 0.5), "LU": (0, 0.5, 0.5, 0), "UD": (0, 0, 0.5, 0.5),
     "RLU": (0.333, 0.333, 0.333, 0), "RLD": (0.333, 0.333, 0, 0.333), "LUD": (0, 0.333, 0.333, 0.333),
     "RLUD": (0.25, 0.25, 0.25, 0.25), "Nothing":(0,0,0,0)}

plot_actions(action_policy)