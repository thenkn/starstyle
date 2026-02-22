"""
LNNS - Line Numbers and Styling module
A simple utility for adding line numbers and styling to text.
"""


def add_line_numbers(text):
    """
    Add line numbers to text.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text with line numbers added
    """
    lines = text.split('\n')
    numbered_lines = []
    for i, line in enumerate(lines, start=1):
        numbered_lines.append(f"{i}. {line}")
    return '\n'.join(numbered_lines)


def style_with_stars(text):
    """
    Add star styling to text.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text styled with stars
    """
    lines = text.split('\n')
    max_length = max((len(line) for line in lines), default=0)
    border = '*' * (max_length + 4)
    
    styled_lines = [border]
    for line in lines:
        styled_lines.append(f"* {line.ljust(max_length)} *")
    styled_lines.append(border)
    
    return '\n'.join(styled_lines)


def lnns(text, add_numbers=True, add_stars=True):
    """
    Apply LNNS (Line Numbers and Star Styling) to text.
    
    Args:
        text (str): Input text
        add_numbers (bool): Whether to add line numbers
        add_stars (bool): Whether to add star styling
        
    Returns:
        str: Processed text
    """
    result = text
    
    if add_numbers:
        result = add_line_numbers(result)
    
    if add_stars:
        result = style_with_stars(result)
    
    return result


if __name__ == '__main__':
    sample_text = """Hello World
This is a test
Star Style"""
    
    print("Original text:")
    print(sample_text)
    print("\n" + "="*50 + "\n")
    
    print("With LNNS:")
    print(lnns(sample_text))
