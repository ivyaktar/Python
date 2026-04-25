# python syntax compared to java . give every step by step distinction so i could look at it as a complete note sheet

# Python vs Java: Detailed Syntax Notes (with explanations)

This version goes deeper into explanations, especially up to Topic 9. You can copy directly from here.

---

## 1) Hello world and program entry

**Python**

```python
print("Hello, world")
print('Hello World!')
print(4.5)
print(4.5,"Hello")
print('hello','end',87,False,end='\n')
print(87,False,end='|')

print(4.5,"Hello")

```

- No class or function is required. The interpreter executes line by line.
- The `print()` function outputs text.

**Java**

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world");
    }
}

```

- Java requires all code to be inside a class.
- `main` is the entry point where execution begins.
- `System.out.println()` prints text to the console.

**Key idea**: Python is interpreted and starts directly at the first line. Java needs a compiled class with a defined entry point method `main`.

---

## 2) Comments and documentation

**Python**

```python
# This is a single line comment
"""This is a docstring (documentation string).
   Usually placed at the top of modules, classes, or functions.
   It can be accessed using obj.__doc__.
"""

```

- `#` starts a comment until the end of the line.
- Triple quotes `"""` or `'''` are used for multi-line docstrings.

**Java**

```java
// This is a single line comment
/* This is a multi-line comment */
/** Javadoc comment used to generate documentation */

```

- `//` creates single line comments.
- `/* ... */` creates multi-line comments.
- `/** ... */` Javadoc comments are processed by the `javadoc` tool to create API documentation.

**Key idea**: Python docstrings become part of the runtime object. Java Javadoc comments are for generating external documentation.

---

## 3) Variables and data types

**Python**

```python
x = 42          # integer
y = 3.14        # float
name = "Ivy"    # string
ok = True       # boolean

x = "now a string"  # allowed (dynamic typing)

#  data types

# int=-2345,0,133

# float=-9.7

# string = "hello", 'hello"', "'", oppposite quotation mark diye wrapped.

#boolean : True; False;

#VARIABLES 
hello= 'time'
world='world'

print(hello,world)

world=hello

print(hello,world)

hello='no'

print(hello,world) #top to bottom recognised. not bottom to top jabe

##naming convention

hello_world #snake case
helloWord #camel case

xx9hello noT work
hello9
```

- No type declarations are needed.
- Types are decided at runtime.
- A variable can change type later.

**Java**

```java
int x = 42;
double y = 3.14;
String name = "Ivy";
boolean ok = true;

var n = 10;  // type inference (Java 10+)

```

- Java requires explicit type declarations (`int`, `double`, etc.).
- Variable type cannot change after declaration.
- `var` can infer type at compile-time, but the type is still fixed.

**Key idea**: Python = dynamically typed. Java = statically typed and checked at compile-time.

---

## 4) Printing and string formatting

**Python**

```python
user = "Ivy"
age = 20
print(f"Hi {user}, age {age}")          # f-string (preferred)
print("Hi {} age {}".format(user, age)) # format method

```

- f-strings are powerful and easy for inserting variables.
- `.format()` is older but still used.

**Java**

```java
String user = "Ivy";
int age = 20;
System.out.printf("Hi %s, age %d%n", user, age);
String s = String.format("Hi %s age %d", user, age);

```

- `printf` works like C-style formatting with `%` specifiers.
- `String.format` creates formatted strings without printing them.

**Key idea**: Python’s f-strings are concise. Java uses format specifiers with `%` symbols.

---

## 5) Operators and math

**Python**

```python
3 / 2    # 1.5 (true division)
3 // 2   # 1 (floor division)
3 ** 2   # 9 (power)
3 % 2    # 1 (modulo)

```

- `/` always gives a float.
- `//` gives integer floor division.
- `*` is the power operator.

**Java**

```java
3 / 2;         // 1 (integer division since both are int)
3 / 2.0;       // 1.5 (double division)
Math.pow(3,2); // 9.0 (power)
3 % 2;         // 1 (modulo)

```

- Division result depends on operand type.
- Java has no `*`, instead uses `Math.pow`.
- Java has `++` and `-` for increment/decrement (not in Python).

**Key idea**: Python separates float division and floor division. Java uses operator overloading depending on type.

---

## 6) Conditional statements

**Python**

```python
x = 5
if x < 0:
    print("negative")
elif x == 0:
    print("zero")
else:
    print("positive")

```

- Python uses `elif` instead of `else if`.
- Indentation matters — no braces required.

**Java**

```java
int x = 5;
if (x < 0) {
    System.out.println("negative");
} else if (x == 0) {
    System.out.println("zero");
} else {
    System.out.println("positive");
}

```

- Java uses braces `{}` to define blocks.
- `else if` is two words.

**Key idea**: Python uses indentation. Java uses braces.

---

## 7) Switch / Match statements

**Python (3.10+)**

```python
status = 404
match status:
    case 200:
        print("ok")
    case 400 | 404:
        print("client error")
    case _:
        print("other")

```

- Python’s `match` is like switch but supports *pattern matching*.
- `case _` is the default case.

**Java (14+)**

```java
int status = 404;
String msg = switch (status) {
    case 200 -> "ok";
    case 400, 404 -> "client error";
    default -> "other";
};
System.out.println(msg);

```

- Modern Java `switch` can return values (called *switch expressions*).
- Multiple values can be combined in a case.

**Key idea**: Python `match` is more powerful (pattern matching). Java’s modern `switch` simplifies old-style `case`.

---

## 8) Loops (for and while)

**Python**

```python
for i in range(3):
    print(i)

for i, val in enumerate([10, 20, 30]):
    print(i, val)

n = 3
while n > 0:
    n -= 1

# special: loop else
for x in [1, 2, 3]:
    if x == 2:
        break
else:
    print("no break happened")

```

- `for` loops iterate directly over sequences.
- `enumerate` gives index + value.
- `while` is similar to Java.
- `for ... else` runs the else block only if loop ends normally (not broken).

**Java**

```java
for (int i = 0; i < 3; i++) {
    System.out.println(i);
}

for (int val : new int[]{10, 20, 30}) {
    System.out.println(val);
}

int n = 3;
while (n > 0) {
    n--;
}

```

- Classic `for (init; condition; update)` loop.
- Enhanced `for-each` loop for arrays and collections.
- No direct equivalent of Python’s `for else`.

**Key idea**: Python `for` is sequence-based. Java `for` can be C-style or enhanced for collections.

---

## 9) Functions and parameters

**Python**

```python
def greet(name="world") -> str:
    return f"Hello {name}"

# multiple return values
def stats(a: int, b: int):
    return a + b, a * b
s, p = stats(2, 3)

# variable arguments
def add(*nums):
    return sum(nums)

# keyword arguments
def power(base, *, exp=2):
    return base ** exp

```

- Functions are defined with `def`.
- Can have default parameters.
- Can return multiple values as a tuple.
- `args` = variable arguments. `*kwargs` = variable keyword arguments.
- Return type hints are optional.

**Java**

```java
class Utils {
    static String greet(String name) {
        return "Hello " + name;
    }
    static String greet() { // overload method
        return greet("world");
    }
    static int[] stats(int a, int b) {
        return new int[]{a + b, a * b};
    }
    static int add(int... nums) { // varargs
        int s = 0;
        for (int n : nums) s += n;
        return s;
    }
}

```

- Functions (methods) must be inside a class.
- Java uses **method overloading** to simulate default parameters.
- Multiple return values usually handled with arrays, custom objects, or `Pair`/`Record`.
- `int... nums` is varargs.

**Key idea**: Python functions are flexible with default, keyword, and variable arguments. Java requires method overloading and varargs.

Perfect 👍 I’ll continue from **Topic 10** and keep the same structure you used (Python code, Java code, explanation, and “Key idea”) — but with **much more detailed explanations** like you asked.

Here’s the continuation:

---

## 10) Classes and Objects

**Python**

```python
class Person:
    def __init__(self, name, age):   # constructor
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I am {self.name}, age {self.age}"

p = Person("Ivy", 20)
print(p.greet())

```

- `class` defines a class.
- `__init__` is the constructor (called automatically when object created).
- `self` must be explicitly written as the first parameter of methods (it represents the object instance).
- Attributes can be added dynamically even outside the constructor.

**Java**

```java
class Person {
    String name;
    int age;

    // constructor
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    String greet() {
        return "Hi, I am " + name + ", age " + age;
    }
}

public class Main {
    public static void main(String[] args) {
        Person p = new Person("Ivy", 20);
        System.out.println(p.greet());
    }
}

```

- Java classes define fields and methods.
- Constructors have the same name as the class (no `__init__`).
- `this` refers to the current object.
- Attributes must be declared before use.

**Key idea**: Python classes are lightweight and flexible (dynamic attributes, no explicit type requirements). Java classes are stricter with types and structure.

---

## 11) Encapsulation and Access Modifiers

**Python**

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance   # private (name-mangled)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

```

- Prefix `__` makes variables *name-mangled* (harder to access directly, but not truly private).
- No true enforcement of private/protected, it’s by convention.

**Java**

```java
class Account {
    private double balance;

