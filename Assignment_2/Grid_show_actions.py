import matplotlib.pyplot as plt


def plot_actions(ar):
    arrows = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1), "RD": (1, 0, 0, -1), "RU": (1, 0, 0, 1),
              "RL": (1, 0, -1, 0), "LD": (-1, 0, 0, -1), "LU": (-1, 0, 0, 1), "UD": (0, 1, 0, -1),
              "RLU": (1, 0, -1, 0, 0, 1), "RLD": (1, 0, -1, 0, 0, -1), "LUD": (-1, 0, 0, 1, 0, -1),
              "RLUD": (1, 0, -1, 0, 0, 1, 0, -1)}

    scale = 0.2
    fig, ax1 = plt.subplots(figsize=(7, 7))
    for r, row in enumerate(ar):
        for c, cell in enumerate(row):
            if cell is None:
                pass
            elif len(cell) == 7:
                pass
            elif len(cell) == 4:
                plt.arrow(c, 5 - r, scale * arrows[cell][0], scale * arrows[cell][1], head_width=0.1)
                plt.arrow(c, 5 - r, scale * arrows[cell][2], scale * arrows[cell][3], head_width=0.1)
                plt.arrow(c, 5 - r, scale * arrows[cell][4], scale * arrows[cell][5], head_width=0.1)
                plt.arrow(c, 5 - r, scale * arrows[cell][6], scale * arrows[cell][7], head_width=0.1)
            elif len(cell) == 3:
                plt.arrow(c, 5 - r, scale * arrows[cell][0], scale * arrows[cell][1], head_width=0.1)
                plt.arrow(c, 5 - r, scale * arrows[cell][2], scale * arrows[cell][3], head_width=0.1)
                plt.arrow(c, 5 - r, scale * arrows[cell][4], scale * arrows[cell][5], head_width=0.1)
            elif len(cell) == 2:
                plt.arrow(c, 5 - r, scale * arrows[cell][0], scale * arrows[cell][1], head_width=0.1)
                plt.arrow(c, 5 - r, scale * arrows[cell][2], scale * arrows[cell][3], head_width=0.1)
            else:
                plt.arrow(c, 5 - r, scale * arrows[cell][0], scale * arrows[cell][1], head_width=0.1)
    plt.axvline(x=0.5, color='b')
    plt.axvline(x=1.5, color='b')
    plt.axvline(x=2.5, color='b')
    plt.axvline(x=3.5, color='b')
    plt.axhline(y=1.5, color='b')
    plt.axhline(y=2.5, color='b')
    plt.axhline(y=3.5, color='b')
    plt.axhline(y=4.5, color='b')
    plt.savefig('plot.png')
    plt.show()
