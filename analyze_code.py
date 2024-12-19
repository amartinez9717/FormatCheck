import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
model = joblib.load('code_smells_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Define a mapping of model output to code smell descriptions
code_smell_descriptions = {
    "NoError": "No code smell detected.",
    "Long Method": "The method is too long and might need refactoring.",
    "Magic Number": "The use of hardcoded numbers without context. Consider replacing with named constants.",
    "Deep Nesting": "Too many nested loops or conditions. This might affect readability and performance.",
    "Inefficient Loop": "The loop could be optimized to improve performance.",
    "Poor Naming": "The function or variable names are not descriptive. Consider renaming for clarity."
}

def analyze_code():
    code_files = ['file1.py', 'file2.py']  # Add your files dynamically (you could list files in a directory)
    results = []
    
    for file in code_files:
        try:
            with open(file, 'r') as f:
                code = f.read()

            if not code.strip():  # Skip empty files
                results.append((file, "No code found"))
                continue

            # Split the code into functions or logical sections (you can adjust this logic as needed)
            code_sections = split_code_into_sections(code)
            
            all_issues = []
            
            for section in code_sections:
                # Preprocess the code using the same vectorizer as during training
                X = vectorizer.transform([section])  # Transform the raw code into numerical features

                # Use the trained model to predict issues
                analysis_result = model.predict(X)  # Predicting on the transformed data

                # Get the description for the predicted code smell
                issue = code_smell_descriptions.get(analysis_result[0], "Unknown issue")
                if issue != "No code smell detected.":
                    all_issues.append(f"{issue}:\nSection {section}\n")
                    #all_issues.append(issue)

            if all_issues:
                results.append((file, "\n".join(all_issues)))
            else:
                results.append((file, "No code smell detected."))

        except Exception as e:
            results.append((file, f"Error analyzing file: {str(e)}"))
    
    return results

def split_code_into_sections(code):
    """
    Split the code into logical sections such as functions or methods.
    This is a simple implementation, you can refine it based on your use case.
    """
    # Split the code into functions based on the 'def ' keyword (you can adjust based on your needs)
    sections = []
    functions = code.split('def ')
    for func in functions:
        if func.strip():
            sections.append("def " + func.strip())
    return sections

def write_results_to_file(results):
    # Write the results to a text file
    with open("pattern_recognition_report.txt", "w") as f:
        for file, result in results:
            f.write(f"File: {file}, \nIssues: \n{result}\n")

if __name__ == "__main__":
    # Run the analysis
    results = analyze_code()
    
    # Write the results to a file
    write_results_to_file(results)
