#############################################
# File Name: setup.py
# Author: helailiang
# Mail: helailiang@reddatetech.com
# Created Time:  2020-04-26 01:25:34 AM
#############################################


from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name = "bsn_sdk_py",
    version = "1.0.1",
    keywords = ("bsn","区块链", "北京红枣", "bsn_sdk_py"),
    description = "这是bsn sdk",
    long_description = long_description,
    long_description_content_type="text/markdown",
    license = "MIT Licence",
    url = "https://github.com/helailiang/bsn-sdk-python",
    author = "helailiang",
    author_email = "helailiang@reddatetech.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    python_requires='>=3.6',
    install_requires = ['hkdf==0.0.3','cryptography==3.2','fabric-sdk-py==0.8.1']
)