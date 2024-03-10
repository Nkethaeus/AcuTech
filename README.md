# AcuTech

AcuTech is an innovative smartphone-based audio classification system designed for the identification and classification of acute coughs using a Convolutional Neural Network (CNN) and a Random Forest Classifier.

## Overview

This project focuses on the development of a cough classifier designed to analyze users' cough recordings and predict their underlying ailment, with a focus on acute coughs such as bronchitis and pneumonia. The primary objective is to evaluate the performance of the Convolutional Neural Network combined with Random Forest (CNN-RF) model against the Support Vector Machine (SVM) model in identifying coughs accurately. Previous local studies have shown that SVM performed better in classifying various audios, but none have been found for audio classification on coughs.

## Process

1. **Data Collection:** Gathered cough recordings of varying lengths for classification.
2. **Data Preprocessing:** Cleaned and normalized the audio data.
3. **Mel-Spectrogram Conversion:** Converted the normalized audio data to mel-spectrogram images for training.
4. **Model Training:** Trained the CNN-RF and SVM models on the preprocessed data.
5. **Evaluation:** Evaluated the models using validation accuracy and f-score metrics.
6. **Results Analysis:** Analyzed the results to determine the effectiveness of each model.

## Technologies Used

- Python for data processing and general implementation
- TensorFlow & Scikit-learn for building and implementing the CNN-RF and SVM models
- Anvil for web interface and hosting the web server
- HTML, CSS for frontend

## Results

After retraining and retesting the two models, significant improvements were observed in their performance. The CNN-RF model showed a notable increase in validation accuracy, rising from the initial 38.05% to 63.23%. Additionally, the f-score for this model improved from 0.49 to 0.58. 

In comparison, the SVM model continued to demonstrate superior performance, achieving a validation accuracy of 87.50% and an f-score of 0.86. These results indicate the effectiveness of both models in audio length classification, with SVM showing particularly strong performance.

## Usage

To utilize AcuTech, simply download the smartphone application from the designated platform and follow the on-screen instructions to record and analyze audio samples. The application will then employ advanced CNN algorithms to classify the presence of acute coughs, providing valuable insights into respiratory health in real-time.

## Group Members

- Jan Airick Indefonso (Project Manager)
- Jerome Saulo (Back-End Developer)
- Geronimo Dayos III (UI/UX Designer)
- Francesca Linda Ramos (Front-End Developer)

## Acknowledgements

We would like to thank Ms. Thonie Fernandez for her guidance and support throughout this project.

---

*AcuTech was developed to fulfill the requirements for the degree of Bachelor of Science in Computer Science, with specialization in Software Engineering at FEU Alabang. The project was completed and submitted during the 1st semester of A.Y. 2023-2024.*
