# Exception Handling in Python for Beginners

Python is a powerful and flexible programming language, but like all languages, it's not immune to errors. In Python, there are two main types of errors: syntax errors and exceptions. Syntax errors are problems with your code that prevent it from running at all, while exceptions are errors that occur while your code is running. This article will focus on handling exceptions, which is a crucial aspect of writing robust, reliable Python code.

Compile Error = SYNTAX CODINGANMU BERMASALAH

```py
print(('hehe)
```

Run Time Error: Exception error muncul pas kodenya running

## Understanding Exceptions

In Python, exceptions are events that occur during the execution of a program that disrupt the normal flow of the program's instructions. When an error occurs, Python will usually stop and generate an error message. These exceptions need to be handled to prevent your program from crashing.

Here are some common types of Python exceptions:

- `TypeError`: This is raised when an operation or function is applied to an object of an inappropriate type.
- `ValueError`: This occurs when a function receives an argument of the correct type but inappropriate value.
- `IndexError`: This is raised when a sequence subscript is out of range.
- `KeyError`: This happens when a dictionary key is not found.
- `FileNotFoundError`: This is raised when a file or directory is requested but doesn't exist.

## Basic Exception Handling: Try and Except

The most common way to handle exceptions in Python is using `try` and `except` blocks. Here's a basic structure:

```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to execute if the exception is raised
```

For example:

```python
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("Sorry, this file does not exist.")
```

In this example, if the file "non_existent_file.txt" does not exist, instead of crashing, the program will print the message "Sorry, this file does not exist."

## Catching Multiple Exceptions

Sometimes, a block of code may raise more than one type of exception. You can catch multiple exceptions by using multiple `except` blocks:

```python
try:
    # Code that might raise an exception
except ExceptionType1:
    # Code to execute if ExceptionType1 is raised
except ExceptionType2:
    # Code to execute if ExceptionType2 is raised
```

## Finally: Cleaning Up After Exceptions

The `finally` keyword in Python is used to create a block of code that will always be executed whether an exception has been raised or not. This is often used for cleanup actions, like closing files or releasing resources:

```python
try:
    file = open("file.txt", "r")
finally:
    file.close()
```

In this example, whether opening the file succeeds or fails, the file will be closed.

## Conclusion

Exception handling is a fundamental part of programming in Python. By understanding and using exception handling, you can make your programs more robust and reliable, and provide better user experiences. Remember that exceptions are not necessarily bad – they are your program's way of communicating that something unexpected has happened, and it's your job as a programmer to decide how to respond. Happy coding!