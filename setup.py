from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests==2.36.0',
        'numpy==2.4.5',
        'pandas==3.0.3',
    ],
)