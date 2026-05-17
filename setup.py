from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'requests',
        'numpy>=1.21.0',
        'pandas',
    ],
)