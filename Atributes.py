

# Atributos

Agilidade = 1
Força = 1
Presença = 1 
Intelecto = 1
Vigor = 1




def Change_Atributes(Agilidade=Agilidade, Força=Força, Presença=Presença, Intelecto=Intelecto, Vigor=Vigor):

    print("Atributos:")
    print(f"""
[1] Agilidade: {Agilidade}
[2] Força: {Força}
[3] Presença: {Presença}
[4] Intelecto: {Intelecto}
[5] Vigor: {Vigor}
""")

    user_input = input("Seleciona o Atributo que queres alterar: ")

    while user_input not in ["1","2","3","4","5"]:

        pass

    else:

        if user_input == "1":
        
            x = int(input("Seleciona a quantidade de pontos: "))
            Agilidade = x
         
        
        if user_input == "2":
        
            x = int(input("Seleciona a quantidade de pontos: "))
            Força = x
           

        if user_input == "3":
        
            x = int(input("Seleciona a quantidade de pontos: "))
            Presença = x
            

        if user_input == "4":
                
            x = int(input("Seleciona a quantidade de pontos: "))
            Intelecto = x
            

        if user_input == "5":
                
            x = int(input("Seleciona a quantidade de pontos: "))
            Vigor = x
            


