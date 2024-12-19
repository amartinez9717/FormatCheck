def generate_feedback():
    with open('analysis_report.txt', 'r') as f:
        analysis_feedback = f.read()

    with open('pattern_recognition_report.txt', 'r') as f:
        ml_feedback = f.read()

    with open('feedback_report.txt', 'w') as f:
        f.write("Static Analysis Feedback:\n")
        f.write(analysis_feedback+"\n")
        f.write("ML Pattern Recognition Feedback:\n")
        f.write(ml_feedback+"\n")

if __name__ == "__main__":
    generate_feedback()
