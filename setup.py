from setuptools import setup, find_packages
from setuptools import setup

setup(
    name='ufwmanager',
    version='0.1',
    description='UFW Manager tool with JSON database',
    author='Aahil Shaikh',
    author_email='aahils2019@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,  # includes db.json
    install_requires=[],        # add dependencies if needed
    entry_points={
        'console_scripts': [
            'ufwmanager=tool:main',  # calls main() in tool.py
        ],
    },
)
