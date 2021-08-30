# Movie-recommender
Movie-recommender uses parameter like cast, director, genre and keywords to calculate similarity between movies. This technique is popularly known as content based filtering. 
Note: The movie dataset used in the project contains top tmdb movies before July 2017. 

## Process
1) I used the popular movies dataset present in Kaggle: https://www.kaggle.com/rounakbanik/the-movies-dataset which contains metadata for over 45000 movies.
2) Extracted the top movies from the dataset, leaving only 9000 movies 
3) Applied preprocessing to create our smd dataset. 
4) Created a flask back end to serve the application.
5) Used Data Structures concepts like sets, heapsort and other efficiency algorithms to speed up recommendations
6) Used front end template from https://github.com/inboxpraveen/recommendation-system to create a full fledged local running flask application  
