# 💸 SMART BUDGET

## Présentation [ FR ]
Smart Budget est un mini outil codé en Python permettant de :
- Gérer son budget mensuel simplement
- Recevoir un feedback animé selon sa situation
- Voir un classement des utilisateurs les plus économes

## Overview [ EN ]
Smart Budget is a minimalist Python tool that helps you:
- Manage your monthly budget in a fun way
- Get dynamic feedback based on your finances
- View a ranking of users based on savings

## ⚙️ Prérequis / Requirements

- Python 3.x installé sur votre machine  
- Un navigateur moderne pour consulter la page HTML

## Lancer le projet / Run
Depuis la racine du projet / from projetct root 

```bash
python script/smart_budget.py


MAP SMART_BUDGET/
├── assets/
│ ├── css/
│ │ └── style.css
│ ├── icons/
│ └── imgs/
├── pages/
│ ├── contact/
│ └── home/
├── public/
│ └── index.html
├── script/
│ ├── smart_budget.py
│ ├── utils.py
│ └── save.json
├── .gitignore
├── package.json
└── README.md


🧠 Fonctionnement
Le script propose à l’utilisateur d’entrer :

Son revenu mensuel

Ses dépenses principales : logement, nourriture, transport

Le montant à mettre de côté

Il affiche ensuite un bilan avec une réaction adaptée :

✅ Bon équilibre : "Yatta ! Tu gères ton argent comme un pro ! all green!（＾∀＾●）ﾉｼ"

⚠️ Danger : "Oof… tu es dans le rouge ! ！yabai! aka desu !!"

😅 Équilibré juste : "C’est serré…だけど walla"

Les données utilisateurs sont stockées dans save.json.