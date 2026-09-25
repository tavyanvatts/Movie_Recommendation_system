import os
import streamlit as st
import pickle
import pandas as pd


try:
    import gdown
except ImportError:
    os.system('pip install gdown')
    import gdown

FILES_TO_DOWNLOAD = {
    "movies_dict.pkl": "1aAP_qAHj2IPHBSu-krj_iLcCY85ZKz2G",
    "movies.pkl": "1pjd9-oW4Bt0RdEyYEBxTuanb0dkQ2wY_",
    "similarity.pkl": "1do8NLqFLMs046svy2p9PtDZ9jPFrmxEQ"
}
for filename, file_id in FILES_TO_DOWNLOAD.items():
    if not os.path.exists(filename):
        with st.spinner(f"Downloading {filename} from cloud storage... Please wait."):
            url = f"https://drive.google.com/uc?id={file_id}"
            gdown.download(url, filename, quiet=False)

def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
  recommended_movies = []
  for i in movies_list:
    recommended_movies.append(movies.iloc[i[0]].title)
  return recommended_movies
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Select Movie to recommend', movies['title'].values)

if st.button('Recommend'):
    recommended_movies = recommend(selected_movie_name)
    for i in recommended_movies:
        st.write(i)