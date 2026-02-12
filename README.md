# Dossier de Sécurisation de l'Infrastructure - Module M11

Site web complet pour le dossier de sécurisation de l'infrastructure conforme aux normes RGPD, NIS2, DORA, PSSI et CIS.

## 📁 Structure du site

```
globalsecurity/
├── index.html                  # Page d'accueil avec navigation vers toutes les sections
├── matrice-risques.html        # Section 0 - Matrice de risque (12 risques identifiés)
├── gestion-reseau.html         # Section 1 - Gestion du réseau (segmentation VLAN, NGFW, VPN)
├── gestion-os.html             # Section 2 - Gestion des OS (migration, hardening, EDR)
├── gestion-data.html           # Section 3 - Gestion des données (classification, stockage)
├── confidentialite.html        # Section 4 - Confidentialité (chiffrement, RGPD, DLP)
├── gestion-acces.html          # Section 5 - Gestion des accès (IAM, PAM, MFA)
├── sauvegardes.html            # Section 6 - Sauvegardes (stratégie 3-2-1, tests)
├── tracabilite.html            # Section 7 - Traçabilité des accès (logging, SIEM)
├── surveillance.html           # Section 8 - Surveillance sécurité (monitoring, IDS/IPS)
├── gestion-changements.html    # Section 9 - Gestion des changements (ITIL, CMDB)
├── monitoring.html             # Section 10 - Monitoring (infrastructure, applicatif)
├── tests.html                  # Section 11 - Tests automatiques (scans, pentests)
├── mises-a-jour.html           # Section 12 - Mises à jour (patching, automatisation)
├── plan-budget.html            # Section 13 - Plan & Budget (phasage sur 12 mois)
├── conclusion.html             # Section 14 - Conclusion (synthèse et signatures)
├── css/
│   └── style.css               # Stylesheet principal (design moderne et responsive)
└── js/
    └── main.js                 # JavaScript pour navigation mobile
```

## 🎨 Caractéristiques du design

- **Design moderne et aéré** : Interface claire avec espaces visuels optimisés
- **Responsive** : S'adapte parfaitement aux mobiles, tablettes et desktop
- **Navigation intuitive** : Header fixe avec navigation rapide entre sections
- **Code couleur** : Badges de criticité (critique/élevé/moyen/faible)
- **Tableaux clairs** : Présentation structurée des données techniques
- **Typography professionnelle** : Police Inter pour une lecture optimale

## 📊 Contenu du dossier

### Conformité réglementaire
- ✅ RGPD (UE 2016/679) - Protection des données personnelles
- ✅ NIS2 (Directive 2022/2555) - Gestion des risques et incidents
- ✅ DORA (Règlement UE 2022/2554) - Résilience opérationnelle numérique
- ✅ PSSI - Politique de Sécurité des Systèmes d'Information
- ✅ Charte Informatique - Règles d'usage du SI
- ✅ Benchmarks CIS - Durcissement OS et équipements
- ✅ EBIOS Risk Manager (ANSSI) - Méthode d'analyse de risque

### Points clés couverts
- 12 risques identifiés et traités (matrice EBIOS)
- 7 VLANs de segmentation réseau
- Classification des données sur 4 niveaux de criticité
- Stratégie de sauvegarde 3-2-1 avec RTO/RPO définis
- Plan de déploiement sur 12 mois (5 phases)
- 40+ mesures de sécurité documentées

## 🚀 Utilisation

### Ouvrir le site
1. Ouvrez `index.html` dans votre navigateur
2. Naviguez entre les sections via le menu en haut
3. Sur mobile, utilisez le bouton menu (☰)

### Personnalisation
Les champs marqués `[X]` ou `[NOM]` sont à compléter avec les informations spécifiques :
- Nom de l'entreprise
- Consultant sécurité
- Paramètres techniques (délais, seuils, etc.)
- Budget estimatif

### Sections "À compléter"
Chaque page contient une section "Notes et justifications" pour adapter le contenu au contexte spécifique de l'organisation.

## 📱 Compatibilité

- ✅ Chrome / Edge / Firefox / Safari
- ✅ Mobile (iOS / Android)
- ✅ Tablette
- ✅ Impression (optimisée pour PDF)

## 🎯 Objectifs pédagogiques

Ce site présente un dossier de sécurisation complet qui peut servir de :
- **Référence pédagogique** pour comprendre la sécurité infrastructure
- **Wiki technique** avec toutes les bonnes pratiques référencées
- **Document professionnel** prêt à être présenté en comité

## 📝 Notes

- Aucune donnée sensible n'est incluse dans ce template
- Tous les exemples sont génériques et à adapter
- Le code est commenté et maintenable
- Design system cohérent avec variables CSS

---

**Version** : 1.0 Draft
**Module** : M11 - Infrastructure Sécurisée
**Conformité** : RGPD · NIS2 · DORA · PSSI · CIS
