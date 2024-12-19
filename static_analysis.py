import subprocess

def run_flake8():
    try:
        result = subprocess.run(['flake8', '--max-line-length=88'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error during flake8 analysis: {e}"

def run_pylint(files):
    try:
        result = subprocess.run(['pylint'] + files, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error during pylint analysis: {e}"

def run_radon(files):
    try:
        result = subprocess.run(['radon', 'cc'] + files, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error during radon analysis: {e}"

if __name__ == "__main__":
    files_to_analyze = ['file1.py', 'file2.py']  # Replace with your files or directories
    flake8_output = run_flake8()
    pylint_output = run_pylint(files_to_analyze)
    radon_output = run_radon(files_to_analyze)

    with open("analysis_report.txt", "w") as report_file:
        report_file.write("Flake8 Report:\n")
        report_file.write(flake8_output + "\n")
        report_file.write("Pylint Report:\n")
        report_file.write(pylint_output + "\n")
        report_file.write("Radon Cyclomatic Complexity Report: \nA: 1-10 (Excelente)\nB: 11-20 (Bueno)\nC: 21-30 (Promedio)\nD: 31-40 (Deficiente)\nE: 41-50 (Pobre)\nF: 50+ (Fallido)\n")
        report_file.write(radon_output + "\n")
