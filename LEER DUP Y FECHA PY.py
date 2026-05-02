import pandas as pd
import os

path = r"C:\Users\Thomas\OneDrive\Escritorio\entrega andres\thomas-assessment-main\thomas-assessment\reports"

files = [f for f in os.listdir(path) if f.endswith(".csv")]

print("Archivos encontrados:", files)


dfs = []
for f in files:
    file_path = os.path.join(path, f)
    print(f"Leyendo: {file_path}")
    df = pd.read_csv(file_path)
    dfs.append(df)


datos = pd.concat(dfs, ignore_index=True)

if "created_at" in datos.columns:
    datos["created_at"] = pd.to_datetime(datos["created_at"], errors="coerce")

antes = len(datos)
datos = datos.drop_duplicates()
despues = len(datos)

print(f"Duplicados eliminados: {antes - despues}")


print(os.listdir(path))
print(datos)

