from django.shortcuts import render
import requests
from django.http import HttpResponse
from bs4 import BeautifulSoup
from textblob import TextBlob
from django.http import JsonResponse
#from imdb import Cinemagoer

def movie_review(movie_name):
   
   #declare string to use in url for webscraping and the final output string to website
   url_movie_string = ""
   output = ""


   #replace spaces, dashes, and colons in movie name with dashes to get url string
   for movie_character in movie_name:
      if movie_character == '-' or movie_character == ' ':
         url_movie_string += '_'
      elif movie_character == ':':
         continue
      else:
         url_movie_string += movie_character
   
   #print(url_movie_string)

   #create the full url for webscraping
   movie_url = "https://www.rottentomatoes.com/m/"+url_movie_string

   #print (movie_url)
   
   #get url request for movie name and check if url was found
   response = requests.get(movie_url)

   if response.status_code < 200 or response.status_code >= 300:
      #send error message because status code must be between 200-299 to be a successful response
      output = "Could not find movie, try again :)"
      #print(output)
      return output
   
   #print(response.text)


   
   #Use Beautiful Soup class to extract movie review from response HTML
   soup = BeautifulSoup(response.text, "html.parser")
   review_set = soup.find_all("div", {"class": "review js-clamp"})

   #if there is no reviews for movie, print error message
   if len(review_set) == 0:
      output = "Could not find any reviews for this movie"
      return output

   #declare counter for sentiment analysis and number of reviews
   movie_sentiment_counter = 0
   review_counter = 0

   #loop through all the review elements on the website and extract review text for sentiment analysis
   for review_element in review_set:   
      review_text = review_element.text.strip()
      review_counter += 1
      #declare sentiment review object 
      movie_analysis = TextBlob(review_text)
      movie_sentiment_counter  += movie_analysis.sentiment.polarity
      #print(review_text)

   #if the total sentiment is positive, movie is good, otherwise bad
   if movie_sentiment_counter > 0:
      output = "This movie is good"
   elif movie_sentiment_counter < 0:
      output = "This movie is bad"
   else:
      output = "This movie is mid"
   
   #print out the output
   print(output)

   

   """
   for review in reviews_containers:
      review_text = review.find("div", {"class": "the_review"}).text.strip()
      print(review_text)

   
   review_element = soup.find('div', {'class': 'review_area'})
   review_text = review_element.text.strip()
   
   print(review_text)
   """      



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

def movie_review_view(request, movie_name):
    output = movie_review(movie_name)
    return JsonResponse({'output': output})


#run movie review method
def main():
   movie_review("Big Hero 6")
   movie_review("Spider-man: No Way Home")
   movie_review("Doctor Strange In the Multiverse of Madness")
   movie_review("Jaws The Revenge")

#ensure main() is only called if script is run as main module
if __name__ == "__main__":
   main()


# Create your views here.
