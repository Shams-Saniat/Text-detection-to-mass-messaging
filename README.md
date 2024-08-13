# Mass Messaging and Database Input System

This project aims to automate the process of extracting data from images, storing it in a database, and sending messages to targeted audiences. The system eliminates manual data entry, reducing human error and saving valuable time.

## Table of Contents
- [Background Study](#background-study)
- [Proposed System](#proposed-system)
- [Applications](#applications)
- [Literature Review](#literature-review)
- [Technologies Used](#technologies-used)
- [Database](#database)
- [Twilio Messaging API](#twilio-messaging-api)
- [Results and Analysis](#results-and-analysis)

## Background Study
- The project focuses on sending messages to a targeted audience and automating database input.
- The system extracts data from images and stores it in a database for later use, such as sending marketing messages.

## Proposed System
The system involves several steps:
1. **Capture:** Acquire the image containing the necessary data.
2. **Preprocess:** Prepare the image for further analysis.
3. **Localize:** Identify the regions of interest within the image.
4. **Connected Component Analysis:** Analyze the connected components within the localized areas.
5. **Segmentation:** Divide the image into smaller segments.
6. **Character Recognition:** Use OCR to recognize characters from the segmented image.

## Problem Statement
- Manual data entry is prone to errors, time-consuming, and inefficient in managing manpower.
- The system aims to automate text detection and data storage, allowing for efficient database management and targeted messaging.

## Applications
- **Announcements:** Send mass notifications to a specific group.
- **Promotional Purposes:** Automate marketing campaigns.
- **Spam Messaging:** Efficiently handle large volumes of unsolicited messages.
- **Supermall/Hospital Management:** Manage large datasets efficiently, such as patient information in hospitals.

## Literature Review
- Python combined with OpenCV is powerful for computer vision tasks.
- **Algorithms Used:**
  - **Adaptive Thresholding:** For binarizing the image.
  - **OTSU Algorithm:** For image segmentation.
  - **Image Scissoring:** For precise image cutting.
  - **Optical Character Recognition (OCR):** For text extraction.

## Technologies Used
- **Pytesseract:** An open-source OCR engine sponsored by Google, known for its accuracy and efficiency.
- **OpenCV:** Used for image processing and computer vision tasks.

## Database
The system uses a database to store extracted data, ensuring that the information is readily available for messaging purposes.

## Twilio Messaging API
- **Twilio API** allows for sending and receiving messages.
- Compatible with multiple programming languages, including PHP, Python, Java, and Node.js.

## Results and Analysis
- The system successfully detects and processes images, stores data in the database, and sends messages via SMS.
- Achieved high accuracy in image detection and data processing.
