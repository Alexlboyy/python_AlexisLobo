import socket
import platform #Permet d'obtenir des informations sur le systeme d'explotation

hostname = socket.gethostname()
adresse_ip = socket.gethostbyname(hostname)
py_ver = platform.python_version()
proc = platform.processor()

print("================INFORMATION================")
print("Le nom de la machine :" + " " + hostname)
print("============================================")
print("L'adresse IP de la machine : " + adresse_ip)
print("============================================")
print("La version du Python : " + "Python " + py_ver)
print("============================================")
print("Votre processeur : " + proc)
print("============================================")

print("test de sauvegarde)")