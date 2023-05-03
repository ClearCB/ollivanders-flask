from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Flask API",
    version="1.0.0",
    author="ClearCB",
    author_email="abelcasasccb@gmail.com",
    description="Flask CRUD Mongo Api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ClearCB/ollivanders-flask",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "attrs==22.2.0",
        "black==23.1.0",
        "cachetools==5.3.0",
        "chardet==5.1.0",
        "click==8.1.3",
        "colorama==0.4.6",
        "coverage==7.2.2",
        "distlib==0.3.6",
        "dnspython==2.3.0",
        "exceptiongroup==1.1.1",
        "filelock==3.10.7",
        "flask==2.2.5",
        "flask-cors==3.0.10",
        "iniconfig==2.0.0",
        "itsdangerous==2.1.2",
        "jinja2==3.1.2",
        "markupsafe==2.1.2",
        "mypy-extensions==1.0.0",
        "packaging==23.0",
        "pathspec==0.11.1",
        "platformdirs==3.2.0",
        "pluggy==1.0.0",
        "pymongo==4.3.3",
        "pyproject-api==1.5.1",
        "pytest==7.2.2",
        "six==1.16.0",
        "tomli==2.0.1",
        "tox==4.4.7",
        "virtualenv==20.21.0",
        "werkzeug==2.2.3",
    ],
)
