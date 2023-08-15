# Projet 9: LitReviews - Django Web App
***

## <b>Etape 1</b>
Créez un environnement virtuel dans le répertoire local en utilisant la commande suivante dans le terminal : 
`python3 -m venv .env` 
<br>
<br>
Démarrer l'environnement virtuel : 
`source .env/bin/activate` 

---

## <b>Etape 2</b>
Initialisez un répertoire git avec à la commande `git init`


Puis clonez le répertoire distant : \
`git clone https://github.com/lisa367/OPC-Projet_9.git`

Votre répertoire local devrait désormais avoir la structure suivante : 
<pre>OPC-Projet_9/
        | .env/
        | src/
                | lit_reviews/
                        | base.py
                        | modele.py
                | reviews_app/
                        | base.py
                        | vue.py               
                | tickets_app/
                        | base.py
                        | controleur.py
                | static/
                        | css/
                            | style.css
                | media/
        | .gitignore
        | README.md
        | requirements.txt
</pre>
---

## <b>Etape 3</b>
Déplacez-vous dans le dossier OPC-Projet_9 : `cd OPC-Projet_9`
<br>
<br>
Assurez-vous que l'interpréteur Python sélectionné par votre éditeur de code est bien celui de l'environnement virtuel, puis installez les dépendences du projet grâce à la commande : \
`pip install -r requirements.txt`

---

## <b>Etape 4</b>
Déplacez-vous dans le dossier src : `cd src`
Créez, puis appliquez les migrations pour la base de données : \
`python manage.py makemigrations`
<br>
`python manage.py migrate`

---

## <b>Etape 5</b>
Enfin, lancez le serveur local : `python manage.py runserver`