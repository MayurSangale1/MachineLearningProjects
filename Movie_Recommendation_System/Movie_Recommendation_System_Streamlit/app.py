import streamlit as st
import pickle as pk
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse= True, key=lambda x:x[1])[1:6]
    recommended = []
    for i in movie_list:
        recommended.append((movies.iloc[i[0]]).title)
    return recommended


movies_dict = pk.load(open('movie_list.pkl',"rb"))
similarity = pk.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommendation System')

selected_movie = st.selectbox(
    'how would you like to be contacted',
    movies['title'].values
)
if st.button('Recommend'):
    recommendation = recommend(selected_movie)
    for i in recommendation:
        st.write(i)