from setuptools import setup, find_packages

setup(
    name="cocup",
    version="0.0.1",                     
    description="Thom's COokie CUtter for Python",
    author="Thomas J. Booth",
    author_email="thoboo@biosustain.dtu.dk",
    packages=find_packages(),           
    install_requires=[],
    python_requires=">=3.10",               # Minimum Python version
    entry_points={                           # Optional CLI entry point
        "console_scripts": [
            "cocup=cocup.__main__:main",
        ],
    },
)
