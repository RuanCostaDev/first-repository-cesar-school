rendaMensal = float(input("Insira sua renda mensal: "))
if(rendaMensal <= 2112.00):
  print("Isento")
elif rendaMensal >= 2112.01 and rendaMensal <= 2826.65:
  print("Alíquota = 7,5")
elif rendaMensal >= 2826.66 and rendaMensal <= 3751.05:
  print("Alíquota = 15")
elif rendaMensal >= 3751.06 and rendaMensal <= 4664.68:
  print("Alíquota = 22,5")
else:
  print("Alíquota = 27,5")
