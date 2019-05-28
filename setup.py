from setuptools import setup, find_packages

setup(
    name='qt_utils',
    version="0.6",
    description='PyQt5 helpers, qtDesigner helpers',
    author = 'Tim Olson',
    author_email = 'timjolson@user.noreplay.github.com',
    packages=find_packages(),
    install_requires=['PyQt5'],
    tests_require=['pytest'],
)