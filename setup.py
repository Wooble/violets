import os
from setuptools import setup, find_packages

version = {}  # will be set by exec below

with open(os.path.join(os.path.dirname(__file__),
                       'violets/version.py'), 'rb') as fp:
    exec(fp.read(), version)

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name='violets',
    version=version['__version__'],
    packages=find_packages(),
    author='Geoffrey Spear',
    author_email='geoffspear@gmail.com',
    url='http://violets.rtfd.org',
    description='A roguelike game engine',
    long_description=readme,
    keywords='game engine roguelike',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    install_requires=requirements,
    )
