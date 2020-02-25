# AirBnB clone - The console

AirBnB clone is a web application project that works very similar to AirBnB.com but does not have all the features.
In this first phase, we will write a command interpreter to manage the AirBnB objects. Also, we will test with some cases.

![AirBnB project's tree](https://raw.githubusercontent.com/dgquintero/dgquintero.github.io/master/images/Screen%20Shot%202020-02-19%20at%205.21.14%20PM.png)

## Table of contents

- 1. [Getting Started](#Getting-Started)  
- 1.1. [Prerequisites](#Prerequisites)
- 1.2. [Installing](#Installing)
- 2. [Running the tests](#Running-the-tests)
- 3. [Built With](#Built-With)
- 4. [Authors](#Authors)
- 5. [License](#License)
## Getting Started

When you run the console ./console.py on the terminal, the shell issues a command prompt (hbnb) , where you can type your input and is goint to be executed when you hit Enter. The output or the result that you asked for, will be displayed on the terminal.

### Prerequisites

#### Python Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using  `python3` (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `PEP 8`  style (version 1.7 or more)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

#### Python Unit Tests

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder  `tests`
-   You have to use the  [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g "unittest module")
-   All your test files should be python files (extension:  `.py`)
-   All your test files and folders should start by  `test_`
-   Your file organization in the tests folder should be the same as your project
-   e.g., For  `models/base_model.py`, unit tests must be in:  `tests/test_models/test_base_model.py`
-   e.g., For  `models/user.py`, unit tests must be in:  `tests/test_models/test_user.py`
-   All your tests should be executed by using this command:  `python3 -m unittest discover tests`
-   You can also test file by file by using this command:  `python3 -m unittest tests/test_models/test_base_model.py`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### Installing

Step by step how to run HBNB

*First of all clone the repository* 

```
git clone "https://github.com/dgquintero/AirBnB_clone.git"
```

*Go to the directory AirBNnB_clone*
```
cd AirBnB_clone/
```
*Run it on interactive mode*
```
./console.py
```

## Running the tests

The AirBnB_clone works like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

The AirBnB_clone works like this in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Built With

* [Python](https://www.python.org) - Programming language.



## Authors
* **Oscar Rodriguez** - [Github](https://github.com/oscarmrt) - [Twitter](https://twitter.com/OscaRT07)
* **Daniel Quintero** - [Github](https://github.com/dgquintero) - [Twitter](https://twitter.com/danielq02)


## License

AirBnB_clone has an open source license [Open Source Definition](https://opensource.org/osd) — in brief, they allow software to be freely used, modified, and shared
