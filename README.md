# **Project Title: 0x00. AirBnB clone - The console**
## The Domains/Concepts covered in this project: `Python` `OOP`

**Background Context**

**Welcome to the AirBnB clone project!**
Before starting, please read the **AirBnB** concept page.

**First step: Write a command interpreter to manage your AirBnB objects.**
This is the first step towards building your first full web application: the **AirBnB clone**. This first 
step is very important because you will use what you build during this project with all other following 
projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

  * put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of 
your future instances
  * create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
  * create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
  * create the first abstracted storage engine of the project: File storage.
  * create all unittests to validate all our classes and storage engine

**What’s a command interpreter?**

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage 
the objects of our project:

  * Create a new object (ex: a new User or a new Place)
  * Retrieve an object from a file, a database etc…
  * Do operations on objects (count, compute stats, etc…)
  * Update attributes of an object
  * Destroy an object

## Tasks :page_with_curl:

**0. README, AUTHORS**

  * Write a `README.md`:
    * description of the project
    * description of the command interpreter:
      * how to start it
      * how to use it
examples
  * You should have an `AUTHORS` file at the root of your repository, listing all individuals having contributed content to the 
repository. For format, reference Docker’s AUTHORS page
  * You should use branches and pull requests on GitHub - it will help you as team to organize your work

  * [AirBnB_clone](https://github.com/kelvinnmuia/AirBnB_clone)

## **The Project Description**

The console Is a custom command line interpreter that will be used for managing the AirBnB objects in the following ways:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## **Description of The Console or Command Interpreter**

### **A. Starting and Using The Interpreter in Interactive Mode**

1. Run `./console` on your terminal to launch the Command Interpreter
2. On the `(hbnb)` prompt Type help to get the list of all the available commands in the Command Interpreter
3. Type Quit to exit the Command Interpreter

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

### **B. Starting and Using The Interpreter In Non-Interactive Mode**

#### **Option 1**
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

#### **Option 2: Starting By The Use of "echo"**

This entails "piping" an input into the command with the use of `echo`, as shown below

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

#### **Option 3: Starting With A File of Commands**

You can also pipe in a file with one command per line, as seen below

```
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```
