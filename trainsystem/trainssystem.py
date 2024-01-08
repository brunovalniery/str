#Sistemas de Tempo Real'
#Bruno Valniery Gomes de Sousa

#Importações necessárias
import threading
from tkinter import *
import time



#Função para visualizar a posição dos trens na janela
def visualizarPosicaoDosTrens(window):
    window.geometry("400x550")    

    trilhoVerde = canvas.create_rectangle(20, 20, 380, 120, outline="green", width="5")
    trilhoAmarelo = canvas.create_rectangle(20, 150, 185, 250, outline="yellow", width="5")
    trilhoAzul = canvas.create_rectangle(220, 150, 380, 250, outline="blue", width="5")
    trilhoVermelho = canvas.create_rectangle(20, 280, 380, 380, outline="red", width="5")


#Função para criar o painel de controle com botões de aumento e diminuição de velocidade
def painelDeControle(window):
    global amarelo
    global azul
    global vermelho
    global verde


    botaoAumentarVelocTremAmarelo= Button(window, text="  +  ", bg='yellow', command= lambda: aumentarVelocidade(amarelo))
    botaoDiminuirVelocTremAmarelo = Button(window, text="  -  ", bg='yellow', command=lambda: diminuirVelocidade(amarelo))
    botaoAumentarVelocTremAmarelo.place(x = 20, y = 450)
    botaoDiminuirVelocTremAmarelo.place(x = 20, y = 500)
    

    botaoAumentarVelocTremAzul= Button(window, text="  +  ", bg='blue', command=lambda: aumentarVelocidade(azul))
    botaoDiminuirVelocTremAzul = Button(window, text="  -  ", bg='blue', command=lambda: diminuirVelocidade(azul))
    botaoAumentarVelocTremAzul.place(x = 120, y = 450)
    botaoDiminuirVelocTremAzul.place(x = 120, y = 500)
   

    botaoAumentarVelocTremVermelho= Button(window, text="  +  ", bg='red', command=lambda: aumentarVelocidade(vermelho))
    botaoDiminuirVelocTremVermelho = Button(window, text="  -  ", bg='red', command= lambda: diminuirVelocidade(vermelho))
    botaoAumentarVelocTremVermelho.place(x = 220, y = 450)
    botaoDiminuirVelocTremVermelho.place(x = 220, y = 500)
    
    botaoAumentarVelocTremVerde = Button(window, text="  +  ", bg='green', command=lambda: aumentarVelocidade(verde))
    botaoDiminuirVelocTremVerde = Button(window, text="  -  ", bg='green', command= lambda: diminuirVelocidade(verde))
    botaoAumentarVelocTremVerde.place(x = 320, y = 450)
    botaoDiminuirVelocTremVerde.place(x = 320, y = 500)
    


#Funcao que aumenta a velocidade que sera utilizado como parametro na funcao time.sleep(velocidadeTremCor)
def aumentarVelocidade(trem):
    global velocidadeTremVerde
    global velocidadeTremVermelho
    global velocidadeTremAmarelo
    global velocidadeTremAzul
    global verde
    global amarelo
    global vermelho
    global azul

    if(trem == verde):
        if(velocidadeTremVerde <= 0.1):
            velocidadeTremVerde = 0.1
        else:
            velocidadeTremVerde -= 0.1
    elif (trem == amarelo):
        if(velocidadeTremAmarelo <= 0.1):
            velocidadeTremAmarelo = 0.1
        else:
            velocidadeTremAmarelo -= 0.1
    elif (trem == vermelho):
        if(velocidadeTremVermelho <= 0.1):
            velocidadeTremVermelho = 0.1
        else:
            velocidadeTremVermelho -= 0.1
    elif (trem == azul):
        if(velocidadeTremAzul <= 0.1):
            velocidadeTremAzul = 0.1
        else:
            velocidadeTremAzul -= 0.1
    else:
        print("cor inválida!")

