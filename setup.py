from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Read the contents of your README.md file for the long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    # The name of your project
    name='filevault',
    
    # Version number
    version='1.0.0',
    
    # A short, one-sentence summary of the project
    description='A command-line tool for secure file encryption and decryption.',
    
    # A long description for the project, taken from the README
    long_description=long_description,
    long_description_content_type='text/markdown', # This is important for rendering on PyPI
    
    # The URL for the project's homepage
    url='https://github.com/your_username/filevault', # <-- CHANGE THIS to your GitHub URL
    
    # The name of the author
    author='Your Name', # <-- CHANGE THIS to your name
    
    # The author's email address
    author_email='your.email@example.com', # <-- CHANGE THIS to your email

    # License for the project
    license='MIT',
    
    # Automatically find all packages in the 'src' directory
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    
    # List of dependencies
    install_requires=requirements,
    
    # Define the command-line script
    entry_points={
        'console_scripts': [
            # This creates the 'filevault' command and maps it to the main function
            # in your cli.py module.
            'filevault=filevault.cli:main',
        ],
    },
    
    # Classifiers help users find your project
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'Topic :: Security :: Cryptography',
    ],
    
    # Specify the Python version required
    python_requires='>=3.8',
)
