from setuptools import setup, find_packages

# Package set-up

setup(
    name='filter_medals',
    version='0.1',
    py_modules=['filter_medals'],
    description='A command-line tool to filter countries based on medal counts',
    author='John',
    author_email='johnernest978@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'filter-medals=filter_medals:main',
        ],
    },
    install_requires=[],
    python_requires='>=3.6',
)

