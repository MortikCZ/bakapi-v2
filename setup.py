from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bakapiv2',
    version='0.2',
    url='https://github.com/MortikCZ/bakapi-v2',
    project_urls = {
        "Documentation": "https://github.com/MortikCZ/bakapi-v2/blob/main/README.md",
        "Source Code": "https://github.com/MortikCZ/bakapi-v2/blob/main/bakapi-v2.py",
        "Issues"    : "https://github.com/MortikCZ/bakapi-v2/issues"
    },
    author='Lukáš S.',
    description='Klient k API Bakalářů v jazyce Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),    
    install_requires=['requests'],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Czech",
    ],
)