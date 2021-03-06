#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        liste_saisie = []
        while len(liste_saisie) < 10:
            liste_saisie.append(int(input('saisir un nombre entier'))
        reponse = True
            for element in range(length(liste_saisie)):
                if element <= element+1
                    continue
                else 
                    reponse = False
                    break
        return reponse


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        word1 = input('saisir le premier mot')
        word2 = input('saisir le deuxième mot')
        if len(word1) == len(word2):
            word1 = list[word1]
            word2 = list[word2]
            for letter in rang(len(word1)):
                if letter in word2:
                    word2.remove(letter)
                else:
                    break
    return len(word2) == 0


def contains_doubles(items: list) -> bool:
    return len(items) == len(set(items))


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres
    sentence_set = set(sentence)
    resultat = {}
        for letter in sentence_set:
            resultat[lettre] = sentence.count(lettre)
    return resultat


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
