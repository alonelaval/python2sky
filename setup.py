# -*- coding:utf-8 -*-
# author：huawei


from setuptools import setup, find_packages

packages = ['python2sky']

install_requires = ["grpcio", "grpcio-tools"]

test_requirements = [
    'pytest-httpbin==0.0.7',
    'pytest-cov',
    'pytest-mock',
    'pytest-xdist',
    'PySocks>=1.5.6, !=1.5.7',
    'pytest>=3'
]

setup(
    name="python2sky",
    version="0.2.2",
    keywords=("skywalking", "agent", "skywalking aget", "apm", "trace", "distributed trace"),
    description="skywalking agent for python",
    long_description="apm agent",
    license="apache Licence",

    url="https://github.com/alonelaval/python2sky",
    author="huawei",
    author_email="120huawei@163.com",

    include_package_data=True,
    platforms="any",
    packages=find_packages(exclude=['tests', 'test.*']),
    install_requires=install_requires

)