    Account(double balance) {
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public double getBalance() {
        return balance;
    }
}

```

- Java enforces encapsulation with modifiers:
    - `public` = accessible everywhere
    - `private` = only inside class
    - `protected` = inside package + subclasses
    - *default* (no keyword) = package-private

**Key idea**: Python relies on naming conventions for encapsulation, while Java enforces strict access rules.

---

## 12) Inheritance

**Python**

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):   # inherits from Animal
    def speak(self):
        return "Woof"

d = Dog()
print(d.speak())

```

- Inheritance is declared by putting parent class in parentheses.
- Methods can be overridden easily.
- `super()` can call parent methods.

**Java**

```java
class Animal {
    String speak() {
        return "Some sound";
    }
}

class Dog extends Animal {
    @Override
    String speak() {
        return "Woof";
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        System.out.println(d.speak());
    }
}

```

- Java uses `extends` for single inheritance.
- `@Override` annotation makes overriding explicit.
- `super` keyword calls parent methods.

**Key idea**: Python and Java both support single inheritance. Python also supports multiple inheritance (not in Java).

---

## 13) Polymorphism

**Python**

```python
class Cat:
    def speak(self): return "Meow"

class Dog:
    def speak(self): return "Woof"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat())
animal_sound(Dog())

```

- Polymorphism in Python is **duck typing**: if an object has the right method, it works (no need for shared base class).

**Java**

```java
interface Animal {
    String speak();
}

class Cat implements Animal {
    public String speak() { return "Meow"; }
}

class Dog implements Animal {
    public String speak() { return "Woof"; }
}

public class Main {
    static void animalSound(Animal a) {
        System.out.println(a.speak());
    }
    public static void main(String[] args) {
        animalSound(new Cat());
        animalSound(new Dog());
    }
}

```

- Java uses **interfaces or inheritance** to enforce polymorphism.
- Types are checked at compile time.

**Key idea**: Python polymorphism is flexible (based on behavior). Java enforces strict type-based polymorphism.

---

## 14) Abstract Classes and Interfaces

**Python**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

```

- Use `ABC` module for abstract classes.
- `@abstractmethod` forces subclasses to implement the method.
- Python has no strict “interface” keyword — abstract classes act as interfaces.

**Java**

```java
abstract class Shape {
    abstract double area();
}

class Circle extends Shape {
    double r;
    Circle(double r) { this.r = r; }
    double area() { return 3.14 * r * r; }
}

interface Drawable {
    void draw();
}

class Square implements Drawable {
    public void draw() { System.out.println("Drawing square"); }
}

```

- Java separates `abstract class` (can have fields + methods) and `interface` (pure contracts).
- A class can implement multiple interfaces but extend only one class.

**Key idea**: Python merges abstract classes and interfaces. Java has distinct constructs for both.

---

👉 Do you want me to continue with **Topic 15: Constructors and Overloading** next, following the same detailed format?

Great 🙌 let’s continue from **Topic 15** in the same structured way with detailed code + explanations + key idea.

---

## 15) Constructors and Overloading

**Python**

```python
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

p1 = Person("Ivy", 20)   # custom values
p2 = Person()            # default constructor

```

- Python uses `__init__` as the constructor.
- Only **one constructor per class**, but you can simulate overloading by:
    - Using default parameters
    - Using variable arguments (`args`, `*kwargs`)

```python
class Student:
    def __init__(self, *args):
        if len(args) == 0:
            self.name, self.age = "Unknown", 0
        elif len(args) == 2:
            self.name, self.age = args

```

**Java**

```java
class Person {
    String name;
    int age;

    // constructor overloading
    Person() {
        this("Unknown", 0);
    }

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

public class Main {
    public static void main(String[] args) {
        Person p1 = new Person("Ivy", 20);
        Person p2 = new Person(); // default constructor
    }
}

```

- Constructors in Java must have the same name as the class.
- Java allows **constructor overloading**: multiple constructors with different parameter lists.
- `this(...)` calls another constructor from inside a constructor.

**Key idea**: Python handles flexibility with default/variable arguments. Java achieves it through explicit constructor overloading.

---

## 16) Static vs Instance Members

**Python**

```python
class Counter:
    count = 0   # class variable (shared by all objects)

    def __init__(self):
        Counter.count += 1   # modify class variable

    def show(self):
        print(f"Object count = {Counter.count}")

    @staticmethod
    def greet():
        print("Hello from static method")

```

- Class variables = shared by all objects.
- Instance variables = unique per object.
- `@staticmethod` defines a method that doesn’t need `self` or `cls`.
- `@classmethod` takes `cls` (the class itself) as parameter.

**Java**

```java
class Counter {
    static int count = 0;  // static variable shared by all objects

    Counter() {
        count++;
    }

    void show() {
        System.out.println("Object count = " + count);
    }

    static void greet() {
        System.out.println("Hello from static method");
    }
}

public class Main {
    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        c1.show();
        Counter.greet();
    }
}

```

- `static` = shared across all objects of the class.
- Non-static members belong to each instance separately.
- Static methods can be called without creating an object.

**Key idea**: Python uses decorators (`@staticmethod`, `@classmethod`). Java uses the `static` keyword.

---

## 17) Inner and Nested Classes

**Python**

```python
class Outer:
    def __init__(self, name):
        self.name = name

    class Inner:
        def display(self):
            print("This is an inner class")

```

- Inner classes exist but are not very common in Python.
- Typically used for logical grouping of classes.
- Access is through `Outer.Inner`.

```python
o = Outer("outer")
i = Outer.Inner()
i.display()

```

**Java**

```java
class Outer {
    String name;
    Outer(String name) { this.name = name; }

    class Inner {
        void display() {
            System.out.println("This is an inner class of " + name);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Outer outer = new Outer("outer");
        Outer.Inner inner = outer.new Inner();
        inner.display();
    }
}

```

- Java has:
    - **Inner classes** (non-static, tied to outer instance).
    - **Static nested classes** (can exist without outer instance).
    - **Anonymous inner classes** (used in event handling, implementing interfaces quickly).

**Key idea**: Inner classes are rare in Python but heavily used in Java for encapsulation and event-driven programming.

---

## 18) Method Overloading and Overriding

**Python**

```python
class MathOps:
    def add(self, a, b, c=0):
        return a + b + c   # default param = simulated overloading

class Parent:
    def show(self): print("Parent")

class Child(Parent):
    def show(self): print("Child")   # overrides

```

- **Overloading**: simulated using default parameters or variable arguments (`args`).
- **Overriding**: just redefine the method in the subclass.

**Java**

```java
class MathOps {
    int add(int a, int b) { return a + b; }
    int add(int a, int b, int c) { return a + b + c; }  // method overloading
}

class Parent {
    void show() { System.out.println("Parent"); }
}

class Child extends Parent {
    @Override
    void show() { System.out.println("Child"); }   // method overriding
}

```

- **Overloading**: multiple methods with same name but different parameters.
- **Overriding**: subclass redefines method from parent with same signature.

**Key idea**: Python has flexible arguments so no strict overloading, while Java supports true overloading + overriding.

---

👉 Should I continue with **Topic 19: Packages and Modules** next, or do you want me to cover **Exception Handling**first?

Perfect! Let’s continue with **Topic 19: Packages/Modules and Imports** and then cover **Exception Handling**. I’ll keep the same detailed style.

---

## 19) Packages, Modules, and Imports

**Python**

```python
# mymodule.py
def greet(name):
    return f"Hello {name}"

# main.py
import mymodule

print(mymodule.greet("Ivy"))

# or selective import
from mymodule import greet
print(greet("Ivy"))

```

- Python modules are `.py` files containing functions, classes, or variables.
- Packages are directories with `__init__.py` file (can be empty) to organize modules hierarchically.
- `import` loads the module, `from ... import` selectively imports members.
- Python supports aliases: `import mymodule as mm`.

**Java**

```java
// In file Utils.java
package mypackage;

public class Utils {
    public static String greet(String name) {
        return "Hello " + name;
    }
}

// In Main.java
import mypackage.Utils;

public class Main {
    public static void main(String[] args) {
        System.out.println(Utils.greet("Ivy"));
    }
}

```

- Java packages group related classes.
- File path must match the package structure (`mypackage/Utils.java`).
- `import` statement allows using classes from packages.
- Classes without `public` are package-private by default.

**Key idea**: Python modules are lightweight and flexible. Java packages are strict, require folder structure, and are used to enforce namespace control.

---

## 20) Exception Handling

**Python**

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Other error: {e}")
else:
    print("No exception occurred")
finally:
    print("Always executed")

```

- `try` block contains risky code.
- `except` handles specific or generic exceptions.
- `else` runs if no exception occurred.
- `finally` always executes (cleanup code).
- Python exceptions are objects and can be raised manually with `raise`.

**Java**

```java
try {
    int x = 1 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero");
} catch (Exception e) {
    System.out.println("Other error: " + e);
} finally {
    System.out.println("Always executed");
}

```

- `try` block contains risky code.
- `catch` handles exceptions.
- `finally` always executes.
- Java has **checked exceptions** (must be declared with `throws`) and **unchecked exceptions** (RuntimeException).

**Key idea**: Python’s exception system is dynamic and flexible. Java enforces strict compile-time checks for certain exceptions, improving reliability in large applications.

---

If you want, I can **continue with Topic 21: File Handling and I/O, and then Multithreading**, keeping this **deep explanation style**.

Do you want me to continue with that next?

Great! Let’s continue with **Topic 21: File Handling and I/O**, then **Topic 22: Multithreading**, keeping the detailed Python vs Java comparison.

---

## 21) File Handling and I/O

**Python**

```python
# Writing to a file
with open("data.txt", "w") as f:
    f.write("Hello, Ivy\n")
    f.write("Python is fun!\n")

# Reading from a file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line
with open("data.txt") as f:
    for line in f:
        print(line.strip())

```

- `open(filename, mode)` opens files in different modes: `"r"`=read, `"w"`=write, `"a"`=append, `"rb"`/`"wb"`=binary.
- `with` statement ensures automatic file closure.
- `.read()`, `.readline()`, `.readlines()` are used to read file contents.
- `.write()` writes to the file.

**Java**

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {
        // Writing to a file
        try (FileWriter fw = new FileWriter("data.txt")) {
            fw.write("Hello, Ivy\n");
            fw.write("Java is fun!\n");
        } catch (IOException e) {
            System.out.println("File error: " + e);
        }

        // Reading from a file
        try (BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("File error: " + e);
        }
    }
}

```

- Java uses classes like `FileReader`, `FileWriter`, `BufferedReader`, `BufferedWriter`.
- `try-with-resources` ensures automatic closure of streams.
- Java separates byte streams (`InputStream/OutputStream`) and character streams (`Reader/Writer`).

**Key idea**: Python file handling is concise and high-level. Java requires explicit streams and exception handling, which is more verbose but very precise.

---

## 22) Multithreading

**Python**

```python
import threading
import time

def task(name):
    for i in range(3):
        print(f"Task {name} running {i}")
        time.sleep(0.5)

# Create threads
t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()
print("All tasks completed")

```

- `threading.Thread(target=..., args=...)` creates a new thread.
- `start()` begins execution.
- `join()` waits for thread to finish.
- Python has **GIL (Global Interpreter Lock)**, so CPU-bound threads are limited; best for I/O-bound tasks.

**Java**

```java
class Task extends Thread {
    private String name;
    Task(String name) { this.name = name; }
    public void run() {
        for (int i = 0; i < 3; i++) {
            System.out.println("Task " + name + " running " + i);
            try { Thread.sleep(500); } catch (InterruptedException e) {}
        }
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Task t1 = new Task("A");
        Task t2 = new Task("B");
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println("All tasks completed");
    }
}

```

- Java threads are created by extending `Thread` or implementing `Runnable`.
- `start()` calls the `run()` method on a new thread.
- `sleep()` pauses thread; `join()` waits for completion.
- Java threads can run truly in parallel on multiple CPU cores.

**Key idea**: Python threading is easier to write but limited by GIL. Java threading is more verbose but allows true parallelism.

---

If you want, I can **finish the last few topics**:

- **Topic 23: Lambda Expressions and Functional Programming**
- **Topic 24: Collections / Data Structures (List, Map, Set, etc.)**
- **Topic 25: Final Notes / Summary of Python vs Java differences**

Do you want me to continue with those next?

Perfect! Let’s finish the final topics with **detailed Python vs Java comparisons**, explanations, and key ideas.

---

## 23) Lambda Expressions and Functional Programming

**Python**

```python
# Lambda function (anonymous)
square = lambda x: x ** 2
print(square(5))  # 25

# Using map, filter, reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x%2==0, numbers))

from functools import reduce
sum_all = reduce(lambda a, b: a + b, numbers)

```

- Lambda functions are **anonymous, single-expression functions**.
- `map` applies a function to every item.
- `filter` selects items based on a condition.
- `reduce` accumulates values.
- Python supports functional programming, including higher-order functions.

**Java**

```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1,2,3,4,5);

        // Lambda function with streams
        List<Integer> squared = numbers.stream()
                                       .map(x -> x*x)
                                       .collect(Collectors.toList());

        List<Integer> evens = numbers.stream()
                                     .filter(x -> x % 2 == 0)
                                     .collect(Collectors.toList());

        int sumAll = numbers.stream().reduce(0, (a, b) -> a + b);
    }
}

