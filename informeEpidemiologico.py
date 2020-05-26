import pandas as pd

def Test():
    pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/input/ReporteDiario/CamasHospital_Diario.csv").to_csv("Test.csv")
    
Test()

if __name__ == '__main__':
    Test()