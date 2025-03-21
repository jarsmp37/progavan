import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay

import os
os.chdir(r"C:\Users\Jaime\Documents\GitHub\Prograavanzada\datascience")
def entrenamiento():
    df=pd.read_csv("Hotel_Reservations.csv")
    global X_test

    #Cambiar nombres de columnas
    nombres_espanol = {
        'Booking_ID': 'ID_Reserva',
        'no_of_adults': 'Num_Adultos',
        'no_of_children': 'Num_Ninos',
        'no_of_weekend_nights': 'Noches_FinSemana',
        'no_of_week_nights': 'Noches_Semana',
        'type_of_meal_plan': 'Tipo_Plan_Comidas',
        'required_car_parking_space': 'Estacionamiento_Requerido',
        'room_type_reserved': 'Tipo_Habitacion',
        'lead_time': 'Dias_Antelacion',
        'arrival_year': 'Año_Llegada',
        'arrival_month': 'Mes_Llegada',
        'arrival_date': 'Dia_Llegada',
        'market_segment_type': 'Tipo_Segmento_Mercado',
        'repeated_guest': 'Huesped_Repetido',
        'no_of_previous_cancellations': 'Cancelaciones_Previas',
        'no_of_previous_bookings_not_canceled': 'Reservas_Previas_NoCanceladas',
        'avg_price_per_room': 'Precio_Promedio_Habitacion',
        'no_of_special_requests': 'Solicitudes_Especiales',
        'booking_status': 'Cancelado'
    }

    df.rename(columns=nombres_espanol, inplace=True)

    # cambiar lo que dice en el data frame de inglés a español
    traduccion_plan_comidas = {
        'Meal Plan 1': 'Plan 1',
        'Not Selected': 'No Seleccionado',
        'Meal Plan 2': 'Plan 2',
        'Meal Plan 3': 'Plan 3'
    }

    # Aplicar la traducción a la columna
    df['Tipo_Plan_Comidas'] = df['Tipo_Plan_Comidas'].replace(traduccion_plan_comidas)

    cancelacion = {
        'Not_Canceled':0,
        'Canceled':1
    }

    # Aplicar la traducción a la columna
    df["Cancelado"] = df["Cancelado"].replace(cancelacion).infer_objects(copy=False)

    df['Fecha_Llegada'] = pd.to_datetime({
        'year': df['Año_Llegada'],
        'month': df['Mes_Llegada'],
        'day': df['Dia_Llegada']
    }, errors='coerce')

    df = df.dropna(subset=['Fecha_Llegada'])
    coluclave = ["Dias_Antelacion", "Solicitudes_Especiales", "Mes_Llegada", "Huesped_Repetido"]
    X = df[coluclave]
    y = df["Cancelado"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    return rf_model

def prediccion_usuario(rf_model,Dias_Antelacion,Solicitudes_Especiales,Mes_Llegada,Huesped_Repetido):
    dato=pd.DataFrame([[Dias_Antelacion,Solicitudes_Especiales,Mes_Llegada,Huesped_Repetido]],columns=X_test.columns)
    y_pred = rf_model.predict(dato)
    if y_pred[0]==0:
        return f"El cliente probablemente no va a cancelar"
    elif y_pred[0]==1:
        return f"El cliente probablemente va a Cancelar"