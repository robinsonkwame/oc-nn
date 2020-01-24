from setuptools import find_packages, setup

setup(
    name='ocnn',
    version='0.0.2',
    description="One class neural networks for Anomaly detection",
    long_description_content_type='text/markdown',
    author="Raghavendra Chalapathy, Kwame Porter Robinson",
    author_email='kwamepr@umich.edu',
    url='https://github.com/robinsonkwame/oc-nn',
    packages=find_packages(include=['src*']),
    include_package_data=True,
    license="BSD license"
)
