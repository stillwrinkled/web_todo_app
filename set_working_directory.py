import os

def set_working_directory():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_directory)
