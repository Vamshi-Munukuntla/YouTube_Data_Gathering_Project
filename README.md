# YouTube API Data Gathering using Streamlit Web App
### *Get any YouTube channel data (worldwide) with just a single click* *
Web App - https://youtube-data-gathering-project.streamlit.app/


## Project Description

The project focuses on leveraging the YouTube API to collect comprehensive data on channels globally. A user-friendly Streamlit web app was developed, enabling users to input their API key and channel ID for seamless retrieval and download of channel-specific data in CSV format.



## Objectives

1. Streamline the process of extracting key statistics and metadata from YouTube channels.
2. Develop an interactive web app for users to retrieve and download channel data using their API key and channel ID.
3. Create instructional videos to guide students in obtaining API Key and Channel ID's.


## Data Source

Utilized the YouTube API, specifically the Channels, PlaylistItems, and Videos endpoints, to collect relevant data on channels, playlists, and videos.


## Tools and Technologies

1. Python Environment
2. YouTube API
3. Streamlit for web app development
4. Pandas for data manipulation
5. Jupyter Notebooks for initial testing

## Data Exploration

Utilized the Channels endpoint to extract channel statistics like total views, total subscribers, and total number of videos uploaded.

Additionally, extracted the uploads playlist ID for each channel and then retrieved video meta data for every video from the playlist.


## Data Cleaning
The API provides data in JSON format, with relevant information nested within dictionaries.
Retrieving this data required careful navigation through nested structures.

The `get()` method was enmployed to handle potential errors, and `try` and `except` blocks were strategically implemented for error handling.

Separate functions were created for Channels, PlaylistItems, and VideoIds to enhance code readability and facilitate error detection.

## Data Analysis

Utilized PlaylistItems to retrieve video IDs associated with each channel's upload playlist.
Subsequently, used the Videos endpoint to fetch comprehensive video matadata such as video title, description, published date, tags, duration, views, likes, favorites, and comments

## Exception Handling

Robust exception handling using try and except blocks for scenarios such as 
1. No API Key
2. Incorrect API Key
3. No Channel ID
4. Incorrect Channel ID
5. Channel with no videos


## Results
Transformed the gathered data into a structured Pandas DataFrame, making it easy to analyze and manipulate. This data serves as a comprehensive snapshot of a given YouTube channel's content and engagement.


## Challenges

**Data Retrieval Limitations**: The YouTube API limits data retrieval to a maximum of 50 items at a time.

**Next Page Token Utilization** : Overcame the 50-item limit using the `next page token` concept provided by the YouTube API.

**Dynamic While Loop**: Implemented a dynamic `while` loop to handle varying item counts during data retrieval.


## Future Improvements

Consider enhancements such as incorporating additional YouTube API features, optimizing data retrieval processes, or expanding the web app's functionality to handle multiple channels simultaneously.

## Code Structure
Organized the project code into a clear and modular structure. Functions for Channels, PlaylistItems, and VideoIds were created for readability and ease of error detection. Detailed comments and documentation within the code for ease of understanding.

## Conclusion
The project simplifies the extraction of YouTube channel data through a user-friendly web app, providing valuable insights into channel performance and content engagement. The implementation of exception handling ensures a smooth user experience, even in the face of potential API limitations and errors.

## Acknowledgments
Acknowledges the use of the YouTube API and any other external libraries or resources that contributed to the project.

## Contributors
[Vamshi Munukuntla](https://github.com/Vamshi-Munukuntla)




## 
*After provided proper API Key and YouTube Channel ID.