#Funcao que diminui a velocidade que sera utilizado como parametro na funcao time.sleep(velocidadeTremCor)
def diminuirVelocidade(trem):
    global velocidadeTremVerde
    global velocidadeTremVermelho
    global velocidadeTremAmarelo
    global velocidadeTremAzul
    global verde
    global amarelo
    global vermelho
    global azul

    if(trem == verde):
        if(velocidadeTremVerde >= 2):
            velocidadeTremVerde = 2
        else:
            velocidadeTremVerde += 0.1
    elif (trem == amarelo):
        if(velocidadeTremAmarelo >= 2):
            velocidadeTremAmarelo = 2
        else:
            velocidadeTremAmarelo += 0.1
    elif (trem == vermelho):
        if(velocidadeTremVermelho >= 2):
            velocidadeTremVermelho = 2
        else:
            velocidadeTremVermelho += 0.1
    elif (trem == azul):
        if(velocidadeTremAzul >= 2):
            velocidadeTremAzul = 2
        else:
            velocidadeTremAzul += 0.1
    else:
        print("cor inválida!")


def trilhoVerde(window, canvas):
    global velocidadeTremVerde
    L1=0
    L2=0
    L3=0
    L4=0
    global mutexL3L5
    global mutexL3L13
    global sem1

    tremVerde = canvas.create_rectangle(10, 10, 30, 30, fill="green")

    while(1):
        L1=0
        L2=0
        L3=0
        L4=0
        while (L1<36):
            canvas.move(tremVerde, 10, 0)
            time.sleep(velocidadeTremVerde)    
            L1 = L1+1
        
        while (L2 < 10):
            canvas.move(tremVerde, 0, 10)
            time.sleep(velocidadeTremVerde)  
            L2=L2+1
        
        sem1.acquire()
        mutexL3L13.acquire()
        
        while (L3 < 16):
            canvas.move(tremVerde, -10, 0)
            time.sleep(velocidadeTremVerde)   
            L3=L3+1   
        
        mutexL3L5.acquire()
        mutexL3L13.release()
        
        while (L3 < 36):
            canvas.move(tremVerde, -10, 0)
            time.sleep(velocidadeTremVerde)   
            L3=L3+1

        while (L4 < 10):
            canvas.move(tremVerde, 0, -10)
            time.sleep(velocidadeTremVerde)   
            L4=L4+1
        
        mutexL3L5.release()
        sem1.release()
        
    
                
                  
        

def trilhoAmarelo(window, canvas):
    L5=0
    L6=0
    L7=0
    L8=0
    global mutexL3L5
    global mutexL6L16
    global mutexL7L9
    global sem1
    global sem2
    global velocidadeTremAmarelo

    TremAmarelo = canvas.create_rectangle(10, 240, 30, 260, fill="yellow")

    while(1):
        L5=0
        L6=0
        L7=0
        L8=0
        while (L8 < 10):
            canvas.move(TremAmarelo, 0, -10)
            L8=L8+1
            time.sleep(velocidadeTremAmarelo)
        
        sem1.acquire()
        mutexL3L5.acquire()

        while (L5 < 17):
            canvas.move(TremAmarelo, 10, 0)
            time.sleep(velocidadeTremAmarelo)
            L5=L5+1
        
        mutexL6L16.acquire()
        mutexL3L5.release()
        sem2.acquire()
        sem1.release()
        
                
        while (L6 < 10):
            canvas.move(TremAmarelo, 0, 10) 
            time.sleep(velocidadeTremAmarelo)
            L6=L6+1 
        
        mutexL7L9.acquire()
        mutexL6L16.release()
        #sem2.release()
                
        while (L7<17):
            canvas.move(TremAmarelo, -10, 0)
            time.sleep(velocidadeTremAmarelo)   
            L7 = L7+1
        
        mutexL7L9.release()
        sem2.release()
    
