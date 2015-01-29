#!/usr/bin/python

fd = open("/etc/passwd", "r")

cadenas = fd.readlines()

dicc_lista = {}

for cadena in cadenas:
    particion = cadena.split(":")
    identificador = particion[0]
    shell = particion[-1][:-1]
    dicc_lista[identificador] = shell

print dicc_lista["root"]

try:
    print dicc_lista["imaginario"]
except KeyError:
    print "No se encuentra el identificador"
