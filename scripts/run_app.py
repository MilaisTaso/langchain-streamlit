import subprocess
import sys

def run_command(target):
    command = f"poetry run streamlit run src/api/{target}.py"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        run_command(target)
    else:
        print("Add command line arguments. -- python run_app.py [target] --")
