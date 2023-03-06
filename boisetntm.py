import streamlit as st
import random

st.title("Bois et Ntm")

start = st.button("Start")

number = 0


def GameRules(number):
    special_rule = ""

    if number == 1:
        text = "De quelle couleur et motif sont tes sous-vêtements ? (Montre si t'es un homme ou femme (dépend du contexte))"
    
    elif number == 2:
        text = "As tu déjà fantasmé sur une personne présente dans la pièce ?"
    
    elif number == 3:
        text = "Smack la personne à droite (bouche, front ou joue)"

    elif number == 4:
        text = "As-tu déjà embrassé une personne du même sexe ?"

    elif number == 5:
        text = "Fais 10 pompes (5 si problème au niveau des capacité physique)"

    elif number == 6:
        text = "Israël ou Palestine ? Argumentation attendus si ne préfère pas répondre bois le double de la dose d'alcool (Si fais exprès de pas répondre pour boire alors il bois pas ce fdp)"

    elif number == 7:
        text = "Fais une roue (Les gens au alentour donne une note sur 5 si tu as moins de la moyenne, tu perd)"

    elif number == 8:
        text = "Choisis un adversaire pour faire un concours d'ATR (Les gens au alentour donne une note sur 5 si tu as moins de la moyenne, tu bois) (A LIRE UNIQUEMENT SI LA PERSONNE GAGNE: et si tu gagne ba ta rien nique ta mère aussi)"

    elif number == 9:
        text = "Quelle est la taille moyenne française d'un sexe en érection en 2015 (réponse acceptée à 1 près) ? Réponse: 14.5cm (acceptée entre 13.5cm et 15.5cm) Possibilité de proposer 4 choix si voulus (A: 14, B: 15, C: 16, C: 17)"

    elif number == 10:
        text = "Pour chaque fois que tu t'es fait prendre en train de te masturber par qqn tu bois"

    elif number == 11:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Est-ce que tu as déjà eu un plan cul ?"

    elif number == 12:
        text = "Séducteur Icarien : Ta soif du sexe opposé te mènera à ta perte, tu bois pour chaque conquête que tu as eu dans ta vie (conquête = amoureux/amoureuse; plan cul; coup d'un soir, sexfriend, prostituée, sugar mommy, sugar daddy...)Étant l'auteur de ce gage, c'est moi qui en décide les règles. Le maximum de gorgée à boire est de 10.Cependant, la personne tombée sur le gage doit dire le nombres exact ou approximatif de conquêtes."

    elif number == 13:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Pensez tous les deux à une personne dans le groupe choisis par l'arbitre (vous êtes directement dans le groupe, minimum 4 personnes) (plus le nombre de personne augmente plus l'alcool à boire augmente)"

    elif number == 14:

        text = "(Choisis une autre personne, répondez en même temps à la question si les deux répondent une chose différente les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\nEst-ce que le maximum de jour où tu n'a pas pris de douche dépasse 4 ?"

    elif number == 15:
        text = "Explique comment on fait un 'perfect' au toilette ?"
        
    elif number == 16:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text ="Est-ce que tu as déjà eu un kyste ou un furoncle ?"

    elif number == 17:
        text = "Fruits Ninja: l'arbitre choisit une catégorie de fruit ainsi qu'un autre joueur. Ces 2 Genin vont devoir trouvé 5 fruits dans cette catégorie  (fruits ronds, fruit rouges, fruit commençant par une certaine lettre, fruits à noyau, fruits à coques, fruits provenant de pays tropicaux,...) Le premier qui en trouve 5 distribue 5 gorgées comme il le désire et doit se faire appeler 'Fruits Kage' jusqu'à la fin du tour. Toute personne oubliant de l'appeler par ce titre bois une gorgée automatiquement"

    elif number == 18:
        special_rule ="(Choisis une autre personne, faites le même gage en même temps si les deux réussisse le gage les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Faire une pompe à une main"

    elif number == 19:
        text = "TU BOIS 10 GORGEE (QUITTE A RE-REMPLIR TON VERRE) PENDANT QUE TOUS LE MONDE T'INSULTE"

    elif number == 20:
        text = "Casse toi un glaçon sur la gueule (front de préférence)"

    elif number == 21:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "(Choisis une autre personne, répondez en même temps à la question si les deux répondent une chose différente les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\nEst-ce que la police ta déjà contrôlé ?"

    elif number == 22:
        text = "Donne le nombre d'habitant du Tadjikistan en 2020 (à 1 000 000 près) Réponse: 9.75 millions"

    elif number == 23:
        text = "Mets un glaçon dans ton caleçon/culotte... jusqu'à qu'il fonde(sinon bois 3 gorgées/si tu l'enlèves avant qu'il ai fondu pour x ou y raison tu bois 1 gorgée)"
        
    elif number == 24:
        text = "Est-ce que tu as déjà cliqué sur une pub qui proposait un agrandissement du pénis"

    elif number == 25:
        text = "Si tu es maquillé (visage ou manucure), tu bois"

    elif number == 26:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Si la plupart du temps tu as plusieurs onglets d'ouverts quand tu te masturbes ?"

    elif number == 27:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Si tu es déjà partis avant la fin d'un film au cinéma ?"
        
    elif number == 28:
        text = "Si tu as un paquet de clopes, bois le nombre de gorgée (8 maxi)"

    elif number == 29:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "As tu déjà payé pour du contenu pornographique ?"

    elif number == 30:
        text = "Dégrafe le soutif d'une joueuse, si tu le fais en plus de 5 secondes tu bois"

    elif number == 31:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Si tu as déjà checké ton âge dans le fond d'un verre"

    elif number == 32:
        text = "Laisse-toi faire un bisou dans le cou par la personne de ton choix"

    elif number == 33:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Est-ce que tu as fais un cunni il y a moins de deux semaines ?"

    elif number == 34:
        text = "Pour chaque vêtements (absolument tout) de la couleur noir que tu porte, bois"

    elif number == 35:
        text = "Ferme les yeux ! Si tu arrives à dire ce que chacun a dans son verre sans regarder tous le monde bois"

    elif number == 36:
        text = "Si tu as déjà pensé à quelqu'un d'autre pendant l'acte, bois"

    elif number == 37:
        text = "Tous ceux qui possèdent cette liste d'éléments (ceinture, tong, bijoux, couvre-chef, lunette, sacoche) boivent"

    elif number == 38:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Est-ce que tu as déjà vomis à cause l'alcool ?"

    elif number == 39:
        text = "Bois autant de gorgée que de personne présente"

    elif number == 40:
        text = "Briseur de coeur : Tes piètres qualitées d'amoureux te retombent dessus, bois autant de gorgée que tu as eu de rupture amoureuse"

    elif number == 41:
        text = "Bois autant que tu as de couilles"

    elif number == 42:
        text = "Otaku (mais fier de l'être) : Ton image de no life fantasmant sur des personnages fictifs te colle à la peau. Chaque joueur dit un anime/manga/films d'animation japonais. La première personne qui est à court d'idée bois 5 gorgées [Sale inculte de merde](chaque anime/manga/film d'animation japonais ne peut être cité qu'une seule fois et 5s pour répondre) CE GAGE PEUT ÊTRE CHANGÉ PAR LE MAÎTRE DU JEU EN CHOSISSANT UNE CATÉGORIE DE MANGA/ANIME/FILM d'ANIMATION JAPONAIS SI JAMAIS IL Y A BEAUCOUP D'OTAKU DANS LE JEU(ex.seinen, shoujo, shounen, isekai,  sorti avant les années 2000, yuri, hentai, commençant par la lettre de la personne qui est tombé dessus...)"

    elif number == 43:
        text = "(Choisis une autre personne)\nLe premier (en question d'âge) à s'être masturbé, bois"

    elif number == 44:
        text = "Mister Freeze : Ton caleçon ou ta culotte est réquisitionné pour être placé pendand 15 min au congèlo, après quoi tu devras le/la remettre (sinon bois 4 gorgées)"

    elif number == 45:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Est ce que tu as déjà subis une opération à la queue ?"

    elif number == 46:
        text = "Challenge de groupe: essayer de compter jusqu'à 10, une personne commence par 1 et un autre suit etc. (pas le droit de suivre un ordre précis de personne) les personnes qui disent le même nombre en même temps boivent le nombre de gorgés auquel ils ont perdu. "

    elif number == 47:
        text = "Paparazzi : choisis un adversaire celui qui montre une photo de l'autre en premier gagne. Le mois de la photo du gagnant est le nombre de gorgée distribué au perdant (1min max)"

    elif number == 48:
        text = "BOIS AUTANT QU'IL Y A DE GARÇON ET BAISE TA MÈRE (QUITTE À RE REMPLIR TON VERRE)"

    elif number == 49:
        text = "COCKTAIL MOLOTOV : CHAQUE JOUEUR VERSE UNE DOSE D'ALCOOL DANS TON VERRE. 1MIN POUR BOIRE LE TOUT. BONNE CHANCE FRÉRO"

    elif number == 50:
        text = "DIABOLO MENTHE : CHAQUE JOUEUR VERSE UN LIQUIDE DANS TON VERRE. 1MIN POUR TROUVER LE LIQUIDE ET 1MIN POUR BOIRE LE TOUT. LA BISE D'ESTEBAN"

    elif number == 51:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Bois 3 gorgées si tu n'as pas été en couple, eut un/une sexfriend/coup d'un soir ou un date avec une personne handicapée"

    elif number == 52:
        text = "Malheureusement tu n'as pas la main verte : pour chaque râteau que tu t'es pris tu bois une gorgée (réponse approximative acceptée). Si tu ne sais pas ou ne trouve pas en 30s tu bois 5 gorgées "

    elif number == 53:
        text = "TOURNÉE GÉNÉRALLE !! : TOUT LE MONDE BOIS UNE GORGÉE "

    elif number == 54:
        st.text("📣TABLE RONDE:On fait un tour de table. A la fin, chaque joueur pointe du doigt la personne qui a sorti la meilleure anecdote.\nA DIRE APRES !! Cette dernière bois le nombre de gorgées que de vote qu'elle a reçu\n(T'as crût que t'allé t'en sortir gagnant fdp ? Ce jeu s'appelle 'Bois et NTM' pour rappel)")
        text = "L'endroit le plus insolite où on s'est masturbé/e"

    elif number == 55:
        st.text("📣TABLE RONDE:On fait un tour de table. A la fin, chaque joueur pointe du doigt la personne qui a sorti la meilleure anecdote.\nA DIRE APRES !! Cette dernière bois le nombre de gorgées que de vote qu'elle a reçu\n(T'as crût que t'allé t'en sortir gagnant fdp ? Ce jeu s'appelle 'Bois et NTM' pour rappel)")
        text = "L'endroit le plus insolite où tu as eu un rapport avec une autre personne (fellation, cunni, sexe, tripotage(dsl je trouve pas le terme exact),..."
    
    elif number == 56:
        special_rule ="(Choisis une autre personne, répondez en même temps à la question si les deux répondent la même chose les 2 bois, si un des deux trichent ou est hors-temps il boit tout seul)\n"
        text = "Est-ce que tu as déjà volé qqchose ?"

    elif number == 57:
        text = "Sale Toxico De Merde : Bois autant de gorgées que de drogue/s tu as pris dans ta vie (max 8 gorgées). De plus, si le maître du jeu est un enculé ou une salope, autorise la personne tombée sur ce gage, que chaque personne ayant consommée une drogue de la personne tombée sur ce gage boivent une gorgée. Libre au toxico de choisir la drogue qu'il/elle souhaite. (En gros il/elle a conso du cannabis il/elle dit 'Tout ceux ayant consommé du cannabis, boivent !') NTM pour rappel. Et ça vaut pour tout le monde.  Bande de droguée va !!"
    
    if special_rule != "":
        st.markdown("Special Rule 🔥🔥🔥"+ special_rule)
        
    st.markdown("Gage "+str(number)+" - "+text)


if start:
    number = random.randint(56,57)
    st.write("Number = "+str(number))
    GameRules(number)