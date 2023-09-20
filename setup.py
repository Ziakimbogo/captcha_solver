from setuptools import setup, find_packages

setup(
    name='captcha_solver',
    version='1.0',
    author='Ziakimbogo',
    author_email='ziakimbogo@hotmail.com',
    description=''' 
    
# Projet de Sauvegarde de Données sur Cloud avec PyPy

## Introduction

captcha-resolver : La solution optimale pour déjouer les CAPTCHAs

Élaboré avec précision et rigueur, le « captcha-resolver » est un outil développé en Python s’appuyant sur la bibliothèque Selenium. Il incarne la solution parfaite pour les professionnels et les amateurs cherchant à automatiser le processus de résolution des CAPTCHAs. Voici quelques caractéristiques saillantes de cet outil :

## Caractéristiques

Détection intelligente: Grâce à l'utilisation de techniques d'apprentissage profond (deep learning), il peut interpréter et résoudre les CAPTCHAs les plus complexes avec une précision remarquable.
Intégration avec Selenium: L'outil s'intègre de manière fluide avec Selenium, permettant une automatisation cohérente et efficace du processus de navigation et de résolution des CAPTCHAs.
Polyvalence: Conçu pour s'attaquer à une variété de CAPTCHAs, y compris ceux basés sur des images et des textes, offrant ainsi une polyvalence inégalée.
Avantages
Gain de temps: En automatisant la résolution des CAPTCHAs, vous économisez un temps précieux qui peut être mieux utilisé ailleurs.
Précision: Grâce à l'intelligence artificielle et à l'apprentissage profond, vous bénéficiez d'un taux de succès élevé, réduisant ainsi les chances d'échec.
Cas d'utilisation
Développement web: Les développeurs web peuvent l'intégrer dans leurs processus de test pour automatiser la vérification des fonctionnalités de sécurité des sites web.
Recherche académique: Les chercheurs peuvent l'utiliser pour faciliter la collecte de données à grande échelle en automatisant la traversée des barrières CAPTCHAs.
Configuration et mise en marche faciles
La mise en route est un jeu d'enfant, grâce à une documentation complète qui guide les utilisateurs à travers chaque étape du processus d'installation et de configuration. De plus, une communauté active est à votre disposition pour répondre à toutes vos questions et vous aider à résoudre les éventuels problèmes.

En conclusion, le « captcha-resolver » est non seulement un outil puissant, mais aussi une innovation qui promet de transformer l'industrie en offrant une solution automatisée, rapide et fiable pour la résolution des CAPTCHAs. Ne manquez pas l'opportunité de faciliter votre travail et de gagner en efficacité avec le « captcha-resolver ».

## Prérequis

Avant de commencer, assurez-vous de satisfaire aux prérequis suivants :

- **PyPy** : Installez la dernière version de PyPy (version 3.x recommandée). [Voir la documentation de PyPy pour les instructions d'installation](https://www.pypy.org/)

## Installation

1. **Clonage du répertoire** : Clonez ce répertoire sur votre machine locale :
   
   ```sh
   git clone https://github.com/Ziakimbogo/captcha_solver.git

This project is licensed under the MIT License. For more details, please see the included LICENSE file.
    ''',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ziakimbogo/captcha_solver.git',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'shutil',
        'requests',
        'cv2', 
        're', 
        'numpy', 
        'ultralytics'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
