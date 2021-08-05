import matplotlib.pyplot as plt

img = plt.imread('test.jpg')
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.savefig('test_box.jpg')
