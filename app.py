import streamlit as st
import pandas as pd
from googleapiclient.discovery import build

# Importing your helper functions
from helper import get_channel_details, fetch_video_ids, get_video_meta_data

# Add Streamlit page config
st.set_page_config(
    page_title="YouTube API Project",
    page_icon=":movie_camera:",
    layout="wide",
    initial_sidebar_state="expanded"
)


def inputs():
    """Get API key and Channel ID from user input."""
    with st.form('Get Channel Data'):
        col1, col2 = st.columns(2)
        api_key = col1.text_input(label='API key', key='api_key')
        channel_id = col2.text_input(label='Channel Id', key='channel_id')

        submitted = st.form_submit_button('Get Data', )

        if submitted and (not api_key or not channel_id):
            st.error('Please provide both the API key and the channel id')
            return None, None, submitted

    return api_key, channel_id, submitted


def get_data(api_key, channel_id):
    """Retrieve channel and video data from the YouTube API."""
    youtube = build(
        serviceName='youtube',
        version='v3',
        developerKey=api_key)

    channel_df = get_channel_details(youtube, channel_id)

    if not channel_df.empty:
        playlist_id = channel_df.loc[0, 'playlist_id']
        total_videos = channel_df.loc[0, 'total_videos']
        if total_videos == str(0):
            return st.warning('No Videos available in the channel.')
        else:
            video_ids = fetch_video_ids(youtube, playlist_id)
            video_df = get_video_meta_data(youtube, video_ids)
            total_df = pd.merge(video_df, channel_df, how='cross')
            return total_df


def download_data(df, file_name):
    """Download and display YouTube data."""
    youtube_data = df.to_csv(index=False)

    # Display Top 5 Rows
    st.write('Top 5 Rows')
    st.dataframe(df.head())

    st.download_button(
        label='Download Data',
        type='primary',
        data=youtube_data,
        file_name=f"{file_name}.csv",
        key='download_button',
        help="Click to download the data as a CSV file."
    )


def sidebar():
    st.sidebar.subheader("YouTube Data Gathering Web App")
    st.sidebar.write('Your favorite youtube channel data is just a click away.')
    st.sidebar.divider()
    st.sidebar.markdown('Source code can be found [here](https://github.com/Vamshi-Munukuntla/YouTube_Data_Gathering_Project)')
    st.sidebar.markdown('**Tutorial to create this app can be found** [here](your_tutorial_link)')
    st.sidebar.divider()
    st.sidebar.markdown('Made by [Vamshi Munukuntla](https://www.linkedin.com/in/vamshi-kumar87/)')


# def faqs():
#     st.subheader("FAQ's")
#
#     faq_data = {
#         "**Step-by-Step tutorial to create this app**": "",
#         "How to get YouTube API Key": "",
#         "How to get YouTube Channel ID": ""
#     }
#
#     for question, video_link in faq_data.items():
#         with st.expander(question):
#             st.video(video_link)


if __name__ == '__main__':
    st.title("YouTube Data Gathering Project")
    st.markdown('##### *Get any YouTube channel data in a matter of seconds.*')

    sidebar()
    api_key, channel_id, submitted = inputs()

    if submitted and api_key is not None and channel_id is not None:
        df = get_data(api_key, channel_id)

        if df is not None and not df.empty:
            download_data(df, df.loc[0, 'channel_title'])

    st.text("\n"*3)
    # faqs()
