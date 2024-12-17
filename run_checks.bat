@echo off
REM Run Checks Script
REM This script runs code quality checks locally and generates a feedback report.

REM Step 1: Clean up old outputs
echo Cleaning up old output files...
del pylint_output.json 2>nul
del flake8_output.txt 2>nul
del radon_output.json 2>nul
del feedback.md 2>nul

REM Step 2: Run Pylint for Static Analysis
echo Running Pylint...
python -m pylint **/*.py --output-format=json > pylint_output.json || echo Pylint failed.

REM Step 3: Run Flake8 for Style Checks
echo Running Flake8...
python -m flake8 **/*.py --format="%%(path)s:%%(row)d:%%(col)d: %%(code)s %%(text)s" > flake8_output.txt || echo Flake8 failed.

REM Step 4: Run Radon for Cyclomatic Complexity
echo Running Radon for Cyclomatic Complexity...
python -m radon cc **/*.py -s -j > radon_output.json || echo Radon failed.

REM Step 5: Generate Feedback Report
echo Generating Feedback...
python - <<EOF
import json

# Initialize feedback
feedback = '## Code Review Feedback\\n'

# Pylint feedback
feedback += '\\n### 1. Static Analysis Feedback (Pylint)\\n'
try:
    with open('pylint_output.json', 'r') as f:
        pylint_issues = json.load(f)
        if pylint_issues:
            for issue in pylint_issues:
                feedback += (
                    f'- **{issue["path"]}** (Line {issue["line"]}, Column {issue["column"]}): '
                    f'{issue["message"]} [{issue["symbol"]}]\\n'
                )
            feedback += '\\n**Suggestions:**\\n'
            feedback += '- Fix Pylint issues by following PEP-8 and Python best practices.\\n'
        else:
            feedback += 'No issues detected.\\n'
except Exception as e:
    feedback += f'Error processing Pylint results: {str(e)}\\n'

# Flake8 feedback
feedback += '\\n### 2. Static Analysis Feedback (Flake8)\\n'
try:
    with open('flake8_output.txt', 'r') as f:
        flake8_issues = f.readlines()
        if flake8_issues:
            for issue in flake8_issues:
                feedback += f'- {issue.strip()}\\n'
            feedback += '\\n**Suggestions:**\\n'
            feedback += '- Fix indentation errors and align code with PEP-8.\\n'
        else:
            feedback += 'No issues detected.\\n'
except Exception as e:
    feedback += f'Error processing Flake8 results: {str(e)}\\n'

# Radon feedback
feedback += '\\n### 3. Cyclomatic Complexity Feedback\\n'
try:
    with open('radon_output.json', 'r') as f:
        radon_issues = json.load(f)
        if radon_issues:
            for file, issues in radon_issues.items():
                for issue in issues:
                    feedback += (
                        f'- **{file}**: Function `{issue["name"]}` at line {issue["lineno"]} '
                        f'has complexity {issue["complexity"]} (Grade: {issue["rank"]}).\\n'
                    )
            feedback += '\\n**Suggestions:**\\n'
            feedback += '- Refactor functions with high complexity into smaller, manageable units.\\n'
        else:
            feedback += 'No complexity issues detected.\\n'
except Exception as e:
    feedback += f'Error processing Radon results: {str(e)}\\n'

# Save feedback
with open('feedback.md', 'w') as f:
    f.write(feedback)
EOF

REM Step 6: Summary Output
echo Checks complete! See 'feedback.md' for the results.
