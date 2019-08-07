from _testbuffer import ndarray

from Register import Register


nome_user= input("Introduza o nome do utilizador para efeitos de registo:\n")
password= input("Introduza a password do utilizador para efeitos de registo:\n")
reg=Register()
reg.register_user(nome_user,password)
# verificar o tipo de variavel
print(type(reg))
