# starstyle
star style

## LNNS - Line Numbers and Star Styling

A simple utility for adding line numbers and styling to text with stars.

### Features

- Add line numbers to text
- Apply star-based styling/borders
- Combine both features for enhanced text presentation

### Usage

```python
from lnns import lnns

# Example text
text = """Hello World
This is a test
Star Style"""

# Apply LNNS with both line numbers and stars
result = lnns(text)
print(result)
```

Output:
```
*********************
* 1. Hello World    *
* 2. This is a test *
* 3. Star Style     *
*********************
```

### Running the module

```bash
python lnns.py
```

### Running tests

```bash
python -m unittest test_lnns -v
```
