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
        "click" == "8.1.3",
        "colorama" == "0.4.6",
        "dnspython" == "2.3.0",
        "flask" == "2.2.3",
        "flask-cors" == "3.0.10",
        "itsdangerous" == "2.1.2",
        "jinja2" == "3.1.2",
        "markupsafe" == "2.1.2",
        "pymongo" == "4.3.3",
        "six" == "1.16.0",
        "werkzeug" == "2.2.3",
    ],
)
