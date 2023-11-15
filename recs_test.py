import os
import pprint

import openai
from dotenv import find_dotenv, load_dotenv
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.llms.openai import OpenAI
from langchain.utilities import GoogleSerperAPIWrapper

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")


llm = OpenAI(temperature=0)
search = GoogleSerperAPIWrapper(type="places")
results = search.results("Italian restaurants in Austin, TX")

def format_places_results(places_results):
    formatted_output = []
    for places_item in places_results:
        formatted_output.append({
            "Title": places_item["title"],
            "Address": places_item["address"],
            "Rating": places_item["rating"],
            "Amount of Ratings": places_item["ratingCount"],
            "Category": places_item["category"],
            "Image Url": places_item["thumbnailUrl"]
        })
    return formatted_output


formatted_results = format_places_results(results["places"])
pprint.pp(formatted_results)