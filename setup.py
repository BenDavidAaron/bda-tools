import datetime
from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

now = datetime.datetime.now()

setup(
    name="bda_tools",  # Required
    version=f"{now.year}.{now.month}.{now.month}",
    description='Minor tools not worth packaging individually',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/BenDavidAaron/bda-tools',
    author='Ben Aaron',
    classifiers=[ 
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    python_requires='>=3.7, <4',
    extras_require={  # Optional
        'test': ['pytest'],
    }
)
