from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='rec_data',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='Compiling recreation data from various sources and pushing into a complete source.',
    long_description=long_description,
    author='Joel McCune',
    license='Apache 2.0',
)
