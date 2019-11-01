Some useful notes selected from the book "Python Workout"

Comparison of different types(turn the input string into an integer)

Python 2 first compare them by type, and then compare them within that type. All integers were smaller than all lists, and all lists were smaller than all strings. In Python 3, you cnnot make such a comparison, it leads to a TypeError.

Use "f-string" to insert values from variables into strings:

e.g. `print(f"Your guess of {user_guess} is too high")`


