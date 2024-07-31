from setuptools import setup, find_packages

setup(
    name='dnd-firefly',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
    ],
    entry_points={
        'console_scripts': [
            'dnd_firefly=firefly.upload:main',
        ],
    },
)