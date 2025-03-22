# Application de Gestion des Ventes 

---
![SALES MANAGE DASBOARD](https://www.toucantoco.com/hubfs/Mobile%20analytics%20tablet.png)
---
**Projet :** Système de gestion des stocks et ventes pour une boutique de ventes des accessoires téléphoniques et de divers produits.   
**Développeur :** Eric KOULODJI
---
[Documentation DRF API web](https://pypi.python.org/pypi/drfdocs/)
---

## Table des matières  
1. [Présentation du projet](#1-présentation-du-projet)  
2. [Objectifs](#2-objectifs)  
3. [Fonctionnalités](#3-fonctionnalités)  
4. [Technologies](#4-technologies)  
5. [Déploiement](#5-déploiement)  
6. [Contraintes](#6-contraintes)  
7. [Planning](#7-planning)  
8. [Budget](#8-budget)  
9. [Validation](#9-validation)  
10. [Livraisons](#10-livraisons)  

---

## 1. Présentation du projet  
L'application de gestion des ventes vise à combler le besoin critique des propriétaires de boutiques de maintenir un contrôle précis sur leurs activités commerciales, particulièrement lorsqu'ils ne sont pas physiquement présents. Le système permettra une supervision à distance des opérations quotidiennes, incluant les entrées et sorties de marchandises, les performances de vente, et la gestion des stocks.

Dans un contexte commercial de plus en plus compétitif, disposer d'informations en temps réel sur ses activités devient un avantage concurrentiel majeur. Cette solution s'adresse donc aux propriétaires soucieux d'optimiser leur gestion et de prendre des décisions commerciales basées sur des données fiables et actualisées.

**Objectif principal :** Permettre aux administrateurs de contrôler ses activités à distance via un tableau de bord analytique.  

---

## 2. Objectifs  
✅ **Pour l'administrateur** :  
-Fournir à l'administrateur une visibilité complète sur les activités de sa boutique

-Automatiser la mise à jour des stocks après chaque transaction

-Simplifier le processus d'enregistrement des ventes pour le boutiquier

-Générer des rapports analytiques permettant d'identifier les tendances et d'optimiser les approvisionnements

-Diminuer les risques de rupture de stock par un système d'alertes préventives

-Améliorer la traçabilité des transactions commerciales

✅ **Pour les employés** :  
- Interface simple pour enregistrer les ventes  
- Mise à jour automatique des stocks  

---

## 3. Fonctionnalités  
### **Gestion des stocks**  
- Enregistrement des articles (nom, prix, fournisseur, catégorie)  
- Alertes personnalisables pour seuils critiques  
- Historique des approvisionnements  

### **Gestion des ventes**  
- Interface type "caisse enregistreuse"  
- Gestion des remises et modes de paiement  
- Historique des transactions 
- Mise en place d'un reçu(ou tickets) pdf après paiement par le client. 

### **Suivi en temps réel**  
- Synchronisation via WebSockets  
- Notifications push (nouvelles ventes, alertes)  

### **Tableau de bord**  
- Statistiques journalières/hebdomadaires/mensuelles  
- Graphiques interactifs (produits les plus vendus)  

---

## 4. Technologies  
| Composant       | Technologie               |  
|-----------------|---------------------------|  
| **Backend**     | Django REST Framework + Django (Python)    |  
| **Base de données** | PostgreSQL + Supabase |  
| **Frontend**    | React.js (web) / Flutter (mobile) |  
| **Notifications** | Firebase Cloud Messaging |  

---

## 5. Déploiement  
- **Backend** : DigitalOcean/AWS  
- **Frontend** : Vercel (web) / Play Store/App Store (mobile)  
- **Base de données** : Supabase ou serveur PostgreSQL dédié  

---

## 6. Contraintes  
✅ **Sécurité** :  
- Authentification JWT  
- Chiffrement des données sensibles  

✅ **Optimisation** :  
- Fonctionnement hors ligne avec synchronisation différée  
- Interface responsive (mobile/desktop)  

---

## 7. Planning  
| Phase               | Durée       |  
|---------------------|-------------|  
| Conception          | 2 semaines  |  
| Développement      | 6 semaines  |  
| Tests              | 1 semaine   |  
| Déploiement        | 1 semaine   |  

**Total estimé :** 10 semaines  

---

## 8. Budget  
### **Coûts de développement**  
| Phase               | Coût (EUR) |  
|---------------------|------------|  
| Conception          | 3 600€     |  
| Backend             | 5 400€     |  
| Frontend            | 7 200€     |  
| Tests               | 2 700€     |  
| Déploiement         | 1 800€     |  
| **Total**           | **20 700€**|  

### **Coûts additionnels**  
- Design/UI : 3 500€  
- Licences : 1 200€  
- Hébergement (1 an) : 1 500€  
- **Total** : **9 800€**  

**Budget total :** **30 500€**  

---

## 9. Validation  
Le projet sera validé après :  
1. Période de test de 2 semaines  
2. Vérification des fonctionnalités selon checklist  
3. Signature d'un procès-verbal de réception  

---

## 10. Livraisons  
- Code source complet (backend/frontend)  
- Documentation technique et utilisateur  
- Applications déployées (web/mobile)  
- Support technique initial (1 mois)  

---

**Signatures**  
_________________________          _________________________  
        Le Client                     Le Développeur  
