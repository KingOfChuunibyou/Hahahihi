# Exercise

Do these exercise in a Python file.

## Question 1: Given these variables:

- Chicken's voice : petok petok petok
- Location and Date of Birth : Antartika, 29 February 2023
- Distance between your house and school
- Number of cat your friend have

What are the data types? Give an example of what it should be. Answer these in your python file:

Write it like this

```py
num_of_cats: int = 12  # Number of cat your friend have
```

**NOTE**

1. This is called type hinting (`:`) where you can **hint** what type the variable should hold. Useful for code clarity.
2. Notice the variable naming? Python has a "best practice" to use **snake case** as the naming convention, where you separate each space of a name with `_`. For instance "chicken count" becomes `chicken_count`. Do not use capital letter when you name your variable.

## Question 2: 

Given a user input two numbers (`input1`, `input2`) and a string (`input_str`) sequentially, output these:

A2.1 Output whether `input1` can be divided by `input2` (`bool`)

A2.2 . We assume that `input1` is a Celcius Degree. Output the Farenheit value! The formula is `(input1 x 9/5) + 32`.

A2.3 Finally, output a string that contains this format: "User input $input1$ and $input2$ with a string `$input_str$`. The boolean value is `$boolval$". $input1$ is user input (`input1`). $input2$ is (`input2`) and $boolval$ is `the output of A.2.1`

### Example
**Input**

```
20
8
mbeee
```

**Output**
```
False
68.0
User input 20 and 8 with a string mbeee. The boolean value is False
```
**Explanation**
`False` since 20 cannot be divided by 8
`68.0` is 20 x 9 / 5 + 32 = 68

## Note

Use `input()` to receive user's input. For example: `
```py
input1 = input()
```
Use print to output the results

**Hint** : `string + string` is  `stringstring` in Python

## Question 3:

A player in some game can be considered **hit the pity** if the counter reaches 90.

Given a number from user. output whether the user hits the pity or not (boolean).

### Example

**Input**
```
80
```

**Output**
```
False
```

**Input**
```
90
```

**Output**
```
True
```