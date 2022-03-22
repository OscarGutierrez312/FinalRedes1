import tkinter as Tk


class Protocolo():
    def __init__(self, root):
        self.__root = root
        self.read_data()

    def read_data(self):
        self.frame = Tk.Frame(self.__root)
        Tk.Label(self.frame,
                 text="Ingrese el mensaje",
                 font=("Arial", 15)).grid(row=0)

        self.input = Tk.Entry(self.frame, width=25)

        self.input.grid(row=0, column=1)

        Tk.Button(self.frame,
                  text='Enter',
                  font=("Arial", 12),
                  command=self.run).grid(row=3,
                                     column=1,
                                     sticky=Tk.W,
                                     pady=4)

        self.frame.pack(pady=150)

    def read(self):
        return str(self.input.get())

    def run(self):
        str = self.read()
        self.clear()
        self.print(self.transform(str))

    def print(self, data):
        self.config(data)
        self.axis.plot(data[0], data[1])


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
    root.geometry("700x700")
    root.update()
    root.mainloop()