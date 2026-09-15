{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0c0150c-1ecd-48dc-a95e-d705266bcf7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "Debugging is the process of identifying, analyzing, and correcting errors (bugs) in a program.\n",
    "\n",
    "debugging is an essential programming skill because real-world software may fail due to:\n",
    "Incorrect program logic\n",
    "Invalid user input\n",
    "Runtime exceptions\n",
    "Incorrect variable values\n",
    "Function-call errors\n",
    "File and resource issue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "544e4f6d-80ba-48af-82e0-551a8490ae24",
   "metadata": {},
   "outputs": [],
   "source": [
    "1. Assertions\n",
    "An assertion is used to check whether a condition that should normally be true is actually true.\n",
    "\n",
    "Syntax\n",
    "assert condition\n",
    "\n",
    "can also provide an error message:\n",
    "\n",
    "assert condition, \"Error message\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9ad8259a-981c-4097-bf17-458148546116",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter age:  15\n"
     ]
    },
    {
     "ename": "AssertionError",
     "evalue": "Age must be 18 or above",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAssertionError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m age = int(input(\u001b[33m\"Enter age: \"\u001b[39m))\n\u001b[32m      2\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m \u001b[38;5;28;01massert\u001b[39;00m age >= \u001b[32m18\u001b[39m, \u001b[33m\"Age must be 18 or above\"\u001b[39m\n\u001b[32m      4\u001b[39m \n\u001b[32m      5\u001b[39m print(\u001b[33m\"Eligible to register\"\u001b[39m)\n",
      "\u001b[31mAssertionError\u001b[39m: Age must be 18 or above"
     ]
    }
   ],
   "source": [
    "age = int(input(\"Enter age: \"))\n",
    "\n",
    "assert age >= 18, \"Age must be 18 or above\"\n",
    "\n",
    "print(\"Eligible to register\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5caf1e72-4af0-4887-99fc-a22ca009385d",
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "Neither light is red! {'ns': 'yellow', 'ew': 'green'}",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAssertionError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 18\u001b[39m\n\u001b[32m     14\u001b[39m     \u001b[38;5;66;03m# Check whether at least one light is red\u001b[39;00m\n\u001b[32m     15\u001b[39m     \u001b[38;5;28;01massert\u001b[39;00m \u001b[33m'red'\u001b[39m \u001b[38;5;28;01min\u001b[39;00m stoplight.values(), \\\n\u001b[32m     16\u001b[39m         \u001b[33m'Neither light is red! '\u001b[39m + str(stoplight)\n\u001b[32m     17\u001b[39m \n\u001b[32m---> \u001b[39m\u001b[32m18\u001b[39m switchLights(market_2nd)\n\u001b[32m     19\u001b[39m print(\u001b[33m\"Traffic Light Status:\"\u001b[39m, market_2nd)\n\u001b[32m     20\u001b[39m \n\u001b[32m     21\u001b[39m switchLights(mission_16th)\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 15\u001b[39m, in \u001b[36mswitchLights\u001b[39m\u001b[34m(stoplight)\u001b[39m\n\u001b[32m     11\u001b[39m         \u001b[38;5;28;01melif\u001b[39;00m stoplight[key] == \u001b[33m'red'\u001b[39m:\n\u001b[32m     12\u001b[39m             stoplight[key] = \u001b[33m'green'\u001b[39m\n\u001b[32m     13\u001b[39m \n\u001b[32m     14\u001b[39m     \u001b[38;5;66;03m# Check whether at least one light is red\u001b[39;00m\n\u001b[32m---> \u001b[39m\u001b[32m15\u001b[39m     \u001b[38;5;28;01massert\u001b[39;00m \u001b[33m'red'\u001b[39m \u001b[38;5;28;01min\u001b[39;00m stoplight.values(), \\\n\u001b[32m     16\u001b[39m         \u001b[33m'Neither light is red! '\u001b[39m + str(stoplight)\n",
      "\u001b[31mAssertionError\u001b[39m: Neither light is red! {'ns': 'yellow', 'ew': 'green'}"
     ]
    }
   ],
   "source": [
    "# assertion\n",
    "\n",
    "market_2nd = {'ns': 'green', 'ew': 'red'}\n",
    "mission_16th = {'ns': 'red', 'ew': 'green'}\n",
    "def switchLights(stoplight):\n",
    "    for key in stoplight.keys():\n",
    "        if stoplight[key] == 'green':\n",
    "            stoplight[key] = 'yellow'\n",
    "        elif stoplight[key] == 'yellow':\n",
    "            stoplight[key] = 'red'\n",
    "        elif stoplight[key] == 'red':\n",
    "            stoplight[key] = 'green'\n",
    "\n",
    "    # Check whether at least one light is red\n",
    "    assert 'red' in stoplight.values(), \\\n",
    "        'Neither light is red! ' + str(stoplight)\n",
    "\n",
    "switchLights(market_2nd)\n",
    "print(\"Traffic Light Status:\", market_2nd)\n",
    "\n",
    "switchLights(mission_16th)\n",
    "print(\"Traffic Light Status:\", mission_16th)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0352d224-985c-4ba5-8d4d-c0140673ea16",
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "List should not be empty",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAssertionError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 9\u001b[39m\n\u001b[32m      5\u001b[39m \n\u001b[32m      6\u001b[39m \u001b[38;5;66;03m# numbers = [10, 20, -10, 30, -1]\u001b[39;00m\n\u001b[32m      7\u001b[39m numbers = []\n\u001b[32m      8\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m9\u001b[39m calculate_average(numbers)\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 2\u001b[39m, in \u001b[36mcalculate_average\u001b[39m\u001b[34m(numbers)\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m calculate_average(numbers):\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m     \u001b[38;5;28;01massert\u001b[39;00m len(numbers) > \u001b[32m0\u001b[39m, \u001b[33m\"List should not be empty\"\u001b[39m\n\u001b[32m      3\u001b[39m \n\u001b[32m      4\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m sum(numbers) / len(numbers)\n",
      "\u001b[31mAssertionError\u001b[39m: List should not be empty"
     ]
    }
   ],
   "source": [
    "def calculate_average(numbers):\n",
    "    assert len(numbers) > 0, \"List should not be empty\"\n",
    "    \n",
    "    return sum(numbers) / len(numbers)\n",
    "\n",
    "# numbers = [10, 20, -10, 30, -1]\n",
    "numbers = []\n",
    "\n",
    "calculate_average(numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9de97425-b8bd-4478-9e87-437562be55d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "2. Exception Handling\n",
    "Exception handling allows a program to manage runtime errors without terminating unexpectedly.\n",
    "\n",
    "Basic Structure\n",
    "try:\n",
    "    # Risky code\n",
    "\n",
    "except ExceptionType:\n",
    "    # Error handling code\n",
    "\n",
    "finally:\n",
    "    # Always executes\n",
    "\n",
    "Exception handling helps identify:\n",
    "- What type of error occurred\n",
    "- Where invalid input was provided\n",
    "- How the program should recover"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eebb893d-f5c6-473b-89e5-b93aa359be2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "3. raise\n",
    "raises an exception whenever it tries to execute invalid code. \n",
    "Python’s exceptions with try and except statements so that the program can \n",
    "recover from exceptions that you anticipated. \n",
    "But you can also raise your own exceptions in your code. \n",
    "\n",
    "Raising an exception is a way of saying, \n",
    "“Stop running the code in this function and move the program execution to the except statement.”\n",
    "\n",
    "Exceptions are raised with a raise statement. In code, a raise statement consists of the following:\n",
    "- The raise keyword\n",
    "- A call to the Exception() function\n",
    "- A string with a helpful error message passed to the Exception() function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "37a20f2a-bdcf-48d5-8e27-e9593f88ccc0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "****\n",
      "*  *\n",
      "*  *\n",
      "****\n",
      "OOOOOOOOOOOOOOOOOOOO\n",
      "O                  O\n",
      "O                  O\n",
      "O                  O\n",
      "OOOOOOOOOOOOOOOOOOOO\n",
      "An exception happened: Width must be greater than 2.\n",
      "An exception happened: Symbol must be a single character string.\n"
     ]
    }
   ],
   "source": [
    "# raise\n",
    "\n",
    "def boxPrint(symbol, width, height):\n",
    "    if len(symbol) != 1:\n",
    "        raise Exception('Symbol must be a single character string.')\n",
    "    if width <= 2:\n",
    "        raise Exception('Width must be greater than 2.')\n",
    "    if height <= 2:\n",
    "        raise Exception('Height must be greater than 2.')\n",
    "    print(symbol * width)\n",
    "\n",
    "    for i in range(height - 2):\n",
    "        print(symbol + (' ' * (width - 2)) + symbol)\n",
    "    print(symbol * width)\n",
    "\n",
    "for sym, w, h in (\n",
    "    ('*', 4, 4),\n",
    "    ('O', 20, 5),\n",
    "    ('x', 1, 3),\n",
    "    ('ZZ', 3, 3)\n",
    "):\n",
    "\n",
    "    try:\n",
    "        boxPrint(sym, w, h)\n",
    "    except Exception as err:\n",
    "        print('An exception happened: ' + str(err))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "205dba44-28a9-499c-84e0-23c69e047aa5",
   "metadata": {},
   "outputs": [],
   "source": [
    "4. Traceback\n",
    "When Python encounters an error, it produces a treasure trove of error information called the traceback. \n",
    "\n",
    "The traceback includes the error message, the line number of the line that caused the error,\n",
    "and the sequence of the function calls that led to the error. \n",
    "\n",
    "This sequence of calls is called the call stack.\n",
    "\n",
    "In programs where functions can be called from multiple places, \n",
    "the call stack can help you determine which call led to the error.\n",
    "\n",
    "The traceback is displayed by Python whenever a raised exception goes unhandled. \n",
    "But you can also obtain it as a string by calling traceback.format_exc(). \n",
    "\n",
    "This function is useful if you want the information from an exception’s traceback \n",
    "but also want an except statement to gracefully handle the exception. \n",
    "You will need to import Python’s traceback module before calling this function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "66eba697-ccd0-41d3-be09-b0312326046e",
   "metadata": {},
   "outputs": [
    {
     "ename": "Exception",
     "evalue": "This is the error message.",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mException\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 6\u001b[39m\n\u001b[32m      2\u001b[39m     bacon()\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m bacon():\n\u001b[32m      4\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m Exception(\u001b[33m'This is the error message.'\u001b[39m)\n\u001b[32m      5\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m6\u001b[39m spam()\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 2\u001b[39m, in \u001b[36mspam\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m spam():\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m     bacon()\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 4\u001b[39m, in \u001b[36mbacon\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m bacon():\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m Exception(\u001b[33m'This is the error message.'\u001b[39m)\n",
      "\u001b[31mException\u001b[39m: This is the error message."
     ]
    }
   ],
   "source": [
    "# Traceback\n",
    "\n",
    "def spam():\n",
    "    bacon()\n",
    "def bacon():\n",
    "    raise Exception('This is the error message.')\n",
    "\n",
    "spam()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "013e8abe-6e46-4646-b441-d957a400dafb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The traceback info was written to errorInfo.txt.\n"
     ]
    }
   ],
   "source": [
    "import traceback\n",
    "try:\n",
    "         raise Exception('This is the error message.')\n",
    "except:\n",
    "         errorFile = open('errorInfo.txt', 'w')\n",
    "         errorFile.write(traceback.format_exc())\n",
    "         errorFile.close()\n",
    "         print('The traceback info was written to errorInfo.txt.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73d3dca2-a7c4-4af6-9398-681a71bce46d",
   "metadata": {},
   "outputs": [],
   "source": [
    "5. Logging\n",
    "The logging module records information about program \n",
    "execution.\n",
    "\n",
    "Unlike print(), logging can record messages based \n",
    "on their severity level.\n",
    "\n",
    "To enable the logging module to display log messages on your screen as your program runs\n",
    "import logging\n",
    "logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')\n",
    "\n",
    "You don’t need to worry too much about how this works, but basically, \n",
    "when Python logs an event, it creates a LogRecord object that holds information about that event. \n",
    "\n",
    "The logging module’s basicConfig() function lets you specify what details about \n",
    "the LogRecord object you want to see and how you want those details displayed.\n",
    "    \n",
    "Common         Logging Levels\n",
    "------------------------------\n",
    "Level\t       Purpose\n",
    "DEBUG\t       Detailed information for debugging\n",
    "INFO\t       General program information\n",
    "WARNING\t       Indicates a possible problem\n",
    "ERROR\t       Indicates that an error occurred\n",
    "CRITICAL\t   Indicates a serious failure"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "978d85b5-dfac-449c-bd7b-acbf464014be",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " 2026-09-08 10:36:21,526 - DEBUG - Some debugging details.\n",
      " 2026-09-08 10:36:21,528 - INFO - The logging module is working.\n",
      " 2026-09-08 10:36:21,529 - WARNING - An error message is about to be logged.\n",
      " 2026-09-08 10:36:21,531 - ERROR - An error has occurred.\n",
      " 2026-09-08 10:36:21,532 - CRITICAL - The program is unable to recover!\n"
     ]
    }
   ],
   "source": [
    "# Logging Levels\n",
    "\n",
    "import logging\n",
    "logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')\n",
    "\n",
    "logging.debug('Some debugging details.')\n",
    "\n",
    "logging.info('The logging module is working.')\n",
    "\n",
    "logging.warning('An error message is about to be logged.')\n",
    "\n",
    "logging.error('An error has occurred.')\n",
    "\n",
    "logging.critical('The program is unable to recover!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "febb05e6-179f-4817-ba25-f67d5c996d38",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "DEBUG: Program started\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number:  78\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "INFO: Age entered: 78\n",
      "DEBUG: Program completed\n"
     ]
    }
   ],
   "source": [
    "import logging\n",
    "\n",
    "# This configures how logging messages should be displayed.\n",
    "logging.basicConfig(\n",
    "    level=logging.DEBUG,       # sets the minimum logging level to DEBUG.\n",
    "    format=\"%(levelname)s: %(message)s\"   # This determines how the log message should appear.\n",
    ")\n",
    "\n",
    "logging.debug(\"Program started\")     # print(\"Program started\")\n",
    "\n",
    "age = int(input(\"Enter number: \"))\n",
    "\n",
    "logging.info(f\"Age entered: {age}\")   # Records the value entered or processed.\n",
    "\n",
    "# WARNING indicates that something may be wrong or requires attention,\n",
    "# but the program does not necessarily stop\n",
    "if age < 18:\n",
    "    logging.warning(\"Age is below eligibility criteria\")  \n",
    "\n",
    "logging.debug(\"Program completed\")  # Tracks detailed execution steps."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "19223ea7-8ca0-4406-a898-e9ac0c7b2898",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "INFO: Application started\n",
      "DEBUG: Loading student records\n",
      "WARNING: Missing optional student email\n",
      "ERROR: Unable to connect to database\n"
     ]
    }
   ],
   "source": [
    "# Logging to a File\n",
    "\n",
    "import logging\n",
    "\n",
    "logging.basicConfig(\n",
    "    filename=\"application.log\",   # which can be used later to analyze program execution\n",
    "    level=logging.DEBUG,\n",
    "    format=\"%(asctime)s - %(levelname)s - %(message)s\"\n",
    ")\n",
    "\n",
    "logging.info(\"Application started\")\n",
    "logging.debug(\"Loading student records\")\n",
    "logging.warning(\"Missing optional student email\")\n",
    "logging.error(\"Unable to connect to database\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "96986145-cf48-444c-a463-4a717d61d5fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " 2026-09-10 17:31:47,302 - DEBUG - Start of program\n",
      " 2026-09-10 17:31:47,305 - DEBUG - Start of factorial(5)\n",
      " 2026-09-10 17:31:47,307 - DEBUG - i is 1, total is 1\n",
      " 2026-09-10 17:31:47,309 - DEBUG - i is 2, total is 2\n",
      " 2026-09-10 17:31:47,311 - DEBUG - i is 3, total is 6\n",
      " 2026-09-10 17:31:47,312 - DEBUG - i is 4, total is 24\n",
      " 2026-09-10 17:31:47,312 - DEBUG - i is 5, total is 120\n",
      " 2026-09-10 17:31:47,313 - DEBUG - End of factorial(5)\n",
      " 2026-09-10 17:31:47,315 - DEBUG - End of program\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "# factorial of a number using logging\n",
    "\n",
    "import logging\n",
    "logging.basicConfig(level=logging.DEBUG, \n",
    "format=' %(asctime)s - %(levelname)s - %(message)s')\n",
    "logging.debug('Start of program')\n",
    "\n",
    "def factorial(n):\n",
    "    logging.debug('Start of factorial(%s)' % (n))\n",
    "    total = 1\n",
    "    for i in range(1, n + 1):\n",
    "        total *= i\n",
    "        logging.debug('i is ' + str(i) + ', total is ' + str(total))\n",
    "    logging.debug('End of factorial(%s)' % (n))\n",
    "    return total\n",
    "print(factorial(5))\n",
    "logging.debug('End of program')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f0c709bd-8582-4017-890b-fd1413e81f26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current folder: C:\\Users\\PRIYANKA M\\APP\n",
      "Check myProgramLog.txt\n"
     ]
    }
   ],
   "source": [
    "# Logging to a File\n",
    "import os\n",
    "import logging\n",
    "\n",
    "print(\"Current folder:\", os.getcwd())   # Get Current Working Directory\n",
    "\n",
    "logging.basicConfig(\n",
    "    filename=\"myProgramLog.txt\",\n",
    "    level=logging.DEBUG,\n",
    "    format=\"%(asctime)s - %(levelname)s - %(message)s\",\n",
    "    force=True\n",
    ")\n",
    "\n",
    "logging.debug(\"Program started\")\n",
    "logging.info(\"Student data loaded\")\n",
    "logging.warning(\"Low attendance\")\n",
    "logging.error(\"Unable to open file\")\n",
    "\n",
    "print(\"Check myProgramLog.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "92bdaf95-4b6a-4f0d-b34f-1117590e3266",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Disabling Logging\n",
    "\n",
    "import logging\n",
    "logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')\n",
    "logging.critical('Critical error! Critical error!')\n",
    "\n",
    "logging.disable(logging.CRITICAL)\n",
    "logging.critical('Critical error! Critical error!')\n",
    "logging.error('Error! Error!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "e5abba2c-c342-45f3-8bdb-77dabd7e17c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "INFO: Calculating student average\n",
      "DEBUG: Received marks: [80, 90, 75]\n",
      "DEBUG: Total marks: 245\n",
      "INFO: Program execution completed\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average = 81.66666666666667\n"
     ]
    }
   ],
   "source": [
    "# Grade calculation using logging, assert, and exceptions\n",
    "\n",
    "import logging\n",
    "\n",
    "logging.basicConfig(level=logging.DEBUG, format=\"%(levelname)s: %(message)s\")\n",
    "\n",
    "def calculate_average(marks):\n",
    "    logging.debug(f\"Received marks: {marks}\")\n",
    "    assert len(marks) > 0, \"Marks list cannot be empty\"\n",
    "    total = sum(marks)\n",
    "    logging.debug(f\"Total marks: {total}\")\n",
    "    average = total / len(marks)\n",
    "    return average\n",
    "\n",
    "try:\n",
    "    marks = [80, 90, 75]\n",
    "    logging.info(\"Calculating student average\")\n",
    "    average = calculate_average(marks)\n",
    "    print(\"Average =\", average)\n",
    "\n",
    "except AssertionError as error:\n",
    "    logging.error(error)\n",
    "\n",
    "except Exception as error:\n",
    "    logging.critical(error)\n",
    "\n",
    "finally:\n",
    "    logging.info(\"Program execution completed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9099a28e-bd91-4c45-9c3f-e340d6a7fc34",
   "metadata": {},
   "outputs": [],
   "source": [
    "6. breakpoint - allows you to pause your program at a specific line so you can inspect variables, \n",
    "evaluate expressions, and step through execution line by line"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a1f92385-0cba-4520-9321-f84926c4fbb8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Halfway done!\n",
      "Heads came up 494 times.\n"
     ]
    }
   ],
   "source": [
    "# breakpoint\n",
    "\n",
    "import random\n",
    "\n",
    "heads = 0\n",
    "for i in range(1, 1001):\n",
    "    if random.randint(0, 1) == 1:   # ❶ possible breakpoint\n",
    "        heads = heads + 1\n",
    "        breakpoint()\n",
    "    if i == 500:                    # ❷ possible breakpoint\n",
    "        print('Halfway done!')\n",
    "        breakpoint()\n",
    "print('Heads came up ' + str(heads) + ' times.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6daaa1b0-3cfa-4fa7-b909-013b20bcd5b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "7. Python Debugger (pdb)\n",
    "Python provides a built-in debugger called pdb.\n",
    "\n",
    "It allows the programmer to:\n",
    "- Pause program execution\n",
    "- Execute the program step by step\n",
    "- Inspect variable values\n",
    "- Check program flow\n",
    "- Identify logical errors\n",
    "\n",
    "Some useful commands are:\n",
    "| Command      | Meaning               |\n",
    "| ------------ | --------------------- |\n",
    "| `n`          | Execute next line     |\n",
    "| `s`          | Step into a function  |\n",
    "| `c`          | Continue execution    |\n",
    "| `p variable` | Print variable value  |\n",
    "| `l`          | Show surrounding code |\n",
    "| `q`          | Quit debugger         |\n",
    "| `w`          | Display call stack    |\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0f1a0b79-d854-403a-a9ad-360f7ec28c5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average = 25.0\n",
      "--Call--\n",
      "> \u001b[32mc:\\users\\priyanka m\\anaconda3\\envs\\boneage\\lib\\site-packages\\ipython\\core\\displayhook.py\u001b[39m(\u001b[92m269\u001b[39m)\u001b[36m__call__\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[32m    267\u001b[39m         self._is_active = \u001b[38;5;28;01mFalse\u001b[39;00m\n",
      "\u001b[32m    268\u001b[39m \n",
      "\u001b[32m--> 269\u001b[39m     \u001b[38;5;28;01mdef\u001b[39;00m __call__(self, result=\u001b[38;5;28;01mNone\u001b[39;00m):\n",
      "\u001b[32m    270\u001b[39m         \"\"\"Printing with history cache management.\n",
      "\u001b[32m    271\u001b[39m \n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "ipdb>  c\n"
     ]
    }
   ],
   "source": [
    "# Average of number inspected by pdb - execute in VS Code\n",
    "\n",
    "import pdb\n",
    "\n",
    "numbers = [10, 20, 30, 40]\n",
    "\n",
    "total = 0\n",
    "for number in numbers:\n",
    "    total += number\n",
    "average = total / len(numbers)\n",
    "\n",
    "print(\"Average =\", average)\n",
    "pdb.set_trace()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5a21f1ab-399f-4cad-b1f9-53832b00f87d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81.66666666666667\n",
      "--Call--\n",
      "> \u001b[32mc:\\users\\priyanka m\\anaconda3\\envs\\boneage\\lib\\site-packages\\ipython\\core\\displayhook.py\u001b[39m(\u001b[92m269\u001b[39m)\u001b[36m__call__\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[32m    267\u001b[39m         self._is_active = \u001b[38;5;28;01mFalse\u001b[39;00m\n",
      "\u001b[32m    268\u001b[39m \n",
      "\u001b[32m--> 269\u001b[39m     \u001b[38;5;28;01mdef\u001b[39;00m __call__(self, result=\u001b[38;5;28;01mNone\u001b[39;00m):\n",
      "\u001b[32m    270\u001b[39m         \"\"\"Printing with history cache management.\n",
      "\u001b[32m    271\u001b[39m \n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "ipdb>  w\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[31m    [... skipping 21 hidden frame(s)]\u001b[39m\n",
      "None\n",
      "  \u001b[32mc:\\users\\priyanka m\\appdata\\local\\temp\\ipykernel_14536\\1330838943.py\u001b[39m(\u001b[92m14\u001b[39m)\u001b[36m<module>\u001b[39m\u001b[34m()\u001b[39m\n",
      "> \u001b[32mc:\\users\\priyanka m\\anaconda3\\envs\\boneage\\lib\\site-packages\\ipython\\core\\displayhook.py\u001b[39m(\u001b[92m269\u001b[39m)\u001b[36m__call__\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[32m    267\u001b[39m         self._is_active = \u001b[38;5;28;01mFalse\u001b[39;00m\n",
      "\u001b[32m    268\u001b[39m \n",
      "\u001b[32m--> 269\u001b[39m     \u001b[38;5;28;01mdef\u001b[39;00m __call__(self, result=\u001b[38;5;28;01mNone\u001b[39;00m):\n",
      "\u001b[32m    270\u001b[39m         \"\"\"Printing with history cache management.\n",
      "\u001b[32m    271\u001b[39m \n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "ipdb>  q\n"
     ]
    }
   ],
   "source": [
    "# Calculate grade inspected by pdb - execute in VS Code\n",
    "\n",
    "import pdb\n",
    "def calculate_grade(marks):\n",
    "    percentage = calculate_percentage(marks)\n",
    "    return percentage\n",
    "\n",
    "def calculate_percentage(marks):\n",
    "    total = sum(marks)\n",
    "    return total / len(marks)\n",
    "\n",
    "marks = [80, 90, 75]\n",
    "\n",
    "print(calculate_grade(marks))\n",
    "\n",
    "pdb.set_trace()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb64f47c-e0e3-4d73-9687-045a39da59f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "Scenario: Debugging a Coin-Toss Game\n",
    "\n",
    "You are developing a Coin Toss Prediction Game for an online gaming application. \n",
    "The program asks the player to predict whether a randomly tossed coin will result in heads or tails.\n",
    "\n",
    "The application is giving unexpected results during testing. \n",
    "As a programmer, you need to use Python debugging techniques to examine the program execution, \n",
    "identify the values of variables at runtime, and verify that the game logic is working correctly.\n",
    "\n",
    "Debugging Techniques Demonstrated Technique\tApplication in the scenario\n",
    "Breakpoint\tbreakpoint() pauses execution\n",
    "Variable inspection\tp guess, p toss, p result\n",
    "Type inspection\tp type(guess)\n",
    "Step execution\tn executes the next statement\n",
    "Continue\tc resumes execution\n",
    "Logical debugging\tVerify result == guess\n",
    "Runtime analysis\tObserve randomly generated values"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
