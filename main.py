import pandas as pd

# Nombre del archivo
archivo = 'concentrado.xlsx'

# DataFrame de ejemplo
df = pd.read_excel(archivo, sheet_name='pedidos')

# Si la columna Guias tiene nan, reemplazar por vacío
df['Guias'] = df['Guias'].fillna('')

# Convertir la columna de guías a string
df['Guias'] = df['Guias'].astype(str)

# Dividir las guías en filas individuales
df['Guias'] = df['Guias'].str.split(',')

# Crear una nueva columna para contar la cantidad de guías
df['Cantidad_guías'] = df['Guias'].apply(len)

# print(df[['Orden', 'Guias', 'Cantidad_guías']])

# Crear una lista para cada fila con múltiples guías divididas
rows = []
for index, row in df.iterrows():

    # elimina las "" de las guías:
    row['Guias'] = [guía.replace('"', '') for guía in row['Guias']]


    if row['Cantidad_guías'] > 1:
        for guía in row['Guias']:
            new_row = row.copy()
            new_row['Guias'] = guía.strip()
            rows.append(new_row)
    else:
        row['Guias'] = row['Guias'][0]
        rows.append(row)

# Crear un nuevo DataFrame con las filas divididas
df_final = pd.DataFrame(rows)

# Eliminar la columna temporal de cantidad de guías
df_final = df_final.drop(columns=['Cantidad_guías'])


# exportar a excel
df_final.to_excel('concentrado_final.xlsx', index=False)
