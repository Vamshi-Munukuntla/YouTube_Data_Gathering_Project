# YouTube API Data Gathering using Streamlit Web App
#### *Get any YouTube channel data (worldwide) with just a single click* *

</br>

## **Step-by-Step tutorial to create this project from scratch**
[![YouTube API Key](https://res.cloudinary.com/marcomontalbano/image/upload/v1703402736/video_to_markdown/images/youtube--bW-FytTQse4-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/bW-FytTQse4?feature=shared "YouTube API Key")

</br>

### **Web App**
https://youtube-data-gathering-project.streamlit.app/

</br>

### **Demo**
[![YouTube API Key](https://res.cloudinary.com/marcomontalbano/image/upload/v1703402736/video_to_markdown/images/youtube--bW-FytTQse4-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/bW-FytTQse4?feature=shared "YouTube API Key")

</br>

## Overview:

![project_screenshot_white_background](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/5fa29ffd-7027-4241-bd56-ee375e280f38)

## 📄Project Description

1. The project focuses on leveraging the YouTube API to collect comprehensive data on channels globally. 
2. A user-friendly Streamlit web app was developed, enabling users to input their API key and channel ID for seamless retrieval and download of channel-specific data in CSV format.

## 🎯Objectives

1. Streamline the process of extracting key statistics and metadata from YouTube channels and store the data in a CSV format.
2. Develop an interactive web app for users to retrieve and download channel data using their API key and channel ID.
3. Create instructional videos to guide students in obtaining API Key and Channel ID's.

![Slide2](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/6c465e26-49a0-4f3c-98bc-53f74dc5449a)

## 🛠Tools and Technologies⚙

![Slide4](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/21699c2b-c485-4df8-bd0f-7e2a956f694f)


## Methodology

1. Utilized the YouTube API, specifically the Channels, PlaylistItems, and Videos endpoints, to collect relevant data on channels, playlists, and videos.

2. Utilized the Channels endpoint to extract channel statistics like total views, total subscribers, and total number of videos uploaded.

3. Additionally, extracted the uploads playlist ID for each channel and then retrieved video meta data for every video from the playlist.

![Slide11](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project/assets/100301262/a845f854-856b-4131-9ead-6b41e80e4077)


## 🧹Data Cleaning
1. The API provides data in JSON format, with relevant information nested within dictionaries. Retrieving this data required careful navigation through nested structures.

2. The `get()` method was enmployed to handle potential errors, and `try` and `except` blocks were strategically implemented for error handling.

3. Dedicated functions were crafted for Channels, PlaylistItems, and VideoIds to enhance code readability and facilitate error detection.

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

## Code Structure
Organized the project code into a clear and modular structure. Functions for Channels, PlaylistItems, and VideoIds were created for readability and ease of error detection. Detailed comments and documentation within the code for ease of understanding.

## Conclusion
The project simplifies the extraction of YouTube channel data through a user-friendly web app, providing valuable insights into channel performance and content engagement. The implementation of exception handling ensures a smooth user experience, even in the face of potential API limitations and errors.

## 🙌Acknowledgments
Acknowledges the use of the YouTube API and any other external libraries or resources that contributed to the project.

## 🙌🤝🏼Contributors
[Vamshi Munukuntla](https://github.com/Vamshi-Munukuntla)




####
*After provided proper API Key and YouTube Channel ID.







