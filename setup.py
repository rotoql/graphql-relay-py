from setuptools import setup, find_packages


tests_require = [
    'pytest>=3.0',
]
dev_require = [] + tests_require

setup(
    name='graphql-relay',
    version='0.4.5',

    description='Relay implementation for Python',
    long_description=open('README.rst').read(),

    url='https://github.com/graphql-python/graphql-relay-py',

    author='Syrus Akbary',
    author_email='me@syrusakbary.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    keywords='api graphql protocol rest relay',

    packages=find_packages(exclude=['tests']),

    install_requires=[
        'six>=1.10.0',
        'graphql-core>=0.5.0,<3',
        'promise>=0.4.0'
    ],
    tests_require=tests_require,
    extras_require={
        'dev': dev_require
    },
)