```

- Java 8+ supports **lambda expressions** and the **Streams API**.
- Streams allow map/filter/reduce operations on collections.
- Functional programming is supported but more verbose than Python.

**Key idea**: Python’s lambda and functional features are concise and built-in. Java requires Streams or functional interfaces but is type-safe.

---

## 24) Collections / Data Structures

**Python**

```python
# List
nums = [1, 2, 3, 4]
nums.append(5)
nums.remove(2)

# Set
s = {1, 2, 3}
s.add(4)
s.discard(2)

# Dictionary (Map)
d = {"name": "Ivy", "age": 20}
d["city"] = "Dhaka"
print(d.get("name"))

# Tuples (immutable)
t = (1, 2, 3)

```

- Python collections are **dynamic, flexible, and heterogeneous**.
- List = ordered, mutable; Tuple = ordered, immutable; Set = unordered, unique elements; Dict = key-value mapping.

**Java**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // List
        List<Integer> nums = new ArrayList<>(Arrays.asList(1,2,3,4));
        nums.add(5);
        nums.remove(Integer.valueOf(2));

        // Set
        Set<Integer> s = new HashSet<>(Arrays.asList(1,2,3));
        s.add(4);
        s.remove(2);

        // Map
        Map<String, Object> d = new HashMap<>();
        d.put("name", "Ivy");
        d.put("age", 20);
        System.out.println(d.get("name"));

        // Array (fixed size)
        int[] arr = {1,2,3};
    }
}

```

- Java collections are **strictly typed**. Generics enforce type safety: `List<Integer>`.
- `ArrayList` = dynamic array, `HashSet` = unordered unique elements, `HashMap` = key-value mapping.
- Arrays are fixed size.

**Key idea**: Python collections are flexible and easy to use. Java collections are more structured, typed, and verbose.

---

## 25) Final Notes / Summary of Python vs Java

| Feature | Python | Java |
| --- | --- | --- |
| Typing | Dynamic | Static |
| Syntax | Concise, readable | Verbose, structured |
| Entry point | Starts from first line | `main()` inside class |
| Functions | Flexible: default, keyword, varargs | Methods inside class; overloading used for defaults |
| OOP | Classes, single/multiple inheritance, duck typing | Classes, single inheritance, interfaces for polymorphism |
| Exception | Flexible, runtime-checked | Checked and unchecked, compile-time checks for some |
| File I/O | `open()` with `with` | Streams with `try-with-resources` |
| Threading | Easy, GIL limits CPU threads | Powerful, true parallelism |
| Functional | `lambda`, map/filter/reduce | Lambda + Streams API |
| Collections | Dynamic and heterogeneous | Strictly typed, structured via generics |
| Compilation | Interpreted | Compiled to bytecode, runs on JVM |

**Overall key idea**:

- **Python**: Quick to write, highly readable, very flexible — great for prototyping, scripting, and data-centric applications.
- **Java**: Strict, structured, and type-safe — preferred for large-scale, enterprise, and multi-threaded applications.

---

✅ This completes a **full Python vs Java note sheet**, covering:

1. Basics (hello world, comments, variables, operators)
2. Control structures (conditionals, loops, switch/match)
3. Functions
4. OOP (classes, inheritance, polymorphism, abstraction, encapsulation, static, inner classes, overloading)
5. Exception handling
6. File I/O
7. Multithreading
8. Lambda & functional programming
9. Collections
10. Summary of major differences

---

If you want, I can **also make a single, fully copy-paste ready PDF-style note** with **all 25 topics combined** for easy offline study.

Do you want me to do that?

Perfect! Let’s continue numbering from where we left off (**Topic 26 was Multithreading**), so the next topic will be **27) Properties and Getters**, and I’ll continue in the **same detailed, copy-paste friendly Python vs Java style**.

---

## 27) Properties and Getters

**Python**

```python
class Person:
    def __init__(self, name):
        self._name = name  # convention: single underscore for "protected"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

p = Person("Ivy")
print(p.name)  # uses getter
p.name = "Alice"  # uses setter

```

- `@property` converts a method into a getter.
- `@<property>.setter` defines the setter method.
- Helps **encapsulate attributes** without changing syntax when accessing them.

**Java**

```java
class Person {
    private String name;

    Person(String name) {
        this.name = name;
    }

    public String getName() { return name; }
    public void setName(String name) {
        if(name == null || name.isEmpty()) throw new IllegalArgumentException("Name cannot be empty");
        this.name = name;
    }
}

Person p = new Person("Ivy");
System.out.println(p.getName());
p.setName("Alice");

```

- Java uses explicit getter/setter methods.
- Encapsulation is enforced via `private` fields.

**Key idea**: Python’s property decorator makes attribute access cleaner. Java requires explicit methods but is very clear and strict.

---

## 28) Modules and Packages

**Python**

```python
# mypackage/mymodule.py
def greet(name):
    return f"Hello {name}"

# main.py
from mypackage.mymodule import greet
print(greet("Ivy"))

```

- Python uses **modules** (`.py` files) and **packages** (folders with `__init__.py`).
- Import system is flexible; can use aliases and selective imports.

**Java**

```java
package mypackage;

public class Utils {
    public static String greet(String name) { return "Hello " + name; }
}

// Main.java
import mypackage.Utils;
System.out.println(Utils.greet("Ivy"));

```

- Java packages are **directory-based**, must match package declarations.
- Classes are imported via `import` statements.

**Key idea**: Python is more flexible and dynamic; Java packages are structured and static.

---

## 29) Build and Run Toolchain

