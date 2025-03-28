## Introduction

Ce rapport présente les résultats d'un test mené afin de déterminer l'efficacité de la réécriture d'un bloc spécifique d'une newsletter pour éviter la coupure par Gmail. L'objectif est de réduire la taille de l'email tout en maintenant la qualité et l'accessibilité du contenu.

## Coupure par Gmail

Gmail coupe les emails dont la taille dépasse 102 KB. Cela entraîne l'affichage d'un message en bas de l'email indiquant que le contenu a été tronqué, ce qui peut nuire à l'expérience utilisateur. Notre objectif est de maintenir l'email en dessous de cette limite pour éviter cette coupure.

## Tests

Chaque taille de fichier est mesurée en octets et représente la taille réelle du fichier, et non sa taille sur le disque.  
Afin de gagner du temps et d'effectuer plus d'itérations, nous avons extrait un bloc de la plus grande newsletter disponible, puis nous l'avons repensé et redéveloppé pour voir si nous pouvions réduire sa taille.

Commande pour mesurer la taille du fichier :  
`stat -f "%z" [nom_du_fichier] | awk '{print $1 / 1024 " KB"}'`

| Taille du fichier | Fichier                                                                                                             | Description           | Réduction |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------- | --------- |
| 18.5977 KB        | [old.html](http://htmlpreview.github.io/?https://github.com/Stratsha/frc-newsletter/blob/main/newsletter/base.html) | Bloc original         | 0%        |
| 7.21289 KB        | [new.html](http://htmlpreview.github.io/?https://github.com/Stratsha/frc-newsletter/blob/main/newsletter/new.html)  | Nouveau bloc Stratsha | 61.2163%  |
| 2.03809 KB        | text.txt                                                                                                            | Texte uniquement      | 89.0412%  |

### Analyse

Les tests sont basés sur une seule section. Analysons si les résultats semblent corrects.

L'"ancien bloc" provient de la plus grande newsletter fournie par le client, à savoir la Newsletter 12, segment 5042.

La taille totale du fichier de la newsletter est de `373.145 KB`, et elle contient 21 sections (y compris le pied de page), ce qui signifie que chaque section ferait environ `17.7688 KB`.  
Puisque notre bloc est à moins de `1 KB` de cette estimation, nous pouvons supposer que les calculs suivants sont raisonnablement précis.

En utilisant l'ancien bloc, la taille estimée de la newsletter serait de `390.5517 KB`.  
En utilisant le nouveau bloc, la taille estimée de la newsletter serait de `151.47069 KB`.

_Prise en compte du boilerplate HTML_

Ce test a été réalisé en utilisant chaque bloc 21 fois, mais en incluant le boilerplate HTML une seule fois. Les calculs précédents dupliquaient du code qui, normalement, n'est nécessaire qu'une seule fois.

En utilisant l'ancien bloc, la taille estimée de la newsletter serait de `368.617 KB`.  
En utilisant le nouveau bloc, la taille estimée de la newsletter serait de `146.646 KB`.

## Points Clés

- Le nouveau bloc réduit la taille de 61.21%, le rendant nettement plus léger que l'ancien bloc.
- Malgré cette réduction, la taille de l'email dépasse encore la limite de coupure de Gmail de 33%, ce qui signifie que des ajustements supplémentaires sont nécessaires.
- Pour éviter la coupure, il pourrait être nécessaire de simplifier le design, réduire la quantité de texte ou supprimer certaines fonctionnalités d'accessibilité.
