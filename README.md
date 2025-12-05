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

# First 5 characters
print(name[:5])       # 'Yashw'

# Last 6 characters
print(name[-6:])      # 'Kasula'

# Middle part
print(name[3:10])     # 'hwanth '

# Reverse the string
print(name[::-1])     # 'slusaK htnawhsaY'
