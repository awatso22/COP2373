import inspect
import AntoniaWatson_ProgrammingAssignment2  # replace with your assignment name (without .py)

# replace docstring_example with your assignment name in the next 2 lines of code
with open("AntoniaWatson_ProgrammingAssignment2.py_design_doc.txt", "w") as doc:
    doc.write(f"# Technical Design Document: {AntoniaWatson_ProgrammingAssignment2.__name__}\n\n")
    # replace with your name, the date, and the description of the program
    doc.write(f"# Name: Antonia Watson\n")
    doc.write(f"# Date: February 12, 2026\n")
    doc.write(f"# Program Description: Spam email scoring\n\n")

    # replace docstring_example with your assignment name
    for name, func in inspect.getmembers(AntoniaWatson_ProgrammingAssignment2, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")

    # replace with link to your repository
    doc.write(f"#Link to your repository: https://github.com/awatso22/COP2373")
print('Complete')