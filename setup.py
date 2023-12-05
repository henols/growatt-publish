from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[open('requirements.txt').read().splitlines()],
    # Other metadata like author, description, etc.
)
