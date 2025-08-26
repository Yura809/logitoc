from gc import is_finalized

from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.minsize(width= 400, height= 300)
        self.title("UI з адаптивним меню ")

        self.is_show_menu = False
        self.frame_width = 0
        self.menu_show_speed = 30


        self.freme = CTkFrame(self, width=0, height=300)
        self.frame.place(x=0, y=0)

        self.label = CTkLabel(self.frame,text="Ваше ім'я")
        self.label.pack(pady=30)
        self.entry = CTkEntry(self.frame)
        self.entry.pack()
        self.label_theme = CTkOptionMenu(self.frame,values=["Темна","Світла"],command=self.change_theme)
        self.label_theme.pack(side="bottom",pady=20)
        # кнопка для відкритя закритя меню
        self.btn = CTkButton(self,text="stop",command=self.toggle_show_menu,width=30)
        self.btn.place(x=0,y=0)
        # поле чату
        self.chat_text = CTkTextbox(self,state="disabled")
        self.chat_text.place(x=0,y=30)
        # поле для вводу повідомлень
        self.message_input = CTkEntry(self,placeholder_text="Ведіть повідомлення:")
        self.message_input.place(x=0,y=250)
        #кнопка надсилання
        self.send_button = CTkButton(self, text="Відправити", width=40, height=30)
        self.send_button.place(x=200,y=250)
        #Викликаємо оновлення UI після відображення вікна
        self.after(100,self.adaptive_ui)
    def toggle_show_show_menu(self):
        self.is_show_menu = not self.is_show_menu
        if self.is_show_menu:
            self.show_menu()
        else:
            self.close_menu()
    def show_menu(self):
        if self.frame_width < 200:
            self.frame_width += self.menu_show_speed
            self.frame.configure(width=self.frame_width)
            self.btn.configure(text="stop",width=self.frame_width)
            self.after(20,self.show_menu)
        else:
            self.frame.configure(width=200)
    def close_menu(self):
        if self.frame_width > 0:
            self.frame_width -= self.menu_show_speed
            self.frame.configure(width=self.frame_width)
            new_text = "право" if self.frame_width <= 30 else "ліво"
            self.btn.configure(text=new_text,width=self.frame_width)
            self.after(20,self.close_menu)
        else:
            self.frame.configure(width=0)


    def change_theme(self,value):
        if value == "Темна":
            set_appearance_mode("dark")
        else:
            set_appearance_mode("light")

    def adaptive_ui(self):
        total_width = self.winfo_width()
        total_height = self.winfo_height()

        menu_width = self.frame_width
        padding_top = 30
        input_height = 30

        self.btn.place(x=menu_width,y=0)
    #Поле чату
    self.chat_text.place("x=menu_widtx,y=padding_top")
    self.chat_text.configure("widtx=total_width - menu_width, height=total_height-input_height - pading_top")
    #поле вводу повідомлення
send_btn_width = self.send_button.winfo_reqwidth()
self.message_imput.place("x=menu_width,y=total_height - imput_height")
self.message_input.configure("width=total_width - menu_width - send_btn_width5")
#Кнопка відправки
self.send_button.place("x=total_width - send_btn_width,y=total_height")

self.after(50,self.adaptive_ui)
