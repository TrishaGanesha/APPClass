# #context manager=resource manages automatically the acquisition and release of resources. It is used with the 'with' statement in Python to ensure that resources are properly cleaned up after use, even if an error occurs.
#  #acquire resource->use resource->release resource
# file=open("file.txt", "w")  # Acquire resource (open the file)
# try:
#     file.write("Hello, World!")  # Use resource (write to the file)
# finally:
#     file.close()  # Release resource (close the file)
# with open("file.txt", "w") as file:  # Acquire resource (open the file)
#     file.write("Hello, World!")  # Use resource (write to the file)
# #why with better than try-finally?The `with` statement is generally considered better than using a `try-finally` block for resource
# # management because it is more concise and readable. It automatically handles the acquisition and release of resources, reducing the risk of errors such as forgetting to close a file or releasing a resource. Additionally, it makes the code cleaner and easier to understand, as the resource management logic is encapsulated within the `with` statement.
students = ["Alice", "Bob", "Charlie", "David"]
with open("students.txt", "w") as file:  # Acquire resource (open the file)
    for student in students:  # Use resource (write to the file)
        file.write(student + "\n")
print("Students written to file successfully.")  # Release resource (file is automatically closed)
print("file closed",file.closed)


#user defined context manager
#__enter__ and __exit__ methods are used to define a user-defined context manager in Python. The __enter__ method is called when the execution flow enters the context of the with statement, and it is responsible for acquiring the resource. The __exit__ method is called when the execution flow exits the context of the with statement, and it is responsible for releasing the resource.?
#enter uses self to refer to the instance of the class and can return a value that will be assigned to the variable specified in the with statement. The exit method also uses self to refer to the instance of the class and takes three additional arguments: exc_type, exc_value, and traceback, which provide information about any exception that may have occurred within the with block. The exit method can handle exceptions if needed, and it should return True if it has handled the exception, or False (or None) if it has not.
#def __enter__(self):  # Acquire resource (open the file)
#def __exit__(self, exc_type, exc_value, traceback):  # Release resource (close the file),exception type,exception value, traceback object

#when as is there then we have to return the value from __enter__ method and assign it to the variable specified in the with statement. If we don't use as, then we don't need to return any value from __enter__ method.
#exception raised and not handled then it will return false so change to true to handle the exception and not propagate it further. If we return True from __exit__ method, then the exception will be suppressed and not propagated further. If we return False or None, then the exception will be propagated further.
#example of user-defined context manager
def demo():
    class FileManager:
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None

        def __enter__(self):
            self.file = open(self.filename, self.mode)  # Acquire resource (open the file)
            return self.file  # Return the file object to be used in the with block

        def __exit__(self, exc_type, exc_value, traceback):
            if self.file:
                self.file.close()  # Release resource (close the file)
            if exc_type is not None:
                print(f"An exception occurred: {exc_value}")  # Handle exception if needed
                return True  # Suppress the exception
            return False  # Propagate the exception if not handled

    with FileManager("students.txt", "w") as file:  # Use user-defined context manager
        students = ["Alice", "Bob", "Charlie", "David"]
        for student in students:
            file.write(student + "\n")  # Use resource (write to the file)
    print("Students written to file successfully.")
#database context manager example
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = self.connect_to_database()  # Acquire resource (connect to the database)
        return self.connection  # Return the connection object to be used in the with block

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.close_connection()  # Release resource (close the database connection)
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")  # Handle exception if needed
            return True  # Suppress the exception
        return False  # Propagate the exception if not handled

    def connect_to_database(self):
        print(f"Connecting to database: {self.db_name}")
        return f"Connection to {self.db_name}"

    def close_connection(self):
        print(f"Closing connection to database: {self.db_name}")
    