from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    README = fh.read()


setup(
    name='django-q-sentry',
    version='0.2.0',
    author='Daniel Welch, Christo Goosen',
    author_email='dwelch2102@gmail.com, christogoosen@gmail.com',
    keywords='django distributed task queue worker scheduler cron redis disque ironmq sqs orm mongodb multiprocessing sentry',
    packages=find_packages(include=['django-q-sentry'], exclude=['.venv', 'dist','build', 'django-q-sentry*egg-info']),
    install_requires=['sentry-sdk>=2.0.0'],
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
