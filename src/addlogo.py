import os
from pathlib import Path

# Chemin racine où se trouvent les fichiers et le logo
root_dir = 'D:/workspaces/wrk_python/LI249/support/'
logo_filename = 'D:/workspaces/wrk_python/LI249/support/images/logo.png'

rd = Path(root_dir)

for dirpath, _, filenames in os.walk(rd):
    for filename in filenames:
        if filename.endswith('.md'):
            file_path = os.path.join(dirpath, filename)
            # Calculer le chemin relatif vers le logo
            rel_path_to_logo = os.path.relpath(
                os.path.join(root_dir, logo_filename),
                start=dirpath
            )
            # Lire le contenu actuel
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Préparer la ligne du logo
            logo_line = f'![Logo]({rel_path_to_logo})\n\n'
            # Écrire avec le logo ajouté au début
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(logo_line + content)
            print(f'Mis à jour : {file_path}')