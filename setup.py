import os
from setuptools import setup


with open("README.md", "r") as fh:
    README = fh.read()


setup(
    name='django-q-sentry',
    version='0.1.5',
    author='Daniel Welch, Christo Goosen',
    author_email='dwelch2102@gmail.com, christogoosen@gmail.com',
    keywords='django distributed task queue worker scheduler cron redis disque ironmq sqs orm mongodb multiprocessing sentry',
    packages=['django_q_sentry'],
    install_requires=['sentry-sdk>=0.16.5'],
    url='https://django-q.readthedocs.org',
    license='MIT',
    description='A Sentry support plugin for Django Q',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
