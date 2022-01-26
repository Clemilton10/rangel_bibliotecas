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
    version='0.3.3',
    description='Bibliotecas Rangel',
    long_description = 'Várias Bibliotecas pra faciliar o dia a dia',
    author='Clemas',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    url = 'https://github.com/Clemilton10/rangel_bibliotecas',
    project_urls = {
        'Código fonte': 'https://github.com/Clemilton10/rangel_bibliotecas',
        'Download': 'https://github.com/Clemilton10/rangel_bibliotecas/rangel_0.3.3.zip'
    },
    keywords = 'Bibliotecas úteis para o dia a dia',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ],
)