import os

import openai
from dotenv import find_dotenv, load_dotenv
from langchain.utilities import GoogleSerperAPIWrapper

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

def fetch_places(query):
    search = GoogleSerperAPIWrapper(type="places")
    results = search.results(query)
    return format_places_results(results["places"])

def format_places_results(places_results):
    formatted_output = []
    for places_item in places_results:
        formatted_output.append({
            "Title": places_item["title"],
            "Address": places_item["address"],
            "Rating": places_item["rating"],
            "Amount of Ratings": places_item["ratingCount"],
            "Category": places_item["category"],
#            "Image Url": places_item["thumbnailUrl"]
        })
    print(formatted_output)
    return formatted_output
