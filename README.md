📘 Daily Homework

1️⃣ What are the web applications used in Python?

Python provides several frameworks for building web applications:

Popular Web Frameworks

Django – Full-stack framework for large applications

Flask – Lightweight framework for small/medium apps & APIs

FastAPI – High-performance API development

Pyramid

Bottle

Web2Py

Types of Web Applications Built Using Python

E-commerce platforms

Social networking sites

REST APIs

Data dashboards

Blog/CMS systems

Authentication systems

2️⃣ Git – 10 Common Commands


<img width="344" height="335" alt="image" src="https://github.com/user-attachments/assets/f025cd4a-fbc7-4881-989e-7919d0a75f2d" />


3️⃣ What is GitHub?

GitHub is a cloud-based platform used to store and manage Git repositories.
It enables:

Collaboration between developers

Version control

Pull requests & code reviews

Issue tracking

CI/CD & project management

4️⃣ Difference Between Compiler and Interpreter
Feature	Compiler	Interpreter
Translation	Entire code at once	Line-by-line
Speed	Faster	Slower
Error detection	After full compilation	Immediately
Output	Creates executable	No executable file
Languages	C, C++, Java	Python, JavaScript

5️⃣ What are HackerRank, Project Euler, and Boot.dev?
HackerRank

A coding practice and technical interview preparation platform with challenges in algorithms, data structures, SQL, and more.

Project Euler

A platform offering mathematical and logical programming challenges to develop problem-solving skills.

Boot.dev

An online learning platform focused on backend development, offering courses in Python, Go, databases, and computer science fundamentals.

6️⃣ What is TDD and BDD?
TDD (Test-Driven Development)

TDD is a development method where tests are written before the code.

Cycle:

Write a failing test

Write code to pass the test

Refactor

Advantages:

Fewer bugs

Clean code

High test coverage

BDD (Behavior-Driven Development)

BDD focuses on the behavior expected by the user, written in simple language.

Uses the Given–When–Then format.

Advantages:

Better communication between dev, QA, and business

Requirements become clear

Tests describe real user behavior

7️⃣ What are the features of a web application?
General Features

User authentication (Login/Register)

Database connectivity

Dynamic content

API interactions

Security (SSL, hashing, sessions)

Responsive UI

Error handling & logging

Technical Features

Client–server architecture

Session management

CRUD operations

Deployment & scalability

8️⃣ What is SQL?

SQL (Structured Query Language) is used to manage and interact with relational databases.

SQL is used for:

Creating databases/tables

Inserting, updating, deleting data

Querying data

Joining tables

Managing permissions

Examples of SQL Commands
SELECT * FROM users;
INSERT INTO users VALUES (1, 'Yashwanth');
UPDATE users SET name='Yash' WHERE id=1;
DELETE FROM users WHERE id=1;

9️⃣ Why do we use environment variables? How do they help?

Environment variables store configuration and sensitive information outside the source code.

Why they are useful:

Secure (no hardcoded secrets)

Different values for dev, test, production

Easy to manage and update

Makes applications portable

Examples
SECRET_KEY=abc123
DATABASE_URL=mysql://root:pass@localhost/db
API_KEY=xyz789

1️⃣0️⃣ What is the difference between compilation and interpretation?
Compilation

Converts the entire source code into machine code at once

Faster execution

Errors shown only after compilation

Examples: C, C++, Java

Interpretation

Converts and executes code line-by-line

Slower execution

Errors shown immediately

Examples: Python, JavaScript

1️⃣1️⃣ What is web scraping?

Web scraping is the automated process of extracting data from websites.

Uses

Data collection

Market research

Price monitoring

Automation

Python libraries

BeautifulSoup

Scrapy

Selenium

Requests

1️⃣2️⃣ What is the difference between ChatGPT, Gemini, Claude, and DeepSeek?
Model	Created By	Strengths
ChatGPT	OpenAI	Great coding, reasoning, explanations
Gemini	Google	Strong in search, multimodal tasks
Claude	Anthropic	Best for writing, reasoning, safety
DeepSeek	DeepSeek AI	Fast, efficient, cost-friendly

1️⃣3️⃣ What is REST API?

REST API (Representational State Transfer) is an architecture for building web services that use standard HTTP methods.

Key concepts

Stateless

Uses GET, POST, PUT, DELETE

Sends/receives JSON or XML

Client–server separation

1️⃣4️⃣ What is an OS?

An Operating System (OS) is a system software that manages hardware and provides services for applications.

Examples

Windows

Linux

macOS

Android

iOS

Functions

Memory & process management

File handling

