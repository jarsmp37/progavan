import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def entrenar_modelo():
    df=pd.read_csv("Diabetes.csv")
    # Diccionario con las traducciones
    traducciones = {
            'Pregnancies': 'Embarazos',
            'Glucose': 'Glucosa',
            'BloodPressure': 'PresionSanguinea',
            'SkinThickness': 'GrosorPiel',
            'Insulin': 'Insulina',
            'BMI': 'IMC',
            'DiabetesPedigreeFunction': 'FuncionPedegreeDiabetes',
            'Age': 'Edad',
            'Outcome': 'Resultado'
        }    

    # Renombrar las columnas
    df.rename(columns=traducciones, inplace=True)        

    # Seleccionar características y variable objetivo
    X = df[['Glucosa']]
    y = df['Resultado']

    # Dividir los datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar el modelo
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    return model

def predecir_diabetes(model, glucosa):
    # Crear un DataFrame con el nuevo dato
    x = pd.DataFrame([glucosa], columns=['Glucosa'])

    # Hacer la predicción
    y_pred = model.predict(x)

    # Devolver el resultado
    if y_pred[0] == 1:
        return "Es probable que se tenga Diabetes"
    else:
        return "Es probable que no se tenga Diabetes"