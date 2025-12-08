import streamlit as st
from googleapiclient.discovery import build
import re
import emoji
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

# Initialize YouTube API
API_KEY = 'AIzaSyCMDpridBIhZCue7tm25exOF-Wq2rL0mKI'
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Helper function to fetch comments
def fetch_comments(video_id):
    comments = []
    nextPageToken = None

    while len(comments) < 1000:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            pageToken=nextPageToken
        )
        response = request.execute()
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        nextPageToken = response.get('nextPageToken')
        if not nextPageToken:
            break
    return comments

# Sentiment analysis function
def sentiment_scores(comment):
    sentiment_object = SentimentIntensityAnalyzer()
    return sentiment_object.polarity_scores(comment)['compound']

# Spam detection function
def detect_spam(comment):
    spam_keywords = ['subscribe', 'check out', 'visit my channel', 'free', 'earn money']
    return any(keyword in comment.lower() for keyword in spam_keywords)

# Streamlit UI
st.title("YouTube Comment Sentiment Analyzer")
video_url = st.text_input("Enter YouTube Video URL:")

if video_url:
    video_id = video_url.strip()[-11:]
    st.write(f"Video ID: **{video_id}**")

    with st.spinner("Fetching comments..."):
        comments = fetch_comments(video_id)

    if comments:
        st.success(f"Fetched {len(comments)} comments successfully!")

        # Data processing
        positive_comments, negative_comments, neutral_comments = [], [], []
        spam_comments = []
        all_words = []
        polarity_scores = []

        for comment_text in comments:
            comment_text = comment_text.lower().strip()
            all_words.extend(re.findall(r'\b\w+\b', comment_text))

            # Sentiment Analysis
            score = sentiment_scores(comment_text)
            polarity_scores.append(score)
            if score > 0.05:
                positive_comments.append(comment_text)
            elif score < -0.05:
                negative_comments.append(comment_text)
            else:
                neutral_comments.append(comment_text)

            # Spam Detection
            if detect_spam(comment_text):
                spam_comments.append(comment_text)

        # Display Results
        st.subheader("Sentiment Analysis Results")
        st.write(f"**Total Comments Analyzed:** {len(comments)}")
        st.write(f"**Positive Comments:** {len(positive_comments)}")
        st.write(f"**Negative Comments:** {len(negative_comments)}")
        st.write(f"**Neutral Comments:** {len(neutral_comments)}")
        st.write(f"**Spam Rate:** {round((len(spam_comments)/len(comments)) * 100, 2)}%")

        # Chart visualization
        fig, ax = plt.subplots()
        ax.bar(['Positive', 'Negative', 'Neutral', 'Spam'],
               [len(positive_comments), len(negative_comments), len(neutral_comments), len(spam_comments)],
               color=['blue', 'red', 'grey', 'purple'])
        st.pyplot(fig)

        # Word Cloud for Frequent Words
        st.subheader("Frequent Words in Comments")
        wordcloud = WordCloud(width=800, height=400, background_color='black').generate(' '.join(all_words))
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)

        # Sample Comments
        st.subheader("Sample Comments")
        st.write("### Top Positive Comment")
        st.success(max(positive_comments, key=sentiment_scores) if positive_comments else "No Positive Comments")

        st.write("### Top Negative Comment")
        st.error(min(negative_comments, key=sentiment_scores) if negative_comments else "No Negative Comments")

        st.write("### Top Spam Comment")
        st.warning(spam_comments[0] if spam_comments else "No Spam Comments")

    else:
        st.warning("No comments found for the given video.")