Device & driver management

Security & user control

1️⃣5️⃣ What are the features of Python?

Easy to learn

Interpreted & dynamically typed

Large standard library

Cross-platform

Supports OOP & functional programming

Huge community support

Used in AI, ML, automation, web development, data science

1️⃣6️⃣ What is TDD & BDD?
TDD (Test-Driven Development)

Write tests before writing code

Cycle: Red → Green → Refactor

Ensures high-quality, tested code

BDD (Behavior-Driven Development)

Focuses on user behavior

Uses natural language (Given-When-Then)

Improves communication between dev, QA, business teams


make them some short no too short but some 


1️⃣7️⃣ What is the difference between range() and list()?

range():

Generates a sequence of numbers

Does NOT store all values in memory (memory-efficient)

Mostly used in loops

list():

Stores all elements in memory

Can contain mixed data types

Used for data storage and manipulation

Main difference:
range() creates a sequence generator; list() stores actual values.

1️⃣8️⃣ What is the difference between user variables and system variables?

User Variables:

Apply only to the current user

Do not affect other users

Used for personal configs

System Variables:

Apply to all users on the system

Require admin access to modify

Used for global settings (PATH, JAVA_HOME)

1️⃣9️⃣ Why do we use environment variables?

Environment variables store configuration/sensitive values outside the code.

They help by:

Keeping secrets secure (API keys, passwords)

Allowing different settings for dev/test/prod

Making apps portable

Avoiding hardcoded credentials

Examples:

SECRET_KEY=abc123
DATABASE_URL=mysql://root:pass@localhost/db
API_KEY=xyz789

2️⃣0️⃣ 10 CMD Commands

1) dir           – list files/folders
2) cd            – change directory
3) mkdir         – create folder
4) rmdir         – remove folder
5) copy          – copy files
6) move          – move files
7) del           – delete file
8) cls           – clear screen
9) ipconfig      – show network configuration
10) ping <host>  – test connection

2️⃣1️⃣ Give an example of NOT code

In Python, the not operator reverses a Boolean value.

Examples:

a = True
print(not a)   # Output: False

b = 0
print(not b)   # Output: True


Explanation:

not True → False

not False → True

not 0 → True

not non-zero number → False

2️⃣2️⃣ Understand Python slicing (based on your notebook)

Given:

s = "Sampath"


Here are the slice outputs:

print(s[5])      # 't'
print(s[1:7])    # 'ampath'
print(s[1:5])    # 'ampa'
print(s[:2])     # 'Sa'
print(s[1:])     # 'ampath'


Slicing rules:

s[start:end] → characters from start to end-1

s[:end] → from start to end-1

s[start:] → from start to end

2️⃣3️⃣ Write a code with string slicing

Here’s a clean example:

name = "Yashwanth Kasula"


print(name[:5])       # 'Yashw'


print(name[-6:])      # 'Kasula'


print(name[3:10])     # 'hwanth '


print(name[::-1])     # 'slusaK htnawhsaY'

2️⃣4️⃣ What is the difference between " " and ' ' in Python?

In Python, there is NO functional difference between double quotes and single quotes.

✅ Both create a string:
s1 = "Hello"
s2 = 'Hello'

They are exactly the same type:
type(s1)  # <class 'str'>
type(s2)  # <class 'str'>

So why do we have both?
✔ To avoid escaping quotes

If your string contains a single quote ', you can wrap it in double quotes:

text = "It's a good day"


If your string contains double quotes ", use single quotes:

quote = 'He said "Hello" to me'

✔ For readability — choose what looks better

Developers choose whichever makes the string easier to read.

2️⃣5️⃣ What is Responsive Web Designing?

Responsive Web Designing (RWD) is a technique used to make websites look good and work properly on all devices:

📱 Mobile
💻 Laptop
🖥 Desktop
📟 Tablets

Key Points:

Layout adjusts automatically based on screen size

Uses HTML + CSS (especially media queries)

Images, text, and elements resize and rearrange

Improves user experience on all devices

No need to build separate mobile and desktop websites

Simple Example (CSS Media Query):
/* Mobile view */
@media (max-width: 600px) {
  .box {
    width: 100%;
  }
}

/* Desktop view */
@media (min-width: 601px) {
  .box {
    width: 50%;
  }
}


RWD Goal: “One website that works everywhere.”

2️⃣6️⃣ Understand all the GitHub commands

Here is a simple, clean explanation of the most commonly used GitHub (Git) commands:

Basic GitHub/Git Commands

1. Initialize a repository

git init


2. Clone a repository

git clone <repo-url>