**Python**

```bash
# Run directly using interpreter
python main.py

# For larger projects, use
python -m module_name  # run module as script

```

- No compilation required, interpreted.
- Tools like `pip`, `venv`, `pyinstaller` manage dependencies and build executables.

**Java**

```bash
# Compile
javac Main.java
# Run
java Main

# For projects
javac -d bin src/*.java
java -cp bin Main

```

- Java requires compilation to bytecode (`.class`) which runs on JVM.
- Build tools like Maven or Gradle manage dependencies, compilation, and packaging (`jar`).

**Key idea**: Python is interpreted and simple to run. Java has a formal compile/run workflow and strong build tool support.

---

## 30) Concurrency and Async

**Python**

```python
import threading, asyncio

# Threading
def task(name):
    print(f"{name} running")
thread = threading.Thread(target=task, args=("T1",))
thread.start()
thread.join()

# Asyncio
import asyncio
async def async_task():
    print("Async task start")
    await asyncio.sleep(1)
    print("Async task end")
asyncio.run(async_task())

```

- Threads run in parallel but limited by GIL.
- `asyncio` provides **cooperative multitasking** without real threads.

**Java**

```java
class Task extends Thread {
    public void run() { System.out.println("Thread running"); }
}
Task t = new Task();
t.start();
t.join();

// Async with CompletableFuture
import java.util.concurrent.*;
CompletableFuture.runAsync(() -> System.out.println("Async task"));

```

- Java threads can run on multiple cores.
- `CompletableFuture` and `ExecutorService` provide async programming and parallelism.

**Key idea**: Python async is lightweight and I/O-focused; Java concurrency is robust, CPU-optimized, and type-safe.

---

## 31) Memory Model and Argument Passing

**Python**

```python
def modify(lst):
    lst.append(4)

nums = [1,2,3]
modify(nums)
print(nums)  # [1,2,3,4]

```

- Python passes **references by value**. Mutable objects (like lists) can be changed.
- Immutable objects (like ints, strings) cannot be changed in-place.

**Java**

```java
void modify(List<Integer> lst) {
    lst.add(4);
}

List<Integer> nums = new ArrayList<>(Arrays.asList(1,2,3));
modify(nums);
System.out.println(nums);  // [1,2,3,4]

```

- Java also passes **references by value** for objects.
- Primitive types are passed by value, objects by reference (copy of reference).

**Key idea**: Both languages pass references similarly, but Python is fully dynamic; Java separates primitives vs objects.

---

## 32) Type Hints vs Generics

**Python**

```python
from typing import List

def sum_list(nums: List[int]) -> int:
    return sum(nums)

nums: List[int] = [1,2,3]

```

- Type hints are **optional**; used for readability and static analysis.
- Python remains dynamically typed at runtime.

**Java**

```java
import java.util.List;
import java.util.ArrayList;

List<Integer> nums = new ArrayList<>();
nums.add(1);
nums.add(2);

```

- Java **Generics** are enforced at compile-time.
- Prevents adding incompatible types.

**Key idea**: Python hints improve clarity; Java generics enforce type safety.

---

## 33) Decorators vs Annotations

**Python**

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()

```

- Decorators wrap functions or methods to add behavior dynamically.

**Java**

```java
@interface Info {
    String author();
}

@Info(author="Ivy")
class MyClass { }

```

- Annotations provide **metadata** for classes, methods, or fields.
- Can be processed at compile-time or runtime via reflection.

**Key idea**: Python decorators modify behavior. Java annotations provide metadata without changing behavior.

---

## 34) Dates and Times

**Python**

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)

tomorrow = now + timedelta(days=1)
print(tomorrow)

```

- `datetime` module handles date/time arithmetic.
- Supports formatting and parsing easily.

**Java**

```java
import java.time.*;

LocalDateTime now = LocalDateTime.now();
LocalDateTime tomorrow = now.plusDays(1);
System.out.println(now);
System.out.println(tomorrow);

```

- Java 8+ `java.time` API is modern, immutable, and type-safe.

**Key idea**: Both have strong date/time support; Java API is more verbose but safer.

---

## 35) Regular Expressions

**Python**

```python
import re

pattern = r"\d+"
text = "I have 12 apples"
matches = re.findall(pattern, text)
print(matches)  # ['12']

```

- `re` module provides `match`, `search`, `findall`, `sub`.

**Java**

```java
import java.util.regex.*;

Pattern pattern = Pattern.compile("\\d+");
Matcher matcher = pattern.matcher("I have 12 apples");
while(matcher.find()) {
    System.out.println(matcher.group());
}

```

- Java uses `Pattern` and `Matcher` classes.

**Key idea**: Python regex is concise; Java regex requires objects but is powerful and flexible.

---

## 36) Testing

**Python**

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

if __name__ == "__main__":
    unittest.main()

```

- Python `unittest` module supports automated testing.
- Can also use `pytest` for simpler syntax.

**Java**

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MathTest {
    @Test
    void testAdd() {
        assertEquals(5, 2 + 3);
    }
}

```

- Java uses **JUnit** for unit testing.
- Strongly integrated with IDEs and build tools.

**Key idea**: Testing frameworks exist in both; Python is simpler, Java more structured.

---

## 37) Entry Point Patterns

**Python**

```python
def main():
    print("Program started")

if __name__ == "__main__":
    main()

```

- Ensures the code runs only when script executed directly, not imported.

**Java**

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Program started");
    }
}

```

- `main` method is always the entry point.

**Key idea**: Python uses `if __name__ == "__main__"`; Java requires `main` method inside class.

---

## 38) Small End-to-End Example (Python vs Java)

**Python: Simple Student Management**

```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    @property
    def average(self):
        return sum(self.grades)/len(self.grades)

s1 = Student("Ivy", [80,90,85])
print(f"{s1.name} average: {s1.average}")

```

**Java: Simple Student Management**

```java
import java.util.*;

class Student {

```

private String name;

private List grades;

```
Student(String name, List<Integer> grades) {
    this.name = name;
    this.grades = grades;
}

public double getAverage() {
    return grades.stream().mapToInt(Integer::intValue).average().orElse(0);
}

public String getName() { return name; }

```

}

public class Main {

public static void main(String[] args) {

Student s1 = new Student("Ivy", Arrays.asList(80,90,85));

System.out.println(s1.getName() + " average: " + s1.getAverage());

}

}

```

* Small real-world example covering **class, constructor, method, property/getter, collection, and calculation**.

---

✅ Now you have a **complete Python vs Java note sheet** with **all 38 topics**, detailed explanations, example code, and key ideas for each.

-

```

- I can also **merge all 38 topics into a single fully formatted document** for easy copy-paste and offline study if you want.
    
    # Python vs Java: Complete Detailed Syntax and OOP Notes
    
    This is a **full Python vs Java note sheet** covering all major topics including syntax, OOP, advanced features, and examples. You can copy directly.
    
    ---
    
    ## 1) Hello world and program entry
    
    **Python**
    
    ```python
    print("Hello, world")
    
