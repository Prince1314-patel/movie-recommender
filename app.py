import streamlit as st
import pandas as pd
import random

# Load the movie data
df_movies = pd.read_csv("clustered_movies.csv")

# Country code to name mapping based on the dataset
country_mapping = {
    'US': 'United States',
    'GB': 'United Kingdom',
    'JP': 'Japan',
    'KR': 'South Korea',
    'CA': 'Canada',
    'ES': 'Spain',
    'AU': 'Australia',
    'CN': 'China',
    'FR': 'France',
    'IN': 'India',
    'MX': 'Mexico',
    'BR': 'Brazil',
    'DE': 'Germany',
    'TW': 'Taiwan',
    'IT': 'Italy',
    'AR': 'Argentina',
    'CO': 'Colombia',
    'TR': 'Turkey',
    'TH': 'Thailand',
    'PL': 'Poland',
    'RU': 'Russia',
    'DK': 'Denmark',
    'IL': 'Israel',
    'SE': 'Sweden',
    'BE': 'Belgium',
    'NO': 'Norway',
    'ZA': 'South Africa',
    'NZ': 'New Zealand',
    'SG': 'Singapore',
    'IE': 'Ireland',
    'RO': 'Romania',
    'NL': 'Netherlands',
    'CL': 'Chile',
    'LB': 'Lebanon',
    'PH': 'Philippines',
    'CZ': 'Czech Republic',
    'AT': 'Austria',
    'IS': 'Iceland',
    'HU': 'Hungary',
    'ID': 'Indonesia',
    'FI': 'Finland',
    'SA': 'Saudi Arabia',
    'HK': 'Hong Kong',
    'EG': 'Egypt',
    'IO': 'India',  # British Indian Ocean Territory, likely not relevant
    'CH': 'Switzerland',
    'PT': 'Portugal',
    'JO': 'Jordan',
    'HR': 'Croatia',
    'PR': 'Puerto Rico',
    'SN': 'Senegal',
    'LU': 'Luxembourg',
    'UA': 'Ukraine',
    'MA': 'Morocco',
    'UY': 'Uruguay',
    'AE': 'United Arab Emirates'
}

# Add full country names to the dataframe
df_movies['lead_prod_country_name'] = df_movies['lead_prod_country'].map(country_mapping).fillna('Unknown')

# Get unique values for dropdowns
genres = sorted(df_movies['main_genre'].unique())
countries = sorted(df_movies['lead_prod_country_name'].unique())
movie_names = df_movies['name'].values

# Function to recommend movies based on user selection
def recommend_movies(recommendation_type, input_value, n_recommendations=5):
    if recommendation_type == "By Movie Name":
        # Recommend movies from the same cluster as the entered movie
        movie = df_movies[df_movies['name'] == input_value].iloc[0]
        cluster = movie['dbscan_clusters']
        cluster_movies = df_movies[df_movies['dbscan_clusters'] == cluster]
        cluster_movies = cluster_movies[cluster_movies['name'] != input_value] 
        if cluster_movies.empty:
            return ["No similar movies found."]
        else:
            if len(cluster_movies) >= n_recommendations:
                return random.sample(list(cluster_movies['name']), n_recommendations)
            else:
                return list(cluster_movies['name'])
    
    elif recommendation_type == "By Genre":
        # Recommend movies from the selected genre
        genre_movies = df_movies[df_movies['main_genre'] == input_value]
        if genre_movies.empty:
            return ["No movies found for this genre."]
        else:
            if len(genre_movies) >= n_recommendations:
                return random.sample(list(genre_movies['name']), n_recommendations)
            else:
                return list(genre_movies['name'])
    
    elif recommendation_type == "By Production Country":
        # Recommend movies from the selected country
        country_movies = df_movies[df_movies['lead_prod_country_name'] == input_value]
        if country_movies.empty:
            return ["No movies found for this country."]
        else:
            if len(country_movies) >= n_recommendations:
                return random.sample(list(country_movies['name']), n_recommendations)
            else:
                return list(country_movies['name'])

# Streamlit App UI
st.title("Movie Recommendation System")
st.write("Choose how you want to get movie recommendations.")
st.divider()

# Let the user choose recommendation type
recommendation_type = st.selectbox("Get recommendations:", 
                                   options=["By Movie Name", "By Genre", "By Production Country"])

# Show input fields based on the selected recommendation type
if recommendation_type == "By Movie Name":
    movie_name = st.selectbox("Select a movie you like:", options=movie_names)
    input_value = movie_name
elif recommendation_type == "By Genre":
    selected_genre = st.selectbox("Select a genre:", options=genres)
    input_value = selected_genre
elif recommendation_type == "By Production Country":
    selected_country = st.selectbox("Select a production country:", options=countries)
    input_value = selected_country

# Allow the user to choose the number of recommendations
n_recommendations = st.slider("Number of Recommendations:", min_value=1, max_value=10, value=5)

# Button to generate recommendations
if st.button("Recommend"):
    recommendations = recommend_movies(recommendation_type, input_value, n_recommendations)
    if isinstance(recommendations, list) and recommendations and recommendations[0].startswith("No "):
        st.error(recommendations[0])
    else:
        st.subheader("Recommended Movies:")
        for i, movie in enumerate(recommendations, 1):
            st.markdown(f"{i}. {movie}")