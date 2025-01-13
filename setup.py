from setuptools import setup, find_packages

setup(
    name='SleepSecurity',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A security monitoring and device hardening tool.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ColDog-Studios/Sleep-Security',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6, <4',
)