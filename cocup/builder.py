'''
builder module for cocup.
This module contains functions for building the architechture of the new package
'''

import os

def scaffold(project_name: str) -> None:
    '''
    makes the directories for the new package
        arguments:
            project_name: the name for the new project
        returns:
            None
    '''
    print(f'make scaffold for {project_name}')
    project_dirs = [
    project_name,
    f"{project_name}/parser",
    f"{project_name}/utils",
    f"{project_name}/tests",
    "example_data/example_in",
    "example_data/example_out"
    ]

    for directory in project_dirs:
        path = os.path.join(directory)
        os.makedirs(path)
    