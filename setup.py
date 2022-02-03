# py -m pip3 install wheel
# py -m pip install twine

# 1- Para testar
# py setup.py pytest

# 2- Para renderizar
# py setup.py bdist_wheel

# 2b- Renderizar zip
# py setup.py sdist

# 3- para instalar
# py -m pip install rangel.whl

# 4- enviar
# py -m twine upload dist/* --repository-url https://test.pypi.org/legacy/ --verbose --user Clemas --password klemas277908
# py -m twine upload dist/* --repository-url https://upload.pypi.org/legacy/ --verbose --user Clemas --password klemas277908

# twine upload -u Clemas -p klemas277908 --repository-url https://upload.pypi.org/legacy/ dist/*

from setuptools import find_packages, setup
setup(
	name='rangel',
	packages=find_packages(),
	version='0.3.9',
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
		'Download': 'https://github.com/Clemilton10/rangel_bibliotecas/rangel_0.3.9.zip'
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