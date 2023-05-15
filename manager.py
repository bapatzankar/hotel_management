from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_Win

class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #----------------LOGO-------------------
        img_logo = Image.open('images/hotel_logo.jpg')
        img_logo = img_logo.resize((230,140),Image.ANTIALIAS)
        self.photoimg_logo = ImageTk.PhotoImage(img_logo)

        lblimg_logo = Label(self.root,image=self.photoimg_logo,bd=4,relief=RIDGE)
        lblimg_logo.place(x=0,y=0,width=230,height=140)
        
        #-----------------BOARD------------------
        img_board = Image.open('images/hotel_board.jpg')
        img_board = img_board.resize((1320,140),Image.ANTIALIAS)
        self.photoimg_board = ImageTk.PhotoImage(img_board)

        lblimg_board = Label(self.root,image=self.photoimg_board,bd=4,relief=RIDGE)
        lblimg_board.place(x=230,y=0,width=1320,height=140)

        #-----------------TITLE------------------
        lbl_title=Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #-----------------MAIN FRAME-------------
        main_frame=Label(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=610)

        #-----------------MENU------------------
        lbl_menu=Label(main_frame, text="MENU", font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #-----------------BUTTON FRAME----------------
        btn_frame=Label(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0,y=40, width=230, height=190)

        cust_btn=Button(btn_frame, text="CUSTOMER", command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame, text="ROOMS",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame, text="DETAILS",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame, text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame, text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #------------------LOBBY IMAGE---------------------
        img_lobby = Image.open('images/lobby.jpeg')
        img_lobby = img_lobby.resize((1315,605),Image.ANTIALIAS)
        self.photoimg_lobby = ImageTk.PhotoImage(img_lobby)

        lblimg_lobby = Label(main_frame,image=self.photoimg_lobby,bd=4,relief=RIDGE)
        lblimg_lobby.place(x=230,y=0,width=1315,height=605)

        #------------------SERVICES---------------------
        #-----------------BUTTON FRAME----------------
        service_frame=Label(main_frame, bd=0)
        service_frame.place(x=0,y=230, width=230)

        img_room = Image.open('images/room.jpeg')
        img_room = img_room.resize((220,175),Image.ANTIALIAS)
        self.photoimg_room = ImageTk.PhotoImage(img_room)
        
        lblimg_room = Label(service_frame,image=self.photoimg_room,bd=4,relief=RIDGE)
        lblimg_room.grid(row=0,column=0,pady=1)
        
        img_food = Image.open('images/food.jpeg')
        img_food = img_food.resize((220,175),Image.ANTIALIAS)
        self.photoimg_food = ImageTk.PhotoImage(img_food)
        
        lblimg_food = Label(service_frame,image=self.photoimg_food,bd=4,relief=RIDGE)
        lblimg_food.grid(row=1,column=0,pady=1)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Cust_Win(self.new_window)









       






root=Tk()
obj = HotelManagementSystem(root)
root.mainloop()