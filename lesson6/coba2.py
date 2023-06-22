"""
User input:

```
7
```

Output:

```
*
**
***
****
*****
******
*******
******
*****
****
***
**
*

```

Pola pikir kebaik

WHY -> HOW -> WHAT
"problem nya apa" -> "gimana gambaran besar" -> "ngodingnya pake apa if apa kaha"
"""

number = int(input())

for i in range(1, number): # * ** ***
    print("*" * i)
for i in range(number, 0, -1): # *** ** * 
    print("*" * i)

