# Guide Complet d'Installation et d'Exécution pour le Projet SOA

## Prérequis
Assurez-vous que votre machine dispose de suffisamment de ressources (RAM, espace disque, etc.) pour exécuter les outils suivants.

## Installation des Outils

### Java JDK
1. Téléchargez Java JDK depuis [Oracle JDK](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
2. Suivez les instructions d'installation pour votre système d'exploitation.

### Spring Boot
1. Assurez-vous que Java JDK est installé et configuré.
2. Téléchargez et installez Spring Tools 4 pour Eclipse ou votre IDE préféré depuis [Spring Tools 4](https://spring.io/tools).

### Angular
1. Installez Node.js depuis [Node.js](https://nodejs.org/).
2. Ouvrez un terminal et exécutez `npm install -g @angular/cli`.

### MySQL
1. Téléchargez et installez MySQL depuis [MySQL Community Server](https://dev.mysql.com/downloads/mysql/).
2. Configurez MySQL avec un utilisateur et une base de données pour votre projet.

### MuleSoft
1. Créez un compte sur [Anypoint Platform](https://anypoint.mulesoft.com/login/).
2. Téléchargez Anypoint Studio depuis votre compte Anypoint.

### Python
1. Téléchargez et installez Python depuis [Python.org](https://www.python.org/downloads/).
2. Assurez-vous d'ajouter Python à votre variable d'environnement PATH.

### Postman
1. Téléchargez et installez Postman depuis [Postman](https://www.postman.com/downloads/).

## Configuration du Projet

1. **Spring Boot** : Ouvrez le projet dans votre IDE et assurez-vous que toutes les dépendances Maven sont correctement résolues.
2. **Angular** : Naviguez vers le dossier du projet Angular et exécutez `npm install` pour installer les dépendances.
3. **MySQL** : Créez la base de données et les tables nécessaires en utilisant le script SQL fourni dans le projet, nom de la base de données= soa,user=root,password=root.
4. **MuleSoft** : Ouvrez Anypoint Studio et configurez votre environnement de travail.

## Exécution du Code

### Avec MuleSoft

1. **Installer ou Compresser les codes sources SpringBoot et Python** :
    - Lancez le code spring boot dans intellij et assurer que l'exécurion est bien dur le port 9090.
    - De meme,Ouvrez le code python dans visual Studio code et exécuter après l'installation des libraries et s'assurer qu'im marche sur le port 5000.

2. **Ouvrir le Projet dans Anypoint Studio** :
   - Lancez Anypoint Studio.
   - Importez votre projet Mule dans l'IDE.
3. **Configurer l'Environnement d'Exécution** :
   - Allez dans les paramètres du projet.
   - Configurez les propriétés requises, comme les points de terminaison et les informations de base de données.
4. **Exécuter le Projet** :
   - Cliquez sur le bouton 'Run' pour démarrer votre application Mule.
   - Vérifiez la console pour s'assurer que l'application démarre sans erreurs.



### Angular
Dans le terminal, naviguez vers le dossier du projet Angular et exécutez `ng serve`.

## Test avec Postman
- Importez la collection de requêtes Postman fournies avec le projet.
- Testez les différents endpoints de l'API; http://localhost:8086/users/mule un exemple pour consulter les users de notre BD.


## NB:
Vous trouverez les liens vers le code source de notre projet dans le rapport. 
