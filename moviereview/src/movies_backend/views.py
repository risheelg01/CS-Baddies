from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
    url_movie_string = ""
    output = ""
    request_body = json.loads(request.body)
    print(request_body)
    movie_name = request_body['data']
    
    print(movie_name)
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
        output = "Could not find movie, try adding the year"
        #print(output)
        return JsonResponse({"message": output})
    
    #print(response.text)


    
    #Use Beautiful Soup class to extract movie review from response HTML
    soup = BeautifulSoup(response.text, "html.parser")
    review_set = soup.find_all("div", {"class": "review js-clamp"})

    #if there is no reviews for movie, print error message
    if len(review_set) == 0:
        output = "Could not find any reviews for this movie"
        return JsonResponse({"message": output})

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
    print(movie_sentiment_counter)
    #if the total sentiment is positive, movie is good, otherwise bad
    if movie_sentiment_counter > 0.1:
        output = "This movie is good"
    elif movie_sentiment_counter < -0.1:
        output = "This movie is bad"
    else:
        output = "This movie is mid"
    
    print(output)
    #print out the output
    return JsonResponse({"message": output})
        # return  HttpResponse("Hello")