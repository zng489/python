def main(valor1, valor2, valor3):
  #anos = ['2021', '2022', '2023']
  #tipos = ['po', 'cnae']
  #tabs = [
  #    '2.6', '1.7', '2.7', '2.9', '1.11', '2.12', '2.4', '2.5', '1.6', '2.13', '1.8', '1.4', 'Pandemia',
  #    '1.12', '2.10', '1.9', '1.3', '1.13', '1.5', '2.8', '2.11', '2.2', '1.1', '2.3', '1.10', '2.1', '1.2'
  #]
  prod1 = df.select(f'{valor1}').distinct().rdd.map(lambda row: row[0]).collect()
  prod2 = df.select(f'{valor2}').distinct().rdd.map(lambda row: row[0]).collect()
  prod3 = df.select(f'{valor3}').distinct().rdd.map(lambda row: row[0]).collect()

  combinacoes = list(product(prod1, prod2, prod3))

  # Exemplo: imprimir as 5 primeiras combinações
  for combo in combinacoes:
    #combinacoes[:5]
    df_filtrado = df.filter(col(f"{valor1}") == combo[0]).filter(col(f"{valor2}") == combo[1]).filter(col(f"{valor3}") == combo[2])
    if df_filtrado.count():
      #print(df_filtrado.count())
      print(f"✅ {combo[0]}, {combo[1]}, {combo[2]} → {df_filtrado.count()} registros encontrados.")
    else:
      continue



def exemplo():
    for i in range(5):
        print(f"Valor de i: {i}")
        return

# 📌 O que acontece?
# O for vai tentar rodar de i = 0 até i = 4.

# Mas logo na 1ª iteração (i = 0), o return é executado.

# Isso interrompe a função inteira imediatamente.

# O loop não vai para o i = 1, i = 2, etc. Ele para ali mesmo.