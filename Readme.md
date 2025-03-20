# Movie Recommendation System

Welcome to the **Movie Recommendation System**—a lightweight and interactive web application engineered with Streamlit and Python. This solution empowers users to discover movies and TV shows that align with their personal preferences through an innovative clustering approach using DBSCAN.

---

## Project Overview

The Movie Recommendation System leverages a pre-clustered dataset (`clustered_movies.csv`) containing comprehensive movie metadata. Users can obtain tailored recommendations based on various selection criteria:
- **By Movie Name**: Select a movie from a dropdown and receive similar titles within the same DBSCAN cluster (excluding the chosen movie).
- **By Genre**: Choose a genre (e.g., *drama*, *comedy*, *scifi*) to get a random selection of movies matching that category.
- **By Production Country**: Pick a full country name (e.g., *United States*, *Japan*) and discover movies produced in that region.

The application is designed to provide an intuitive and seamless user experience with a minimalistic yet powerful interface.

---

## Key Features

- **Multiple Recommendation Methods**:  
  - **Movie Name**: Discover similar movies based on clustering.
  - **Genre**: Explore a specific movie category with a random selection.
  - **Production Country**: Access movies produced in a chosen country with full names (no cryptic codes).

- **Adjustable Recommendation Count**:  
  - Customize the number of recommendations with a slider (range: 1–10, default: 5).  
  - If the selected criteria yield fewer matches, all available options are displayed.

- **User-Friendly Interface**:  
  - Powered by Streamlit for a responsive web experience.  
  - Dropdown menus and error messages ensure clarity and ease of navigation.

- **Comprehensive Data Display**:  
  - Full country names are provided for 56 countries, enhancing clarity and eliminating the ambiguity of country codes.

---

## Getting Started

### Requirements

- **Python Version**: 3.7+
- **Key Libraries**:  
  - `streamlit`
  - `pandas`

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd movie-recommendation-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install streamlit pandas
   ```
   Alternatively, use the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add the Dataset**:
   - Ensure the `clustered_movies.csv` file is placed in the project folder.
   - The CSV must include the following columns: `name`, `main_genre`, `lead_prod_country`, and `dbscan_clusters`.

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   - Open your browser and navigate to [http://localhost:8501](http://localhost:8501).

---

## How to Use

1. **Open the App**:  
   - Launch using the command above.

2. **Select a Recommendation Type**:
   - Choose from “By Movie Name”, “By Genre”, or “By Production Country” using the top dropdown.

3. **Enter Your Preference**:
   - **By Movie Name**: Select your favorite movie from the dropdown.
   - **By Genre**: Choose a genre from the provided list.
   - **By Production Country**: Select a country (displayed in full) from the dropdown.

4. **Set the Number of Recommendations**:  
   - Adjust the slider (1–10) to determine how many recommendations to display.

5. **Receive Your Recommendations**:  
   - Recommendations appear as a numbered list.
   - In cases with no matching titles, an appropriate error message is displayed.

---

## Project Structure

```
movie-recommendation-system/
├── app.py                  # Main application script
├── clustered_movies.csv    # Dataset with movie data
├── requirements.txt        # Python dependencies (optional)
└── README.md               # Project documentation
```

---

## Dataset Details

The application utilizes `clustered_movies.csv`, which should include:
- **name**: Movie/TV show titles.
- **main_genre**: Primary genre (e.g., *drama*).
- **lead_prod_country**: Country code (e.g., *US*).
- **dbscan_clusters**: Cluster labels determined by DBSCAN.

Ensure the dataset is aligned with the supported genres and production countries for full functionality.

---

## Limitations

- **Recommendation Method**:  
  - Recommendations are randomly sampled within the selected criteria without ranking based on popularity or ratings.
  - Only one recommendation type is supported at a time.

- **Static Dataset**:  
  - The application uses a static CSV file; manual data refreshes are required for updates.

---

## Potential Improvements

- **Enhanced Filtering**:  
  - Integrate multi-filter support (e.g., combining genre and country).
  
- **Rich Metadata**:  
  - Incorporate additional movie details such as runtime and ratings.

- **Dynamic Data Integration**:  
  - Connect to a dynamic data source (e.g., an API) for real-time updates.

---

## License

This project is licensed under the MIT License. For further details, please refer to the [LICENSE](LICENSE) file.

---

## Contributions

We welcome contributions to enhance the system. Feel free to submit issues or pull requests on [GitHub](<repository-url>). Your insights and innovative ideas are highly valued.

---

## Notes

- Replace `<repository-url>` with the actual URL of your repository if hosted online.
- Ensure that the `clustered_movies.csv` dataset conforms to the structure and assumptions mentioned above.

---

Embrace the opportunity to explore and enhance our Movie Recommendation System. We appreciate your commitment to innovation and excellence.
```

This version is structured to meet professional standards and is fully prepared for immediate integration into your GitHub repository. Let me know if further adjustments are required.