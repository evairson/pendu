from flask import Flask, render_template, request, redirect, session
from pendu import Pendu
import random


# On crée l'application
app = Flask("MonApplication")
app.secret_key = "cookiesSansGluten"


#Route de base : Page d'accueil
@app.route("/")
def Accueil():
    liste_mots = ["perroquet", "chien", "chat", "poisson", "souris", "lapin", "poule", "cochon", "vache", "cheval"]
    mot = random.choice(liste_mots)

    session["etat_jeu"] = Pendu.initialiser(mot, 6)

    return redirect("/jeu")

#Route pour afficher le jeu
@app.route("/jeu")
def jeu():
    return render_template("Accueil.html", data=session["etat_jeu"])

#Route pour deviner une lettre
@app.route("/deviner", methods=["POST"])
def devine():
    input = request.form["lettre"]
    session["etat_jeu"] = Pendu.deviner(session["etat_jeu"], input)
    return redirect("/jeu")
  
# On lance l'application
app.run("0.0.0.0","5500", debug=True)