# Data Analytics Project using YouTube API & Streamlit Web App
#### *Get any YouTube channel data (worldwide) with just a single click* *

</br>

## **YouTube Tutorial - Step by Step guide to create this project**
[![YouTube API Key](https://res.cloudinary.com/marcomontalbano/image/upload/v1703402736/video_to_markdown/images/youtube--bW-FytTQse4-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/bW-FytTQse4?feature=shared "YouTube API Key")

</br>

## **Web App**
https://youtube-data-gathering-project.streamlit.app/

</br>

## **How to use this app**
[![YouTube API Key](https://res.cloudinary.com/marcomontalbano/image/upload/v1703402736/video_to_markdown/images/youtube--bW-FytTQse4-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/bW-FytTQse4?feature=shared "YouTube API Key")

</br>

## Overview

![project_screenshot_white_background](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/5fa29ffd-7027-4241-bd56-ee375e280f38)

## 📄Project Description

1. The project focuses on leveraging the YouTube API to collect comprehensive data on channels globally. 
2. A user-friendly Streamlit web app was developed, enabling users to input their API key and channel ID for seamless retrieval and download of channel-specific data in CSV format.

## 🎯Objectives

![Slide2](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/6c465e26-49a0-4f3c-98bc-53f74dc5449a)

## 🛠Tools and Technologies

- Python
- YouTube API
- Pandas
- Streamlit

## ⚙Project Setup

![Presentation Deck](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/6a606403-be2b-4fed-8982-7c5ee9b59455)


## 🔄Methodology

![data_retrieval_process short](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/a08024e1-edb7-463d-b5ec-0cee8530d7dc)
![Slide12](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/e1c53527-d4f7-445e-9833-e4513a94f301)
![playlist_endpoint white](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/64f6cedc-5a53-4c2c-9fa2-026e45d00159)
![Slide14](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/a64ced12-6289-4fdb-8ed6-f4485b8198c5)


## 🧹Data Cleaning
1. The API provides data in JSON format, with relevant information nested within dictionaries. Retrieving this data required careful navigation through nested structures.

2. The `get()` method was employed to handle potential errors, and `try` and `except` blocks were strategically implemented for error handling.

3. Dedicated functions were crafted for Channels, Playlist Items, and VideoIds to enhance code readability and facilitate error detection.

## 🤕Exception Handling

Robust exception handling using try and except blocks for scenarios such as 
1. No API Key
2. Incorrect API Key
3. No Channel ID
4. Incorrect Channel ID
5. Channel with no videos


## ✔Results
Transformed the gathered data into a structured Pandas DataFrame, making it easy to analyze and manipulate. This data serves as a comprehensive snapshot of a given YouTube channel's content and engagement.


## 🎁Challenges

**Data Retrieval Limitations**: The YouTube API limits data retrieval to a maximum of 50 items at a time.

**Next Page Token Utilization** : Overcame the 50-item limit using the `next page token` concept provided by the YouTube API.

**Dynamic While Loop**: Implemented a dynamic `while` loop to handle varying item counts during data retrieval.


## 🏗 Future Improvements

Consider enhancements such as incorporating additional YouTube API features, optimizing data retrieval processes, or expanding the web app's functionality to handle multiple channels simultaneously.

## Conclusion
The project simplifies the extraction of YouTube channel data through a user-friendly web app, providing valuable insights into channel performance and content engagement. The implementation of exception handling ensures a smooth user experience, even in the face of potential API limitations and errors.

## 🤝🏼Contributors
[Vamshi Munukuntla](https://github.com/Vamshi-Munukuntla)


####
*After provided proper API Key and YouTube Channel ID.

