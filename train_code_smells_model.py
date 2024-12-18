import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import nltk
from nltk.tokenize import word_tokenize
import os

# Download and verify NLTK resources
try:
    nltk.download('punkt', force=True)  # Ensure punkt is downloaded
except Exception as e:
    print("Error downloading 'punkt':", e)
    exit(1)

# Load dataset with a semicolon delimiter if necessary
try:
    dataset = pd.read_csv("code_smells_dataset.csv", delimiter=";")
    print("Dataset Loaded Successfully.")
except FileNotFoundError:
    print("Error: Dataset file 'code_smells_dataset.csv' not found. Ensure the file exists in the same directory.")
    exit(1)
except pd.errors.ParserError as e:
    print(f"Error: Problem with parsing the dataset. Details: {e}")
    exit(1)


# Define feature extraction
def extract_features(code):
    lines = code.splitlines()
    return {
        "num_lines": len(lines),
        "avg_line_length": sum(len(line) for line in lines) / len(lines) if lines else 0,
        "num_comments": sum(1 for line in lines if line.strip().startswith("#")),
        "num_tokens": len(word_tokenize(code)),
    }

# Extract features
try:
    features = pd.DataFrame([extract_features(code) for code in dataset["code"]])
    labels = dataset["label"]
    print("Features Extracted Successfully.")
except KeyError as e:
    print(f"Error: Missing column in dataset: {e}. Ensure 'code' and 'label' columns are present.")
    exit(1)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train the model
try:
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    print("Model Trained Successfully.")
except Exception as e:
    print("Error during model training:", e)
    exit(1)

# Evaluate the model
try:
    y_pred = model.predict(X_test)
    print("Model Evaluation:\n", classification_report(y_test, y_pred))
except Exception as e:
    print("Error during model evaluation:", e)
    exit(1)

# Save the model
try:
    joblib.dump(model, "code_smells_model.pkl")
    print("Model saved as 'code_smells_model.pkl'.")
except Exception as e:
    print("Error saving the model:", e)
    exit(1)
