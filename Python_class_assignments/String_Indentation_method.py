def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)

example = """
        This is an example of intendation.
        We are learning something new
        Good luck!
"""
output = indent(example, 5)
print(output)