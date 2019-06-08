from setuptools import setup, find_packages

name = 'entryWidget'

import logging
logging.basicConfig(filename=f'install-{name}.log', level=logging.DEBUG)
logging.debug(find_packages())

setup(
    name=name,
    version="0.5",
    packages = find_packages(),
    install_requires = ['PyQt5'],
    dependency_links = [
        'https://github.com/timjolson/generalutils.git'
    ],
    tests_require = ['pytest', 'pytest-qt']
)
