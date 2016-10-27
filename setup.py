from setuptools import find_packages, setup
from channels_api import __version__

setup(
    name='channels_api',
    version=__version__,
    url='https://github.com/chiora93/channels-api',
    author='Simone Chiorazzo',
    author_email='chiora93@gmail.com',
    description="Helps build a RESTful API on top of WebSockets using channels.",
    long_description=open('README.rst').read(),
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.8',
        'channels>=0.14',
        'djangorestframework>=3.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
