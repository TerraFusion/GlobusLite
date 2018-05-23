from setuptools import setup, find_packages

setup(
    name='globuslite',
    version='0.1.0',
    author='Landon T. Clipp',
    author_email='clipp2@illinois.edu',
    packages=find_packages(),
    description='A lite Python API to the Globus data transfer services.',
    long_description='globuslite provides a lightweight interface to the Globus \
    data transfer services. It abstracts the authentication flow and other \
    administrative details from the user to make interacting with the Globus \
    services seamless.',
    url = 'https://github.com/TerraFusion/globuslite',
    keywords = ['globus', 'lite', 'light', 'lightweight', 'data', 'transfer'],
)
