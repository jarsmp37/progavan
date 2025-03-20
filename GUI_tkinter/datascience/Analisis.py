import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

def grafico_embarazos(df, paciente_valor=None):
    plt.figure(figsize=(8, 6))
    df['Embarazos'].value_counts().sort_index().plot(kind="bar", color="Green")
    if paciente_valor is not None:
        plt.axvline(paciente_valor, color="red", linestyle="--", label="Paciente")
    plt.title("Distribución de Embarazos")
    plt.xlabel("Número de Embarazos")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.show()

def grafico_glucosa(df, paciente_valor=None):
    plt.figure(figsize=(8, 6))
    sns.histplot(df["Glucosa"], kde=True, color="green", label="Distribución")
    if paciente_valor is not None:
        plt.axvline(paciente_valor, color="red", linestyle="--", label="Paciente")
    plt.title("Distribución de Glucosa")
    plt.xlabel("Nivel de Glucosa")
    plt.ylabel("Densidad")
    plt.legend()
    plt.show()

def grafico_presion_sanguinea(df, paciente_valor=None):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df["PresionSanguinea"], color="orange", label="Distribución")
    if paciente_valor is not None:
        plt.axvline(paciente_valor, color="red", linestyle="--", label="Paciente")
    plt.title("Distribución de Presión Sanguínea")
    plt.xlabel("Presión Sanguínea")
    plt.legend()
    plt.show()

def grafico_grosor_piel(df, paciente_valor=None):
    plt.figure(figsize=(8, 6))
    sns.histplot(df['GrosorPiel'], bins=20, kde=True, color='purple', label="Distribución")
    if paciente_valor is not None:
        plt.axvline(paciente_valor, color='red', linestyle='--', label="Paciente")
    plt.title('Distribución del Grosor de la Piel')
    plt.xlabel('Grosor de la Piel')
    plt.ylabel('Densidad')
    plt.legend()
    plt.show()

def grafico_insulina(df, paciente_valor=None):
    plt.figure(figsize=(8, 6))
    sns.histplot(df["Insulina"], kde=False, bins=15, color="purple", label="Distribución")
    if paciente_valor is not None:
        plt.axvline(paciente_valor, color="red", linestyle="--", label="Paciente")
    plt.title("Distribución de Insulina")
    plt.xlabel("Nivel de Insulina")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.show()

def grafico_imc(df, paciente_valor=None):
    plt.figure(figsize=(8, 6))
    sns.kdeplot(df["IMC"], shade=True, color="red", label="Distribución")
    if paciente_valor is not None:
        plt.axvline(paciente_valor, color="blue", linestyle="--", label="Paciente")
    plt.title("Distribución de IMC")
    plt.xlabel("Índice de Masa Corporal (IMC)")
    plt.ylabel("Densidad")
    plt.legend()
    plt.show()

def grafico_edad(df, paciente_valor=None):
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Edad'], bins=20, kde=True, color='gray', label="Distribución")
    if paciente_valor is not None:
        plt.axvline(paciente_valor, color='red', linestyle='--', label="Paciente")
    plt.title('Distribución de Edad')
    plt.xlabel('Edad')
    plt.ylabel('Densidad')
    plt.legend()
    plt.show()