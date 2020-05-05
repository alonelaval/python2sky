# -*- coding:utf-8 -*-
# author：huawei


from setuptools import setup, find_packages




packages = ['python2sky']

requires =["grpcio==1.28.1","grpcio-tools==1.28.1"]

test_requirements = [
    'pytest-httpbin==0.0.7',
    'pytest-cov',
    'pytest-mock',
    'pytest-xdist',
    'PySocks>=1.5.6, !=1.5.7',
    'pytest>=3'
]

setup(
    name = "python2sky",
    version = "0.1.1",
    keywords = ("skywalking","agent","skywalking aget","apm","trace","distributed trace"),
    description = "skywalking agent for python",
    long_description = "apm agent",
    license = "apache Licence",

    url = "https://github.com/alonelaval/python2sky",
    author = "huawei",
    author_email = "120huawei@163.com",

    packages = packages,
    include_package_data = True,
    platforms = "any",
    install_requires = requires,


)
