import streamlit as st
import pickle
import pandas as pd

# Add animated background using CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(-45deg, #1f4037, #99f2c8, #1c92d2, #f2fcfe);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .stApp {
        background-color: transparent;
    }

    h1 {
        color: white;
        text-align: center;
    }

    .stSelectbox label, .stButton button {
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Title
st.title('🎬 Movie Recommender System')

# Movie selector
selected_movie_name = st.selectbox(
    'Select a movie you like:',
    movies['title'].values)

# Recommend button
if st.button('Recommend'):
    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
        return recommended_movies

    recommendations = recommend(selected_movie_name)

    st.subheader("You may also like:")
    for i in recommendations:
        st.markdown(f"✅ {i}")

