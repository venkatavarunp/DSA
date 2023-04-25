# Recursion
Recursion is a process of calling the same function to achieve desired output.

Recursion needs a base case to break out the recurring function calls.

Recursion of two ways
- single branch
- two or multiple branches
**Factorial**

factorial of n can be 

`n! = n*(n-1)!`
```python
def factorial(n):
    # Base case: n=1
    if n==1:
        return 1
    # Recursive case: n*(n-1)!
    return n*factorial(n-1)
```
**Fibonacci Number**

Fibonacci series is given as

`F(n)=F(n-1)+F(n-2) where F(0)=0,F(1)=1`
```python
def fibonacci(n):
    # Base case: n=0 or 1
    if n<=1:
        return n
    # Recursive case: fib(n)=fib(n-1)+fib(n-2)
    return fibonacci(n-1)+fibonacci(n-2)
```
