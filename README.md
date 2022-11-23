# README #

## What is this repository for? ##

This repository contains Python code for Security Device that uses a FSM.

Here is the original assignment:
(http://cs.iit.edu/~virgil/cs330/mail.fall2022/pa.html).

This code implements a FSM that has 2 states. It unlocks when the pin 949271 is in the input and locks when the pin 949274 is in the input. The device is intially in the Locked state on startup. 

The program discards any other inputs that aren't 0-9, whether it be 
alphabet characters or special characters.

## How do I get set up? ##

Instructions in this README file are for a Windows 11 environment

### Summary of set up ###

You must have 'pyinstaller' installed before you can complete set up.

### Configuration ###

1. Clone and open the repository:

```
$ git clone https://github.com/coleyadron/cs330project.git
```

2. Make sure all the unit tests pass:

```
$ pyinstaller --version
```

3. If pyinstaller is not installed then:

```
$ pip install pyinstaller
```

4. Build the executable:

```
$ pyinstaller.exe --onefile 330proj(Final).py
```

5. Change the directory:

```
$ cd dist
```

6. Run the executable:

```
$ "330proj(final).exe"
```

The device will prompt you with two main functions, manual and forced entry. Manual allows for user input to manually change the state of the device. While forced entry randomly generates inputs until the device is unlocked.

For manual entry, enter characters from the keyboard follow by Enter/Return
The application will consume the characters and print 'Lock'/'Unlock' as it encounters the pins respectively.

### License ###

[GNU Public License](https://www.gnu.org/licenses/gpt-3.0.html)

### Who do I talk to? ###

Email cyadron@hawk.iit.edu
