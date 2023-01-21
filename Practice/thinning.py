from skimage.morphology import skeletonize, thin
import matplotlib.pyplot as plt
import cv2

# image thinning operation
image = cv2.imread('img.jpg', 0)
thinned = thin(image)
thinned_partial = thin(image, max_iter=25)

fig, axes = plt.subplots(1, 2, figsize=(8, 8), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(thinned, cmap=plt.cm.gray)
ax[0].set_title('thinned')
ax[0].axis('off')

ax[1].imshow(thinned_partial, cmap=plt.cm.gray)
ax[1].set_title('partially thinned')
ax[1].axis('off')

fig.tight_layout()
plt.show()