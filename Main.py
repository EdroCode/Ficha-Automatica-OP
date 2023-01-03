import atributes


def main():

    Atributos()



def Atributos():

    # Atributos

    Agilidade = 1
    Força = 1
    Presença = 1 
    Intelecto = 1
    Vigor = 1


    print("""
    
    """)
    print("Para começar vamos distribuir os Atributos.")
    print("Quando crias um personagem, os teus atributos começam em 1 e recebes 4 pontos para distribuir entre eles, podendo reduzir um atributo para 0 para receber 1 ponto.")
    print("""
    
Agilidade: 1
Força: 1
Presença: 1 
Intelecto: 1
Vigor: 1
    
    """)
    print("Seleciona o atributo que queres mudar")
    Change_Atributes()



def Change_Atributes(Agilidade, Força, Presença, Intelecto, Vigor):

    print("Atributos:")
    print(f"""
[1] Agilidade: {Agilidade}
[2] Força: {Força}
[3] Presença: {Presença}
[4] Intelecto: {Intelecto}
[5] Vigor: {Vigor}
""")

    user_input = input(print("Seleciona o Atributo que queres alterar: "))

    while user_input not in ["1","2","3","4","5"]:

        pass

    else:

        if user_input == "1":
        
            x = int(input("Seleciona a quantidade de pontos: "))
            Agilidade = x
            Show_Atributes()
        
        if user_input == "2":
        
            x = int(input("Seleciona a quantidade de pontos: "))
            Força = x
            Show_Atributes()

        if user_input == "3":
        
            x = int(input("Seleciona a quantidade de pontos: "))
            Presença = x
            Show_Atributes()

        if user_input == "4":
                
            x = int(input("Seleciona a quantidade de pontos: "))
            Intelecto = x
            Show_Atributes()

        if user_input == "5":
                
            x = int(input("Seleciona a quantidade de pontos: "))
            Vigor = x
            Show_Atributes()


def Show_Atributes(Agilidade, Força, Presença, Intelecto, Vigor):

    print("Atributos:")
    print(f"""
[1] Agilidade: {Agilidade}
[2] Força: {Força}
[3] Presença: {Presença}
[4] Intelecto: {Intelecto}
[5] Vigor: {Vigor}
""")

    print("Seleciona o que queres fazer:")
    print("[1]Alterar Atributo")
    print("[2]Próxima Fase")
    user_input = input("")

    while user_input not in ["1","2"]:

        print("Wrong Input")
        user_input = input("")

    else:

        if user_input == "1":

            Change_Atributes()

        if user_input == "2":

            
            pass










if __name__ == "__main__":
    main()




