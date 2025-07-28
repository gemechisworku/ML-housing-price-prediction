# ML-housing-price-prediction

## Overview

ML-housing-price-prediction is a machine learning project that predicts housing prices based on various features such as location, size, number of rooms, and more. The project demonstrates data preprocessing, feature engineering, model selection, training, and evaluation.

## Features

- Data cleaning and preprocessing (handling missing values, outliers, encoding categorical variables)
- Prediction pipeline via Flask App (REST API for real-time price prediction)
- Exploratory data analysis (EDA) and visualizations
- Multiple regression models (Linear Regression, Random Forest, etc.)
- Model evaluation metrics (RMSE, MAE, R²)

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/gemechisworku/ML-housing-price-prediction.git
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your dataset in the `data/` directory.
2. Run the main script:
    ```
    python application.py
    ```
3. Visit http://127.0.0.1:5000/ to access the app and perform predictions

## Project Structure

- `data/` - Raw and processed datasets
- `notebooks/` - Jupyter notebooks for EDA and model training
- `src/` - Source code for data processing and modeling
- `artifacts/` - pkl files

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.