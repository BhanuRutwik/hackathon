# Import cv2(OpenCV) module using the import keyword
import cv2
# Import pyplot of matplotlib module using the import keyword
import matplotlib.pyplot as plt
# Use the seaborn library using use() asdfasf
plt.style.use('seaborn')

# function and store it in a variable
gvn_image = cv2.imread("sampleimage.png")
# Change the color code of the given image to RGB format using the cvtColor() function
# to get the original colors
gvn_image = cv2.cvtColor(gvn_image, cv2.COLOR_BGR2RGB)
# Pass some random image size to be plotted(width, length) to the figure() function
plt.figure(figsize=(6,6))
# Plot the given original image using the imshow() function
plt.imshow(gvn_image)
plt.axis("off")
# Give the Title of the image using the title() function
plt.title("Given Sample Image")
# Display the plot(image) using the plot function
plt.show()
# Pass the given image, COLOR_BGR2GRAY as arguments to the cvtColor() function
# to convert the given image to grayscale image
# Store it in a variable
grayscle_image = cv2.cvtColor(gvn_image, cv2.COLOR_BGR2GRAY)
# Pass some random image size to be plotted(width, length) to the figure() function
plt.figure(figsize=(6,6))
# Plot the above Grayscale image for the given image using the imshow() function
plt.imshow(grayscle_image, cmap="gray")
plt.axis("off")
# Give the Title of the image using the title() function
plt.title("Grayscale Image")
# Display the grayscale image using the plot function
plt.show()
# Get the inverted image of by passing the above grayscale image as an 
# argument to the bitwise_not() function
invertd_image = cv2.bitwise_not(grayscle_image)
plt.figure(figsize=(6,6))
plt.imshow(invertd_image, cmap="gray")
plt.axis("off")
plt.title("Inverted Image")
plt.show()

print("fifth file")