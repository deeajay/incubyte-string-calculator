# String Calculator

Scope of work: https://blog.incubyte.co/blog/tdd-assessment/

Quick start (macOS)
1. Clone the repo:
```bash
git clone <repository-url>
cd incubyte-string-calculator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
# or, if only running tests:
pip install pytest
```

Usage
```python
from src.string_calculator import StringCalculator

sc = StringCalculator()
print(sc.add(""))    # 0
print(sc.add("1"))   # 1
```

Run tests
- From project root:
```bash
python3 -m pytest -q tests/test_string_calculator.py
# or
pytest -q tests/test_string_calculator.py
```

Troubleshooting
- If `pytest: command not found`, run it with `python3 -m pytest` or install pytest into the active environment (`pip install pytest`).
- Ensure the current working directory is the project root so tests can locate the `src` package.