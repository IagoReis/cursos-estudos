print("Olá João, o valor da sua fatura é de R$999.99")
print("Olá {}, o valor da sua fatura é de R$ {}".format("João", 999.99))
print("Olá {}, o valor da sua fatura é de R$ {:f}".format("João", 999.99))
print("Olá {}, o valor da sua fatura é de R$ {:.2f}".format("João", 999.99))
print("Olá {}, o valor da sua fatura é de R$ {:8.2f}".format("João", 999.99))
print("Olá {}, o valor da sua fatura é de R$ {:08.2f}".format("João", 999.99))
print("\n\n\n")
print("Olá João, sua fatura está 10 dias em atraso")
print("Olá {}, sua fatura está {} dias em atraso".format("João", 10))
print("Olá {}, sua fatura está {:d} dias em atraso".format("João", 10))
print("Olá {}, sua fatura está {:5d} dias em atraso".format("João", 10))
print("Olá {}, sua fatura está {:05d} dias em atraso".format("João", 10))
ano = 2020
mes = 1
dia = 3
print("Olá {0}, sua fatura está {1:05d} dias em atraso. Venceu em {4:02d}/{3:02d}/{2}".format("João", 10, ano, mes, dia))
