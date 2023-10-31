import cv2

# Read the image in RGB format
image = cv2.imread('passportsize.png')  # Replace 'your_image_path.jpg' with the actual path to your image

if image is not None:
    # Display the original image
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Invert the grayscale image using bitwise NOT
    inverted_image = cv2.bitwise_not(gray_image)

    # Display the inverted image
    cv2.imshow('Inverted Image', inverted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)

    # Display the blurred image
    cv2.imshow('Blurred Image', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Create the pencil sketch by dividing the grayscale image by the inverted, blurred image
    pencil_sketch = cv2.divide(gray_image, 255 - blurred_image, scale=256)

    # Display the pencil sketch
    cv2.imshow('Pencil Sketch', pencil_sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the pencil sketch as an image
    cv2.imwrite('pencil_sketch.png', pencil_sketch)

else:
    print("Image not found. Please check the image path.")
