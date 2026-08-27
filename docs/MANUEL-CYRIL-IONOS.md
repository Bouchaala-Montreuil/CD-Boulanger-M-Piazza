# Manuel IONOS — domaine `cd-boulangerie.fr`

Bonjour Cyril,

Ces instructions concernent uniquement la configuration du domaine chez IONOS. La partie GitHub sera faite séparément.

## Objectif

Relier le domaine `cd-boulangerie.fr` au site Internet de CD Boulangerie hébergé sur GitHub Pages.

## 1. Ouvrir la zone DNS IONOS

1. Se connecter à son compte IONOS.
2. Ouvrir **Domaines & SSL**.
3. Repérer le domaine **cd-boulangerie.fr**.
4. Cliquer sur la roue dentée ou sur **Actions**, puis **DNS**.

## 2. Remplacer les anciens enregistrements du site

Dans la liste DNS, supprimer ou remplacer uniquement les anciens enregistrements Web suivants s'ils sont présents :

- l'enregistrement **A** du domaine principal qui pointe vers `217.160.0.9` ;
- l'enregistrement **AAAA** du domaine principal qui pointe vers `2001:8d8:100f:f000::200` ;
- l'enregistrement **A** de `www` qui pointe vers `212.227.172.250`.

Ces anciennes adresses correspondent à la page IONOS par défaut et empêchent GitHub de vérifier le domaine.

## 3. Ajouter les enregistrements GitHub Pages

Cliquer sur **Ajouter un enregistrement** et créer les quatre lignes suivantes, une par une :

| Type | Nom / Host | Pointe vers / Valeur |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

Puis créer cette ligne :

| Type | Nom / Host | Pointe vers / Valeur |
|---|---|---|
| CNAME | `www` | `bouchaala-montreuil.github.io` |

Dans IONOS, le domaine principal peut être représenté par `@`, par un champ vide ou par `cd-boulangerie.fr`. Il s'agit du même emplacement.

Pour le CNAME, saisir uniquement :

```text
bouchaala-montreuil.github.io
```

Ne pas saisir `https://` et ne pas ajouter `/CD-Boulanger-M-Piazza`.

## 4. Ne pas modifier la messagerie

Ne pas supprimer ni modifier :

- les enregistrements **MX** ;
- les enregistrements **TXT** liés à la messagerie ;
- les enregistrements SPF, DKIM ou DMARC ;
- les serveurs de noms (NS).

Ces enregistrements peuvent être nécessaires pour les adresses e-mail IONOS.

## 5. Terminer

1. Enregistrer toutes les modifications.
2. Vérifier que les cinq nouveaux enregistrements apparaissent dans la zone DNS.
3. Envoyer simplement un message pour confirmer que c'est terminé.

Il n'est pas nécessaire de modifier GitHub : cette partie sera faite ensuite.

La propagation DNS peut prendre quelques minutes, parfois jusqu'à 24 ou 48 heures. Pendant ce délai, il est normal que le site ne soit pas encore accessible avec le domaine.

**Ne jamais envoyer le mot de passe IONOS.**
