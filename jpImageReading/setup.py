#pip install requests

from setuptools import setup, find_packages

setup(
    name='my_project',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.26.0',  # Ensure you have requests library installed
    ],
)
