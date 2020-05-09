from setuptools import setup, find_packages


setup(
    name='qt_utils',
    version="0.6",
    description='PyQt5 helpers and widgets, qtDesigner helpers',
    author = 'timjolson',
    author_email = 'timjolson@user.noreply.github.com',
    packages=find_packages(),
    install_requires=['PyQt5==5.9'],
    tests_require=['pytest', 'pytest-qt'],
)
