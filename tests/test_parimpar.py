import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "src" / "parimpar.py"
PYTHON = sys.executable


def run_script(input_text):
    completed = subprocess.run([PYTHON, str(SCRIPT)], input=input_text, text=True, capture_output=True, check=True)
    output = completed.stdout.strip()
    prompt = "Digite um numero para saber se e par ou impar: "
    if output.startswith(prompt):
        output = output[len(prompt):]
    return output


def test_parimpar_even_number():
    assert run_script("10\n") == "O numero é par."


def test_parimpar_odd_number():
    assert run_script("7\n") == "O numero é impar."
