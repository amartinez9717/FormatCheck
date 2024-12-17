import openai
import glob
import os
import traceback

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
report = "## AI-Powered Code Quality Report\n\n"

# Iterate over all Python files
for file in glob.glob("**/*.py", recursive=True):
    try:
        with open(file, "r") as f:
            content = f.read()
        print(f"Analyzing {file}...")

        # Updated OpenAI Completion Call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert Python code reviewer. Analyze the code for issues and provide actionable suggestions."},
                {"role": "user", "content": f"Code:\n{content}"}
            ],
            max_tokens=500,
            temperature=0.5
        )

        # Accessing response correctly in openai>=1.0.0
        suggestions = response['choices'][0]['message']['content']
        report += f"### File: {file}\n{suggestions}\n\n"

    except Exception as e:
        print(f"Error analyzing {file}: {traceback.format_exc()}")
        report += f"### File: {file}\nError: {str(e)}\n\n"

# Write the report to a markdown file
with open("ai_feedback.md", "w") as feedback_file:
    feedback_file.write(report)
