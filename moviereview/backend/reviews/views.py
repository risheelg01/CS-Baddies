from django.shortcuts import render
import requests
from django.http import HttpResponse
from bs4 import BeautifulSoup
from textblob import TextBlob
#from imdb import Cinemagoer

def movie_review(movie_name):
   
   #declare string to use in url for webscraping
   url_movie_string = ""


   #replace spaces, dashes, and colons in movie name with dashes to get url string
   for movie_character in movie_name:
      if movie_character == '-' or movie_character == ' ':
         url_movie_string += '_'
      elif movie_character == ':':
         continue
      else:
         url_movie_string += movie_character
   
   print(url_movie_string)

   movie_url = "https://www.rottentomatoes.com/m/"+url_movie_string

   print (movie_url)
   
         



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
   movie_review("Spider-man: No Way Home")

#ensure main() is only called if script is run as main module
if __name__ == "__main__":
   main()


# Create your views here.
