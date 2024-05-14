import threading
import socket
import tkinter
from tkinter import simpledialog
from tkinter import scrolledtext

class Client:
    
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        
        msg = tkinter.Tk()
        msg.withdraw()
        self.nickname = simpledialog.askstring("NICKNAME", "Choose nickname:")
        
        self.gui_done = False
        self.running = True
        
        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)
        
        gui_thread.start()
        receive_thread.start()
    
    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg='Lightgray')
        
        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="lightgray")
        self.chat_label.config(state='disabled')
        self.chat_label.pack(padx=20, pady=5)
        
        self.text_area = scrolledtext.ScrolledText(self.win)
        self.text_area.config(font=("Arial", 12))
        self.text_area.pack(padx=20, pady=5)
        
        self.msg_label = tkinter.Label(self.win, text="Message:", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)
        
        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)
        
        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)
        
        self.gui_done = True
        
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()
        
    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end-1c')}" 
        message += '\n'
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')

                
    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)
        
    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(2048).decode('utf-8')  
                if message == "NickName":  # Compare with string
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)
                        self.text_area.yview('scroll', -1, 'units')
                        self.text_area.config(state='disable')
            except Exception as e:
                print("Error:", e)
                self.sock.close()
                break

if __name__ == "__main__":
    client = Client("127.0.0.1", 4010)