    ```
    
    - Interpreter executes line by line.
    - `print()` outputs text.
    
    **Java**
    
    ```java
    public class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello, world");
        }
    }
    
    ```
    
    - Java requires all code inside a class.
    - `main` is the entry point.
    
    **Key idea**: Python is minimal and interpreted. Java is compiled and structured.
    
    ---
    
    ## 2) Comments and documentation
    
    **Python**
    
    ```python
    # single line
    """docstring for modules/classes/functions"""
    
    ```
    
    - `#` for single line, triple quotes for multi-line.
    
    **Java**
    
    ```java
    // single line
    /* multi line */
    /** Javadoc comment */
    
    ```
    
    - Javadoc can generate external documentation.
    
    ---
    
    ## 3) Variables and data types
    
    **Python**
    
    ```python
    x = 42
    y = 3.14
    name = "Ivy"
    x = "string now"
    
    ```
    
    - Dynamic typing; type can change.
    
    **Java**
    
    ```java
    int x = 42;
    double y = 3.14;
    String name = "Ivy";
    
    ```
    
    - Static typing; type fixed.
    
    ---
    
    ## 4) Printing and string formatting
    
    **Python**
    
    ```python
    name = "Ivy"
    age = 20
    print(f"Hi {name}, age {age}")
    
    ```
    
    - f-strings concise.
    
    **Java**
    
    ```java
    String name = "Ivy";
    int age = 20;
    System.out.printf("Hi %s, age %d", name, age);
    
    ```
    
    - Java uses format specifiers.
    
    ---
    
    ## 5) Operators and math
    
    **Python**
    
    ```python
    3 / 2  # 1.5
    3 // 2 # 1
    3 ** 2 # 9
    
    ```
    
    **Java**
    
    ```java
    3 / 2;        // 1
    3 / 2.0;      // 1.5
    Math.pow(3,2); // 9.0
    
    ```
    
    ---
    
    ## 6) Conditional statements
    
    **Python**
    
    ```python
    if x>0:
        print("positive")
    elif x==0:
        print("zero")
    else:
        print("negative")
    
    ```
    
    **Java**
    
    ```java
    if(x>0){System.out.println("positive");}
    else if(x==0){System.out.println("zero");}
    else{System.out.println("negative");}
    
    ```
    
    ---
    
    ## 7) Switch / Match
    
    **Python 3.10+**
    
    ```python
    match code:
        case 200: print("OK")
        case 404: print("Not found")
        case _: print("Default")
    
    ```
    
    **Java 14+**
    
    ```java
    String msg = switch(code){
        case 200 -> "OK";
        case 404 -> "Not found";
        default -> "Default";
    };
    
    ```
    
    ---
    
    ## 8) Loops
    
    **Python**
    
    ```python
    for i in range(3): print(i)
    while x>0: x-=1
    
    ```
    
    **Java**
    
    ```java
    for(int i=0;i<3;i++){System.out.println(i);}
    while(x>0){x--;}
    
    ```
    
    ---
    
    ## 9) Functions
    
    **Python**
    
    ```python
    def greet(name="world"): return f"Hello {name}"
    def add(*nums): return sum(nums)
    
    ```
    
    **Java**
    
    ```java
    static String greet(String name){return "Hello "+name;}
    static int add(int... nums){int s=0; for(int n:nums)s+=n; return s;}
    
    ```
    
    ---
    
    ## 10) Classes and Objects
    
    **Python**
    
    ```python
    class Person:
        def __init__(self, name): self.name=name
        def greet(self): print(f"Hi {self.name}")
    p = Person("Ivy")
    p.greet()
    
    ```
    
    **Java**
    
    ```java
    class Person{
     String name;
     Person(String name){this.name=name;}
     void greet(){System.out.println("Hi "+name);}
    }
    Person p=new Person("Ivy"); p.greet();
    
    ```
    
    ---
    
    ## 11) Inheritance
    
    **Python**
    
    ```python
    class Animal: pass
    class Dog(Animal): pass
    
    ```
    
    **Java**
    
    ```java
    class Animal{} class Dog extends Animal{}
    
    ```
    
    ---
    
    ## 12) Polymorphism
    
    **Python**
    
    ```python
    for obj in [Bird(), Plane()]: obj.fly()
    
    ```
    
    **Java**
    
    ```java
    Flyable[] arr={new Bird(),new Plane()}; for(Flyable f:arr) f.fly();
    
    ```
    
    ---
    
    ## 13) Encapsulation
    
    **Python**
    
    ```python
    self.__balance = 0
    
    ```
    
    **Java**
    
    ```java
    private int balance;
    
    ```
    
    ---
    
    ## 14) Abstraction
    
    **Python**
    
    ```python
    from abc import ABC,abstractmethod
    class Shape(ABC): @abstractmethod
    def area(self): pass
    
    ```
    
    **Java**
    
    ```java
    abstract class Shape{abstract double area();}
    
    ```
    
    ---
    
    ## 15) Interfaces
    
    **Python**
    
    ```python
    class Flyable: def fly(self): raise NotImplementedError
    
    ```
    
    **Java**
    
    ```java
    interface Flyable{void fly();}
    
    ```
    
    ---
    
    ## 16) Static members
    
    **Python**
    
    ```python
    class Counter:
        count=0
        def __init__(self): Counter.count+=1
    
    ```
    
    **Java**
    
    ```java
    static int count=0;
    Counter(){count++;}
    
    ```
    
    ---
    
    ## 17) Packages and imports
    
    **Python**
    
    ```python
    import math
    print(math.sqrt(16))
    
    ```
    
    **Java**
    
    ```java
    import java.util.*;
    System.out.println(Math.sqrt(16));
    
    ```
    
    ---
    
    ## 18) Exception handling
    
    **Python**
    
    ```python
    try:1/0
    except ZeroDivisionError: print("error")
    finally: print("done")
    
    ```
    
    **Java**
    
    ```java
    try{int x=1/0;} catch(ArithmeticException e){System.out.println("error");} finally{System.out.println("done");}
    
    ```
    
    ---
    
    ## 19) File handling
    
    **Python**
    
    ```python
    with open("f.txt","w") as f: f.write("hello")
    
    ```
    
    **Java**
    
    ```java
    try(FileWriter fw=new FileWriter("f.txt")){fw.write("hello");}
    
    ```
    
    ---
    
    ## 20) Multithreading
    
    **Python**
    
    ```python
    import threading
    thread = threading.Thread(target=lambda: print("running"))
    thread.start()
    
    ```
    
    **Java**
    
    ```java
    class Task extends Thread{public void run(){System.out.println("running");}}
    new Task().start();
    
    ```
    
    ---
    
    ## 21) Properties and Getters
    
    **Python**
    
    ```python
    @property
    def name(self): return self._name
    @name.setter
    def name(self,value): self._name=value
    
    ```
    
    **Java**
    
    ```java
    public String getName(){return name;}
    public void setName(String name){this.name=name;}
    
    ```
    
    ---
    
    ## 22) Modules and Packages
    
    **Python**
    
    ```python
    from mypackage.mymodule import greet
    print(greet("Ivy"))
    
    ```
    
    **Java**
    
    ```java
    import mypackage.Utils;
    System.out.println(Utils.greet("Ivy"));
    
    ```
    
    ---
    
    ## 23) Build and Run Toolchain
    
    **Python**: `python main.py`
    
    **Java**: `javac Main.java` then `java Main`
    
    ---
    
    ## 24) Concurrency and Async
    
    **Python**: `threading` and `asyncio` examples
    
    **Java**: `Thread`, `Runnable`, `CompletableFuture`
    
    ---
    
    ## 25) Memory Model and Argument Passing
    
    **Python**: mutable objects can be changed in functions, immutable cannot
    
    **Java**: objects references by value, primitives by value
    
    ---
    
    ## 26) Type Hints vs Generics
    
    **Python**: optional type hints
    
    **Java**: generics enforce type safety
    
    ---
    
    ## 27) Decorators vs Annotations
    
    **Python**: `@decorator` wraps functions
    
    **Java**: `@Annotation` provides metadata
    
    ---
    
    ## 28) Dates and Times
    
    **Python**: `datetime` module
    
    **Java**: `java.time` API
    
    ---
    
    ## 29) Regular Expressions
    
    **Python**: `re` module
    
    **Java**: `Pattern` and `Matcher`
    
    ---
    
    ## 30) Testing
    
    **Python**: `unittest`
    
    **Java**: `JUnit`
    
    ---
    
    ## 31) Entry Point Patterns
    
    **Python**: `if __name__ == "__main__"`
    
    **Java**: `public static void main`
    
    ---
    
    ## 32) Small End-to-End Example
    
    **Python**
    
    ```python
    class Student:
        def __init__(self,name,grades): self.name=name; self.grades=grades
        @property
        def average(self): return sum(self.grades)/len(self.grades)
    
    s1=Student("Ivy",[80,90,85])
    print(s1.name,s1.average)
    
    ```
    
    **Java**
    
    ```java
    class Student{
     private String name;
     private List<Integer> grades;
     Student(String name,List<Integer> grades){this.name=name;this.grades=grades;}
     public double getAverage(){return grades.stream().mapToInt(Integer::intValue).average().orElse(0);}
     public String getName(){return name;}
    }
    public class Main{
     public static void main(String[] args){
      Student s1=new Student("Ivy",Arrays.asList(80,90,85));
      System.out.println(s1.getName()+" average: "+s1.getAverage());
     }
    }
    
    ```
    

---

# Python vs. Java Syntax Comparison

# Python vs Java: a complete syntax note sheet

Use this as a quick study sheet. Each topic shows Python, Java, and the key idea.

---

## 1) Hello world and program entry

**Python**

```python
print("Hello, world")

```

Run: `python app.py`

**Java**

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world");
    }
}

```

Compile then run: `javac HelloWorld.java` then `java HelloWorld`

**Key idea**: Python runs top to bottom. Java needs a class with `main`.

---

## 2) Comments and doc strings

**Python**

```python
# single line
"""Module or function doc string
Explains purpose.
"""

```

**Java**

```java
// single line
/* block comment */
/** Javadoc comment for API docs */

```

**Key idea**: Python uses `#` and triple quotes for docs. Java uses `//`, `/* */`, and `/** */`.

---

## 3) Variables and basic types

**Python**

```python
x = 42            # int
y = 3.14          # float
name = "Ivy"      # str
ok = True         # bool
x = "now a string"  # dynamic type

```

**Java**

```java
int x = 42;
double y = 3.14;
String name = "Ivy";
boolean ok = true;
var n = 10;       // local type inference since Java 10

```

**Key idea**: Python is dynamically typed. Java is statically typed.

---

## 4) Printing and string formatting

**Python**

```python
user = "Ivy"
age = 20
print(f"Hi {user}, age {age}")          # f string
print("Hi {} age {}".format(user, age)) # format method

```

**Java**

```java
String user = "Ivy";
int age = 20;
System.out.printf("Hi %s, age %d%n", user, age);
String s = String.format("Hi %s age %d", user, age);

```

**Key idea**: Python f strings are very direct. Java uses format specifiers.

---

## 5) Operators and math

**Python**

```python
3 / 2    # 1.5 true division
3 // 2   # 1 floor division
3 ** 2   # 9 power
3 % 2    # 1 modulo

```

**Java**

```java
3 / 2;        // 1 integer division since both operands are int
3 / 2.0;      // 1.5 double division
Math.pow(3,2);// 9.0 power
3 % 2;        // 1 modulo

```

**Key idea**: Python has `//` and `**`. Java does not have them. Java division depends on operand types. Java has `++` and `--`. Python does not.

---

## 6) Control flow: if, elif, else and switch or match

