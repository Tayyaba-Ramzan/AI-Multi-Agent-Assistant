from agents import function_tool

@function_tool
def solve(expression: str) -> str:
    """
    Evaluates a basic mathematical expression passed as a string.

    This tool allows the AI agent to compute real-time math expressions using Python's built-in `eval()` function.
    It supports standard arithmetic operations including:

    - Addition (+)
    - Subtraction (-)
    - Multiplication (*)
    - Division (/)
    - Exponents (**)
    - Parentheses for grouping

    Example:
        >>> solve("3 + 5 * (2 - 1)")
        'Result: 8'

    Parameters:
        expression (str): A valid arithmetic expression formatted as a Python-compatible string.
                          Example: "45 * 12 + (102 / 3) - 16**2"

    Returns:
        str: A string containing the result of the evaluated expression. 
             If an error occurs during evaluation (e.g., invalid syntax), an error message is returned.

    Warning:
        This function uses Python’s `eval()` internally, which may pose security risks if used on untrusted input.
        In production environments, consider using a math parser like `sympy` or `asteval` for safer evaluation.

    Usage:
        This tool is designed for simple to moderately complex numerical computations, not for symbolic algebra.
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error solving expression: {str(e)}"
