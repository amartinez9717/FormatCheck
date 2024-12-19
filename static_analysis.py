import subprocess

def run_static_analysis():
    try:
        result = subprocess.run(['flake8', '--max-line-length=88'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error during static analysis: {e}"

if __name__ == "__main__":
    output = run_static_analysis()
    with open("flake8_report.txt", "w") as f:
        f.write(output)
