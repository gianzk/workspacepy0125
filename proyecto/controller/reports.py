from config.app import *
import pandas as pd

def GenerateReportPaisQueMenosCompró(app: App): ##En pandas
    conn = app.bd.getConection()
    df_ventas = pd.read_sql_query("SELECT * FROM VENTAS", conn)
    df_postal = pd.read_sql_query("SELECT * FROM POSTALCODE", conn)

    # Paso 2: Unir las tablas usando merge en pandas
    df_merge = df_ventas.merge(df_postal, how="left", left_on="postal_code", right_on="code")

    # Paso 3: Agrupar por país, sumando la cantidad de productos comprados
    df_report = df_merge.groupby(['pais'], as_index=False)['quantity'].sum()

    # Paso 4: Identificar el país con la menor cantidad comprada
    df_report = df_report.sort_values(by="quantity", ascending=True)

    # Obtener el país con la menor cantidad comprada
    pais_menos_compra = df_report.iloc[0]

    # Paso 5: Guardar el reporte en un archivo CSV con nombre personalizado
    path = "/workspaces/workspacepy0125/proyecto/files/data-01.csv"
    pais_menos_compra.to_csv(path, index=False)

    # Paso 6: Enviar el reporte por correo
    sendMail(app, path)


def sendMail(app:App,data):
    app.mail.send_email('from@example.com','Reporte_Final_Cristhian_Tello','Reporte_Final_Cristhian_Tello',data)