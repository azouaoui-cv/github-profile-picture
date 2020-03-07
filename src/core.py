"""
Core utilities
"""

###########
# Imports #
###########
import numpy as np
from . import COLORS_STR_2_RGB

def create_logo(colors, counts, margin=20, block=50):
    """
    Create random GitHub logo
    """
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
