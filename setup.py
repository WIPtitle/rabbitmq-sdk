from setuptools import setup, find_packages

setup(
    name='rabbitmq_sdk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pika',
    ],
    author='Matteo Galvagni',
    author_email='nope@mail.com',
    description='Rabbitmq sdk for projects',
    url='https://github.com/galvagnimatteo/rabbitmq-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
