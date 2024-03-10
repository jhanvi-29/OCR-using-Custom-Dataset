# OCR-using-Custom-Dataset
This project is used to detect OCR of Retail Receipts using EasyOCR, Gaussian Threshold for pre-processing data and custom model training 

- Dataset used OCR Receipts from Grocery Stores Text Detection - retail dataset 
- Data Pre-Processing is implemented by Gaussian Threshold method using OpenCV, using this technique we can enchance more details of the image,
  using ImgProcessing.py you can pre-process all images together in a folder
- Data modelling is done using this custom dataset, model training is done using Tessaract,EasyOCR,DistiltBert
- Model Detection is saved JSON file
- Flask API code is also included for end-to-end pipeline system architecture.
