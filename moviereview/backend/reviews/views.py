from django.shortcuts import render
import requests
from django.http import HttpResponse
from bs4 import BeautifulSoup
from textblob import TextBlob
from imdb import Cinemagoer

def movie_review(movie_name):
   

   #Cinemagoer only lets you use the rating and not the text reviews, have to use Beautiful Soup
   """
   #create an instance of IMDB module
   movie_search = Cinemagoer()
   #search for movie on IMDB with movie name input
   search_result = movie_search.search_movie(movie_name)
   
   #print(search_result[0])
   
   #if movie not found, return error message
   if len(search_result) == 0:
      return "Movie not found, try again"
   
   #Retrieve first search result and get movie object through movie ID
   movie_ID = search_result[0].movieID
   movie = movie_search.get_movie(movie_ID)

   movie_search.update(movie) 
   info=movie.default_info
   print(info)
   #Extract movie reviews from IMDB database and store them in a list
   movie_search.update(movie, 'review')
   reviews = movie['review']

   #if no reviews for movie, return error message
   if len(reviews) == 0:
      return "No reviews for " +str(movie_name)
"""

#run movie review method
def main():
   movie_review("Big Hero 6")

#ensure main() is only called if script is run as main module
if __name__ == "__main__":
   main()


# Create your views here.
