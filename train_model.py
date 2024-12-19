import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Example dataset (code and labels)
data = [
    ("def foo(): pass", "NoError"),
    ("def calculate(a, b): return a + b", "Long Method"),
    ("x = 42", "Magic Number"),
    ("def bad_func():\n  for i in range(10):\n    for j in range(10):\n      print(i + j)", "Deep Nesting"),
    ("result = []\nfor i in range(100):\n  result.append(i * 2)", "Inefficient Loop"),
    ("def very_long_function():\n  return sum([i for i in range(100)])", "Long Method"),
    ("y = 0\nx = y + 5\n# TODO: Replace magic number 5 with a constant", "Magic Number"),
    ("def bad_naming_function():\n  tmp1 = 10\n  tmp2 = 20\n  return tmp1 + tmp2", "Poor Naming")
]

# Convert to a DataFrame
df = pd.DataFrame(data, columns=["code", "label"])

# Create the TF-IDF vectorizer and transform the code data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['code'])

# Train the model (RandomForestClassifier used as an example)
model = RandomForestClassifier()
model.fit(X, df['label'])

# Save the model and vectorizer
joblib.dump(model, 'code_smells_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