def trilhoAzul(window, canvas):
    L13=0 
    L14=0
    L15=0
    L16=0  
    global mutexL9L15
    global mutexL6L16
    global mutexL3L13
    global sem1
    global sem2
    global velocidadeTremAzul

    TremAzul = canvas.create_rectangle(370, 140, 390, 160, fill="blue")

    while(1):
        L13=0 
        L14=0
        L15=0
        L16=0  
        while (L14<10):
            canvas.move(TremAzul, 0, 10)
            time.sleep(velocidadeTremAzul)   
            L14 = L14+1
        
        sem2.acquire()
        mutexL9L15.acquire()

        while (L15 < 16):
            canvas.move(TremAzul, -10, 0)
            time.sleep(velocidadeTremAzul)
            L15=L15+1
        
        sem1.acquire()
        mutexL6L16.acquire()
        sem2.release()
        mutexL9L15.release()
        
        while (L16 < 10):
            canvas.move(TremAzul, 0, -10)
            time.sleep(velocidadeTremAzul) 
            L16=L16+1
        
        mutexL3L13.acquire()
        mutexL6L16.release()
        sem1.release()
                
        while (L13 < 16):
            canvas.move(TremAzul, 10, 0)
            time.sleep(velocidadeTremAzul)
            L13=L13+1

        mutexL3L13.release()


def trilhoVermelho(window, canvas):
    L9=0
    L10=0
    L11=0
    L12=0
    global velocidadeTremVermelho
    global mutexL7L9
    global mutexL9L15
    global sem2

    TremVermelho = canvas.create_rectangle(10, 370, 30, 390, fill="red")

    while(1):
        L9=0
        L10=0
        L11=0
        L12=0
        while (L12 < 10):
            canvas.move(TremVermelho, 0, -10)
            time.sleep(velocidadeTremVermelho)
            L12=L12+1
        
        sem2.acquire()
        mutexL7L9.acquire()        

        while (L9 < 15):
            canvas.move(TremVermelho, 10, 0) 
            time.sleep(velocidadeTremVermelho)
            L9=L9+1

        mutexL9L15.acquire()
        mutexL7L9.release()
        


        while (L9 < 36):
            canvas.move(TremVermelho, 10, 0)
            time.sleep(velocidadeTremVermelho) 
            L9=L9+1
        
        mutexL9L15.release()

        while (L10 < 10):
            canvas.move(TremVermelho, 0, 10)
            time.sleep(velocidadeTremVermelho)  
            L10=L10+1 

        while (L11 < 36):
            canvas.move(TremVermelho, -10, 0)
            time.sleep(velocidadeTremVermelho) 
            L11=L11+1
                        
        sem2.release()
   

mutexL3L5 = threading.Lock()
mutexL3L13 = threading.Lock()
mutexL6L16 = threading.Lock()
mutexL7L9= threading.Lock()
mutexL9L15 = threading.Lock()


#criando e inicializando semaforos
sem1 = threading.Semaphore(2) #cruzamento do primeiro conjunto de trilhos (L2, L7 e 13)
sem2 = threading.Semaphore(2) #cruzamento do segundo conjunto de trilhos (L6, L11 e L14)

# variaveis que identificam qual o trem atraves de um valor int para serem utilizadas a ex: command=lambda: aumentarVelocidade(azul)
verde = 1 
vermelho = 2
amarelo = 3
azul = 4

#variaveis que controlam a velocidade dos trens
velocidadeTremAmarelo = 1
velocidadeTremAzul = 1
velocidadeTremVermelho = 1
velocidadeTremVerde = 1

window = Tk()
canvas = Canvas(window, width=400, height=400)
canvas.pack()

#criação das threads
t1 = threading.Thread(target=visualizarPosicaoDosTrens, args=[window] )
t2 = threading.Thread(target=trilhoVerde, args=[window, canvas] )
t3 = threading.Thread(target=trilhoVermelho, args=[window, canvas] )
t4 = threading.Thread(target=trilhoAmarelo, args=[window, canvas] )
t5 = threading.Thread(target=trilhoAzul, args=[window, canvas] )
t6 = threading.Thread(target=painelDeControle, args=[window] )

# inicia as threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

window.mainloop()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()