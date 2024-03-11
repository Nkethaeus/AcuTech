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
- HTML and CSS for front-end development

## Results

After retraining and retesting the two models, significant improvements were observed in their performance. The CNN-RF model showed a notable increase in validation accuracy, rising from the initial 38.05% to 63.23%. Additionally, the f-score for this model improved from 0.49 to 0.58. 

In comparison, the SVM model continued to demonstrate superior performance, achieving a validation accuracy of 87.50% and an f-score of 0.86. These results indicate the effectiveness of both models in audio length classification, with SVM showing particularly strong performance.

## Recommendations

The researchers recommend preparing a dataset with around 2,000-10,000 samples, especially for classifying coughs. It seems that part of what made CNN-RF perform bad is the limited dataset the researchers had to use to train the model. Without enough data to learn from, the model was not able to effectively discern and distinguish the features and structure of the recordings that differentiate each acute cough from each other. 

In addition to that, the researchers also recommend using datasets that have audio files recorded with little to no background noise. Background noise makes identifying variances much more difficult, as it adds irrelevant interferences and impedes the extraction of relevant features.

## Usage

### For Users

To try out AcuTech, download the APK from this repository and install it on your Android device. Follow the on-screen instructions to record your cough, and await the completion of the analysis. The app will then present the results as percentages, indicating the likelihood that your cough aligns with one of the various acute coughs covered in this project.

### For Training

To retrain AcuTech using your own dataset, first, ensure your dataset is organized and placed appropriately. If your dataset requires normalization, place it in the `dataset_train_unclean` folder and execute the `clean.py` script. Each recording will be automatically split into 3-second segments and appropriately named for further processing. Alternatively, if your dataset is already normalized, place it in the dataset_train_clean folder.

It is essential to maintain accurate labeling for each recording, as this information is critical for model training.

Next, update the CSV file containing the filenames of the recordings and their respective labels to reflect any changes or additions.

Finally, open the `acs-ccnrf.ipynb` notebook, verify that the file paths are correctly specified in the 'Loading of Dataset & Metadata' cell, and execute all cells in the notebook to initiate the retraining process.
\ \
> Note: The app requires the Anvil client to be running for proper functionality. To use the app, [create an Anvil account](https://anvil.works/sign-up) and name the file 'upload'. Then, copy the client code from `anvil/client_code.py` and ensure it is executed after pasting. 
>
> You will also need to replace the Anvil server uplink key in the 'Anvil Server Connection' cell in `acs-ccnrf.ipynb`. To obtain a server uplink key, click the Uplink button on Anvil and copy the provided server uplink key.

## Group Members

- [Jan Airick Indefonso](https://www.linkedin.com/in/jan-airick-indefonso-54a76426b/) (*Project Manager*)
- [Jerome Saulo](https://www.linkedin.com/in/jerome-saulo/) (*Back-End Developer*)
- [Geronimo Dayos III](https://www.linkedin.com/in/john-dayos-678a22253/) (*UI/UX Designer*)
- [Francesca Linda Ramos](https://www.linkedin.com/in/france-ramos/) (*Front-End Developer*)

## Acknowledgements

We would like to thank Ms. Thonie Fernandez for her guidance and support throughout this project.

---

*AcuTech was developed to fulfill the requirements for the degree of Bachelor of Science in Computer Science, with specialization in Software Engineering at FEU Alabang. The project was completed and submitted during the 1st semester of A.Y. 2023-2024.*
