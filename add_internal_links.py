import os
import re

# Define internal links to add to relevant pages
internal_links = {
    'matrice-risques.html': [
        ('gestion-reseau.html', 'Pour plus de détails sur la sécurisation réseau, consultez notre section <a href="gestion-reseau.html">Gestion du Réseau</a>.'),
        ('surveillance.html', 'Découvrez notre approche de <a href="surveillance.html">Surveillance de la Sécurité</a> pour la détection proactive des menaces.')
    ],
    'gestion-reseau.html': [
        ('matrice-risques.html', 'Voir aussi l\'<a href="matrice-risques.html">Analyse des Risques</a> pour comprendre les menaces réseau.'),
        ('surveillance.html', 'Complétez avec notre système de <a href="surveillance.html">Surveillance et IDS/IPS</a>.')
    ],
    'gestion-os.html': [
        ('mises-a-jour.html', 'Pour la politique de patching, consultez <a href="mises-a-jour.html">Gestion des Correctifs</a>.'),
        ('monitoring.html', 'Voir aussi <a href="monitoring.html">Supervision Technique</a> pour le monitoring des OS.')
    ],
    'gestion-data.html': [
        ('confidentialite.html', 'En savoir plus sur la <a href="confidentialite.html">Protection des Données RGPD</a>.'),
        ('sauvegardes.html', 'Consultez notre <a href="sauvegardes.html">Stratégie de Sauvegarde</a> pour la protection des données.')
    ],
    'confidentialite.html': [
        ('gestion-data.html', 'Voir la <a href="gestion-data.html">Gestion des Données</a> pour les aspects techniques.'),
        ('tracabilite.html', 'Découvrez nos mesures de <a href="tracabilite.html">Traçabilité et Audit</a>.')
    ],
    'gestion-acces.html': [
        ('tracabilite.html', 'Complétez avec <a href="tracabilite.html">Traçabilité et PAM</a> pour l\'audit des accès.'),
        ('confidentialite.html', 'Voir aussi <a href="confidentialite.html">Protection des Données</a> pour les droits d\'accès RGPD.')
    ],
    'sauvegardes.html': [
        ('gestion-data.html', 'Voir <a href="gestion-data.html">Gestion des Données</a> pour le chiffrement.'),
        ('tests.html', 'Consultez <a href="tests.html">Tests de Sécurité</a> pour les tests de restauration.')
    ],
    'tracabilite.html': [
        ('surveillance.html', 'Complétez avec <a href="surveillance.html">Surveillance Sécurité</a> et SIEM.'),
        ('gestion-acces.html', 'Voir aussi <a href="gestion-acces.html">Gestion des Accès</a> pour l\'authentification.')
    ],
    'surveillance.html': [
        ('monitoring.html', 'Voir aussi <a href="monitoring.html">Supervision Technique</a> pour l\'infrastructure.'),
        ('tracabilite.html', 'Complétez avec <a href="tracabilite.html">Traçabilité et SIEM</a>.')
    ],
    'gestion-changements.html': [
        ('tests.html', 'Voir <a href="tests.html">Tests de Sécurité</a> pour la validation des changements.'),
        ('mises-a-jour.html', 'Consultez <a href="mises-a-jour.html">Gestion des Correctifs</a> pour les processus de mise à jour.')
    ],
    'monitoring.html': [
        ('surveillance.html', 'Complétez avec <a href="surveillance.html">Surveillance Sécurité</a> pour le monitoring sécurité.'),
        ('gestion-os.html', 'Voir <a href="gestion-os.html">Gestion des OS</a> pour la configuration système.')
    ],
    'tests.html': [
        ('sauvegardes.html', 'Voir <a href="sauvegardes.html">Sauvegardes</a> pour les tests de restauration.'),
        ('gestion-changements.html', 'Consultez <a href="gestion-changements.html">Change Management</a> pour les processus de test.')
    ],
    'mises-a-jour.html': [
        ('gestion-os.html', 'Voir <a href="gestion-os.html">Gestion des OS</a> pour les configurations système.'),
        ('tests.html', 'Consultez <a href="tests.html">Tests de Sécurité</a> pour valider les correctifs.')
    ]
}

# Process each file
for filename, links in internal_links.items():
    filepath = filename

    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the main closing tag
        last_section_end = content.rfind('  </main>')

        if last_section_end != -1:
            # Create the related links section
            related_section = '\n\n    <div class="section-card">\n'
            related_section += '      <h2><span class="section-icon">📚</span> Pages liées</h2>\n'
            related_section += '      <ul class="content-list">\n'

            for link_file, link_text in links:
                related_section += f'        <li>{link_text}</li>\n'

            related_section += '      </ul>\n'
            related_section += '    </div>'

            # Insert before </main>
            content = content[:last_section_end] + related_section + '\n' + content[last_section_end:]

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"[OK] Added internal links to {filename}")
        else:
            print(f"[ERROR] Could not find insertion point in {filename}")
    else:
        print(f"[ERROR] File not found: {filename}")

print("\nInternal links added successfully!")
