# Computer Vision and Image Processing

## Steps for the Computer Vision
1) Search for the problem
2) Developing the model for the problem
3) Deploy it via an application

## Basic Python Library

```
    from PIL import Image
    image = Image.open(myImage)

    import matplotlib.pyplot as plt
    plt.imshow(image)

    image.format:PNG
    image.size:(512, 512)
    image.mode:RGB

    from PIL import ImageOps
    image_grey = ImageOps.grayscale(image)
    image_grey.mode:L
    image_grey.save("lenna.jpg")

    image_grey = Image.open("babara.jpg")
    image_grey.mode:L
    image_grey.quantize(2)


```

## Useful URLs

* How to concatenate images with Python, Pillow
```
	https://note.nkmk.me/en/python-pillow-concat-images/
```

