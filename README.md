# Projet 4 - Développez un programme logiciel en Python - OpenClassrooms

## Mise en place du projet:

#### I) Windows :
Dans Windows Powershell, naviguer vers le dossier souhaité.

###### - Récupération du projet

    $ git clone https://github.com/Appryll/Projet4-Developpez-un-programme-logiciel-en-Python.git

###### - Activer l'environnement virtuel
    $ cd Projet4-Developpez-un-programme-logiciel-en-Python 
    $ python -m venv env 
    $ ~env\scripts\activate
    
###### - Installer les paquets requis
    $ pip install -r requirements.txt

###### - Lancer le programme
    $ python main.py

###### - Quitter l'envirement virtuel
    deactivate

-----
#### II) MacOS, Linux :
Dans le terminal, naviguer vers le dossier souhaité.

###### - Récupération du projet

    $ git clone https://github.com/Appryll/Projet4-Developpez-un-programme-logiciel-en-Python.git

###### - Activer l'environnement virtuel
    $ cd Projet4-Developpez-un-programme-logiciel-en-Python 
    $ python3 -m venv env 
    $ source env/bin/activate
    
###### - Installer les paquets requis
    $ pip install -r requirements.txt

###### - Lancer le programme
    $ python3 main.py

###### - Quitter l'envirement virtuel
    deactivate

------

#### III) Générer un rapport flake8

    $ flake8 --format=html --htmldir=flake8_rapport