**Python**

```python
x = 5
if x < 0:
    print("neg")
elif x == 0:
    print("zero")
else:
    print("pos")

# structural pattern match since Python 3.10
status = 404
match status:
    case 200:
        print("ok")
    case 400 | 404:
        print("client error")
    case _:
        print("other")

```

**Java**

```java
int x = 5;
if (x < 0) {
    System.out.println("neg");
} else if (x == 0) {
    System.out.println("zero");
} else {
    System.out.println("pos");
}

// switch, with modern switch expressions (Java 14+)
int status = 404;
String msg = switch (status) {
    case 200 -> "ok";
    case 400, 404 -> "client error";
    default -> "other";
};
System.out.println(msg);

```

**Key idea**: Python uses `elif`. Java uses `else if`. Modern Java switch can return values. Python has `match` for patterns.

---

## 7) Loops: for and while

**Python**

```python
for i in range(3):
    print(i)

for i, val in enumerate([10, 20, 30]):
    print(i, val)

n = 3
while n > 0:
    n -= 1

# loop else runs only if loop did not break
for x in [1, 2, 3]:
    if x == 2:
        break
else:
    print("no break")

```

**Java**

```java
for (int i = 0; i < 3; i++) {
    System.out.println(i);
}

for (int val : new int[]{10, 20, 30}) {
    System.out.println(val);
}

int n = 3;
while (n > 0) {
    n--;
}

```

**Key idea**: Python loop is for each by default. Java has classic index loop and enhanced for each. Python has `for else`which Java does not.

---

## 8) Functions and parameters

**Python**

```python
def greet(name="world") -> str:
    return f"Hello {name}"

# many return values
def stats(a: int, b: int):
    return a + b, a * b
s, p = stats(2, 3)

# variable args
def add(*nums):
    return sum(nums)

# keyword args
def power(base, *, exp=2):
    return base ** exp

```

**Java**

```java
class Utils {
    static String greet(String name) {
        return "Hello " + name;
    }
    static String greet() { // overload
        return greet("world");
    }
    static int[] stats(int a, int b) {
        return new int[]{a + b, a * b};
    }
    static int add(int... nums) { // varargs
        int s = 0; for (int n : nums) s += n; return s;
    }
}

```

**Key idea**: Python has default and keyword args. Java uses overloading and varargs. Python returns tuples for many values. Java often returns arrays, records, or small classes.

---

## 9) Lambdas and functional style

**Python**

```python
nums = [1, 2, 3, 4]
squares = [x * x for x in nums]            # list comp
odds = list(filter(lambda x: x % 2 == 1, nums))

```

**Java**

```java
import java.util.*;
import java.util.stream.*;

List<Integer> nums = List.of(1, 2, 3, 4);
List<Integer> squares = nums.stream().map(x -> x * x).toList();
List<Integer> odds = nums.stream().filter(x -> x % 2 == 1).toList();

```

**Key idea**: Python uses comprehension for a clear style. Java uses streams and lambdas.

---

## 10) Core collections

**Python lists**

```python
nums = [1, 2, 3]
nums.append(4)
first = nums[0]

```

**Java lists**

```java
import java.util.*;
List<Integer> nums = new ArrayList<>(List.of(1, 2, 3));
nums.add(4);
int first = nums.get(0);

```

**Python tuples**

```python
pair = (1, "a")
a, b = pair

```

**Java records for a simple pair**

```java
record Pair<T, U>(T first, U second) {}
Pair<Integer,String> p = new Pair<>(1, "a");

```

**Sets**

```python
s = {1, 2, 3}
s.add(2)

```

```java
Set<Integer> s = new HashSet<>(List.of(1, 2, 3));
s.add(2);

```

**Dict or map**

```python
ages = {"Ivy": 20, "Mushfiq": 22}
ages["Ivy"]

```

```java
Map<String,Integer> ages = new HashMap<>();
ages.put("Ivy", 20);
ages.put("Mushfiq", 22);
ages.get("Ivy");

```

**Key idea**: Python has literal syntax for list, tuple, set, dict. Java uses classes in `java.util`.

---

## 11) Strings and slicing

**Python**

```python
s = "banana"
s[1:4]      # "ana"
s[::-1]     # reverse
multi = """
line one
line two
"""

```

**Java**

```java
String s = "banana";
s.substring(1, 4);      // "ana"
new StringBuilder(s).reverse().toString();
String multi = """
line one
line two
"""; // text block Java 15+

```

**Key idea**: Python supports slices. Java uses methods. Java has text blocks for multiline.

---

## 12) Classes and objects

**Python**

```python
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

p = Point(1, 2)
p.move(3, 4)

```

**Java**

```java
public class Point {
    private int x;
    private int y;
    public Point(int x, int y) { this.x = x; this.y = y; }
    public void move(int dx, int dy) { x += dx; y += dy; }
    public int getX() { return x; }
    public int getY() { return y; }
}
Point p = new Point(1, 2);
p.move(3, 4);

```

**Key idea**: Python uses `self`. Java uses `this`. Java often hides fields and exposes getters.

---

## 13) Data classes and compact carriers

**Python**

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str

```

**Java**

```java
public record User(int id, String name) {}

```

**Key idea**: Python `dataclass` auto generates methods. Java `record` auto generates constructor and accessors.

---

## 14) Inheritance and interfaces

**Python**

```python
class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "woof"

```

**Java**

```java
interface Speak {
    String speak();
}
class Animal implements Speak {
    public String speak() { return "..."; }
}
class Dog extends Animal {
    @Override public String speak() { return "woof"; }
}

```

**Key idea**: Java has classes, abstract classes, and interfaces. Python uses single or multiple inheritance and duck typing.

---

## 15) Properties and getters

**Python**

```python
class Person:
    def __init__(self, age: int):
        self._age = age
    @property
    def age(self) -> int:
        return self._age
    @age.setter
    def age(self, v: int):
        if v < 0:
            raise ValueError("age cannot be negative")
        self._age = v

```

**Java**

```java
class Person {
    private int age;
    public Person(int age) { this.age = age; }
    public int getAge() { return age; }
    public void setAge(int v) {
        if (v < 0) throw new IllegalArgumentException("age cannot be negative");
        age = v;
    }
}

```

**Key idea**: Python property decorator gives field like access. Java uses getters and setters.

---

## 16) Exceptions

**Python**

```python
try:
    1 / 0
except ZeroDivisionError as e:
    print("bad math")
else:
    print("ran with no error")
finally:
    print("always runs")

```

**Java**

```java
try {
    int x = 1 / 0;
} catch (ArithmeticException e) {
    System.out.println("bad math");
} finally {
    System.out.println("always runs");
}

```

**Checked vs unchecked**

In Java some exceptions must be declared or caught, for example `IOException`. Python has no checked exceptions.

**Try with resources vs with**

**Python**

```python
with open("data.txt") as f:
    text = f.read()

```

**Java**

```java
import java.nio.file.*;
try (var lines = Files.lines(Path.of("data.txt"))) {
    lines.forEach(System.out::println);
}

```

**Key idea**: Resource blocks close files for you.

---

## 17) File input and output

**Python**

```python
# read text
with open("a.txt", encoding="utf-8") as f:
    data = f.read()
# write text
with open("b.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")

```

**Java**

```java
import java.nio.file.*;
import java.io.IOException;

try {
    String data = Files.readString(Path.of("a.txt"));
    Files.writeString(Path.of("b.txt"), "hello\n");
} catch (IOException e) {
    // handle
}

```

**Key idea**: Java file methods throw checked exceptions.

---

## 18) Modules and packages

**Python**

```python
# file structure
mypkg/
    __init__.py
    util.py

# util.py
def add(a, b):
    return a + b

# use
from mypkg.util import add

```

**Java**

```java
// file: src/mypkg/Util.java
package mypkg;
public class Util { public static int add(int a, int b){ return a + b; } }

// use
import mypkg.Util;
int s = Util.add(2, 3);

```

**Key idea**: Python package folder needs `__init__.py`. Java uses `package` statement that matches folder path.

---

## 19) Build and run toolchain

**Python**: run scripts with `python`, manage libraries with `pip`, use virtual environment for project isolation.

**Java**: compile with `javac`, run with `java`. For projects use Maven or Gradle to manage builds and dependencies.

---

## 20) Concurrency and async

**Python**

```python
# threads
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as ex:
    results = list(ex.map(lambda x: x*x, [1,2,3]))

# async io
import asyncio

async def work(x):
    await asyncio.sleep(1)
    return x * x

async def main():
    vals = await asyncio.gather(*(work(i) for i in range(3)))

asyncio.run(main())

```

**Java**

```java
import java.util.concurrent.*;

ExecutorService pool = Executors.newFixedThreadPool(4);
Future<Integer> f = pool.submit(() -> 42);
int v = f.get();
pool.shutdown();

CompletableFuture<Integer> cf = CompletableFuture.supplyAsync(() -> 42)
    .thenApply(x -> x * 2);
int out = cf.join();

```

**Key idea**: Python has a global interpreter lock for CPU bound threads. Java threads run in parallel. Both have async tools for IO bound work.

---

## 21) Memory model and argument passing

Python passes references to objects by assignment. Java is pass by value, and the value of a variable for an object is a reference. So both can mutate objects inside a call. Rebinding a parameter in Python does not affect the caller.

---

## 22) Type hints vs generics

**Python**

```python
from typing import List, Dict, Optional, TypeVar, Generic