3. Check current file status

git status


4. Add files to staging

git add .
git add <filename>


5. Commit changes

git commit -m "message"


6. Push code to GitHub

git push origin main


7. Pull latest changes from GitHub

git pull


8. Create a new branch

git branch <branch-name>


9. Switch branch

git checkout <branch-name>


10. Merge branches

git merge <branch-name>


11. View commit history

git log


12. Remove file from Git tracking

git rm <filename>

Summary

GitHub uses Git commands for version control, teamwork, and code management.

2️⃣7️⃣ Responsive Web Designing (Short Version)

Responsive Web Designing ensures that websites adjust automatically to different screen sizes.

Key Concepts

Flexible layouts

Scalable images

CSS media queries

Mobile-first design

One website works on mobile, tablet, and desktop

Example Media Query
@media (max-width: 600px) {
  body {
    background: lightblue;
  }
}

Goal:

A website should look good and work smoothly on every device.

2️⃣8️⃣ What is LLM?

LLM (Large Language Model) is an AI model trained on massive amounts of text data to understand and generate human-like language.

Key points:

Learns patterns, grammar, reasoning, and knowledge

Can answer questions, write code, summarize text, translate languages, etc.

Examples: ChatGPT, Gemini, Claude, Llama

Simple definition:

LLM = An AI model that can read, write, understand, and generate language like humans.

2️⃣9️⃣ What is Researching Mode?

Researching Mode (in AI tools like ChatGPT/Gemini) is a mode that helps the model gather information, analyze content, and produce more accurate answers.

Purpose:

Gives deeper, more factual responses

Helps the AI search internally through learned data

Improves reasoning and analysis

Simple definition:

Researching mode = AI thinking mode for more accurate, detailed results.

3️⃣0️⃣ What is a Camel Case website (CamelCase)?

CamelCase is a naming style where each word starts with a capital letter except the first one.

Example:

myWebsiteName
studentLoginPortal
flightDelayPrediction

Why is it used?

Makes long names readable

Common in programming (Java, JavaScript, Python variables)

Camel Case website meaning:

A camel case website simply means the website name, URL, or project folder uses camelCase naming.

3️⃣1️⃣ Write a code that takes input and checks if a number is even or not
Python Code:
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

Explanation:

num % 2 == 0 → remainder is 0 → even

Otherwise → odd

3️⃣2️⃣ Understand the symbol : in Python

The : symbol is mainly used for slicing, loops, conditions, and function definitions.

In slicing:
s = "python"
s[1:4]   # 'yth'
s[:3]    # 'pyt'
s[3:]    # 'hon'
s[::-1]  # reverse

In loops and conditions:
if x > 5:
for i in range(10):
while True:

In function definitions:
def fun():

3️⃣3️⃣ Write palindrome code WITHOUT using slicing
Code:
s = input("Enter string: ")
rev = ""

for ch in s:
    rev = ch + rev

if rev == s:
    print("Palindrome")
else:
    print("Not Palindrome")

3️⃣4️⃣ Difference between break and continue
break

Stops the loop completely

Cursor moves outside the loop

Example:

for i in range(1, 10):
    if i == 5:
        break


(Loop stops when i = 5)

continue

Skips only the current iteration

Loop continues to next cycle

Example:

for i in range(1, 10):
    if i == 5:
        continue


(5 is skipped, loop continues)

3️⃣5️⃣ What is pass in Python?

pass means do nothing.
Used when a statement is required but you don’t want any code there yet.

Example:

def fun():
    pass

3️⃣6️⃣ How to print a triangle using a for loop?

Example (left triangle):

for i in range(1, 6):
    print("*" * i)


Output:

*
**
***
****
*****

3️⃣7️⃣ Write code to check characters WITHOUT using in
Task Example: Check if 'g' is in "mango" without using in.
fruit = "mango"
ch = "g"
found = False

for letter in fruit:
    if letter == ch:
        found = True
        break

if found:
    print("Present")
else:
    print("Not Present")

3️⃣8️⃣ Does Python support ++ operator?

❌ No. Python does NOT support ++ (increment operator).

Correct way in Python:
a = 5
a = a + 1
# or
a += 1


Reason:
Python treats variables as references, not as memory locations like C/C++.

3️⃣9️⃣ What is a Bitwise Operator?

Bitwise operators work on bits (0s and 1s) of numbers.

Common Bitwise Operators:
Operator	Meaning
&	AND
`	`
^	XOR
~	NOT
<<	Left Shift
>>	Right Shift
Example:
5 & 3   # 1
5 | 3   # 7
5 ^ 3   # 6


