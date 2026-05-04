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



datos["recalculated_total"] = datos["quantity"] * datos["unit_price"] * (1 - datos["discount"])


datos["error_reason"] = ""

datos.loc[datos["quantity"] <= 0, "error_reason"] += "quantity inválida; "
datos.loc[datos["unit_price"] < 0, "error_reason"] += "unit_price inválido; "
datos.loc[datos["discount"] < 0, "error_reason"] += "discount negativo; "
datos.loc[datos["discount"] > 1, "error_reason"] += "discount mayor a 1; "
datos.loc[datos["created_at"].isna(), "error_reason"] += "fecha inválida; "

invalidos = datos[datos["error_reason"] != ""]


invalidos.to_csv(os.path.join(path, "tabla_errores.csv"), index=False)



print("Registros inválidos encontrados:", len(invalidos))
print(invalidos)


antes = len(datos)
datos = datos.drop_duplicates()
despues = len(datos)

print(f"Duplicados eliminados: {antes - despues}")


print(os.listdir(path))
print(datos)

