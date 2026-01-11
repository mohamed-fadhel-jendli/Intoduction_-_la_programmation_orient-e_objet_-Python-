# Importation des modules nécessaires
import os
import datetime
# Dictionnaire pour stocker les questions et réponses
reponses={}
def charger_reponses(nom_fichier="reponses.txt"):
    global reponses
    # Vérifier si le fichier existe
    if os.path.exists(nom_fichier):
        with open(nom_fichier,'r',encoding='utf-8') as f:
            for ligne in f:
                if ':' in ligne:
                    # Séparer la question et la réponse
                    q,rep=ligne.strip().split(':',1)
                    reponses[q.strip().lower()]=rep.strip()
    else:
        # Créer le fichier s'il n'existe pas
        open(nom_fichier,'w',encoding='utf-8').close()
    return reponses
def sauvegarder(q,rep,nom_fichier="reponses.txt"):
    with open(nom_fichier,'a',encoding='utf-8') as f:
        f.write(q+":"+rep+"\n")
def log_historique(q,rep):
    with open("historique.txt",'a',encoding='utf-8')as f:
        t=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{t}]{q}->{rep}\n")
def afficher_histo():
    if os.path.exists("historique.txt"):
        with open("historique.txt",'r',encoding='utf-8') as f:
            contenu=f.read()
            if contenu:
                print("\n=== HISTORIQUE ===\n"+contenu)
            else:
                print("Historique vide.")
    else:
        print("Pas d'historique.")
# Message d'accueil
print("\n=== CHATBOT INTERACTIF ===")
print("Type 'quit' pour arrêter, 'histo' pour l'historique\n")
# Charger les réponses existantes
charger_reponses()
# Boucle principale du chatbot
while True:
    user_input = input("Vous: ").strip()
    # Ignorer les entrées vides
    if not user_input:
        continue
    # Commande pour quitter
    if user_input.lower()=="quit":
        print("Au revoir!")
        break
    # Commande pour afficher l'historique
    if user_input.lower()=="histo":
        afficher_histo()
        continue
    q_lower = user_input.lower()
    # Vérifier si la question est connue
    if q_lower in reponses:
        rep=reponses[q_lower]
        print(f"Bot: {rep}\n")
        log_historique(user_input,rep)
    else:
        # Apprendre une nouvelle réponse
        rep=input("Bot: Je sais pas. Dis-moi la réponse: ").strip()
        if rep:
            reponses[q_lower]=rep
            sauvegarder(user_input,rep)
            log_historique(user_input,f"[APPRIS] {rep}")
            print("Ok, Merci!\n")
        else:
            print("Ok, pas grave.\n")