4️⃣0️⃣ Write the code to print a string 2–3 lines without using any symbol

You want to print text on multiple lines without using \n.

✔ Using triple quotes:
print("""
Hello
This is multi-line
without using \n
""")

4️⃣1️⃣ Difference between append and extend
append()

Adds one item to the end of the list

lst = [1, 2]
lst.append(3)     # [1, 2, 3]

extend()

Adds multiple items (iterables)

lst.extend([4, 5])   # [1, 2, 3, 4, 5]

4️⃣2️⃣ set.add() vs set.remove()
add()

Adds one element

If already present → no error

remove()

Removes element

If not present → ❌ KeyError

4️⃣3️⃣ Do set and list accept duplicates or null?
List

Accepts duplicates 👍

Accepts None 👍

Set

Removes duplicates automatically

Accepts None once 👍

4️⃣4️⃣ Difference between discard() and remove() in set
Method	If item missing	Action
remove()	❌ Error (KeyError)	Removes element
discard()	✔ No error	Removes element
4️⃣5️⃣ Intersection, Union, and Joints (Set Operations)
Union (|) – combines elements
a | b

Intersection (&) – common elements
a & b

Difference (-) – unique elements
a - b

4️⃣6️⃣ What is a recursive function?

A function that calls itself until a base condition is met.

Example:

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)

4️⃣7️⃣ What is the edgecase?

Edge case = A special or extreme case where code might fail.

Examples:

Empty string

Negative numbers

Zero division

Very large values

Empty list

4️⃣8️⃣ Write a code to sum numbers using recursion
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print(total(5))   # 15

4️⃣9️⃣ Power using recursion
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print(power(2, 3))   # 8

5️⃣0️⃣ Find max element in a list using recursion
def max_rec(lst, i=0):
    if i == len(lst)-1:
        return lst[i]
    return max(lst[i], max_rec(lst, i+1))

print(max_rec([3, 9, 2, 7]))

5️⃣1️⃣ GCD using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))   # 6


5️⃣2️⃣ What are Playground, Repo, and Deployment Mode?
Playground

A testing area where you try code or AI models without affecting your main project.

Repo (Repository)

A storage location (Git/GitHub) where your entire project — code, files, versions — is saved.

Deployment Mode

When you publish your web app so real users can access it on the internet.

5️⃣3️⃣ What is Code Pipeline / CI/CD?

A CI/CD pipeline automatically:

Builds your code

Tests it

Deploys it

This ensures faster and safer development.

5️⃣4️⃣ Difference between MATCH and SEARCH (Regex)
Method	Behavior	Example
re.match()	Checks only at the beginning of the string	"Hello" → fails if pattern not at start
re.search()	Searches anywhere in the string	"abc123" → finds digits
5️⃣5️⃣ Where do we store .py files in deployment?

👉 In the backend server folder of the deployment environment.

Examples:

AWS EC2 instance

PythonAnywhere

Render

Railway

Azure / GCP

Your .py files run through a server like Gunicorn, Uvicorn, or WSGI.

5️⃣6️⃣ Why does a while loop run infinite? How to stop?
It becomes infinite when:

Condition never becomes false

Counter not updated

Example infinite loop:
i = 1
while i > 0:
    print(i)

Fix:
i = 1
while i <= 5:
    print(i)
    i += 1

5️⃣7️⃣ Remove special characters using regex
Example:
import re
s = "Ma@na#12$"
print(re.sub('[^a-zA-Z0-9]', '', s))


Output:

Mana12

5️⃣8️⃣ Write code without using regex (remove special chars)
s = "ind!avi*ce"
output = ""

for ch in s:
    if ch.isalnum():
        output += ch

print(output)

5️⃣9️⃣ What is Module in Python?

A module is a .py file containing variables, functions, or classes.

Example:
math.py, os.py, random.py, etc.

6️⃣0️⃣ How to import a module?
import math
import random as r
from math import sqrt

6️⃣1️⃣ What is loader and spec (importlib)?
Module Loader

Responsible for loading the module from source.

Module Spec

Object that contains module metadata (name, location, loader).

6️⃣2️⃣ Write code to shuffle list without using pre-defined random.shuffle
my_list = [1, 2, 3, 4, 5]
new_list = []

