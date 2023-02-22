import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import random

path_to_images = './hw1/avatars'

files = os.listdir(path_to_images)

image = cv2.imread(os.path.join(path_to_images, files[0]))
def_shape = image.shape
print(def_shape)

# Check that images' shapes are the same
assert all(
    cv2.imread(os.path.join(path_to_images, files[i])).shape == def_shape
    for i in range(1, len(files))
), "Pixel by pixel comparison is impossible, shapes diverge"

image = np.stack(
    list((cv2.imread(os.path.join(path_to_images, path)) for path in files)), axis=-1
)

start_time = time.time()
gen_image = np.empty((def_shape[0], def_shape[1], def_shape[2]), dtype=np.uint8)
for H in range(def_shape[0]):
    for W in range(def_shape[1]):
        for CH in range(def_shape[2]):
            occurences = image[H, W, CH, :]
            uniq_values, counts = np.unique(occurences, return_counts=True)
            probas = counts / len(occurences)
            gen_image[H, W, CH] = random.choices(uniq_values, weights=probas)[0]
end_time = time.time()

print(f"Time for generating image = {(end_time - start_time):.2f}")

plt.imshow(gen_image[:, :, ::-1])
plt.savefig('./hw1/figure1.png')
plt.show()
