import os
import cv2

def gaussian_threshold(image_path, output_folder, threshold_value=55, max_value=255):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian thresholding
    _, thresholded_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Save the thresholded image
    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, thresholded_image)

def gaussian_threshold_all_images(input_folder, output_folder, threshold_value=55, max_value=255):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust as per your image types
            image_path = os.path.join(input_folder, filename)
            gaussian_threshold(image_path, output_folder, threshold_value, max_value)

# Example usage:
input_folder = 'BIllReceiptImageCollection'
output_folder = 'outputfolder'
gaussian_threshold_all_images(input_folder, output_folder, threshold_value=127, max_value=255)

