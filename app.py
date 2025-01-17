import streamlit as st
import pickle
import pandas as pd
moviews_dict = pickle.load(open('movie_dict.pkl', 'rb'))    
moviews = pd.DataFrame(moviews_dict)


similarity = pickle.load(open('similarity.pkl', 'rb'))  

def recommend(movie):
    index = moviews[moviews['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(moviews.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')
st.write('Welcome to the Movie Recommender System. Select a movie and click on the Recommend button to get recommendations.')   

selected_movie_name = st.selectbox('Select a movie:', moviews['title'].values)   
st.write('You selected:', selected_movie_name)

if  st.button('Recommend'):
    recommended_movies = recommend(selected_movie_name) 
    for i in recommended_movies:
        st.write(i)