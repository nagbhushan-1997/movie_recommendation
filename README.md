# Movie Recommendation Content-Based System

This project is a content-based movie recommendation system. It recommends movies to users based on the similarity of movie content.

## Features

- Recommend movies based on content similarity
- Uses cosine similarity for measuring similarity between movies
- Utilizes TF-IDF vectorization for text data

## Requirements

The following libraries are required to run the application:

- `pandas`
- `numpy`
- `scikit-learn`
- `flask`

You can install the required libraries using the following command:

```bash
pip install pandas numpy scikit-learn flask
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/movie_recommendation_content_based_system.git
```

2. Navigate to the project directory:

```bash
cd movie_recommendation_content_based_system
```

3. Run the application:

```bash
python app.py
```

4. Open your web browser and go to `http://127.0.0.1:5000/` to use the movie recommendation system.

## Project Structure

- `app.py`: The main application file that contains the Flask web server and recommendation logic.
- `movies.csv`: The dataset containing movie information.
- `templates/`: Directory containing HTML templates for the web interface.

## How It Works

1. The movie data is loaded from `movies.csv`.
2. TF-IDF vectorization is applied to the movie descriptions.
3. Cosine similarity is calculated between movies.
4. The application provides recommendations based on the similarity scores.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- The dataset used in this project is sourced from [MovieLens](https://grouplens.org/datasets/movielens/).

-   Thank you for your support!!!
