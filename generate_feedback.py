def generate_feedback():
    with open('flake8_report.txt', 'r') as f:
        flake8_feedback = f.read()

    with open('pattern_recognition_report.txt', 'r') as f:
        ml_feedback = f.read()

    feedback = f"Static Analysis Feedback:\n{flake8_feedback}\n\nML Pattern Recognition Feedback:\n{ml_feedback}"

    with open('feedback_report.txt', 'w') as f:
        f.write(feedback)

if __name__ == "__main__":
    generate_feedback()