T = TypeVar('T')

def add(a: int, b: int) -> int:
    return a + b

def first(xs: List[T]) -> Optional[T]:
    return xs[0] if xs else None

```

**Java**

```java
import java.util.*;

class Box<T> {
    private T value;
    public Box(T value) { this.value = value; }
    public T get() { return value; }
}
Box<Integer> b = new Box<>(10);

```

**Key idea**: Python type hints are optional and checked by tools. Java generics are enforced by the compiler.

---

## 23) Decorators vs annotations

**Python**

```python
import time

def timed(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"took {time.time() - t0:.3f}s")
    return wrapper

@timed
def work():
    ...

```

**Java**

```java
import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface Timed {}

class Service {
    @Timed
    void work() { /* use an interceptor in a framework to time this */ }
}

```

**Key idea**: Python decorators wrap functions. Java annotations mark elements and frameworks act on them.

---

## 24) Dates and times

**Python**

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
now = datetime.now(ZoneInfo("Asia/Dhaka"))

```

**Java**

```java
import java.time.*;
ZonedDateTime now = ZonedDateTime.now(ZoneId.of("Asia/Dhaka"));

```

**Key idea**: Use `zoneinfo` in Python and `java.time` in Java for time zone safe work.

---

## 25) Regular expressions

**Python**

```python
import re
m = re.search(r"(\w+)@(\w+)", "hi a@b")
if m:
    user, host = m.groups()

```

**Java**

```java
import java.util.regex.*;
Matcher m = Pattern.compile("(\\w+)@(\\w+)").matcher("hi a@b");
if (m.find()) {
    String user = m.group(1);
    String host = m.group(2);
}

```

**Key idea**: Same regex flavor with small differences in escapes.

---

## 26) Testing

**Python**

```python
# test_sample.py
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()

```

**Java**

```java
// JUnit 5
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class MathTest {
    @Test void adds() { assertEquals(4, 2 + 2); }
}

```

**Key idea**: Python ships with `unittest`. Java often uses JUnit with a build tool.

---

## 27) Entry point patterns

**Python**

```python
def main():
    print("run")

if __name__ == "__main__":
    main()

```

**Java**

```java
public class App {
    public static void main(String[] args) {
        System.out.println("run");
    }
}

```

**Key idea**: Python uses `__name__` guard. Java uses the `main` method.

---

## 28) Small end to end example

**Python**

```python
from dataclasses import dataclass
from typing import Iterable

@dataclass
class Item:
    name: str
    price: float

def total(items: Iterable[Item]) -> float:
    return sum(it.price for it in items)

basket = [Item("apple", 1.2), Item("banana", 0.8)]
print(total(basket))

```

**Java**

```java
import java.util.*;

record Item(String name, double price) {}

class App {
    static double total(List<Item> items) {
        return items.stream().mapToDouble(Item::price).sum();
    }
    public static void main(String[] args) {
        List<Item> basket = List.of(new Item("apple", 1.2), new Item("banana", 0.8));
        System.out.println(total(basket));
    }
}

```

---

## 29) Quick cheat sheet

- Print: `print()` vs `System.out.println()`
- Input: `input()` vs `Scanner` or `Console`
- List vs ArrayList: `[1,2]` vs `new ArrayList<>(List.of(1,2))`
- Dict or Map: `{k: v}` vs `new HashMap<>()`
- Set: `{1,2}` vs `new HashSet<>()`
- Function: `def f(x):` vs `static T f(T x)` in a class
- Exception: `try/except/finally` vs `try/catch/finally`
- With resources: `with open(...)` vs `try (...) {}`
- Data class: `@dataclass` vs `record`
- Pattern matching: `match` vs `switch` expression
- Module import: `import pkg.mod` vs `import pkg.Class`

---

## 30) Running code and project tips

**Python**

- Use `python -m venv .venv` then `pip install ...` inside it.
- Format with `black` and lint with `ruff` or `flake8`.

**Java**

- Use Maven or Gradle for dependency and build.
- Use `mvn test` or `gradle test` for tests.

You now have a compact but complete map of Python and Java syntax side by side.

# Python vs. Java Syntax Comparison

## 1. Basic Structure

### Java

```java
// Filename: HelloWorld.java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

```

### Python

```python
# Filename: hello_world.py
print("Hello, World!")

```

**Key Differences:**

- Java requires class definition and `main` method
- Python executes code directly from top to bottom
- Java uses braces `{}` for code blocks
- Python uses indentation (typically 4 spaces) for code blocks

## 2. Variables and Data Types

### Java (Statically Typed)

```java
// Primitive types
int age = 25;
double price = 19.99;
char grade = 'A';
boolean isJavaFun = true;

// Reference types
String name = "John";
int[] numbers = {1, 2, 3};

```

### Python (Dynamically Typed)

```python
# Variables (no type declaration needed)
age = 25
price = 19.99
grade = 'A'
is_python_fun = True
name = "John"
numbers = [1, 2, 3]

```

**Key Differences:**

- Java requires explicit type declaration
- Python infers types automatically
- Java has primitive types and reference types
- Python treats everything as objects

## 3. Control Structures

### If-Else Statements

### Java

```java
int x = 10;
if (x > 5) {
    System.out.println("x is greater than 5");
} else if (x == 5) {
    System.out.println("x is equal to 5");
} else {
    System.out.println("x is less than 5");
}

```

### Python

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

```

### Loops

### Java

```java
// For loop
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// While loop
int i = 0;
while (i < 5) {
    System.out.println(i);
    i++;
}

// For-each loop
int[] numbers = {1, 2, 3, 4, 5};
for (int num : numbers) {
    System.out.println(num);
}

```

### Python

```python
# For loop
for i in range(5):
    print(i)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# For-each loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

```

**Key Differences:**

- Java uses parentheses `()` around conditions, Python doesn't
- Java uses braces `{}` for code blocks, Python uses indentation
- Python uses `elif` instead of `else if`
- Python's `for` loop is more like Java's for-each loop

## 4. Functions/Methods

### Java

```java
public class MathUtils {
    // Method with return type
    public static int add(int a, int b) {
        return a + b;
    }

    // Method without return type
    public static void printMessage(String message) {
        System.out.println(message);
    }

    // Method call
    int result = add(5, 3);
    printMessage("Hello");
}

```

### Python

```python
# Function with return value
def add(a, b):
    return a + b

# Function without return value
def print_message(message):
    print(message)

# Function call
result = add(5, 3)
print_message("Hello")

```

**Key Differences:**

- Java requires specifying return type and parameter types
- Python uses `def` keyword instead of specifying return type
- Java methods must be inside a class
- Python functions can be defined anywhere

## 5. Classes and Objects

### Java

```java
public class Person {
    // Fields
    private String name;
    private int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method
    public void introduce() {
        System.out.println("Hi, I'm " + name + " and I'm " + age + " years old.");
    }

    // Getter
    public String getName() {
        return name;
    }

    // Setter
    public void setName(String name) {
        this.name = name;
    }
}

// Usage
Person person = new Person("Alice", 30);
person.introduce();

```

### Python

```python
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

    # Getter (not always necessary in Python)
    def get_name(self):
        return self.name

    # Setter (not always necessary in Python)
    def set_name(self, name):
        self.name = name

# Usage
person = Person("Alice", 30)
person.introduce()

```

**Key Differences:**

- Python uses `__init__` instead of a constructor with the class name
- Python explicitly includes `self` as the first parameter in methods
- Java uses access modifiers (public, private, protected)
- Python uses naming conventions (e.g., `_name` for protected, `__name` for private)

## 6. Lists/Arrays

### Java

```java
// Array (fixed size)
int[] numbers = new int[3];
numbers[0] = 1;
numbers[1] = 2;
numbers[2] = 3;

// ArrayList (dynamic size)
import java.util.ArrayList;
ArrayList<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");
names.add("Charlie");

// Access elements
int first = numbers[0];
String firstName = names.get(0);

// Loop through
for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}

for (String name : names) {
    System.out.println(name);
}

```

### Python

```python
# List (dynamic size)
numbers = [1, 2, 3]
names = ["Alice", "Bob", "Charlie"]

# Access elements
first = numbers[0]
firstName = names[0]

# Loop through
for number in numbers:
    print(number)

for i in range(len(names)):
    print(names[i])

```

**Key Differences:**

- Java arrays have fixed size, ArrayLists are dynamic
- Python lists are always dynamic
- Java uses `get()` and `add()` methods for ArrayLists
- Python uses bracket notation for both access and modification

## 7. Exception Handling

### Java

```java
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero: " + e.getMessage());
} finally {
    System.out.println("This always executes");
}

```

### Python

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")
finally:
    print("This always executes")

```

**Key Differences:**

- Java uses `catch`, Python uses `except`
- Both have similar `try` and `finally` blocks
- Java exceptions are checked (must be handled or declared)
- Python exceptions are unchecked

## 8. Comments

### Java

```java
// Single-line comment

/*
Multi-line
comment
*/

/**
 * Javadoc comment
 * @param x the first number
 * @return the sum of x and y
 */
public int add(int x, int y) {
    return x + y;
}

```

### Python

```python
# Single-line comment

"""
Multi-line comment
(or docstring)
"""

def add(x, y):
    """
    Function docstring
    :param x: the first number
    :param y: the second number
    :return: the sum of x and y
    """
    return x + y

```

