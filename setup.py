from setuptools import setup, find_packages


setup(
    name='qt_utils',
    version="0.6",
    description='PyQt5 helpers and widgets, qtDesigner helpers',
    author = 'Tim Olson',
    author_email = 'tim.lsn@gmail.com',
    packages=find_packages(),
    install_requires=['PyQt5'],
    tests_require=['pytest'],
)
