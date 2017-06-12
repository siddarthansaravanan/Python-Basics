def flattening(image2):
    s = image2.shape[0] * image2.shape[1]
    flat = image2.reshape(1, s)
    return flat[0]
