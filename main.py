"""
GitHub logo creation script
"""

###########
# Imports #
###########
import os
import matplotlib.pyplot as plt; plt.ion()
import numpy as np

from src.core import create_logo


if __name__ == "__main__":

    #########
    # Setup #
    #########
    username = input("Enter your GitHub username:\n")

    ##################
    # Logo rendering #
    ##################
    save = False
    while not save:
        # Create the logo image
        img = create_logo(username)
        plt.imshow(img)
        plt.axis("off")
        answer = input("Save logo? (yes or no)\n")
        save = answer.lower() == "yes" or answer.lower() == "y"
    # Save the selected logo
    cwd = os.getcwd()
    path = os.path.join(cwd, "figures", f"github-logo-{username}.png")
    plt.savefig(path, dpi=600)
    print(f"Saved logo @ {path}")
