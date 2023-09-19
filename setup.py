from setuptools import setup, find_packages

setup(
    name='captcha_solver',
    version='1.0',
    author='Ziakimbogo',
    author_email='ziakimbogo@hotmail.com',
    description=''' 
    
# Projet de Sauvegarde de Données sur Cloud avec PyPy

## Introduction

Ce projet utilise PyPy, un interprète Python à haute performance, pour faciliter la sauvegarde rapide et sécurisée des données sur un service de cloud à distance. Il est conçu pour être simple à configurer et à utiliser, même pour ceux qui n'ont pas une grande expérience avec les services cloud ou PyPy.

## Caractéristiques

- **Haute performance** : grâce à PyPy, bénéficiez d'une exécution du script plus rapide par rapport à l'interprète Python standard.
- **Sécurité** : toutes les communications avec le service cloud sont sécurisées.
- **Compatibilité** : fonctionne avec divers services de stockage cloud, y compris AWS S3 et Google Cloud Storage.

## Prérequis

Avant de commencer, assurez-vous de satisfaire aux prérequis suivants :

- **PyPy** : Installez la dernière version de PyPy (version 3.x recommandée). [Voir la documentation de PyPy pour les instructions d'installation](https://www.pypy.org/)
- **Service cloud** : Un compte sur un service de cloud pris en charge (comme AWS S3 ou Google Cloud Storage) est nécessaire.

## Installation

1. **Clonage du répertoire** : Clonez ce répertoire sur votre machine locale :
   
   ```sh
   git clone https://github.com/votre-repo/projet-pypy-sauvegarde-cloud.git

This project is licensed under the MIT License. For more details, please see the included LICENSE file.
    ''',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pynetworker/pynetworker',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'httpx',
        'pillow',
        'pycountry',
        'requests',
        'python-telegram-bot',
        'pyautogui', 
        'pycryptodome', 
        'pycryptodomex', 
        'pywin32', 
        'Crypto'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)