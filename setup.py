from setuptools import setup
from setuptools import find_packages

setup(
    name='sorl-multi-engine',
    version='0.0.1',
    url='https://github.com/jjdelc/sorl-multi-engine',
    author='jjdelc',
    author_email='jjdelc@gmail.com',
    packages=find_packages(),
    platforms='any',
    description='Allows to stack many engine processors for Sorl thumbnails',
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 1 - Planning"
        "Environment :: Web Environment"
        "Framework :: Django"
        "Intended Audience :: Developers"
        "License :: OSI Approved :: BSD License"
        "Operating System :: OS Independent"
        "Programming Language :: Python"
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content"
        "Topic :: Multimedia :: Graphics"
    ],
    install_requires=[
        'sorl-thumbnail',
    ],
)
