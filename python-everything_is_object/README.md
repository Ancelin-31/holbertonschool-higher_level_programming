![Python Mutable vs Immutable](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)  
*Image source: [Wikipedia - Python Logo](https://en.wikipedia.org/wiki/File:Python-logo-notext.svg)*

# Understanding Mutability in Python: What I Learned

As I worked through this project, I explored some fundamental — yet surprisingly subtle — concepts in Python: **mutability**, **object identity**, and how Python handles **function arguments**. These are critical ideas that can deeply influence the way your code behaves. In this post, I’ll walk through what I learned, using lots of examples to make it all clear. If you’ve ever been confused by lists changing unexpectedly or variables behaving strangely in functions, this is for you.

---

## ID and Type: Every Object Has Them

In Python, every value you work with is an **object**, and each object has two core attributes: its **type** and **identity** (its location in memory). You can explore these using the built-in `type()` and `id()` functions.

```python
x = 5
print(type(x))  # <class 'int'>
print(id(x))    # Something like 9788800

y = x
print(id(y))    # Same as x — they point to the same object

y = 6
print(id(y))    # Different now! Because integers are immutable
```

The id() function returns a unique identifier for an object during its lifetime. When you assign one variable to another, you're just copying a reference — not cloning the object. But if you assign a new value, and the object is immutable, Python creates a new object instead.

### Mutable Objects

Mutable objects are those that can be changed after they are created. Lists, dictionaries, and sets are good examples. If two variables refer to the same mutable object, and one of them modifies it, the change is visible through the other.

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] – a changed too!

print(id(a) == id(b))  # True – they are the same object
```

Mutables can be dangerous if you’re not careful: modifying them in one place can have unexpected consequences elsewhere in your code.

### Immutable Objects

Immutable objects cannot be changed after they are created. Integers, floats, strings, and tuples are examples of this. Assigning a new value creates a new object, even if it looks like you’re “changing” a variable.

```python
x = "hello"
y = x
y = "world"
print(x)  # 'hello' – x is untouched

print(id(x) == id(y))  # False – different objects
```

Tuples are a bit tricky: they are immutable, but they can hold mutable objects:

```python
t = ([1, 2], 3)
t[0].append(4)
print(t)  # ([1, 2, 4], 3) – the list inside the tuple *was* mutated!
```

## Why It Matters: Python Treats Them Differently

Knowing whether something is mutable or immutable helps you predict how your variables behave. For example, copying a mutable object like a list just copies a reference, not a true copy:

```python
a = [1, 2, 3]
b = a
b[0] = 100
print(a)  # [100, 2, 3] – surprise!

# Use slicing or copy module for a shallow copy
c = a[:]
c[0] = 999
print(a)  # [100, 2, 3] – unchanged
```

For immutable types, copying and changing just creates a new object:

```python
s = "hello"
t = s
t += " world"
print(s)  # 'hello' – original unchanged
```

Mutable objects can be used to store state, while immutable objects are often safer to pass around.

## How Arguments Are Passed: Object References

In Python, arguments are passed by object reference, also described as “call by sharing.” Whether a function modifies the argument depends on whether the object is mutable.

```python
def modify_list(lst):
    lst.append(99)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 99] – list was modified!
```

Now compare with an immutable object:

```python
def modify_string(s):
    s += " world"
    print("Inside:", s)

my_str = "hello"
modify_string(my_str)
print("Outside:", my_str)  # 'hello' – unchanged!
```

So: if you pass a mutable object to a function, and the function modifies it, your original object is affected. If it’s immutable, the function can't change it directly.

## Final Thoughts

Understanding mutability, identity, and how Python passes arguments has made my code more predictable and robust. I’ve stopped being surprised by functions changing my lists and started thinking more intentionally about whether I want to share state between objects. These concepts might seem subtle at first, but mastering them leads to cleaner, safer, and more efficient Python code.

By Ancelin CHEVALLIER.
