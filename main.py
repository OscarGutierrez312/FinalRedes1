import tkinter as Tk


class Protocolo():
    def __init__(self, root):
        self.__root = root
        self.txt_Consola = ""
        self.data = {}
        self.state = 0
        self.Rp_Boxes = []
        self.Tx_Boxes = []
        self.Rc_Boxes = []
        self.Num_Trama = 0
        self.txt_Rec = "Mensaje Recibido: "
        self.read_data()

    def read_data(self):
        self.frame = Tk.Frame(self.__root)
        self.frame['background']='#c1e6f6'
        Tk.Label(self.frame,
                 text="Ingrese el mensaje:",
                 font=("Arial", 15)).grid(row=0)

        self.input = Tk.Entry(self.frame, width=50)

        self.input.grid(row=0, column=1)

        Tk.Button(self.frame, text='Enter', font=("Arial", 12), command=self.run).grid(row=0, column=2, sticky=Tk.W, padx=40, pady=2)

        Tk.Label(self.frame,
                 text="Ingrese el numero de tramas: ",
                 font=("Arial", 15)).grid(row=1)

        self.n_frames = Tk.Entry(self.frame, width=5)

        self.n_frames.grid(row=1, column=1, sticky=Tk.W)

        self.frame.pack(pady=30)

    def read_msg(self):
        return str(self.input.get())

    def read_numb(self):
        return int(self.n_frames.get())

    def transmisor(self, transmitiendo):

        Tk.Label(self.frame, text="Transmisor", font=("Arial", 15)).grid(row=1, columnspan=2)

        Tk.Label(self.frame, text="Header", font=("Arial", 5)).grid(row=2, column = 0)
        Tk.Label(self.frame, text="OK", font=("Arial", 5)).grid(row=2, column=1)
        Tk.Label(self.frame, text="ENQ", font=("Arial", 5)).grid(row=2, column=2)
        Tk.Label(self.frame, text="CONT", font=("Arial", 5)).grid(row=2, column=3)
        Tk.Label(self.frame, text="DATOS", font=("Arial", 5)).grid(row=2, column=4)
        Tk.Label(self.frame, text="SOL", font=("Arial", 5)).grid(row=2, column=5)
        Tk.Label(self.frame, text="LIST", font=("Arial", 5)).grid(row=2, column=6)
        Tk.Label(self.frame, text="N° Tr", font=("Arial", 5)).grid(row=2, column=7)
        Tk.Label(self.frame, text="INFO", font=("Arial", 5)).grid(row=2, column=8)
        Tk.Label(self.frame, text="Trailer", font=("Arial", 5)).grid(row=2, column=9)


        aux=Tk.Text(self.frame, height=1, width=15)
        aux.grid(row=3, column=0, padx=2, pady=2, sticky=Tk.N)

        self.Tx_Boxes.append(aux)

        for i in range(1, 8):
            aux=Tk.Text(self.frame, height=1, width=5)
            aux.grid(row=3, column=i, padx=2, pady=2, sticky=Tk.N)
            self.Tx_Boxes.append(aux)

        aux = Tk.Text(self.frame, height=1, width=15)
        aux.grid(row=3, column=8, padx=2, pady=2, sticky=Tk.N)

        self.Tx_Boxes.append(aux)

        aux =Tk.Text(self.frame, height=1, width=15)
        aux.grid(row=3, column=9, padx=2, pady=2, sticky=Tk.N)

        self.Tx_Boxes.append(aux)

        if transmitiendo:
            Tk.Button(self.frame, text='Enviar', font=("Arial", 12), command=self.transmitir).grid(row=2, column=11,
                                                                                                     sticky=Tk.NW,
                                                                                                     padx=20, pady=2)


    def receptor(self):

        Tk.Label(self.frame, text="Receptor",font=("Arial", 15)).grid(row=4, columnspan=2)
        Tk.Label(self.frame, text="Header", font=("Arial", 5)).grid(row=5, column=2)
        Tk.Label(self.frame, text="ENCAP", font=("Arial", 5)).grid(row=5, column=4)
        Tk.Label(self.frame, text="INFO", font=("Arial", 5)).grid(row=5, column=6)
        Tk.Label(self.frame, text="Trailer", font=("Arial", 5)).grid(row=5, column=7)


        for i in range(3):
            aux=Tk.Text(self.frame, height=1, width=15)
            aux.grid(row=6, column=(i*2)+1, padx=2, pady=2, sticky=Tk.N, columnspan=2)
            self.Rc_Boxes.append(aux)
        aux = Tk.Text(self.frame, height=1, width=15)
        aux.grid(row=6, column=7, padx=2, pady=2, sticky=Tk.N)
        self.Rc_Boxes.append(aux)

    def respuesta(self, respondiendo):


        Tk.Label(self.frame, text="Respuesta", font=("Arial", 15)).grid(row=7, columnspan=2)

        Tk.Label(self.frame, text="Header", font=("Arial", 5)).grid(row=8, column=0)
        Tk.Label(self.frame, text="OK", font=("Arial", 5)).grid(row=8, column=1)
        Tk.Label(self.frame, text="ENQ", font=("Arial", 5)).grid(row=8, column=2)
        Tk.Label(self.frame, text="CONT", font=("Arial", 5)).grid(row=8, column=3)
        Tk.Label(self.frame, text="DATOS", font=("Arial", 5)).grid(row=8, column=4)
        Tk.Label(self.frame, text="SOL", font=("Arial", 5)).grid(row=8, column=5)
        Tk.Label(self.frame, text="LIST", font=("Arial", 5)).grid(row=8, column=6)
        Tk.Label(self.frame, text="N° Tr", font=("Arial", 5)).grid(row=8, column=7)
        Tk.Label(self.frame, text="INFO", font=("Arial", 5)).grid(row=8, column=8)
        Tk.Label(self.frame, text="Trailer", font=("Arial", 5)).grid(row=8, column=9)

        aux = Tk.Text(self.frame, height=1, width=15)
        aux.grid(row=9, column=0, padx=2, pady=2, sticky=Tk.N)
        self.Rp_Boxes.append(aux)

        for i in range(1, 8):
            aux=Tk.Text(self.frame, height=1, width=5)
            aux.grid(row=9, column=i, padx=2, pady=2, sticky=Tk.N)
            self.Rp_Boxes.append(aux)

        aux = Tk.Text(self.frame, height=1, width=15)
        aux.grid(row=9, column=8, padx=2, pady=2, sticky=Tk.N)
        self.Rp_Boxes.append(aux)

        aux = Tk.Text(self.frame, height=1, width=15)
        aux.grid(row=9, column=9, padx=2, pady=2, sticky=Tk.N)
        self.Rp_Boxes.append(aux)

        if respondiendo:
            Tk.Button(self.frame, text='Responder', font=("Arial", 12), command=self.responder).grid(row=6, column=11, sticky=Tk.NW,
                                                                                           padx=20, pady=2)


    def transmitir(self):

        if self.state == 0:
            self.state += 1
            self.siguiente_paso(True, False, False)
            self.txt_Consola += "Control: Permiso para\n transmitir.\n"
            self.data["rc"] = [self.data.get("tx")[0], "", "", self.data.get("tx")[9]]

        else:

            self.siguiente_paso(False, True, False)
            self.data["rc"][2] = self.data.get("tramas")[self.Num_Trama]
            msg = ""
            for i in list(self.data.get("tramas")[self.Num_Trama]):
                msg += i
                self.txt_Rec += i
            self.txt_Consola += "Transmisión: Enviando\n Trama: " + str(self.Num_Trama+1) + " de " + str(
                self.data.get("n_tramas")) + "\n Enviando: " + msg + "\n"
            self.state += 1
            self.Num_Trama += 1

        aux = ""
        for i in self.data.get("tx")[1:8]:
            aux += i

        self.data["rc"][1] = aux
        self.data["tx"] = ["", "", "", "", "", "", "", "", "","",""]

        self.actualizar()


    def responder(self):

        #self.state += 1
        #self.data["rp"][2] = str(self.state)
        if self.state == 1:
            self.state += 1
            self.txt_Consola += "Control: Listo para\n transmitir.\n"
            self.data["rc"] = [self.data.get("rp")[0], "", "", self.data.get("rp")[9]]
            #self.data["tx"] = ["10000001", "00", "00", "11", "01", "00", "11", "0" + str(self.state + 1), "", "10000001"]
            self.siguiente_paso(False, True, False)
            self.data["rp"][7] = "0" + str(self.state - 1)
        elif self.Num_Trama == self.data.get("n_tramas"):
            self.siguiente_paso(False, False, True)
            self.txt_Consola += "Transmisión: Finalizado\n con Exito: "
        else:
            self.state += 1
            self.data["rc"] = [self.data.get("rp")[0], "", "", self.data.get("rp")[9]]
            self.data["tx"] = ["10000001", "01", "00", "00", "11", "00", "00", "0" + str(self.state),
                               self.data.get("tramas")[self.Num_Trama],
                               "10000001"]
            self.txt_Consola += "Transmisión: Recibido\n con Exito: "

        aux = ""
        for i in self.data.get("rp")[1:8]:
            aux += i
        self.data["rc"][1] = aux
        self.data["rp"] = ["", "", "", "", "", "", "", "", "",""]
        self.actualizar()

    def siguiente_paso(self, permisos, datos, finalizado):
        if permisos:
            self.data["rp"] = ["10000001","00","00","11","01","00","11","0"+str(self.state),"", "10000001"]
        if datos:
            self.data["tx"] = ["10000001", "01", "00", "00", "11", "00", "00", "0" + str(self.state), self.data.get("tramas")[self.Num_Trama],
                               "10000001"]
            self.data["rp"] = ["10000001", "11", "00", "00", "11", "00", "00", "0" + str(self.state+1),self.data.get("tramas")[self.Num_Trama],
                               "10000001"]
        if finalizado:
            self.data["rc"] = ["", "", "", ""]
            self.data["tx"] = ["", "", "", "", "", "", "", "", "", ""]
            self.data["rp"] = ["", "", "", "", "", "", "", "", "", ""]

    def actualizar(self):
        print(self.state)

        for idx, box in enumerate(self.Rp_Boxes):
            box.delete('1.0', Tk.END)
            box.insert('1.0',self.data.get("rp")[idx])

        for idx, box in enumerate(self.Tx_Boxes):
            box.delete('1.0', Tk.END)
            box.insert('1.0',self.data.get("tx")[idx])

        for idx, box in enumerate(self.Rc_Boxes):
            box.delete('1.0', Tk.END)
            box.insert('1.0',self.data.get("rc")[idx])

        self.txt_area.delete('1.0', Tk.END)
        self.txt_area.insert('1.0', self.txt_Consola)
        self.resp.configure(text= self.txt_Rec)

    def crear(self):
        self.clear()
        self.frame = Tk.Frame(self.__root)
        self.frame['background'] = '#c1e6f6'
        Tk.Label(self.frame, text="Mensaje a Transmitir: " + self.data['msg'], font=("Arial", 15)).grid(row=0, columnspan=13)
        self.transmisor(True)
        self.receptor()
        self.respuesta(True)
        self.txt_area = Tk.Text(self.frame, height=30, width=25)
        self.txt_area.grid(row=0, column=13, rowspan=10, padx=50)
        self.resp = Tk.Label(self.frame, text=self.txt_Rec, font=("Arial", 15))
        self.resp.grid(row=7, columnspan=13)
        self.frame.pack(padx=25, pady=30)
        self.actualizar()

    def run(self):
        self.data["msg"] = self.read_msg()
        self.data["n_tramas"] = self.read_numb()
        self.data["tx"] = ["10000001","00","00","11","01","11","00","00", "", "10000001"]
        self.data["rc"] = ["","","",""]
        self.data["rp"] = ["","","","","","","","","",""]
        #print(self.data)
        self.div_tramas()
        self.crear()


    def div_tramas(self):
        tramas = []
        chars = list(self.data.get("msg"))
        numCar = len(chars)
        #print(numCar)
        n_tramas = int(self.data.get("n_tramas"))
        packets = numCar // n_tramas
        if numCar % 2 == 0:
            #print(packets)
            for i in range(n_tramas):
                tramas.append(chars[(i * packets):(i * packets) + packets])
        else:
            #print(packets + 1)
            for i in range(n_tramas):
                if i == n_tramas - 1:
                    tramas.append(chars[(i * packets):len(chars)])
                else:
                    tramas.append(chars[(i * packets):(i * packets) + packets])
        self.data["tramas"] = tramas




    def print(self, data):
        pass
        #self.config(data)



    def clear(self):
        for widget in root.winfo_children():
            widget.destroy()
        self.frame.pack_forget()

    def restart(self):
        self.clear()
        self.read_data()



if __name__ == '__main__':
    root = Tk.Tk()
    screen = Protocolo(root)
    root.title("Protocolo de Enlace de Datos")
    root.geometry("1300x700")
    root['background']='#c1e6f6'
    root.update()
    root.mainloop()