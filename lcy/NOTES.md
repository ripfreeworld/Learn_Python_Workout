## Some useful notes selected from the book

1. Comparison of different types(turn the input string into an     integer): <br>
Python 2 first compare them by type, and then compare them within that type. All integers were smaller than all lists, and all lists were smaller than all strings. In Python 3, you cnnot make such a comparison, it leads to a TypeError.

2. Use "f-string" to insert values from variables into strings:<br> e.g. <pre>print(f"Your guess of {user_guess} is too high")</pre>

3. `for` and `while` loops in Python support an `else` clause, just as if statements do. The `else` attached to a loop means: Only execute this code if we didn't encounter a `break`.<br>
e.g. <pre>
for vowel in 'aeiou':
&nbsp;  if word[0] == vowel:
&nbsp;      starts_with_vowel = True
&nbsp;      break
else:
&nbsp;  starts_with_vowel = False
</pre>
4. strings are immutable: <pre>
s = 'abcd'
s[0] = '!'</pre>
This code leads to an exception.<br>
Strings are the most common type used as dictionary keys. If strings were mutable, then they wouldn't be allowed as dict keys.

