import os
from PIL import Image
import matplotlib.pyplot as plt

my_img = "lenna.png"

cwd = os.getcwd()
print(cwd)

image_path=os.path.join(cwd, my_img)
print(image_path)

image = Image.open(my_img)
image.show()

plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.show()

