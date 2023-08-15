from setuptools import setup, find_packages

setup(
    name='ofertas',
    version='0.1',
    description='Programa para obtener ofertas de videojuegos de la pagina de Eneba',
    author='Naras',
    author_email='naraspjp@outlook.com',
    url='https://github.com/naraspjp/ofertas',
    packages=find_packages(),
    install_requires=['request', 'bs4', 'pandas'],
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)