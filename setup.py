# pip3 install wheel

# 1- Para testar
# python setup.py pytest

# 2- Para renderizar
# python setup.py bdist_wheel

# 3- para instalar
# pip install rangel.whl

from setuptools import find_packages, setup
setup(
    name='rangel',
    packages=find_packages(),
    version='0.1.3',
    description='Bibliotecas Rangel',
    author='Clemas',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)