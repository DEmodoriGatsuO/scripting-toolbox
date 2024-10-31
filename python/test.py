def contains_question_mark(input_string):
    """
    Checks if the input string contains a '?' character.

    Parameters:
    - input_string (str): The string to check.

    Returns:
    - bool: True if the string contains '?', False otherwise.
    """
    return '?' in input_string

# Example usage
test_string = r"C:\Users\???\open-interpreter-docker\container-simple\Dockerfile"
result = contains_question_mark(test_string)
print(f"Does the string contain a '?': {result}")