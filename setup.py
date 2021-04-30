# coding: utf-8

"""
    BinckBank.OpenApi
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  

NAME = "swagger-client"
VERSION = "1.0.0"


REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="BinckBank.OpenApi",
    author_email="",
    url="https://github.com/Worldcycler/PyBinck",
    keywords=["Swagger", "BinckBank.OpenApi"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
      BinckBank OpenAPI is an API Platform to access BinckBank&#39;s trading services.    Curious? Request your access key after reading the documentation on Github: https://github.com/binckbank-api/client-js#binck-openapi-documentation      # noqa: E501
    """
)
