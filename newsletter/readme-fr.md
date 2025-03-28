## Introduction

Ce rapport présente les résultats d'un test mené afin de déterminer l'efficacité de la réécriture d'un bloc spécifique d'une newsletter pour éviter la coupure par Gmail. L'objectif est de réduire la taille de l'email tout en maintenant la qualité et l'accessibilité du contenu.

## Coupure par Gmail

Gmail coupe les emails dont la taille dépasse 102 KB. Cela entraîne l'affichage d'un message en bas de l'email indiquant que le contenu a été tronqué, ce qui peut nuire à l'expérience utilisateur. Notre objectif est de maintenir l'email en dessous de cette limite pour éviter cette coupure.

## Tests

Chaque taille de fichier est mesurée en octets et représente la taille réelle du fichier, et non sa taille sur le disque.  
Afin de gagner du temps et d'effectuer plus d'itérations, nous avons extrait un bloc de la plus grande newsletter disponible, puis nous l'avons repensé et redéveloppé pour voir si nous pouvions réduire sa taille.

Commande pour mesurer la taille du fichier :  
`stat -f "%z" [nom_du_fichier] | awk '{print $1 / 1024 " KB"}'`

### Bloc simple

| Taille du fichier | Fichier                                                                                                              | Description           | Réduction |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------- | --------- |
| 18.5977 KB        | [base.html](http://htmlpreview.github.io/?https://github.com/Stratsha/frc-newsletter/blob/main/newsletter/base.html) | Bloc original         | 0%        |
| 7.21289 KB        | [new.html](http://htmlpreview.github.io/?https://github.com/Stratsha/frc-newsletter/blob/main/newsletter/new.html)   | Nouveau bloc Stratsha | 61.2163%  |
| 2.03809 KB        | text.txt                                                                                                             | Texte uniquement      | 89.0412%  |

### Newsletter simulée

Cette version essaie de simuler une newsletter complète, en multipliant le bloc jusqu'a atteindre une quantité de contenu qui correspond à la plus grande newsletter existante en notre possession.

| Taille du fichier | Fichier                                                                                                                      | Description                             | Réduction |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | --------- |
| 373.715 KB        | [base-big.html](http://htmlpreview.github.io/?https://github.com/Stratsha/frc-newsletter/blob/main/newsletter/base-big.html) | Bloc original multiplié 21 fois         | 0%        |
| 146.646 KB        | [new-big.html](http://htmlpreview.github.io/?https://github.com/Stratsha/frc-newsletter/blob/main/newsletter/new-big.html)   | Nouveau bloc Stratsha multiplié 21 fois | 60.7599%  |

### Newsletter complète minifiée

Cette version utilise une technique appelée la minification, qui permet de supprimer les caractères inutiles comme certains espaces

| Taille du fichier | Fichier                                                                                                                              | Description                             | Réduction |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- | --------- |
| 258.691 KB        | [base-big.min.html](http://htmlpreview.github.io/?https://github.com/Stratsha/frc-newsletter/blob/main/newsletter/base-big.min.html) | Bloc original multiplié 21 fois         | 0%        |
| 94.3301 KB        | [new-big.min.html](http://htmlpreview.github.io/?https://github.com/Stratsha/frc-newsletter/blob/main/newsletter/new-big.min.html)   | Nouveau bloc Stratsha multiplié 21 fois | 63.5356%  |

### Analyse

Les tests sont basés sur une seule section. Puis cette sections est dupliquée pour simuler une newsletter entière. Analysons si les résultats semblent corrects.

L'"ancien bloc" provient de la plus grande newsletter fournie par le client, à savoir la Newsletter 12, segment 5042.

La taille totale du fichier de la newsletter est de `373.145 KB`, et elle contient 21 sections (y compris le pied de page).  
Notre newsletter simulée fait `373.715 KB`, la rapprochant très fortement de la newsletter complète, nous pensons donc que même si une marge d'erreur est à prévoir, les calculs précédents sont pertinents.

En utilisant le nouveau bloc minifié, la taille estimée de la newsletter serait de `373.145 KB`.

## Points Clés

- Nos tests ont montré que la taille de la newsletter pouvait être réduit de plus de `74%` par rapport à la newsletter actuelle
- La taille total entrerait donc, de justesse, sous les `102 KB` qui déclanchent la coupure de l'email sur Gmail

## Pistes pour réduire encore plus la taille

- Le design actuel n'a que très peu simplifié, un design plus simple permettrait de réduire encore plus la taille du fichier
- L'exemple utilisé était le plus grand disponible, des newsletter plus courte seraient encore plus légères

## Difficultés possibles

- La nouvelle newsletter à été développée selon les bonnes pratiques actuelles, mais n'a pas été testée sur tous les clients emails, certains ajustements nécéssaire à la bonne lecture de l'email sur les vieux clients peuvent augementer la taille du fichier
- Les techniques de minifications utilisées altèrent le code HTML, ce qui peut générer des problèmes d'interprétation du code selon les clients emails, des tests supplémentaires devront être effectués afin de valider la solution actuelle
