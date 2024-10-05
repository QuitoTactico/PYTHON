import os

ruta = r"C:\Users\Esteban\Downloads\-CODE-\DnD-AI\media\entity\icons\boss_icons"
archivos = os.listdir(ruta)

archivos_filtered = [archivo.title().replace("-", " ")[:-4] for archivo in archivos]

print(archivos)
print(archivos_filtered)
