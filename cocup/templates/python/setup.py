from setuptools import setup, find_packages

setup(
    name="{project_name}",
    version="0.0.1",
    description="{description}",
    author="{author}",
    author_email="{email}",
    packages=find_packages(),
    install_requires=[
        {requirements}
        ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "{project_name}={project_name}.main:main",
        ],
    },
)
