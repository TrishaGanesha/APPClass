#debugging techniques to rectify errors in the code when encountered during runtime or compilation.identfying analyzing and correcting erros in a program
#different types of debugging techniques include:
#1. Print Debugging: Inserting print statements in the code to display variable values and
#    execution flow.
#2. Logging: Using logging libraries to log messages at different levels (info, warning, error) for better tracking of issues.
#3. Interactive Debugging: Using interactive debuggers (like pdb in Python) to step through the code, inspect variables, and evaluate expressions.
#4. Unit Testing: Writing test cases to validate individual functions or modules, helping to catch errors early.
#5. Code Review: Having peers review the code to identify potential issues and suggest improvements.
#6 Exception Handling: Implementing try-except blocks to gracefully handle errors and provide meaningful error messages.
#7 assert statements: Using assert statements to check for conditions that should always be true, helping to catch logical errors during development.
#8 breakpoints: Setting breakpoints in the code to pause execution at specific points, allowing for inspection of the program state.
#9. call stack analysis: Analyzing the call stack to trace the sequence of function calls leading to an error, aiding in identifying the root cause.
#10. default debugging tools: Utilizing built-in debugging tools provided by IDEs (Integrated Development Environments) to facilitate the debugging process.pde python debugging

#debugging is essential programming skill because:incorrect program logic,invalid user input,runtime exceptions,incorrect data types,unhandled exceptions,logical errors,function call errors,file and resource issues
# 1.Assertion 
# syntax: assert condition, "error message"
assert 5 > 3, "5 is not greater than 3"
def calculate_average(numbers):
    assert len(numbers)> 0, "The list of numbers cannot be empty"
    return sum(numbers) / len(numbers)
numbers = [10, 20, 30]
average = calculate_average(numbers)
print("Average:", average)
avg=[]
print("Average of empty list:", calculate_average(avg))  # This will raise an AssertionError

#2.Exception handling is a mechanism in programming languages to handle runtime errors gracefully, allowing the program to continue executing or provide meaningful error messages instead of crashing. It involves using try-except blocks to catch and handle exceptions that may occur during program execution.

#3.Logging
#the logging module records information about program execution unlike print(),logging can record message based on severity levels, log messages can be directed to different outputs, such as console, files, or external logging systems, logging can be configured to include timestamps, log levels, and other contextual information for better debugging and analysis.
#commomn   logging levels:
#level       purpose
#DEBUG       Detailed information, typically of interest only when diagnosing problems.
#INFO        Confirmation that things are working as expected.general program information
#WARNING     An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
#ERROR       Due to a more serious problem, the software has not been able to perform some function.indicates that an error occured
#critical    indicates a serious failure
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
logging.debug("Program started")
age=int(input("Enter your age: "))
logging.info(f"Age entered:{age}")
if age<18:
    logging.warning("User is not eligible for the service.")
logging.debug("Program completed")

#python debugger (pdb) is a built-in module that allows developers to set breakpoints, step through code, inspect variables, and evaluate expressions interactively. It helps identify and fix bugs by providing a controlled environment for debugging.
# it allows the programmer to:
# pause program execution
# execute the program step by step
# inspect variable values 
# check program flow
# identify logical errors

# commands     meaning
# n            execute the next line of code
#s            step into a function call
# c            continue execution until the next breakpoint
# p            print the value of a variable or expression
# l            show surrounding lines of code for context
# q            quit the debugger and exit the program
# w            display the current call stack to see the sequence of function calls leading to the current point in execution

import pdb
marks=[90,87,76]
total=sum(marks)
# breakpoint()  # Set a breakpoint here
pdb.set_trace()
average=total/len(marks)
print("Average marks:",average)
