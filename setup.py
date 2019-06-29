from setuptools import setup, find_packages

setup(
    name='qt_utils',
    version="0.6",
    description='PyQt5 helpers, qtDesigner helpers',
    author = 'Tim Olson',
    author_email = 'tim.lsn@gmail.com',
    packages=find_packages(),
    dependency_links=[
    #         'https://github.com/timjolson/generalutils.git'
            'https://github.com/timjolson/entrywidget.git',
            'https://github.com/timjolson/sympyentrywidget.git'
    #         'https://github.com/timjolson/adjustablewidget.git'
            ],
    install_requires=['PyQt5'],
    tests_require=['pytest'],
)
