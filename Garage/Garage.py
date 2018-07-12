#!/usr/local/bin/python3 python3
# -*- coding: utf-8 -*-

class Garage:
    """
    Garage dans lequel sont stockées toutes les voitures que l'on créé.
    Les voitures sont représentées par une liste de Véhicules.

    La classe Garage permet de :

        - Connaître quelles voitures sont contenues dans le garage ainsi que
        leurs caractéristiques.
        - Ajouter un véhicule aux voitures déjà existantes.
    """

    def __init__(self):
        self.garage = []

    def __repr__(self):
        if not self.garage:
            return("Le garage est vide ")
        else:
            return("La liste contient \n{}".format(self.garage))

    def __str__(self):
        print(repr(self))

    def add(self, voiture):
        #Faire une vérification sur le type d'objet ajouté.
        self.garage.append(voiture)
        return self.garage
