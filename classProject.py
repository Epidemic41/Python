# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:53:23 2022

@author: Dax Martineau, David Lee
"""
#dataset source
#https://files.grouplens.org/datasets/movielens/ml-latest-small.zip

import pandas as pd

df = pd.read_csv('movies.csv', index_col='title') #import movieID title and genre dataset
ratDf = pd.read_csv('ratings.csv', index_col='rating') #import MovieId rating dataset

genreInput = input("What is your favorite genre? ") #promt user for genre they like listed in movies.csv

likeGenre = (df [ df['genres'].str.contains(genreInput) ]).index #query for genre and store movie title
likeId = (df [ df['genres'].str.contains(genreInput) ])['movieId'] #query for genre and store movieID

genreInput2 = input("What is a genre you do not like? ") #query for genre for genre they dont like listed in movies.csv

disGenre = (df [ df['genres'].str.contains(genreInput2) ]).index #query for genre and store movie title
dislikedId = (df [ df['genres'].str.contains(genreInput2) ])['movieId'] #query for genre and store movieID

recGenre=likeGenre[~likeGenre.isin(disGenre)].dropna() #removes unliked genres from liked movietitle list
recId=likeId[~likeId.isin(dislikedId)].dropna() #removes unliked genres from liked movieID list

result_size = recGenre.size #store number of recomended titles

avgRat = [] #used to store that ratings per title
print() #formatting
print("Movie Recommendations") #formatting

for i in range(10): #get ratings for first ten results
    likeRat = (ratDf [ ratDf['movieId'] == recId[i] ]).index #print movie title
    
    if likeRat.size > 0: #make sure movie has ratings
        ratList = 0.0 #prevents ratings from different movies from spilling over
        
        for i in range(likeRat.size): #get average rating per movie
            ratList += likeRat[i] #add rating from same movie
        ratList = ratList / float(likeRat.size) #calcualte average rating per movie
        avgRat.append(round(ratList, 1)) #adding rating to array that corralates to it's movie
        
for i in range(10):
    print(recGenre[i], 'Rating:', avgRat[i]) #print the movie title and average rating of 10 movies
    
    

    
    
    
     
    
    
    






