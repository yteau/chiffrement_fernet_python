from cryptography.fernet import Fernet

# Génération d'une clé de chiffrement aléatoire
cle = Fernet.generate_key()

# Création d'un objet de chiffrement avec la clé générée
crypteur = Fernet(cle)

# Message à chiffrer
message = "Ceci est un message secret."

# Chiffrement du message
message_chiffre = crypteur.encrypt(message.encode())

# Affichage du message chiffré
print("Message chiffré : ", message_chiffre)

# Déchiffrement du message
message_dechiffre = crypteur.decrypt(message_chiffre)

# Affichage du message déchiffré
print("Message déchiffré : ", message_dechiffre.decode())

""" Exemple simple de chiffrement de bout en bout en utilisant la bibliothèque de chiffrement cryptography de Python.
Dans cet exemple, nous générons une clé de chiffrement aléatoire avec Fernet.generate_key() qui crée une clé de 32 octets.

Ensuite, nous créons un objet de chiffrement crypteur avec la clé générée, en utilisant la méthode Fernet(cle).

Nous définissons ensuite notre message à chiffrer dans la variable message.

Nous chiffrons le message en utilisant la méthode encrypt() de l'objet crypteur. Cette méthode prend une chaîne de caractères encodée en entrée et renvoie la chaîne chiffrée.

Nous affichons le message chiffré en utilisant print("Message chiffré : ", message_chiffre).

Nous déchiffrons le message chiffré en utilisant la méthode decrypt() de l'objet crypteur. Cette méthode prend une chaîne chiffrée encodée en entrée et renvoie la chaîne déchiffrée.

Enfin, nous affichons le message déchiffré en utilisant print("Message déchiffré : ", message_dechiffre.decode()).

NB : pour un chiffrement de bout en bout, les clés de chiffrement doivent être connues uniquement des parties concernées. Dans cet exemple, la clé est générée aléatoirement et n'est pas partagée entre les parties. Dans une situation réelle, les clés seraient échangées entre les parties à l'aide d'un protocole de communication sécurisé. """