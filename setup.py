import os
import re

from setuptools import setup

HERE = os.path.dirname(os.path.abspath(__file__))


def get_version():
    filename = os.path.join(HERE, 'flask_basicauth.py')
    contents = open(filename).read()
    pattern = r"^__version__ = '(.*?)'$"
    return re.search(pattern, contents, re.MULTILINE).group(1)


setup(
    name='Flask-BasicAuth',
    version=get_version(),
    url='https://github.com/jpvanhal/flask-basicauth',
    license='BSD',
    author='Janne Vanhala',
    author_email='janne.vanhala@gmail.com',
    description='HTTP basic access authentication for Flask.',
    long_description=(
        open('README.rst').read() + '\n\n' +
        open('CHANGES.rst').read()
    ),
    py_modules=['flask_basicauth'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    test_suite='test_basicauth.suite',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
