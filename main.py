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
        self.fondo = '#9bb5b6'
        self.txt_Rec = "Mensaje Recibido: "
        self.read_data()

    def read_data(self):
        self.frame = Tk.Frame(self.__root)
        self.frame['background'] = self.fondo
        self.input = Tk.Entry(self.frame, width=50)
        self.input.grid(row=0, column=1)
        self.n_frames = Tk.Entry(self.frame, width=5)
        self.n_frames.grid(row=1, column=1, sticky=Tk.W)
        button = Tk.Button(self.frame, text='Enter', font=("Arial", 12), command=self.run)
        button.grid(row=0, column=2, sticky=Tk.W, padx=40, pady=2)
        Tk.Label(self.frame, text="Ingrese el numero de tramas: ", font=("Arial", 15), bg=self.fondo).grid(row=1)
        Tk.Label(self.frame, text="Ingrese el mensaje:", font=("Arial", 15), bg=self.fondo).grid(row=0)
        self.__root.bind('<Return>', lambda event: self.run())
        self.frame.pack(pady=30)

    def read_msg(self):
        return str(self.input.get())

    def read_numb(self):
        return int(self.n_frames.get())

    def transmisor(self, labels):

        Tk.Label(self.frame, text="Envia", font=("Arial", 15), bg=self.fondo).grid(row=1, columnspan=2)

        for idx, lbl in enumerate(labels):
            Tk.Label(self.frame, text=lbl, font=("Arial", 8), bg=self.fondo).grid(row=2, column=idx, sticky=Tk.S)

        aux = Tk.Text(self.frame, height=1, width=15, bg=self.fondo)
        aux.grid(row=3, column=0, padx=2, pady=2, sticky=Tk.N)
        self.Tx_Boxes.append(aux)

        for i in range(1, 8):
            aux = Tk.Text(self.frame, height=1, width=5, bg=self.fondo)
            aux.grid(row=3, column=i, padx=2, pady=2, sticky=Tk.N)
            self.Tx_Boxes.append(aux)

        aux = Tk.Text(self.frame, height=1, width=15, bg=self.fondo)
        aux.grid(row=3, column=8, padx=2, pady=2, sticky=Tk.N)
        self.Tx_Boxes.append(aux)

        aux = Tk.Text(self.frame, height=1, width=15, bg=self.fondo)
        aux.grid(row=3, column=9, padx=2, pady=2, sticky=Tk.N)
        self.Tx_Boxes.append(aux)

        self.btn_trans = Tk.Button(self.frame, text='Enviar', font=("Arial", 12),
                                   command=self.transmitir)
        self.btn_trans.grid(row=2, column=11, sticky=Tk.NW, padx=20, pady=2)

    def receptor(self, labels):

        Tk.Label(self.frame, text="Receptor", font=("Arial", 15), bg=self.fondo).grid(row=4, columnspan=2)

        for idx, lbl in enumerate(labels):
            Tk.Label(self.frame, text=lbl, font=("Arial", 8), bg=self.fondo).grid(row=5, column=2*idx+1, sticky=Tk.S)

        for i in range(3):
            aux = Tk.Text(self.frame, height=1, width=15, bg=self.fondo)
            aux.grid(row=6, column=(i*2)+1, padx=2, pady=2, sticky=Tk.N, columnspan=2)
            self.Rc_Boxes.append(aux)
        aux = Tk.Text(self.frame, height=1, width=15, bg=self.fondo)
        aux.grid(row=6, column=7, padx=2, pady=2, sticky=Tk.N)
        self.Rc_Boxes.append(aux)

    def respuesta(self, respondiendo, labels):

        Tk.Label(self.frame, text="Respuesta", font=("Arial", 15), bg=self.fondo).grid(row=7, columnspan=2)

        for idx, lbl in enumerate(labels):
            Tk.Label(self.frame, text=lbl, font=("Arial", 8), bg=self.fondo).grid(row=8, column=idx, sticky=Tk.S)

        aux = Tk.Text(self.frame, height=1, width=15, bg=self.fondo)
        aux.grid(row=9, column=0, padx=2, pady=2, sticky=Tk.N)
        self.Rp_Boxes.append(aux)

        for i in range(1, 8):
            aux = Tk.Text(self.frame, height=1, width=5, bg=self.fondo)
            aux.grid(row=9, column=i, padx=2, pady=2, sticky=Tk.N)
            self.Rp_Boxes.append(aux)

        aux = Tk.Text(self.frame, height=1, width=15, bg=self.fondo)
        aux.grid(row=9, column=8, padx=2, pady=2, sticky=Tk.N)
        self.Rp_Boxes.append(aux)

        aux = Tk.Text(self.frame, height=1, width=15, bg=self.fondo)
        aux.grid(row=9, column=9, padx=2, pady=2, sticky=Tk.N)
        self.Rp_Boxes.append(aux)

        if respondiendo:
            self.btn_resp = Tk.Button(self.frame, text='Responder', font=("Arial", 12), command=self.responder,
                                      state=Tk.DISABLED)
            self.btn_resp.grid(row=6, column=11, sticky=Tk.NW, padx=20, pady=2)

    def transmitir(self):

        if self.state == 0:
            self.state += 1
            self.siguiente_paso(True, False, False, False)
            self.txt_Consola += "Control: Permiso para\n transmitir.\n"
            self.data["rc"] = [self.data.get("tx")[0], "", "", self.data.get("tx")[9]]
        elif self.Num_Trama == self.data.get("n_tramas")-1:
            self.siguiente_paso(False, True, False, True)
            self.enviar()
        else:
            self.siguiente_paso(False, True, False, False)
            self.enviar()

        self.limpiar("tx")

        self.btn_resp['state'] = Tk.NORMAL
        self.btn_trans['state'] = Tk.DISABLED

        self.actualizar()

    def enviar(self):
        self.data["rc"][2] = self.data.get("tramas")[self.Num_Trama]
        msg = ""
        for i in list(self.data.get("tramas")[self.Num_Trama]):
            msg += i
            self.txt_Rec += i
        self.txt_Consola += "Transmisión: Enviando\n Trama: " + str(self.Num_Trama + 1) + " de " + str(
            self.data.get("n_tramas")) + "\n Enviando: " + msg + "\n"
        self.state += 1
        self.Num_Trama += 1

    def responder(self):

        if self.state == 1:
            self.state += 1
            self.txt_Consola += "Control: Listo para\n transmitir.\n"
            self.data["rc"] = [self.data.get("rp")[0], "", "", self.data.get("rp")[9]]
            self.siguiente_paso(False, True, False, False)
            self.data["rp"][7] = "0" + str(self.state - 1)
        elif self.Num_Trama == self.data.get("n_tramas")-1:
            self.state += 1
            self.data["rc"] = [self.data.get("rp")[0], "", "", self.data.get("rp")[9]]
            self.data["tx"] = ["10000001", "01", "11", "00", "11", "00", "00", "0" + str(self.state),
                               self.data.get("tramas")[self.Num_Trama],
                               "10000001"]
            self.txt_Consola += "Transmisión: Recibido\n con Exito: "
        elif self.Num_Trama == self.data.get("n_tramas"):
            self.siguiente_paso(False, False, True, False)
            self.txt_Consola += "Transmisión: Finalizado\n con Exito: "
        else:
            self.state += 1
            self.data["rc"] = [self.data.get("rp")[0], "", "", self.data.get("rp")[9]]
            self.data["tx"] = ["10000001", "01", "00", "00", "11", "00", "00", "0" + str(self.state),
                               self.data.get("tramas")[self.Num_Trama],
                               "10000001"]
            self.txt_Consola += "Transmisión: Recibido\n con Exito: "

        self.limpiar("rp")

        self.btn_resp['state'] = Tk.DISABLED
        self.btn_trans['state'] = Tk.NORMAL

        self.actualizar()

    def limpiar(self, obj):
        aux = ""
        for i in self.data.get(obj)[1:8]:
            aux += i
        self.data["rc"][1] = aux
        self.data[obj] = ["", "", "", "", "", "", "", "", "", ""]

    def siguiente_paso(self, permisos, datos, finalizado, ultimo):
        if permisos:
            self.data["rp"] = ["10000001", "00", "00", "11", "01", "00", "11", "0"+str(self.state), "", "10000001"]
        if datos:
            self.data["tx"] = ["10000001", "01", "00", "00", "11", "00", "00", "0" + str(self.state),
                               self.data.get("tramas")[self.Num_Trama],
                               "10000001"]
            self.data["rp"] = ["10000001", "11", "00", "00", "11", "00", "00", "0" + str(self.state+1),
                               self.data.get("tramas")[self.Num_Trama],
                               "10000001"]
        if ultimo:
            self.data["rp"] = ["10000001", "11", "11", "11", "00", "00", "00", "0" + str(self.state + 1),
                               self.data.get("tramas")[self.Num_Trama],
                               "10000001"]
        if finalizado:
            self.data["rc"] = ["10000001", "", "", "10000001"]
            self.data["tx"] = ["", "", "", "", "", "", "", "", "", ""]

    def actualizar(self):
        for idx, box in enumerate(self.Rp_Boxes):
            box.configure(state='normal')
            box.delete('1.0', Tk.END)
            box.insert('1.0', self.data.get("rp")[idx])
            box.configure(state='disabled')
        for idx, box in enumerate(self.Tx_Boxes):
            box.configure(state='normal')
            box.delete('1.0', Tk.END)
            box.insert('1.0', self.data.get("tx")[idx])
            box.configure(state='disabled')
        for idx, box in enumerate(self.Rc_Boxes):
            box.configure(state='normal')
            box.delete('1.0', Tk.END)
            box.insert('1.0', self.data.get("rc")[idx])
            box.configure(state='disabled')
        self.txt_area.configure(state='normal')
        self.txt_area.delete('1.0', Tk.END)
        self.txt_area.insert('1.0', self.txt_Consola)
        self.txt_area.configure(state='disabled')
        self.resp.configure(text=self.txt_Rec)

    def crear(self):
        labels = [
            "Header",
            "OK",
            "ENQ",
            "CONT",
            "DATOS",
            "SOL",
            "LIST",
            "NSL",
            "INFO",
            "Trailer"
        ]
        labels1 = [
            "Header",
            "Protocolo",
            "INFO",
            "Trailer"
        ]
        self.clear()
        self.frame = Tk.Frame(self.__root)
        self.frame['background'] = self.fondo
        Tk.Label(self.frame, text="Mensaje a Transmitir: " + self.data['msg'], font=("Arial", 15), bg=self.fondo).grid(
            row=0, columnspan=13)
        self.transmisor(labels)
        self.receptor(labels1)
        self.respuesta(True, labels)
        self.txt_area = Tk.Text(self.frame, height=30, width=25)
        self.txt_area.grid(row=0, column=13, rowspan=10, padx=50)
        self.resp = Tk.Label(self.frame, text=self.txt_Rec, font=("Arial", 15), bg=self.fondo)
        self.resp.grid(row=10, columnspan=13)

        self.frame.pack(padx=25, pady=30)
        self.actualizar()

    def run(self):
        self.data["msg"] = self.read_msg()
        self.data["n_tramas"] = self.read_numb()
        self.data["tx"] = ["10000001", "00", "00", "11", "00", "11", "00", "00", "", "10000001"]
        self.data["rc"] = ["", "", "", ""]
        self.data["rp"] = ["", "", "", "", "", "", "", "", "", ""]
        self.div_tramas()
        self.crear()

    def div_tramas(self):
        tramas = []
        chars = list(self.data.get("msg"))
        numCar = len(chars)
        n_tramas = int(self.data.get("n_tramas"))
        packets = numCar // n_tramas
        if numCar % 2 == 0:
            for i in range(n_tramas):
                tramas.append(chars[(i * packets):(i * packets) + packets])
        else:
            for i in range(n_tramas):
                if i == n_tramas - 1:
                    tramas.append(chars[(i * packets):len(chars)])
                else:
                    tramas.append(chars[(i * packets):(i * packets) + packets])
        self.data["tramas"] = tramas

    def clear(self):
        for widget in root.winfo_children():
            widget.destroy()
        self.frame.pack_forget()

    def restart(self):
        self.clear()
        self.__init__(self.__root)


if __name__ == '__main__':
    root = Tk.Tk()
    screen = Protocolo(root)
    root.title("Protocolo de Enlace de Datos")
    root.geometry("1350x700")
    root['background'] = '#9bb5b6'
    root.update()
    root.mainloop()