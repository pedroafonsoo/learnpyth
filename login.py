import hash as h

email = input("Introduza o seu email:\n")
password = input("Introduza a sua password:\n")
pos_at = email.find("@")
if (pos_at != -1):
    nome = email[0:pos_at]
    print("Olá", nome, " bem-vindo à linguagem de programação Python")
    print("A sua password é:" + password)
    #Encript password
    #print("A sua password é:" + h.hash_password(password))
else:
    print("email incorreto")
