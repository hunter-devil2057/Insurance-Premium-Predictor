# Health Insurance Premium Predictor

## Overview
The Health Insurance Premium Predictor is a web-based application built using Streamlit and Python. It predicts health insurance premiums based on user inputs such as age, sex, BMI, number of children, smoking status, and region. The application uses a RandomForestRegressor model from scikit-learn, trained on an insurance dataset, to make predictions.

## Features
- **Interactive UI**: Built with Streamlit, offering a simple and user-friendly interface.
- **Navigation**: Includes two pages:
  - **About**: Displays information about the application with a relevant image.
  - **Predict**: Allows users to input their details and receive a predicted insurance premium.
- **Machine Learning Model**: Utilizes RandomForestRegressor for accurate predictions.
- **Input Parameters**:
  - Age
  - Sex (Male/Female)
  - BMI (Body Mass Index)
  - Number of Children
  - Smoking Status (Yes/No)
  - Region (SouthEast, SouthWest, NorthEast, NorthWest)

## Prerequisites
To run this project locally, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hunter-devil2057/Insurance-Premium-Predictor.git
   cd Insurance-Premium-Predictor
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv insuranceprediction
   source insuranceprediction/bin/activate  # On Windows: insuranceprediction\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required Python packages using the provided `requirements.txt` file or manually.
   ```bash
   pip install -r requirements.txt
   ```
   Required packages:
   - streamlit
   - pandas
   - scikit-learn

4. **Dataset**:
   - The application uses an `insurance.csv` dataset, which should be placed in the project root directory.
   - Ensure the dataset includes the following columns: `age`, `sex`, `bmi`, `children`, `smoker`, `region`, and `charges`.

5. **Image**:
   - The About page displays an image (`health_insurance.jpeg`). Ensure this file is available in the project root directory or update the path in the code if stored elsewhere.

## Usage
1. **Run the Application**:
   ```bash
   streamlit run insurance.py
   ```
   This will start the Streamlit server, and the application will be accessible in your browser at `http://localhost:8501`.

2. **Navigate the Application**:
   - **About Page**: View information about the project and the health insurance image.
   - **Predict Page**: Enter the required details (age, sex, BMI, number of children, smoking status, and region) and click the "Predict" button to see the predicted insurance premium.

## Code Structure
- **insurance.py**: Main application file containing the Streamlit interface, data preprocessing, and RandomForestRegressor model.
- **insurance.csv**: Dataset used for training the model.
- **health_insurance.jpeg**: Image displayed on the About page.
- **requirements.txt**: Lists the Python dependencies.

## Model Details
- **Algorithm**: RandomForestRegressor from scikit-learn.
- **Features**:
  - `age`: Numeric (integer)
  - `sex`: Encoded as 0 (male) or 1 (female)
  - `bmi`: Numeric (float)
  - `children`: Numeric (integer)
  - `smoker`: Encoded as 0 (yes) or 1 (no)
  - `region`: Encoded as 0 (SouthEast), 1 (SouthWest), 2 (NorthEast), or 3 (NorthWest)
- **Target**: `charges` (insurance premium, float)
- **Preprocessing**: Categorical features (`sex`, `smoker`, `region`) are encoded numerically before training.

## Limitations
- The application assumes the `insurance.csv` dataset is available and correctly formatted.
- File paths for the dataset and image are hardcoded. Update them if the files are moved or renamed.
- The result provided by the application is only limited within the csv file. That is, the output it is going to be provided is going to be based on the data available in `insurance.csv` file
- The model is trained on the provided dataset and may not generalize well to significantly different data distributions.
- Input validation is minimal; users should ensure valid inputs (e.g., non-negative age and BMI).

## Contact
For questions or feedback, please open an issue on GitHub or reach out via:  
[[LinkedIn](https://img.icons8.com/color/24/linkedin.png)](https://www.linkedin.com/in/manish-shiwakoti-01721b260)  | [[Instagram](https://img.icons8.com/color/24/instagram-new.png)](https://www.instagram.com/manish.shiwakoti/)  | [[Gmail](https://img.icons8.com/color/24/gmail.png)](mailto:manishshiwakoti42@gmail.com) |  [[Phone](https://img.icons8.com/color/24/phone.png)](tel:+9779866556820)