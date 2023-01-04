import Atributes
import time



def main():

    Atributos()



def Atributos():

    

    time.sleep(1)
    print("""
    
    """)
    print("Para começar vamos distribuir os Atributos.")
    time.sleep(1)
    print("Quando crias um personagem, os teus atributos começam em 1 e recebes 4 pontos para distribuir entre eles, podendo reduzir um atributo para 0 para receber 1 ponto.")
    time.sleep(1)
    print("""
    
Agilidade: 1
Força: 1
Presença: 1 
Intelecto: 1
Vigor: 1
    
    """)
    time.sleep(1)
    print("Seleciona uma opção: ")
    print("[1] Mudar Atributos")
    print("[2] Próxima Fase")
    print("[3] Verificar Atributos")
    print("")
    user_input = input("")

    while user_input not in ["1","2","3"]:

        print("Wrong Input")
        user_input = input("")

    else:

        if user_input == "1":

            Atributes.Change_Atributes()
  











if __name__ == "__main__":
    main()




