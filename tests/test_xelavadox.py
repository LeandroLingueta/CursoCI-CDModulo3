import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "src" / "xelavadox.py"
PYTHON = sys.executable


def run_script(input_text):
    completed = subprocess.run([PYTHON, str(SCRIPT)], input=input_text, text=True, capture_output=True, check=True)
    output = completed.stdout.strip()
    prompt = "Digite um numero para elevar ele a ele mesmo: "
    if output.startswith(prompt):
        output = output[len(prompt):]
    return output


def test_xelavadox_small_number():
    assert run_script("2\n") == "2 elevado a 2 é 4"


def test_xelavadox_three():
    assert run_script("3\n") == "3 elevado a 3 é 27"
