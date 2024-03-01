from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("lenna.png")
plt.imshow(image)

print("Image format: ", image.format)
print("Image size: ", image.size)
print("Image mode: ", image.mode)

