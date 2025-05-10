import random 
import time 
import customtkinter as ctk

"""
palabras=["raton","arbol"]

clave= random.choice(palabras)

acierto=False

while not acierto : 

    entrada= input("introduce palabra\n")
    

    if entrada== clave: 
        palabras.remove(clave)
        if len(palabras)==0 :
            print("lo lograste pedazo de hijo dasdfaflsa\n") 
            break
        print("felicidades pedazo de mono\n")
        
        clave=random.choice(palabras) 

    else:
        contadorA=0
        contadorB=0  
        for i in clave:
            contadorB=0 
            for j in entrada: 
                if i==j :
                    if contadorA== contadorB:
                        print("Letra correcta = ",i,j,contadorA,contadorB)
                    else:
                        print("Letra correcta, posicion inconrrecta",i,j,contadorA,contadorB)
                else:
                    print("Letra incorrecta, posicion incorrecta",i,j,contadorA,contadorB)
                contadorB+=1
            contadorA+=1 """
class MyCheckboxFrame(ctk.CTkFrame):

    def __init__(self, master,values):
        super().__init__(master)
        self.values= values
        self.checkboxes=[]

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10,0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Mi app")
        self.geometry("400x600")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame= MyCheckboxFrame(self, values=["value 1","value 2","value 3"])
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsw")

        self.button = ctk.CTkButton(self, text="Boton", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        print("Chequeo de Cajas:", self.checkbox_frame.get())

app = App()
app.mainloop()

            
            
        

                












