import pandas as pd
import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_channel_details(youtube, channel_id):

    """
    Get details of a YouTube channel using the provided API key and channel ID.

    Parameters:
    - YouTube (googleapiclient.discovery.Resource): YouTube API resource.
    - channel_id (str): YouTube channel ID.

    Returns:
    - pd.DataFrame: DataFrame containing channel details.
    """

    try:
        request = youtube.channels().list(
            part="snippet, contentDetails, statistics",
            id=channel_id)
        response = request.execute()

        items = response.get('items', [])

        if not items:
            return st.error("Channel Not Found. Please Check your Channel ID.")

        channel = items[0]
        snippet = channel.get('snippet', {})
        content_details = channel.get("contentDetails", {})
        statistics = channel.get('statistics', {})

        channel_details = {
            'channel_title': snippet.get('title', None),
            'playlist_id': content_details.get('relatedPlaylists', {}).get('uploads', None),
            'total_views': statistics.get('viewCount', 0),
            'total_subscribers': statistics.get('subscriberCount', 0),
            'total_videos': statistics.get('videoCount', 0),
        }
        # # Check if channel has no videos
        # if channel_details['total_videos'] == 0:
        #     return st.error("This channel currently has no videos.")

        return pd.DataFrame([channel_details])
    except HttpError as e:
        if e.resp.status == 400:
            return st.error(f"API Key not Found")
        else:
            return st.error(f"Error getting channel details: {e}")


def fetch_video_ids(youtube, playlist_id):

    """
    Fetch video IDs from a YouTube playlist.

    Parameters:
    - YouTube (googleapiclient.discovery.Resource): YouTube API resource.
    - playlist_id (str): YouTube playlist ID.

    Returns:
    - list: List of video IDs.
    """

    all_video_ids = []
    page_token = None

    try:
        while True:
            request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=page_token
            )

            response = request.execute()
            items = response.get('items', [])

            for item in items:
                video_id = item.get("contentDetails", None).get("videoId", None)
                all_video_ids.append(video_id)

            page_token = response.get('nextPageToken')
            if not page_token:
                break

        return all_video_ids

    except HttpError as e:
        if e.resp.status == 404:
            return st.error(f"No Videos Available in the Channel.")
        else:
            return st.error(f"Error getting channel details: {e}")


def get_video_meta_data(youtube, video_ids):

    """
    Get metadata for a list of YouTube videos.

    Parameters:
    - YouTube (googleapiclient.discovery.Resource): YouTube API resource.
    - video_ids (list): List of YouTube video IDs.

    Returns:
    - pd.DataFrame: DataFrame containing video metadata.
    """
    all_video_details = []

    try:
        for i in range(0, len(video_ids), 50):
            current_video_ids = video_ids[i:i + 50]
            request = youtube.videos().list(
                part="snippet, contentDetails, statistics",
                id=",".join(current_video_ids)
            )
            response = request.execute()

            items = response.get('items', [])

            for item in items:
                snippet = item.get("snippet", {})
                content_details = item.get('contentDetails', {})
                statistics = item.get('statistics', {})

                tag_list = snippet.get('tags', [])
                tags = ",".join(tag_list) if tag_list else None

                video_details = {
                    'video_title': snippet.get('title', None),
                    'description': snippet.get('description', None),
                    'published_at': snippet.get('publishedAt', None),
                    'tags': tags,
                    'video_duration': content_details.get('duration', None),
                    'views': statistics.get('viewCount', 0),
                    'likes': statistics.get('likeCount', 0),
                    'favorites': statistics.get('favoriteCount', 0),
                    'comments': statistics.get('commentCount', 0)
                }
                all_video_details.append(video_details)
        return pd.DataFrame(all_video_details)

    except HttpError as e:
        st.error('Error getting video Details:{e}')
