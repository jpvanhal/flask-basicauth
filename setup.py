from setuptools import setup

setup(
    name='Flask-BasicAuth',
    version='0.1.0',
    url='https://github.com/jpvanhal/flask-basicauth',
    license='BSD',
    author='Janne Vanhala',
    author_email='janne.vanhala@gmail.com',
    description='HTTP basic access authentication for Flask.',
    long_description=open('README.rst').read() + '\n\n' +
                     open('CHANGES.rst').read(),
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
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
