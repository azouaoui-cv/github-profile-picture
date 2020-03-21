"""
Core utilities
"""

###########
# Imports #
###########
import numpy as np
from . import COLORS_STR_2_RGB
from .data import get_user_data
from .data import get_fill_values

def create_logo(username, margin=20, block=50):
    """
    Create random GitHub logo
    """
    # Get user data
    data = get_user_data(username)
    # Get filling values
    values = get_fill_values(data)
    # Get the color distribution
    colors, counts = np.unique(values, return_counts=True)
    # Sanity check
    assert set(COLORS_STR_2_RGB.keys()) == set(colors), f"Invalid colors in {colors}"
    #########
    # Setup #
    #########
    side = 2 * margin + 5 * block
    # Empty image
    img = np.zeros((side, side, 3), dtype='uint8')
    # Fill image with light gray
    img[:, :] = COLORS_STR_2_RGB['#ebedf0']
    # Draw colors based on contributions distribution
    choices = np.random.choice(colors, size=15, replace=True, p=counts / sum(counts))
    # Populate empty image
    counter = 0
    try:
        for i in range(margin, side - block, block):
            for j in range(margin, side - block, block):
                img[j:j+block,i:i+block] = COLORS_STR_2_RGB[choices[counter]]
                counter += 1
    except:
        pass
    # Induce vertical symmetry
    img[:,side//2:] = img[:,:side//2][:,::-1]
    return img
