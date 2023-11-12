
# **Project Title: 0x00. AirBnB clone - The console**

## **The Project Description**

The console is a custom command line interpreter that will be used for managing the AirBnB objects in the following ways:

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

#### **Option 1: Starting By The Use of "echo"**

This entails "piping" an input into the command with the use of `echo`, as shown below

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

#### **Option 2: Starting With A File of Commands**

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
