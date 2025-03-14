# Python Strings and Formatters

## Strings in Python

In Python, a string is a sequence of characters enclosed in quotes. Strings can be defined using:

- Single quotes (`'Hello'`)
- Double quotes (`"Hello"`)
- Triple quotes (`'''Hello'''` or `"""Hello"""`) for multi-line strings.

### 1. Raw Strings
A raw string (`r"..."`) treats backslashes (`\`) as literal characters and does not interpret escape sequences.

```python
raw_string = r"Hello\t,\n World\\d"
print(raw_string)  # Output: Hello\t,\n World\\d
```

### 2. Normal Strings
A normal string interprets escape sequences like `\t` (tab) and `\n` (newline):

```python
normal_string = "Hello\t,\n World\\d"
print(normal_string)
```

### 3. Multi-line Strings
Triple quotes allow multi-line strings:

```python
triple_quotes = """Hello
World"""
print(triple_quotes)
```

## String Concatenation

Strings can be concatenated using `+`:

```python
my_string = "hello "
my_string_2 = "World"
my_string_3 = my_string + "" + my_string_2
print(my_string_3)  # Output: hello World
```

## String Indexing and Slicing

- Indexing starts from `0`.
- Slicing format: `[start:end:step]`.

```python
my_string = "Hello World"
print(my_string[-1])    # Output: d (last character)
print(len(my_string))   # Output: 11
print(my_string[6:10:2]) # Output: Wr (characters from index 6 to 9, step 2)
```

## String Methods

```python
print(my_string.upper())  # Converts to uppercase: "HELLO WORLD"
print(my_string.lower())  # Converts to lowercase: "hello world"
print("Hello World".split())  # Splits string into list: ['Hello', 'World']
print("hel-lo wor-ld".split("l"))  # Splitting on 'l': ['he', '-lo wor-', 'd']
```

## Joining Strings

```python
my_string_6 = "hello world"
print(my_string_6.join(["hello world"]))  # Output: hello world
```

## Loops in Strings
Strings are iterable, meaning you can loop through them like a list:

```python
for char in "Hello":
    print(char)
```

## Notes
- **Indexing** starts from `0`.
- **String length** starts from `1`.
- **Slicing** includes `start`, `end`, and `step` where `end` is exclusive.
- **Strings are immutable**, meaning their values cannot be changed after creation.

### Happy Coding! 🚀

