import pandas

excel_file = "lista_nomes.xlsx"

df_data = pandas.read_excel(excel_file, header=1)
print(df_data)

soma = 0

print("Sistema Operacional Android: ")
for posicao in range(len(df_data)):
    nome = df_data.iloc[posicao]["NOME"]
    sistema = df_data.iloc[posicao]["SISTEMA"] 
    if isinstance(sistema,str):
        
        if "Android" in sistema:
          soma += 1
        
        
print(soma)
