"""
GitHub logo creation script
"""

###########
# Imports #
###########
import os
import matplotlib.pyplot as plt; plt.ion()
import numpy as np

from src.data import get_fill_values, get_user_data
from src.core import create_logo
from src import COLORS_STR_2_RGB


if __name__ == "__main__":

    #########
    # Setup #
    #########
    username = input("Enter your GitHub username:\n")

    ########
    # Core #
    ########
    # Scrap the GitHub page of the provided username
    data = get_user_data(username)
    # Select the relevant HTML elements
    values = get_fill_values(data)
    # Compute the color distribution
    colors, counts = np.unique(values, return_counts=True)
    # Sanity check
    assert set(COLORS_STR_2_RGB.keys()) == set(colors), f"Invalid colors in {colors}"

    ##################
    # Logo rendering #
    ##################
    save = False
    while not save:
        # Create the logo image
        img = create_logo(colors, counts)
        plt.imshow(img)
        plt.axis("off")
        answer = input("Save logo? (yes or no)\n")
        save = answer.lower() == "yes" or answer.lower() == "y"
    # Save the selected logo
    cwd = os.getcwd()
    path = os.path.join(cwd, "figures", f"github-logo-{username}.png")
    plt.savefig(path, dpi=600)
    print(f"Saved logo @ {path}")
