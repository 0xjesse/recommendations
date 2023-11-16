import os

import openai
import pandas as pd
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from langchain.utilities import GoogleSerperAPIWrapper

# Load environment variables
load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Function to fetch places
def fetch_places(query):
    search = GoogleSerperAPIWrapper(type="places")
    results = search.results(query)
    return format_places_results(results["places"])

# Function to format places results
def format_places_results(places_results):
    formatted_output = []
    for places_item in places_results:
        formatted_output.append({
            "Title": places_item["title"],
            "Address": places_item["address"],
            "Rating": places_item["rating"],
            "Amount of Ratings": places_item["ratingCount"],
            "Category": places_item["category"],
            # "Image Url": places_item["thumbnailUrl"] # Uncomment if needed
        })
    return formatted_output

# Streamlit UI Components
# Streamlit UI for sorting and filtering
st.title("Local Gems")

# App description or bio
st.subheader("Discover Your Next Favorite Spot")
st.text("Local Scout helps you find the best places anywhere. Whether you're looking for the best clubs in Austin, cozy Italian restaurants in NY, or delightful bakeries in California, Local Scout is your go-to guide for discovering local gems.")

query = st.text_input("Enter a location (e.g., 'Italian restaurants in Austin, TX')")

# Sorting option
sort_order = st.selectbox("Sort by Rating:", ["Highest First", "Lowest First"])

# Filtering option
min_rating = st.slider("Minimum Rating:", 0.0, 5.0, 3.5, 0.1)

if st.button("Search"):
    if query:
        with st.spinner('Fetching results...'):
            results = fetch_places(query)
            if results:
                # Convert to DataFrame
                df = pd.DataFrame(results)

                # Sort the DataFrame
                if sort_order == "Highest First":
                    df = df.sort_values(by="Rating", ascending=False)
                else:
                    df = df.sort_values(by="Rating", ascending=True)

                # Filter the DataFrame
                df = df[df["Rating"] >= min_rating]

                # Display the DataFrame
                st.dataframe(df)
            else:
                st.write("No results found.")
