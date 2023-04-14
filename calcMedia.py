def calcMedia():

  print("Calcule a média de uma sequência de números.\n\n");
  
  entradas = [];

  entrada = "";

  while entrada.lower() != "calc":
    entrada = input("Insira um valor numérico ou 'CALC' para encerrar e calcular a média.\n");

    if(entrada.lower() != "calc"):
      entradas.append(int(entrada));

  somatoria = 0;
  
  for valor in entradas:
    somatoria += valor;


  media = somatoria / len(entradas);
  
  print("\n\nA média dos valores inseridos é ", media);
