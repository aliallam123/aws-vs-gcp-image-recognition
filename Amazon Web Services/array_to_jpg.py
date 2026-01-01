import pickle
import numpy as np
from PIL import Image
import os

def unpickle(file):
    with open(file, 'rb') as fo:
        data_dict = pickle.load(fo, encoding='bytes')
    return data_dict

os.makedirs("cifar10_images", exist_ok=True)

batch = unpickle("CIFAR-10 Python/data_batch_1")
images = batch[b"data"]
labels = batch[b"labels"]

for i in range(100):  # start small
    img = images[i]
    r = img[0:1024].reshape(32, 32)
    g = img[1024:2048].reshape(32, 32)
    b = img[2048:].reshape(32, 32)
    img_3d = np.dstack((r, g, b))
    im = Image.fromarray(img_3d)
    im.save(f"cifar10_images/img_{i}_{labels[i]}.jpg")

print("100 images saved in cifar10_images/")