**Key Differences:**

- Java uses `//` for single-line, `/* */` for multi-line
- Python uses `#` for single-line, `""" """` for multi-line
- Both support documentation comments (Javadoc vs. docstrings)

## 9. Importing Modules/Packages

### Java

```java
// Import specific class
import java.util.ArrayList;

// Import all classes from package
import java.util.*;

// Static import
import static java.lang.Math.PI;

```

### Python

```python
# Import entire module
import math

# Import specific function/class
from math import sqrt

# Import with alias
import numpy as np

# Import all (generally discouraged)
from math import *

```

**Key Differences:**

- Java uses `import package.Class;`
- Python uses `import module` or `from module import function`
- Both support aliasing (Java: `import java.util.Date as UtilDate`)

## 10. String Formatting

### Java

```java
String name = "Alice";
int age = 30;

// Concatenation
String message1 = "Hi, I'm " + name + " and I'm " + age + " years old.";

// String.format()
String message2 = String.format("Hi, I'm %s and I'm %d years old.", name, age);

// StringBuilder (for multiple operations)
StringBuilder sb = new StringBuilder();
sb.append("Hi, I'm ");
sb.append(name);
sb.append(" and I'm ");
sb.append(age);
sb.append(" years old.");
String message3 = sb.toString();

```

### Python

```python
name = "Alice"
age = 30

# Concatenation
message1 = "Hi, I'm " + name + " and I'm " + str(age) + " years old."

# % formatting
message2 = "Hi, I'm %s and I'm %d years old." % (name, age)

# str.format()
message3 = "Hi, I'm {} and I'm {} years old.".format(name, age)

# f-strings (Python 3.6+)
message4 = f"Hi, I'm {name} and I'm {age} years old."

```

**Key Differences:**

- Python has more string formatting options
- Java requires explicit conversion of non-string types
- Python f-strings provide concise syntax

## Summary Table

| Feature | Java | Python |
| --- | --- | --- |
| **File Structure** | Class with main method | Direct execution |
| **Variable Declaration** | Explicit type required | Dynamic typing |
| **Code Blocks** | Braces `{}` | Indentation |
| **Conditionals** | `if (condition) { }` | `if condition:` |
| **Loops** | `for (int i=0; i<5; i++)` | `for i in range(5):` |
| **Functions** | `returnType name(params) {}` | `def name(params):` |
| **Classes** | `class Name { }` | `class Name:` |
| **Constructor** | `ClassName(params) { }` | `__init__(self, params)` |
| **List/Array** | `int[] arr` or `ArrayList<String>` | `list = [1, 2, 3]` |
| **Exception Handling** | `try-catch-finally` | `try-except-finally` |
| **Comments** | `//` and `/* */` | `#` and `""" """` |
| **Imports** | `import package.Class` | `import module` |
| **String Formatting** | `String.format()` | f-strings, `str.format()` |

This comparison should give you a comprehensive understanding of the syntax differences between Python and Java. Keep this as a reference sheet when working with either language!

Let's break down the syntax differences between Python and Java step-by-step. This will serve as a comprehensive note sheet for easy reference.

## Python vs. Java: Syntax Differences

| Feature | Python | Java | Notes |
| --- | --- | --- | --- |
| **Code Blocks** | Indentation (whitespace) defines code blocks. | Curly braces `{}` define code blocks. | Python's reliance on indentation enforces clean and readable code. Java uses braces, which can sometimes lead to less consistent formatting if not managed carefully. |
| **Statements** | Newlines typically indicate the end of a statement. | Semicolons `;` terminate most statements. | Python is more concise. Java requires semicolons, which can be a common source of syntax errors for beginners. |
| **Variable Declaration & Typing** | Dynamically typed. No explicit declaration needed. Type is inferred. | Statically typed. Variables must be declared with their type before use. | **Python:** `x = 10` (type inferred as integer)**Java:** `int x = 10;` (type `int` explicitly declared). This is a fundamental difference impacting how you write and think about your code. |
| **Comments** | Single-line: `#`Multi-line: `''' '''` or `""" """` | Single-line: `//`Multi-line: `/* */`Documentation: `/** */` | Python's multi-line comments are technically docstrings, often used for function/class documentation. Java's `/** */` is specifically for generating API documentation. |
| **Case Sensitivity** | Case-sensitive. | Case-sensitive. | Both languages are case-sensitive, meaning `myVariable` and `myvariable` are treated as distinct. |
| **Class Definition** | `class MyClass:` | `public class MyClass { ... }` | Java requires classes to be enclosed within curly braces and often starts with an access modifier like `public`. |
| **Method Definition** | `def my_method(self, arg1):` | `public void myMethod(Type arg1) { ... }` | Python methods are defined with `def`. The `self` parameter is explicit and refers to the instance. Java methods require a return type (e.g., `void` for no return) and have explicit parameter types. Access modifiers are common. |
| **Constructor** | `__init__(self, ...)`method. | A method with the same name as the class: `public MyClass(...) { ... }` | Python uses a special `__init__` method. Java uses a method named exactly like the class, and it's often public. |
| **Function Calls** | `my_function(arg1, arg2)` | `myObject.myMethod(arg1, arg2);` or `MyClass.staticMethod(arg1);` | Python calls functions/methods directly. Java often requires calling methods on an object instance or class. |
| **Printing Output** | `print("Hello")` | `System.out.println("Hello");` | Python's `print` is a built-in function. Java uses a more verbose `System.out.println`statement. |
| **Loops (For)** | `for item in iterable:` | `for (initialization; condition; update) { ... }`or `for (Type variable : iterable) { ... }` | Python's `for` loop iterates directly over items in a sequence. Java has traditional C-style `for` loops with explicit control variables and enhanced `for` loops for iterating over collections (similar to Python's). |
| **Loops (While)** | `while condition:` | `while (condition) { ... }` | Syntax is quite similar, with Python using a colon and Java using parentheses and braces. |
| **Conditional Statements (If/Else)** | `if condition:`    `elif another_condition:`    `else:` | `if (condition) { ... }`    `else if (another_condition) { ... }`    `else { ... }` | Python uses `elif` and colons. Java uses `else if`, parentheses for conditions, and curly braces for blocks. |
| **Boolean Values** | `True`, `False` | `true`, `false` | Case difference for boolean literals. |
| **Null/None** | `None` | `null` | Python uses `None` to represent the absence of a value. Java uses `null`. |
| **Data Structures** | Lists: `[1, 2, 3]`Tuples: `(1, 2, 3)`Dictionaries: `{'a': 1}` | Arrays: `int[] arr = {1, 2, 3};`ArrayLists: `ArrayList<Integer> list = new ArrayList<>();`HashMaps: `HashMap<String, Integer> map = new HashMap<>();` | Python has built-in, highly flexible data structures. Java often requires using classes from its Collections Framework and specifying types. |
| **Imports** | `import module_namefrom package import item` | `import package.ClassName;import package.*;` | Python imports modules or specific items. Java imports classes or all classes within a package. |
| **String Concatenation** | `str1 + str2` | `str1 + str2` | Both use the `+` operator for simple string concatenation. Java also has `StringBuilder` for more efficient concatenation in loops. |
| **Exception Handling** | `try:`    `except ExceptionType as e:`    `finally:` | `try { ... }`    `catch (ExceptionType e) { ... }`    `finally { ... }` | Python uses `try`, `except`, and `finally`with different keywords. Java uses `try`, `catch`, and `finally` with distinct syntax. |
| **Inheritance** | `class Child(Parent):` | `class Child extends Parent { ... }` | Python uses parentheses in the class definition. Java uses the `extends` keyword. |
| **Interfaces** | No direct equivalent; Abstract Base Classes (ABCs) can mimic behavior. | `interface MyInterface { ... }class MyClass implements MyInterface { ... }` | Java has a strong concept of interfaces for defining contracts. Python uses a more duck-typing approach or ABCs for similar patterns. |
| **Type Hinting (Optional)** | Supported (e.g., `def greet(name: str) -> str:`) | Not directly applicable as types are mandatory. | Python 3.5+ introduced optional type hinting, which can improve code readability and allow for static analysis. Java's static typing makes this redundant. |
| **Keywords** | `if`, `else`, `while`, `for`, `def`, `class`, `import`, `return`, `try`, `except`, `None`, `True`, `False`, `and`, `or`, `not`, `is` | `if`, `else`, `while`, `for`, `class`, `import`, `return`, `try`, `catch`, `finally`, `null`, `true`, `false`, `&&`, ` |  |

### Key Takeaways and General Philosophies:

- **Python: Readability and Simplicity**
    - Emphasizes clear, concise, and readable code.
    - Uses whitespace (indentation) to define structure.
    - Dynamically typed, making it faster to write initially.
    - "Batteries included" philosophy with a rich standard library.
- **Java: Robustness and Structure**
    - Emphasizes strict typing, object-oriented principles, and platform independence.
    - Uses curly braces and semicolons for structure and statement termination.
    - Statically typed, leading to more verbose but often more error-resistant code at compile-time.
    - Designed for large-scale enterprise applications and systems.

This note sheet should provide a solid foundation for understanding the fundamental syntax differences between Python and Java. Remember that while syntax is important, the underlying programming paradigms and standard libraries also play a significant role in how you approach problem-solving in each language.