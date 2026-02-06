# Python Projects (OOP + Mini Script)

This repository contains **two Python projects**:
1) **OOP Management System** (Object-Oriented Programming)
2) **Random Website Opener** (Mini script using `random` and `webbrowser`)

---

## 1) OOP Management System (Python)

### Overview
A Python Object-Oriented Programming (OOP) project that simulates a simple
employee–office workflow using the following classes:
**Person**, **Employee**, **Car**, and **Office**.

The project demonstrates how these classes interact together while applying
core OOP principles.

### Key Features
- Manage person mood, health, and money (sleep / eat / buy)
- Employee work logic (happy / tired / lazy)
- Car driving simulation with fuel consumption and velocity limits
- Office operations: hire, fire, reward, deduct, and lateness checking

### OOP Concepts Used
- Encapsulation (validation and property setters)
- Inheritance (Employee inherits from Person)
- Composition (Employee has a Car)
- Static methods and class methods
- Custom exception handling (`ValidationError`)

### Project Structure (Recommended)
```text
oop-project/
│── oop/
│   │── __init__.py
│   │── person.py
│   │── employee.py
│   │── car.py
│   │── office.py
│
│── main.py
```

### How to Run
From the repository root:
```bash
cd oop-project
python main.py


````
### Notes

* The code includes validations for values such as fuel rate, velocity, and health rate.
* Running `main.py` demonstrates the full workflow:
  sleep → eat → buy → work → drive → refuel → check lateness

---

## 2) Random Website Opener

### Overview

A small Python script that randomly selects a website from a predefined list
and opens it using the default web browser.

### Features

* Random website selection using `random.choice`
* Opens the selected website using `webbrowser.open`

### Project Structure (Recommended)

```text
random-website-opener/
│── main.py
```

### How to Run

From the repository root:

```bash
cd random-website-opener
python main.py
```

### Customize Websites List

Open `main.py` and edit the `websites` list:

```python
websites = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.stackoverflow.com",
    "https://www.github.com"
]
```

---

## Requirements

* Python 3.8+

## Author

* Yomna Ali
* GitHub: [https://github.com/yomnaaali](https://github.com/yomnaaali)

````
