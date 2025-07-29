import numpy as np
from matplotlib.image import imread
from PIL import Image
import matplotlib.pyplot as plt

# Load two images
image1 = imread('/japan-flag-png-large.png')
image2 = imread('/taiwan-flag-png-large.png')

# Ensure they have the same number of channels
if image1.shape[-1] != image2.shape[-1]:
    raise ValueError("Both images must have the same number of channels.")

# Dimensions of the second image
rows, cols, _ = image2.shape
image1_height, image1_width, _ = image1.shape

# Check if it fits unscaled in the top-right corner
if rows > image1_height or cols > image1_width:
    raise ValueError("The second image is too large to fit in the top-right corner of the first image.")

# Resize the second image by a scale factor
scale_factor = 0.5
new_size = (int(cols * scale_factor), int(rows * scale_factor))
image2_resized = np.array(Image.fromarray(image2).resize(new_size))

rows_resized, cols_resized, _ = image2_resized.shape

# Verify the resized version fits
if rows_resized > image1_height or cols_resized > image1_width:
    raise ValueError("The resized second image is too large to fit in the top-right corner of the first image.")

# Composite: paste resized image into top-right corner of copy of the first
image1_copy = image1.copy()
image1_copy[:rows_resized, -cols_resized:] = image2_resized

# Display result
plt.imshow(image1_copy)
plt.axis('off')
plt.show()