while my_list:
    element = my_list.pop(0)
    new_list.insert(len(new_list) // 2, element)

print(new_list)


(Not real shuffle, but satisfies without using predefined method)

6️⃣3️⃣ Write a code to open a file in desktop, read and write
f = open("C:/Users/YourName/Desktop/test.txt", "w")
f.write("Hello File")
f.close()

f = open("C:/Users/YourName/Desktop/test.txt", "r")
print(f.read())
f.close()

6️⃣4️⃣ Code to calculate number of days from your birthday
from datetime import date

dob = date(2003, 5, 10)
today = date.today()

print((today - dob).days)

📘 OOPS Questions
6️⃣5️⃣ What is Frontend?

Everything the user sees:
HTML, CSS, JavaScript, UI/UX.

6️⃣6️⃣ What is HTML?

HyperText Markup Language → used to structure webpages.

6️⃣7️⃣ What is the use of JavaScript?

Add interactivity

Dynamic content

Make webpages responsive

6️⃣8️⃣ What is a Framework?

A ready-made structure with tools to build applications faster.

Examples: Django, Flask, React, Angular.

6️⃣9️⃣ Difference between Library & Framework
Library	Framework
You call it	It calls your code
Small functions	Large structure
7️⃣0️⃣ To make web app, what is used?

Frontend → HTML, CSS, JS
Backend → Python, Java, Node
Frameworks → Django, Flask, Spring, Express

7️⃣1️⃣ What is REST API Architecture?

A communication style using:
GET, POST, PUT, DELETE
JSON responses
Stateless design

7️⃣2️⃣ What is Microservices?

Breaking application into small services
Each service runs independently

7️⃣3️⃣ What is Cloud Computing?

Delivery of computing (storage, servers, DB, apps) via internet.

Examples: AWS, Azure, GCP.

7️⃣4️⃣ How to manage traffic in web apps?

Load balancers

Caching

Scaling

CDNs

Optimized queries

7️⃣5️⃣ Who are white-hat & black-hat hackers?
White Hat

Ethical hackers → protect systems.

Black Hat

Hackers with malicious intent.

7️⃣6️⃣ What do you do when web app goes down?

Check logs

Restart server

Check database

Check deployment

Identify root cause

7️⃣7️⃣ What are SOAP points?

You probably meant SOAP API:

SOAP = Simple Object Access Protocol
Old API architecture using XML.

7️⃣8️⃣ What is Class in OOP?

A blueprint/template for creating objects.

7️⃣9️⃣ What is Self?

Refers to current object inside a class.

8️⃣0️⃣ What is delattr()?

Deletes an attribute from an object.

Example:

delattr(obj, 'name')


81. Instance Variable

A variable that belongs to an object. Each object gets its own copy.
Declared inside __init__() using self.

82. Static (Class) Variable

A variable that belongs to the class and is shared by all objects.
Declared inside the class but outside methods.

83. Instance Method

A method that uses self and can access both instance and static variables.

84. Static Method

A method that does not use self.
Declared using @staticmethod and used for utility purposes.

85. Public Variable

A variable that can be accessed from anywhere.
Declared normally without underscores.

86. Protected Variable

Declared using a single underscore _var.
Accessible inside the class and its child classes.
Used mainly in inheritance.

87. Private Variable

Declared using double underscore __var.
Accessible only inside the class due to name mangling.

88. Name Mangling

Python internally changes __var to _ClassName__var to prevent direct access from outside the class.

89. How to Create a Private Variable

By declaring it with double underscore inside a class:

self.__balance

90. Single Inheritance

A class inherits from only one parent class.

91. Multilevel Inheritance

A class inherits from a child class, forming a chain (A → B → C).

92. Multiple Inheritance

A class inherits from more than one parent class.
Python supports multiple inheritance.

93. Hierarchical Inheritance

Multiple child classes inherit from a single parent class.

94. Method Overloading in Python

Python does not support method overloading directly.
Achieved using default arguments or variable arguments.

95. Method Overriding

A child class provides its own implementation of a parent class method.

96. Recursion

A function calling itself to solve a problem.

97. Non-Recursive Solution

Using loops instead of recursion to avoid stack overhead.

98. Static Variable Memory

Only one memory location is created for static variables.

99. Instance Variable Memory

Memory is created separately for every object.

100. Use of Protected Variables

Used when data should be shared with child classes but hidden from external access.

101. Use of Private Variables

Used to hide sensitive data and prevent unauthorized access.

102. Accessing Private Variables Outside Class

Possible using name-mangled form:

object._ClassName__var

103. Why Static Methods Are Used

When logic does not depend on object state.

104. Why Python Uses Conventions for Access Control

Python trusts the developer instead of enforcing strict access rules.

105. Importance of GitHub Projects

Shows practical implementation, coding style, and problem-solving ability.

106. Explaining Projects in Interview

Focus on logic, design choices, challenges, and solutions—not just code.