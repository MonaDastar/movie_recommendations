import requests_with_caching
import json

def get_tastedive_results(name):
    """
    Fetches TasteDive results for a given movie or title.

    Parameters:
    - name (str): The name of the movie or title.

    Returns:
    dict: A dictionary containing TasteDive results.
    """
    parameters = {"q": name, "type": "movies", "limit": 5}
    tastedive_response = requests_with_caching.get("https://tastedive.com/api/similar", params=parameters)
    return json.loads(tastedive_response.text)

def extract_movie_titles(tastedive_data):
    """
    Extracts movie titles from TasteDive data.

    Parameters:
    - tastedive_data (dict): TasteDive data dictionary.

    Returns:
    list: A list of movie titles.
    """
    return [movie["Name"] for movie in tastedive_data.get("Similar", {}).get("Results", [])]

def get_related_titles(movie_titles):
    """
    Retrieves related titles for a list of movie titles.

    Parameters:
    - movie_titles (list): A list of movie titles.

    Returns:
    list: A list of related movie titles.
    """
    related_titles = set()
    for title in movie_titles:
        tastedive_data = get_tastedive_results(title)
        related_titles.update(extract_movie_titles(tastedive_data))
    return list(related_titles)

def get_movie_data(movie_name):
    """
    Fetches movie data from the OMDB API.

    Parameters:
    - movie_name (str): The name of the movie.

    Returns:
    dict: A dictionary containing movie data.
    """
    parameters = {'t': movie_name, 'r': 'json'}
    omdbapi_response = requests_with_caching.get('http://www.omdbapi.com/', params=parameters)
    return json.loads(omdbapi_response.text)

def get_rotten_tomatoes_rating(movie_dict):
    """
    Retrieves the Rotten Tomatoes rating from movie data.

    Parameters:
    - movie_dict (dict): A dictionary containing movie data.

    Returns:
    int: The Rotten Tomatoes rating (percentage).
    """
    ratings = movie_dict.get('Ratings', [])
    for rating in ratings:
        if rating['Source'] == 'Rotten Tomatoes':
            return int(rating['Value'][:2])
    return 0

def get_sorted_recommendations(movie_list):
    """
    Generates sorted movie recommendations based on Rotten Tomatoes ratings.

    Parameters:
    - movie_list (list): A list of movie titles.

    Returns:
    list: A list of recommended movie titles sorted by Rotten Tomatoes ratings.
    """
    related_titles = get_related_titles(movie_list)
    ratings = [get_rotten_tomatoes_rating(get_movie_data(movie)) for movie in related_titles]
    sorted_movies = [title for _, title in sorted(zip(ratings, related_titles), key=lambda x: x[0], reverse=True)]
    return sorted_movies

# Example usage:
movies = get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
print(movies)
