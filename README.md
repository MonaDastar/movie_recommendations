### Project: Movie Recommendations Mashup





This project involves mashing up data from two different APIs, TasteDive and OMDB, to make movie recommendations. The TasteDive API allows querying related items based on a movie (or bands, TV shows, etc.), while the OMDB API provides data about movies, including scores from various review sites.
Project Overview

The main tasks of this project include:

    Fetching TasteDive results for a given movie or title.
    Extracting movie titles from TasteDive data.
    Retrieving related titles for a list of movie titles.
    Fetching movie data from the OMDB API.
    Retrieving the Rotten Tomatoes rating from movie data.
    Generating sorted movie recommendations based on Rotten Tomatoes ratings.

Instructions
Setup

Before running the code, make sure to install the required libraries using the following command:

bash

pip install requests_with_caching

Code Usage

python

# Import necessary libraries
import requests_with_caching
import json

# Function to get TasteDive results for a given movie or title
def get_tastedive_results(name):
    # ... (see code for details)

# Function to extract movie titles from TasteDive data
def extract_movie_titles(tastedive_data):
    # ... (see code for details)

# Function to get related titles for a list of movie titles
def get_related_titles(movie_titles):
    # ... (see code for details)

# Function to fetch movie data from the OMDB API
def get_movie_data(movie_name):
    # ... (see code for details)

# Function to get the Rotten Tomatoes rating from movie data
def get_rotten_tomatoes_rating(movie_dict):
    # ... (see code for details)

# Function to generate sorted movie recommendations based on Rotten Tomatoes ratings
def get_sorted_recommendations(movie_list):
    # ... (see code for details)

# Example usage:
movies = get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
print(movies)