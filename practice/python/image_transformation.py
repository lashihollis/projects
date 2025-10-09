import numpy as np
import matplotlib.pyplot as plt
import codecademylib3

heart_img = np.array([[255,0,0,255,0,0,255],
              [0,255/2,255/2,0,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
              [255,0,255/2,255/2,255/2,0,255],
                  [255,255,0,255/2,0,255,255],
                  [255,255,255,0,255,255,255]])

# This is a helper function that makes it easy for you to show images!
def show_image(image, name_identifier):
  plt.imshow(image, cmap="gray")
  plt.title(name_identifier)
  plt.show()

# Show heart image
show_img = show_image(heart_img,"Heart Image")

# Invert color
inverted_heart_img = 255 - heart_img
show_invert = show_image(inverted_heart_img, "Inverted Heart")

# Rotate heart
rotate = heart_img.T
show_rotate = show_image(rotate, "Rotated Image")

# Random Image
random_img = np.random.randint(0,255, (7,7))
show_random = show_image(random_img, "Random Image")

# Solve for heart image
x = np.linalg.solve(random_img,heart_img)
show_x = show_image(x, "X")

solved_heart_img = np.matmul(random_img,x)
show_solved = show_image(solved_heart_img, "Solved")
