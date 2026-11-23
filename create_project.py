
import os

structure = [
    "src/modes_cuisson",
    "src/regulation_temperature",
    "src/minuterie",
    "src/securite",
    "src/interface_utilisateur",
    "tests/tests_unitaires",
    "tests/tests_integration",
    "docs"
]

root = "cuiseur-riz-ffe"

os.makedirs(root, exist_ok=True)

with open(os.path.join(root, "README.md"), "w", encoding="utf-8") as f:
    f.write("# Cuiseur à riz FFE\n")

for folder in structure:
    path = os.path.join(root, folder)
    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, ".gitkeep"), "w") as f:
        pass

print("Arborescence créée avec succès !")
