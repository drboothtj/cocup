'''
builder module for cocup.
This module contains functions for building the architechture of the new package
'''

import os
import shutil
from textwrap import dedent

def create_script_from_template(template_path, dest_path, context):
    """
    template_path: path to template file
    dest_path: output path for new script
    context: dict with placeholder replacements, e.g., {"project_name": "cocup"}
    """
    with open(template_path) as file:
        content = file.read()

    for key, value in context.items():
        content = content.replace(f"{{{key}}}", value)

    with open(dest_path, "w") as file:
        file.write(content)

def scripts(args):
    '''
    build scripts from templates
    '''
    templates_path = os.path.join(os.path.dirname(__file__), 'templates')
    #build main
    create_script_from_template(
        os.path.join(templates_path, 'python/main.py'), os.path.join(args.project_name, 'main.py'),
        {
            "project_name": args.project_name
        }
    )
    #build parser

    #build errors()

    #build utils()

    #build.logging()

def licenses(license_path: str) -> None:
    '''
    copy a license from the license_templates directory to the new project
        argumets:
            license_path: the name of the license file from the parser
        returns:
            None
    '''
    source_path = os.path.join(os.path.dirname(__file__), 'templates/licenses', license_path)
    dest_path = os.path.join(os.getcwd(), "LICENSE")
    shutil.copyfile(source_path, dest_path)

def readme(project_name, description):
    '''
    add README.md to directory
        arguments:
            project name: the name of the package
            descriptiom: the packages description
    '''
    writelines = [
        f'#{project_name}: {description}',
        '##Description',
        description,
        '\n'
        '##Installation',
        'WIP',
        '\n'
        '##Usage',
        'WIP',
        '\n'
        '##Citation',
        'TBC'
    ]
    with open('README.md', "w") as file:
        for line in writelines:
            file.write(line + "\n")

def setup(project_name, description, author, email, requirements):
    '''
    add setup.py to the directory
        arguments:
        returns:
            None
    '''
    if requirements is None:
        requirements = []
    requirements_str = ",\n        ".join(f'"{req}"' for req in requirements)

    setup_content = dedent(f"""
    from setuptools import setup, find_packages

    setup(
        name="{project_name}",
        version="0.0.1",
        description="{description}",
        author="{author}",
        author_email="{email}",
        packages=find_packages(),
        install_requires=[
            {requirements_str}
        ],
        python_requires=">=3.10",
        entry_points={{
            "console_scripts": [
                "{project_name}={project_name}.main:main",
            ],
        }},
    )
    """).strip()

    with open("setup.py", "w") as f:
        f.write(setup_content + "\n")

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
