from setuptools import setup, find_packages

setup(
    name='ufwmanager',
    version='0.1.0',
    description='UFW Manager tool with JSON database',
    author='Aahil Shaikh',
    author_email='aahils2019@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,  # makes sure db.json is included
    install_requires=[],        # add dependencies here
    entry_points={
        'console_scripts': [
            'ufwmanager=tool:main',  # calls main() in src/tool.py
        ],
    },
    python_requires='>=3.8',
)
