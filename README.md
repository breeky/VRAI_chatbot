# VRAI_chatbot
Projet de chatbot pour l'électif Creation de startup de haute technologie. 
Ce projet se fonde en grande partie sur le projet DeepQA disponible ici : https://github.com/Conchylicultor/DeepQA

Fonctionnement : on pose une question au chatbot, s'il connait la réponse il la donne,
sinon il donne une réponse avec l'algorithme de deep-learning. La réponse est disponible en 
ligne de code dans la console ou en vocal avec le fichier 'output.wav'.

Pour les réponses programmable, on utilise un bot dialogflow.
Pour les autres réponses, on utilise le bot du projet DeepQA.

Pour utiliser ce projet aller dans le fichier Rules.py puis insérer votre hash permettant d'accéder 
aux services de google (DialogFlow et GoogleSpeech) aux lignes contenant 'INSERT_YOUR_HASH_HERE' (modifier également 'CODE' ligne 35)
Verifiez le renvoi au bon bot dialogFlow et configurez le.

Pour le lancer tapez dans une console :
python ".../main.py" --modelTag pretrainedv2 --test interactive
