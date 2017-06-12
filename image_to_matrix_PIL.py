from PIL import Image

fixed_size = (x, y)

def image_matrix(filename, verbose=False):
    image1 = Image.open(filename)
    image1 = image1.resize(fixed_size)
    image1 = list(image1.getdata())
    image1 = np.array(image1)
    return image1