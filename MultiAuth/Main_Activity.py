import locale
import os
import pickle
import sqlite3
import tkinter
import time
import platform
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk, ImageSequence


class SeaofBTCapp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (
                WelcomePage, InsertATM, InsertATM2, FaceAuth, FaceAuth2, InputPin, MainMenu, Withdraw,
                WithdrawConfirm,
                Deposit,
                DepositConfirm,
                BalanceQuery, Register_new_user, New_User,reg_card_swipe):  # ,PageThree,PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(WelcomePage)

    # def show_frame(self, cont):
    #     frame = self.frames[cont]
    #     frame.tkraise()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.update()
        frame.event_generate("<<show_frame>>")

    def get_page(self, cont):
        for page in self.frames.values():
            if str(page.__class__.__name__) == cont:
                return page
        return None


class WelcomePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # # self.bind("<<show_frame>>", self.main_prog)
        # top = Toplevel()
        # top.geometry("180x100")
        # top.title("toplevel")
        # l2 = Label(top, text="This is toplevel window").pack()
        # global password
        # password = StringVar
        # entry_1 = None
        #
        # # #############  Function to parse for only numerical input
        # def validate(input):
        #     if input.isdigit():
        #         return True
        #     elif input == "":
        #         return True
        #     else:
        #         return False
        #
        # entry_1 = Entry(top, textvariable=password, width=64, show='*')
        # entry_1.pack()
        # entry_1.focus()
        #
        # reg = top.register(validate)
        # entry_1.config(validate="key", validatecommand=(reg, '%P'))
        #
        # def getpassword(self):
        #     print(password.get(self))
        #
        # okbtn = Button(top, text="Enter", bg="green", fg="black", width=8, height=3,command=getpassword)
        # okbtn.pack()
        #
        #
        #




        def resize_image(event):
            global photo
            new_width = event.width
            new_height = event.height

            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)

            label.config(image=photo)
            label.image = photo  # avoid garbage collection

        # def pin_input():
        #     top = Toplevel()
        #     top.geometry("180x100")
        #     top.title("toplevel")
        #     l2 = Label(top, text="This is toplevel window")
        #     global entry_1
        #     global password
        #     password = StringVar
        #     entry_1 = None
        #     def cleartxtfield():
        #         global password
        #         new = "3"
        #         password.set(new)
        #
        #     # #############  Function to parse for only numerical input
        #     def validate(input):
        #         if input.isdigit():
        #             return True
        #         elif input == "":
        #             return True
        #         else:
        #             return False
        #
        #     def enternumber(x):
        #         global entry_1
        #         setval = StringVar()
        #         setval = str(x)
        #         # print(setval)
        #         entry_1.insert(END, setval)
        #
        #
        #     entry_1 = Entry(top, textvariable=password, width=64, show='*')
        #     entry_1.place(x=200, y=100)
        #     entry_1.focus()
        #
        #     reg = top.register(validate)
        #     entry_1.config(validate="key", validatecommand=(reg, '%P'))
        #
        #     def getcreds():
        #         # check if four digit entered and is not empty
        #         global passwd
        #         passwd = password.get()
        #         print(f"The Credentials are {passwd}")
        #
        #     def funcbackspace():
        #         length = len(entry_1.get())
        #         entry_1.delete(length - 1, 'end')
        #
        #     def killwindow():
        #         #when the user quits it should clear all the data input fields filled in in the previous steps. and should display information that it is about to quit in a few seconds
        #
        #
        #         command = top.destroy()
        #         # Label(top,text="Goodbye\n (Closing in 2 seconds)")
        #         top.after(2000,top.quit())
        #
        #     cancel = Button(top, width=8, height=3, text="Cancel", bg="red", fg="black", command=killwindow)
        #     cancel.place(x=220, y=150)
        #     backspace = Button(top, width=8, height=3, text="Backspace", bg="red", fg="black", command=funcbackspace)
        #     backspace.place(x=500, y=150)
        #
        #     # ----number Buttons------
        #     def enternumber(x):
        #         global entry_1
        #         setval = StringVar()
        #         setval = str(x)
        #         # print(setval)
        #         entry_1.insert(END, setval)
        #
        #     btn_numbers = []
        #     for i in range(10):
        #         btn_numbers.append(
        #             Button(top, width=8, height=3, text=str(i), bd=6, command=lambda x=i: enternumber(x)))
        #     btn_text = 1
        #     for i in range(0, 3):
        #         for j in range(0, 3):
        #             btn_numbers[btn_text].place(x=220 + j * 140, y=250 + i * 100)
        #             btn_text += 1
        #
        #     btn_zero = Button(top, width=15, height=2, text='0', bd=5, command=lambda x=0: enternumber(x))
        #     btn_zero.place(x=330, y=550)
        #     clear = Button(top, text="Clear", bg="green", fg="white", width=8, height=3, command=cleartxtfield)
        #     clear.place(x=220, y=550)
        #     okbtn = Button(top, text="Enter", bg="green", fg="black", width=8, height=3,command=getcreds)
        #     okbtn.place(x=500, y=550)
        #
        # pin_input()


        copy_of_image = Image.open("resource_images/united_bank.png")
        photoimage = ImageTk.PhotoImage(copy_of_image)

        label = Label(self, image=photoimage)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', resize_image)

        top_left_frame = Frame(self, relief='groove', borderwidth=2)
        top_left_frame.place(relx=1, rely=0.1, anchor=NE)
        center_frame = Frame(self, relief='raised', borderwidth=2)
        center_frame.place(relx=0.5, rely=0.75, anchor=CENTER)
        Button(top_left_frame, text='REGISTER', bg='grey', width=14, height=1,
               command=lambda: controller.show_frame(Register_new_user)).pack()
        Button(center_frame, text='ENTER', fg='white', bg='green', width=13, height=2,
               command=lambda: controller.show_frame(InsertATM)).pack()



class Register_new_user(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)

        # self.bind("<<show_frame>>", self.checkexist)

        def resize_image(event):
            global photo
            new_width = event.width
            new_height = event.height

            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)

            label.config(image=photo)
            label.image = photo  # avoid garbage collection

        copy_of_image = Image.open("resource_images/united_bank.png")
        photoimage = ImageTk.PhotoImage(copy_of_image)

        label = Label(self, image=photoimage)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', resize_image)

        top_left_frame = Frame(self, relief='groove', borderwidth=2)
        top_left_frame.place(relx=1, rely=0.1, anchor=NE)
        center_frame = Frame(self, relief='raised', borderwidth=2)
        center_frame.place(relx=0.5, rely=0.75, anchor=CENTER)
        Button(top_left_frame, text='HomeMenu', bg='grey', width=14, height=1,
               command=lambda: controller.show_frame(WelcomePage)).pack()

        #############3 Function to scan new card to check if it exists

        Button(center_frame, text='New  User', fg='white', bg='green', width=13, height=2,
               command=lambda: controller.show_frame(New_User)).pack()




class New_User(Frame):
    def __init__(self, parent, controller):
        # todo make the entry fields to be private so as to be accessible only from within this class
        self.controller = controller
        Frame.__init__(self, parent)
        # import tkinter as tk

        import tkinter.font as tkFont

        global First_Name_entry_value, Sur_Name_entry_value, National_ID_entry_value, Phone_entry_value, Email_entry_value

        #Make them global
        First_Name_lbl = Label(self)
        ft = tkFont.Font(family='Times', size=10)
        First_Name_lbl["font"] = ft
        First_Name_lbl["fg"] = "#333333"
        First_Name_lbl["justify"] = "center"
        First_Name_lbl["text"] = "First Name"
        First_Name_lbl.place(x=280, y=100, width=70, height=25)

        First_Name_entry = Entry(self)
        First_Name_entry["borderwidth"] = "1px"
        First_Name_entry_value = StringVar()
        ft = tkFont.Font(family='Times', size=10)
        First_Name_entry["font"] = ft
        First_Name_entry["fg"] = "#333333"
        First_Name_entry["justify"] = "left"
        First_Name_entry["text"] = "Entry"
        First_Name_entry["textvariable"] = First_Name_entry_value
        First_Name_entry.place(x=420, y=100, width=270, height=25)

        Sur_Name_lbl = Label(self)
        ft = tkFont.Font(family='Times', size=10)
        Sur_Name_lbl["font"] = ft
        Sur_Name_lbl["fg"] = "#333333"
        Sur_Name_lbl["justify"] = "center"
        Sur_Name_lbl["text"] = "Sur Name"
        Sur_Name_lbl.place(x=280, y=160, width=70, height=25)

        Sur_Name_entry = Entry(self)
        Sur_Name_entry["borderwidth"] = "1px"
        Sur_Name_entry_value = StringVar()
        ft = tkFont.Font(family='Times', size=10)
        Sur_Name_entry["font"] = ft
        Sur_Name_entry["fg"] = "#333333"
        Sur_Name_entry["justify"] = "left"
        Sur_Name_entry["text"] = "Entry"
        Sur_Name_entry["textvariable"] = Sur_Name_entry_value
        Sur_Name_entry.place(x=420, y=160, width=270, height=25)

       
        ft = tkFont.Font(family='Times', size=10)
        National_ID_lbl = Label(self)
        National_ID_lbl["font"] = ft
        National_ID_lbl["fg"] = "#333333"
        National_ID_lbl["justify"] = "left"
        National_ID_lbl["text"] = "National ID"
        National_ID_lbl.place(x=270, y=270, width=115, height=25)

        National_ID_entry = Entry(self)
        National_ID_entry_value = StringVar()
        National_ID_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        National_ID_entry["font"] = ft
        National_ID_entry["fg"] = "#333333"
        National_ID_entry["justify"] = "left"
        National_ID_entry["text"] = "Entry"
        National_ID_entry["textvariable"] = National_ID_entry_value
        National_ID_entry.place(x=420, y=270, width=270, height=25)

        # #############  Function to parse for only numerical input
        def validate(input):
            if input.isdigit():
                return True
            elif input == "":
                return True
            else:
                return False

        reg = self.register(validate)
        National_ID_entry.config(validate="key", validatecommand=(reg, '%P'))

        Phone_lbl = Label(self)
        ft = tkFont.Font(family='Times', size=10)
        Phone_lbl["font"] = ft
        Phone_lbl["fg"] = "#333333"
        Phone_lbl["justify"] = "center"
        Phone_lbl["text"] = "Phone"
        Phone_lbl.place(x=280, y=320, width=70, height=25)

        #Country Code Picker

        list1 = ['+91', '+254', '+880', '+32', '+1', '+20', '+49']
        code = StringVar()
        droplist = OptionMenu(self, code, *list1)
        code.set('+254')
        droplist.place(x=420, y=320, width=60, height=25)

        Phone_entry = Entry(self)
        Phone_entry_value = StringVar()
        Phone_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        Phone_entry["font"] = ft
        Phone_entry["fg"] = "#333333"
        Phone_entry["justify"] = "left"
        Phone_entry["text"] = "Entry"
        Phone_entry["textvariable"] = Phone_entry_value
        Phone_entry.place(x=480, y=320, width=210, height=25)
        reg2 = self.register(validate)
        Phone_entry.config(validate="key", validatecommand=(reg2, '%P'))

        Email_lbl = Label(self)
        ft = tkFont.Font(family='Times', size=10)
        Email_lbl["font"] = ft
        Email_lbl["fg"] = "#333333"
        Email_lbl["justify"] = "center"
        Email_lbl["text"] = "Email"
        Email_lbl.place(x=280, y=370, width=70, height=25)

        Email_entry = Entry(self)
        Email_entry_value = StringVar()
        Email_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        Email_entry["font"] = ft
        Email_entry["fg"] = "#333333"
        Email_entry["justify"] = "left"
        Email_entry["text"] = "Entry"
        Email_entry["textvariable"] = Email_entry_value
        Email_entry.place(x=420, y=370, width=270, height=25)

        Head_Title = Label(self)
        ft = tkFont.Font(family='Times', size=18)
        Head_Title["font"] = ft
        Head_Title["fg"] = "#333333"
        Head_Title["justify"] = "center"
        Head_Title["text"] = "BANK AIR: NEW USER REGISTER"
        Head_Title.place(x=330, y=20, width=370, height=25)

        Continue_btn = Button(self)
        Continue_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Continue_btn["font"] = ft
        Continue_btn["fg"] = "#000000"
        Continue_btn["justify"] = "center"
        Continue_btn["text"] = "Continue..."
        Continue_btn.place(x=500, y=520, width=70, height=25)
        Continue_btn["command"] = self.GButton_155_command



    def GRadio_903_command(self):
        print("command")

    def GRadio_341_command(self):
        print("command")

    def GButton_155_command(self):
        # global First_Name_entry_value, Sur_Name_entry_value, National_ID_entry_value, Phone_entry_value, Email_entry_value
        # print("command")

        #todo: populate a database with the above values by creating a program file that performs such an action
        import helper.db_models.New_user_Init.createtestdb as createanew
        #checks if a database already exists and if it doesn't it creates a new DB with entire Schema


        createanew.main()
        #Populate the above values into the exist/created database
        #todo: create a function that takes in all the above entry fields as parameters that are then used to populate the DB
        import helper.db_models.New_user_Init.populate_data_to_tables as populate_db
        # print(First_Name_entry_value.get())
        F_name = First_Name_entry_value.get()
        # print(Sur_Name_entry_value.get())
        S_name = Sur_Name_entry_value.get()
        # print(National_ID_entry_value.get())
        N_ID = National_ID_entry_value.get()
        # print(code.get())
        # print(Phone_entry_value.get())
        P_number = Phone_entry_value.get()
        # print(Email_entry_value.get())
        E_entry = Email_entry_value.get()
        project = (F_name,S_name,N_ID,P_number,E_entry)
        # project = ('tituss', 'kkemboi', 34176984, 720595663, 'cheseremtitus24@gmail.com');
        connection = populate_db.create_connection('cheserem.db')
        populate_db.add_new_user(connection, project)
        #todo: create a module that queries the users table and retrieves the user_id
        import helper.db_models.return_user_id_from_users_table as get_user_id
        user_id_to_pass_to_reg_card_swipe = get_user_id.get_user_id(N_ID,S_name)
        if user_id_to_pass_to_reg_card_swipe != False:
            self.pass_value(user_id_to_pass_to_reg_card_swipe, reg_card_swipe)
        command=self.controller.show_frame(reg_card_swipe)
        



        # step 1: validate the input email is correct

        # from validate_email import validate_email
        # if validate_email(Email_entry_value):
        #     tkinter.messagebox.showinfo("ERROR!", "Please enter valid email(e.g. info@mail.org)")
        # else:
        #     print(First_Name_entry_value)
        #     print(Sur_Name_entry_value)
        #     print(National_ID_entry_value)


        # root.title("undefined")
        # # setting window size
        # width = 1000
        # height = 700
        # screenwidth = root.winfo_screenwidth()
        # screenheight = root.winfo_screenheight()
        # alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # root.geometry(alignstr)
        # root.resizable(width=False, height=False)

        #

        # if __name__ == "__main__":
        #     root = tk.Tk()
        #     app = App(root)
        #     root.mainloop()

class reg_card_swipe(Frame):
    # TODO: pickle the read in card uid

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)

        self.bind("<<show_frame>>", self.onShowFrame)

        self.bind("<<show_frame>>", self.pin_input)

        # Above line ensures the onShowFrame only runs when the
        # Frame is called with the 'windows.show_frame(InsertATM)
        # Note: it is not within the entry program

        def animate(self, counter):
            canvas.itemconfig(image, image=sequence[counter])
            parent.after(250, lambda: animate(self, (counter + 1) % len(sequence)))

        canvas = Canvas(self, width=600, height=500)
        canvas.pack()
        sequence = [ImageTk.PhotoImage(img)
                    for img in ImageSequence.Iterator(
                Image.open(r'resource_images/atmswipe.gif')
            )]
        image = canvas.create_image(200, 200, image=sequence[0])
        animate(self, 1)
        label = Label(self, text="Please Swipe Atm Card to Continue...", font='times 24 bold').pack(pady=10, padx=10)

        # ############################ Run system commands to initialize and execute nfc program to read the card
        # ###################33#

    def pass_value(self, status, next_page):
        some_input = StringVar()
        value = StringVar()
        value = str(status)
        self.some_entry = Entry(self, textvariable=some_input, width=8)
        self.some_entry.pack()
        some_input.set(value)
        self.controller.show_frame(next_page)
        # button1 = Button(self, text='make widget()Confirm and go to page one',
        #                  command=lambda: self.controller.show_frame(next_page))
        # button1.pack()



    def onShowFrame(self, event):
        #todo: save the read in rfid card ID and save it to the database
        if (platform.system() == "Linux"):
            import helper.Linux.FileReader
            Account_uid_compare = helper.Linux.FileReader.reader()

            # save the credentials to cardswipelogger.db for logging
            import helper.db_models.save_log_card_to_db as saver
            saver.sqltable(Account_uid_compare)

            # should save the value to memory sqlitedb for retrieval or save to local
            # file that will serve as a session.
            # time.sleep(3)
        elif (platform.system() == "Windows"):
            #  TODO: employ use of multiprocessing to ensure # Cant seem to find a work around with tkinter !!
            # the tkinter window does not hang when serial module is called
            # TODO: The program hangs when the loop program in arduinoserial read is called find a work around

            # Read the arduino nfc card from COM and save to the file cheserem.key
            access1 = os.access('cheserem.key', os.F_OK)
            if access1:
                os.remove('cheserem.key')
            try:
                #This line reads the RFID UID and saves it to the file cheserem.key
                import helper.Windows.ArduinoSerialCom
            except:
                # TODO: if there is an error i need the system to play a sound for both a success and an error tone
                response = tkinter.messagebox.askyesno("Card Swipe",
                                                       "Card Swipe Error!!!! Please free application port !  Do "
                                                       "you wish to RETRY ?")
                if response == 1:
                    # self.onShowFrame(event)
                    time.sleep(2)
                    command = self.controller.show_frame(reg_card_swipe)
                else:
                    tkinter.messagebox.showinfo("EXIT", "Thank You for Using The UnitedBank")
                    # command = self.controller.show_frame(WelcomePage)
                    self.quit()

            # the reader parses the cheserem.key file and extracts the main key removing unnecessary characters
            # todo check readability an access of a file
            access = os.access('cheserem.key', os.F_OK)
            readability = os.access('cheserem.key', os.R_OK)
            #Check for Arduino Device
            import helper.Windows.check_rfid_avail  as arduino_plugged_status
            ard_status = arduino_plugged_status.is_available()
            print(f"Is Arduino Plugged in {ard_status}")
            if access and readability:
                import helper.Windows.FileReader
                #todo: after the card uid is read in it should first ensure that a similar card does not exist in the system
                card_creds = helper.Windows.FileReader.format_key()
                # save the credentials to cardswipelogger.db for logging
                import helper.db_models.save_log_card_to_db as saver
                saver.sqltable(card_creds)
                # time.sleep(2)

                import Authenticator.cardexist as cardAuth
                #the card exist module returns true if the key[UID] already exists in the db and returns False otherwise

                status = cardAuth.get_status(card_creds)
                print(f"Does the scanned card already exist in the Database? :  {card_creds}")

                #todo: if the card exists the user should receive an alert that the UID is taken and should use another card instead
                #todo: furthermore it should prompt if the user wants to use another card and if so it should restart the class module one last time



                if (not status): #meaning that the uid doesn't exist and the user is now free to continue withe registration process
                    # messagebox = (self,)
                    #todo: access the populate_data_to_tables and add the entries to the card_auth table
                    # you should ensure that the previous class i.e new_user passess the user_id to this module after checking for non-empty string


                    #todo: 1. pass the User_id from the previous class to be used as input for the card_auth user_id entry
                    def get_user_id(self):
                        # retrieves the account_number/RFID-UID from the previous class[InsertATM]
                        startpage = self.controller.get_page("New_User")
                        value = startpage.some_entry.get()
                        # print(f"The received value is {value}")
                        return value
                    users_table_user_id = get_user_id(self)
                    #todo: 2. provide a pop-up window that takes in the user_password and has a confirm password before saving them to the database
                    # solution will be to use tkinter top so that the password input field appears as a pop up that must be filled and should have a
                    # confirm password prompt


                    top = Toplevel(self)
                    top.geometry("180x100")
                    top.title("toplevel")
                    l2 = Label(top, text="This is toplevel window")







                    #todo: 3. When done it should then again pass the User_id to the next face_auth class
                    #todo: 4. only save all the details to the database once user_id, pin , and UID are registered





                    tkinter.messagebox.showinfo("Success", "Card is Registered Successfully")

                    # time.sleep(1)
                    # card_creds_hold = card_creds
                    # print(f"ATM 1 card number is {card_creds_hold} and is being pickled to Verification/InsertATM")
                    #
                    # with open('Verification/InsertATM/insert1.pkl', 'wb') as output:
                    #     pickle.dump(card_creds_hold, output, pickle.HIGHEST_PROTOCOL)
                    # output.close()
                    # print(f"Data being pickled is {card_creds_hold}")
                    #
                    # self.pass_value(card_creds_hold, FaceAuth)

                    # command = self.controller.show_frame(FaceAuth)
                else:
                    # TODO: if there is an error i need the system to play a sound for both a success and an error tone
                    response = tkinter.messagebox.askyesno("Authentication",
                                                           "AUTH CARD INVALID or EXPIRED!!!! You have 1 tries left !  Do "
                                                           "you wish to RETRY ?")
                    if response == 1:
                        # self.onShowFrame(event)
                        time.sleep(2)
                        command = self.controller.show_frame(InsertATM2)




                    else:
                        tkinter.messagebox.showinfo("EXIT", "Thank You for Using The UnitedBank")
                        # command = self.controller.show_frame(WelcomePage)
                        self.quit()

            elif not access and not ard_status:
                time.sleep(0.4)
                tkinter.messagebox.showerror("RFID Missing","Please Connect RFID device to Continue")
                time.sleep(0.6)
                self.controller.show_frame(WelcomePage)









        else:
            print("Unsupported Platform !!!!!!!!!!")

        # TODO: should show a tkinter message that if yes is selected it starts reading card
        # TODO: format the ArduinoSerialCom code to allow for true or false entry
        # TODO: The code should time out after 10 seconds of inactivity and resume on userinput from
        # a prompt

        ############### probs #########33
        # 1 ensure animation automatically resizes to fill whole page

    def pin_input(self):
        pass


class Face_reg_new(Frame):
    def __init__(self, parent, controller):
        self.controller = controller

        Frame.__init__(self, parent)

        self.bind("<<show_frame>>", self.facerec)

        # self.bind("<<show_frame>>",self.print_it)

        def animates(self, counters):
            canvas.itemconfig(image, image=sequence[counters])
            parent.after(250, lambda: animates(self, (counters + 1) % len(sequence)))

        canvas = Canvas(self, width=400, height=400)
        canvas.pack()
        sequence = [ImageTk.PhotoImage(img)
                    for img in ImageSequence.Iterator(
                Image.open(r'resource_images/face_rec.gif')
            )]
        image = canvas.create_image(200, 200, image=sequence[0])
        animates(self, 1)
        label = Label(self, text="Position Camera Face Upward", background='green', font='times 15 bold').pack(pady=10,
                                                                                                               padx=10)

    def facerec(self, event):
        def getuid(self):
            # retrieves the account_number/RFID-UID from the previous class[InsertATM]
            startpage = self.controller.get_page("InsertATM")
            value = startpage.some_entry.get()
            # print(f"The received value is {value}")
            return value

        account_number = getuid(self)
        # This function performs a post request much like a form submit to a website
        # the website checks the two creds i.e. account_number from rfid secton and requests for related  user id.
        # To check for success of authentication there's need to query

        import helper.db_models.returnUIDfromaccounts as getUID
        UID = getUID.return_uid(account_number)
        # returns uid from accounts table that matches read in rfid account_number
        # print(f"The retrieved UID is {UID}")

        # Successfully gotten the related UID from the accounts database
        # The account_number from the rfid is cross-checked against the accounts db and the related
        # UID is retrieved

        import faces

        account = account_number
        id = UID

        with open('Verification/FaceAuth/FaceAuth1.pkl', 'wb') as output:
            pickle.dump(id, output, pickle.HIGHEST_PROTOCOL)
        output.close()
        print(f"Data id being pickled {id}")
        obj = faces.Authenticate_User(account, id)
        before = obj.get__status()
        print(f"Before calling face_rec status is {before}")
        # After calling the below method once it return true it needs to exit
        obj.opencv()
        after_auth = obj.get__status()
        print(f"After calling face_rec status is {after_auth}")

        condition = obj.get__status()
        # condition = True
        # alobj =
        print("hello world " + str(condition))
        # should save the value to memory sqlitedb for retrieval or save to local
        # file that will serve as a session.
        if condition:
            command = self.controller.show_frame(InputPin)
        else:
            print("Face Auth Failed You'll need to retry the authentication again you only have 1 more tries left")
            command = self.controller.show_frame(FaceAuth2)


class InsertATM(Frame):
    # TODO: pickle the read in card uid
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)

        self.bind("<<show_frame>>", self.onShowFrame)

        # Above line ensures the onShowFrame only runs when the
        # Frame is called with the 'windows.show_frame(InsertATM)
        # Note: it is not within the entry program

        def animate(self, counter):
            canvas.itemconfig(image, image=sequence[counter])
            parent.after(250, lambda: animate(self, (counter + 1) % len(sequence)))

        canvas = Canvas(self, width=600, height=500)
        canvas.pack()
        sequence = [ImageTk.PhotoImage(img)
                    for img in ImageSequence.Iterator(
                Image.open(r'resource_images/atmswipe.gif')
            )]
        image = canvas.create_image(200, 200, image=sequence[0])
        animate(self, 1)
        label = Label(self, text="Please Swipe Atm Card to Continue...", font='times 24 bold').pack(pady=10, padx=10)

        # ############################ Run system commands to initialize and execute nfc program to read the card
        # ###################33#

    def pass_value(self, status, next_page):
        some_input = StringVar()
        value = StringVar()
        value = str(status)
        self.some_entry = Entry(self, textvariable=some_input, width=8)
        self.some_entry.pack()
        some_input.set(value)
        self.controller.show_frame(next_page)
        # button1 = Button(self, text='make widget()Confirm and go to page one',
        #                  command=lambda: self.controller.show_frame(next_page))
        # button1.pack()

        # TODO: Finish RFID read on Linux Platform

    def onShowFrame(self, event):
        if (platform.system() == "Linux"):
            import helper.Linux.FileReader
            Account_uid_compare = helper.Linux.FileReader.reader()

            # save the credentials to cardswipelogger.db for logging
            import helper.db_models.save_log_card_to_db as saver
            saver.sqltable(Account_uid_compare)

            # should save the value to memory sqlitedb for retrieval or save to local
            # file that will serve as a session.
            # time.sleep(3)
        elif (platform.system() == "Windows"):
            #  TODO: employ use of multiprocessing to ensure # Cant seem to find a work around with tkinter !!
            # the tkinter window does not hang when serial module is called
            # TODO: The program hangs when the loop program in arduinoserial read is called find a work around

            # Read the arduino nfc card from COM and save to the file cheserem.key
            access1 = os.access('cheserem.key', os.F_OK)
            if access1:
                os.remove('cheserem.key')
            try:
                import helper.Windows.ArduinoSerialCom
            except:
                # TODO: if there is an error i need the system to play a sound for both a success and an error tone
                response = tkinter.messagebox.askyesno("Card Swipe",
                                                       "Card Swipe Error!!!! Please free application port !  Do "
                                                       "you wish to RETRY ?")
                if response == 1:
                    # self.onShowFrame(event)
                    time.sleep(2)
                    command = self.controller.show_frame(InsertATM2)




                else:
                    tkinter.messagebox.showinfo("EXIT", "Thank You for Using The UnitedBank")
                    # command = self.controller.show_frame(WelcomePage)
                    self.quit()

            # the reader parses the cheserem.key file and extracts the main key removing unnecessary characters
            # todo check readability an access of a file
            access = os.access('cheserem.key', os.F_OK)
            readability = os.access('cheserem.key', os.R_OK)
            #Check for Arduino Device
            import helper.Windows.check_rfid_avail  as arduino_plugged_status
            ard_status = arduino_plugged_status.is_available()
            print(f"Is Arduino Plugged in {ard_status}")
            if access and readability:
                import helper.Windows.FileReader
                card_creds = helper.Windows.FileReader.format_key()
                # save the credentials to cardswipelogger.db for logging
                import helper.db_models.save_log_card_to_db as saver
                saver.sqltable(card_creds)
                # time.sleep(2)
                import Authenticator.cardexist as cardAuth
                status = cardAuth.get_status(card_creds)
                print(f"The results came in as {card_creds}")

                if status:
                    # messagebox = (self,)
                    tkinter.messagebox.showinfo("Success", "AUTH CARD SUCCESS")
                    time.sleep(1)
                    card_creds_hold = card_creds
                    print(f"ATM 1 card number is {card_creds_hold} and is being pickled to Verification/InsertATM")

                    with open('Verification/InsertATM/insert1.pkl', 'wb') as output:
                        pickle.dump(card_creds_hold, output, pickle.HIGHEST_PROTOCOL)
                    output.close()
                    print(f"Data being pickled is {card_creds_hold}")

                    self.pass_value(card_creds_hold, FaceAuth)

                    # command = self.controller.show_frame(FaceAuth)
                else:
                    # TODO: if there is an error i need the system to play a sound for both a success and an error tone
                    response = tkinter.messagebox.askyesno("Authentication",
                                                           "AUTH CARD INVALID or EXPIRED!!!! You have 1 tries left !  Do "
                                                           "you wish to RETRY ?")
                    if response == 1:
                        # self.onShowFrame(event)
                        time.sleep(2)
                        command = self.controller.show_frame(InsertATM2)




                    else:
                        tkinter.messagebox.showinfo("EXIT", "Thank You for Using The UnitedBank")
                        # command = self.controller.show_frame(WelcomePage)
                        self.quit()

            elif not access and not ard_status:
                time.sleep(0.4)
                tkinter.messagebox.showerror("RFID Missing","Please Connect RFID device to Continue")
                time.sleep(0.6)
                self.controller.show_frame(WelcomePage)









        else:
            print("Unsupported Platform !!!!!!!!!!")

        # TODO: should show a tkinter message that if yes is selected it starts reading card
        # TODO: format the ArduinoSerialCom code to allow for true or false entry
        # TODO: The code should time out after 10 seconds of inactivity and resume on userinput from
        # a prompt

        ############### probs #########33
        # 1 ensure animation automatically resizes to fill whole page


class InsertATM2(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.bind("<<show_frame>>", self.onShowFrame2)

        def animate(self, counter):
            canvas.itemconfig(image, image=sequence[counter])
            parent.after(250, lambda: animate(self, (counter + 1) % len(sequence)))

        canvas = Canvas(self, width=600, height=500)
        canvas.pack()
        sequence = [ImageTk.PhotoImage(img)
                    for img in ImageSequence.Iterator(
                Image.open(r'resource_images/atmswipe.gif')
            )]
        image = canvas.create_image(200, 200, image=sequence[0])
        animate(self, 1)
        label = Label(self, text="ON LAST TRY...", background="red", font='times 24 bold').pack(pady=10, padx=10)

        # ############################ Run system commands to initialize and execute nfc program to read the card
        # ###################33#

        # 1 Find a code that skips the first init and does not execute the loop program
        # 2 When loop function completes and some content is saved on local disk automatically redirect to the next page

    def pass_value(self, status, next_page):
        some_input = StringVar()
        value = StringVar()
        value = str(status)
        self.some_entry = Entry(self, textvariable=some_input, width=8)
        self.some_entry.pack()
        some_input.set(value)
        self.controller.show_frame(next_page)
        # button1 = Button(self, text='make widget()Confirm and go to page one',
        #                  command=lambda: self.controller.show_frame(next_page))
        # button1.pack()

    def onShowFrame2(self, event):
        if (platform.system() == "Linux"):
            import helper.Linux.FileReader
            Account_uid_compare = helper.Linux.FileReader.reader()

            # save the credentials to cardswipelogger.db for logging
            import helper.db_models.save_log_card_to_db as saver
            saver.sqltable(Account_uid_compare)

            # should save the value to memory sqlitedb for retrieval or save to local
            # file that will serve as a session.
            # time.sleep(3)
        elif (platform.system() == "Windows"):
            #  TODO: employ use of multiprocessing to ensure # Cant seem to find a work around with tkinter !!
            # the tkinter window does not hang when serial module is called

            # Read the arduino nfc card from COM and save to the file cheserem.key
            time.sleep(3)
            print("Initializing the RFID READER")
            try:
                import helper.Windows.ArduinoSerialCom2
                # the reader parses the cheserem.key file and extracts the main key removing unnecessary characters
                import helper.Windows.FileReader as read_format
                card_creds2 = read_format.format_key()
                # print(card_creds)

                # save the credentials to cardswipelogger.db for logging
                import helper.db_models.save_log_card_to_db as saver
                saver.sqltable(card_creds2)
                # time.sleep(2)
                import Authenticator.cardexist as cardAuth
                status2 = cardAuth.get_status(card_creds2)
                print(f"The results came in as {card_creds2}")

                if status2:
                    # messagebox = (self,)

                    tkinter.messagebox.showinfo("Success", "AUTH CARD SUCCESS")
                    time.sleep(1)
                    card_creds2_hold = card_creds2
                    with open('Verification/InsertATM/insert2.pkl', 'wb') as output:
                        pickle.dump(card_creds2_hold, output, pickle.HIGHEST_PROTOCOL)
                    output.close()
                    print(f"Data2 being pickled is {card_creds2_hold}")
                    self.pass_value(card_creds2_hold, FaceAuth2)

                    # command = self.controller.show_frame(FaceAuth)
                else:
                    # TODO: if there is an error i need the system to play a sound for both a success and an error tone
                    tkinter.messagebox.showerror("Authentication",
                                                 "AUTH CARD INVALID or EXPIRED!!!! You have 0 tries left !  Program "
                                                 "Exit ?")
                    self.quit()



            except:
                tkinter.messagebox.showerror("Swipe Error!","Application Port Not Released! Program Exit Reached !!")
                self.quit()
        else:
            print("Unsupported Platform !!!!!!!!!!")


        # TODO: The code should time out after 10 seconds of inactivity and resume on userinput from
        # a prompt

        ############### probs #########33
        # 1 ensure animation automatically resizes to fill whole page




class FaceAuth(Frame):
    def __init__(self, parent, controller):
        self.controller = controller

        Frame.__init__(self, parent)

        self.bind("<<show_frame>>", self.facerec)

        # self.bind("<<show_frame>>",self.print_it)

        def animates(self, counters):
            canvas.itemconfig(image, image=sequence[counters])
            parent.after(250, lambda: animates(self, (counters + 1) % len(sequence)))

        canvas = Canvas(self, width=400, height=400)
        canvas.pack()
        sequence = [ImageTk.PhotoImage(img)
                    for img in ImageSequence.Iterator(
                Image.open(r'resource_images/face_rec.gif')
            )]
        image = canvas.create_image(200, 200, image=sequence[0])
        animates(self, 1)
        label = Label(self, text="Position Camera Face Upward", background='green', font='times 15 bold').pack(pady=10,
                                                                                                               padx=10)

    def facerec(self, event):
        def getuid(self):
            # retrieves the account_number/RFID-UID from the previous class[InsertATM]
            startpage = self.controller.get_page("InsertATM")
            value = startpage.some_entry.get()
            # print(f"The received value is {value}")
            return value

        account_number = getuid(self)
        # This function performs a post request much like a form submit to a website
        # the website checks the two creds i.e. account_number from rfid secton and requests for related  user id.
        # To check for success of authentication there's need to query

        import helper.db_models.returnUIDfromaccounts as getUID
        UID = getUID.return_uid(account_number)
        # returns uid from accounts table that matches read in rfid account_number
        # print(f"The retrieved UID is {UID}")

        # Successfully gotten the related UID from the accounts database
        # The account_number from the rfid is cross-checked against the accounts db and the related
        # UID is retrieved

        import faces

        account = account_number
        id = UID

        with open('Verification/FaceAuth/FaceAuth1.pkl', 'wb') as output:
            pickle.dump(id, output, pickle.HIGHEST_PROTOCOL)
        output.close()
        print(f"Data id being pickled {id}")
        obj = faces.Authenticate_User(account, id)
        before = obj.get__status()
        print(f"Before calling face_rec status is {before}")
        # After calling the below method once it return true it needs to exit
        obj.opencv()
        after_auth = obj.get__status()
        print(f"After calling face_rec status is {after_auth}")

        condition = obj.get__status()
        # condition = True
        # alobj =
        print("hello world " + str(condition))
        # should save the value to memory sqlitedb for retrieval or save to local
        # file that will serve as a session.
        if condition:
            command = self.controller.show_frame(InputPin)
        else:
            print("Face Auth Failed You'll need to retry the authentication again you only have 1 more tries left")
            command = self.controller.show_frame(FaceAuth2)


class FaceAuth2(Frame):
    def __init__(self, parent, controller):
        self.controller = controller

        Frame.__init__(self, parent)

        self.bind("<<show_frame>>", self.facerec)

        def animates(self, counters):
            canvas.itemconfig(image, image=sequence[counters])
            parent.after(250, lambda: animates(self, (counters + 1) % len(sequence)))

        canvas = Canvas(self, width=400, height=400)
        canvas.pack()
        sequence = [ImageTk.PhotoImage(img)
                    for img in ImageSequence.Iterator(
                Image.open(r'resource_images/face_rec.gif')
            )]
        image = canvas.create_image(200, 200, image=sequence[0])
        animates(self, 1)
        label = Label(self, text="Position Camera Face Upward", background='green', font='times 15 bold').pack(pady=10,
                                                                                                               padx=10)
        b2 = Button(self, text="show print from ATM AUTH init", command=lambda: self.print_it())
        b2.pack()

    def facerec(self, event):
        def print_it(self):
            startpage = self.controller.get_page("InsertATM2")
            value = startpage.some_entry.get()
            # if value == "":
            #     startpage = self.controller.get_page("InsertATM2")
            #     value = startpage.some_entry.get()
            print(f"The received value is {value}")
            return value

        account_number = print_it(self)
        # This function performs a post request much like a form submit to a website
        # the website checks the two creds i.e. account_number from rfid secton and the user id.
        # To check for success of authentication there's need to query
        # for Authentication_user.get_Status()

        import helper.db_models.returnUIDfromaccounts as getUID1
        UID = getUID1.return_uid(account_number)
        # print(f"The retrieved UID is {UID}")

        import faces
        # TODO: Add a progress bar to show the state of face recognition
        # TODO: Ensure the user is able to repeat the Auth 4 times such that the progress bar increments by 25% upto the 100%

        self.account = account_number
        self.id = UID

        # Takes in the matching UID and RFID_UID from the accounts table as input

        with open('Verification/FaceAuth/FaceAuth2.pkl', 'wb') as output:
            pickle.dump(self.id, output, pickle.HIGHEST_PROTOCOL)
        output.close()
        print(f"Data id2 being pickled is {self.id}")

        obj = faces.Authenticate_User(self.account, self.id)
        before = obj.get__status()
        print(f"Before calling face_rec status is {before}")
        # After calling the below method once it return true it needs to exit
        obj.opencv()
        after_auth = obj.get__status()
        print(f"After calling face_rec status is {after_auth}")

        # condition = obj.get__status()
        condition = True
        # alobj =
        print("hello world " + str(condition))
        # should save the value to memory sqlitedb for retrieval or save to local
        # file that will serve as a session.
        if condition:
            command = self.controller.show_frame(InputPin)
        else:
            print("Face Auth Failed You'll need to retry the authentication again you have reached the end of your tries")


class InputPin(Frame):
    # Pickle the uid from the facerec class as well as read in account_number from RFID class and then import them here.

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        label = Label(self, text="PIN INPUT", font='times 15 bold')
        label.pack(pady=10, padx=10)
        self.bind("<<show_frame>>", self.main_prog)

        entry_1 = None
        count = 1
        passwd = StringVar

    def main_prog(self, controller):

        global entry_1
        global password

        password = StringVar()

        def loginauth():

            # Unload pickled data
            card_creds_hold = None
            '''
            in order to expell the error of no such file or directory
            there's need to bash:$> touch insert1.pkl,$path/FaceAuth.pkl
            But since echo is installed in all platforms we'll use echo
            to put in an empty string
            Furthermore to prevent corruption of data in the *pkl file
            after a successful read_in the file should be shredded/deleted

            '''
            # Getting the absolute path
            # BASE_DIR = os.path.dirname(os.path.abspath(__file__))

            # TODO: How to check for existence of a file in py

            with open('Verification/InsertATM/insert1.pkl', 'rb') as account_number_ATM_Swipe:
                card_creds_hold= pickle.load(account_number_ATM_Swipe)
            account_number_ATM_Swipe.close()
            print(f"Read in Pickle Value {card_creds_hold}")
            uid_facerec = None
            with open('Verification/FaceAuth/FaceAuth1.pkl', 'rb') as uid_read:
                uid_facerec = pickle.load(uid_read)
            uid_read.close()
            print(f"Read in Pickle uid is {uid_facerec}")

            # TODO: Check if there are any missing read in values and if so inform the user of the errors
            # if error is unrecoverable restart the login session again.

            # Import the pin retrieve class and retrieve the pin
            import helper.db_models.returnpinfromcard_auth as access_pin

            status = access_pin.return_card_pin(card_creds_hold, uid_facerec)
            # Above call to function returns the pin when it exists and returns False if missing

            user_input_pin = password.get()

            if status:
                DB_password = int(status)

                if user_input_pin == str(DB_password):

                    global National_id
                    # National_id = pinobj.return_id()
                    National_id = 34176984

                    print(f"Within pin compare if statement id is {National_id}")

                    # below sql query pre-saves the preset
                    # name/s retrieved from the client table in test.db through use of the National_id

                    def sqlcon():
                        try:
                            conn = sqlite3.connect('test.db')
                            return conn
                        except sqlite3.Error:
                            print('Connection to database failed ' + str(sqlite3.Error))

                    def matching_account(con):
                        mycursor = con.cursor()
                        query = "SELECT Sur_name,First_name from client WHERE National_id = " + str(National_id)
                        status = mycursor.execute(query)
                        if status:
                            global surname
                            global first_name
                            validate = mycursor.fetchone()
                            # print(validate[0])
                            surname = validate[0]
                            first_name = validate[1]

                            print(f"login debug to check retrieval of surname {surname}  and firstname {first_name} ")

                            # # Research on how to catch database errors such assurname = validate[0] TypeError:
                            # 'NoneType' object is not subscriptable

                        # else:
                        #
                        #     tkinter.messagebox.showerror("Error", "ATM Expired or Invalid ")
                        #
                        #     # Should redirect to the Welcome page
                        #
                        #     command = controller.show_frame(WelcomePage)

                    test = sqlcon()
                    matching_account(test)

                    #####     Username  ##############
                    print("surname = " + surname + " first name " + first_name)

                    #### Debug statement

                    # To be more user friendly display (' Welcome #username')

                    # Furthermore on the top left display the username
                    tkinter.messagebox.showinfo("Login", "Welcome " + surname + " " + first_name)
                    command = self.controller.show_frame(MainMenu)
                    password.set('')
                    # and name == 'cheseremtitus'):
                    # command = lambda: controller.show_frame(MainMenu)
                    # Redirect to FACE RECOGNITION PAGE WITHOUT BUTTON CLICK

                else:

                    print("pin incorrect")

                    response = tkinter.messagebox.askyesno("Authentication",
                                                           "PIN Incorrect!!!! You have 2  tries left !  Do you wish to continue ?")

                    if response == 1:  # and count_tries > 0:
                        # tries_counter()
                        # total_tries = count_tries
                        # print(total_tries)
                        password.set("")
                        entry_1.focus()
                    else:
                        password.set("")
                        tkinter.messagebox.showinfo("EXIT", "Thank You for Using BankAir")
                        command = controller.show_frame(WelcomePage)
            else:
                # When read in card_no from ATM_insert and Face_Auth uid fails to be read in/retrieves an Unavailable entry[False]   do the following:

                response = tkinter.messagebox.YES("Authentication",
                                                  "An Unrecoverable Error Occurred! Your Session is Terminated ! A new Session is being set up "
                                                  "Continue ?")

                if response == 1:  # and count_tries > 0:
                    # tries_counter()
                    # total_tries = count_tries
                    # print(total_tries)
                    tkinter.messagebox.showinfo("Recovery Session", "BankAir: Your New Session is a Click Away!")
                    command = controller.show_frame(WelcomePage)

        def cleartxtfield():
            global password
            new = ""
            password.set(new)

        # #############  Function to parse for only numerical input
        def validate(input):
            if input.isdigit():
                return True
            elif input == "":
                return True
            else:
                return False

        entry_1 = Entry(self, textvariable=password, width=64, show='*')
        entry_1.place(x=200, y=100)
        entry_1.focus()

        reg = self.register(validate)
        entry_1.config(validate="key", validatecommand=(reg, '%P'))

        def getcreds():
            # check if four digit entered and is not empty
            global passwd
            passwd = password.get()
            print(f"The Credentials are {passwd}")

        def funcbackspace():
            length = len(entry_1.get())
            entry_1.delete(length - 1, 'end')

        def killwindow():

            command = self.controller.show_frame(WelcomePage)

        cancel = Button(self, width=8, height=3, text="Cancel", bg="red", fg="black", command=killwindow)
        cancel.place(x=220, y=150)
        backspace = Button(self, width=8, height=3, text="Backspace", bg="red", fg="black", command=funcbackspace)
        backspace.place(x=500, y=150)

        # ----number Buttons------
        def enternumber(x):
            global entry_1
            setval = StringVar()
            setval = str(x)
            # print(setval)
            entry_1.insert(END, setval)

        btn_numbers = []
        for i in range(10):
            btn_numbers.append(
                Button(self, width=8, height=3, text=str(i), bd=6, command=lambda x=i: enternumber(x)))
        btn_text = 1
        for i in range(0, 3):
            for j in range(0, 3):
                btn_numbers[btn_text].place(x=220 + j * 140, y=250 + i * 100)
                btn_text += 1

        btn_zero = Button(self, width=15, height=2, text='0', bd=5, command=lambda x=0: enternumber(x))
        btn_zero.place(x=330, y=550)
        clear = Button(self, text="Clear", bg="green", fg="white", width=8, height=3, command=cleartxtfield)
        clear.place(x=220, y=550)
        okbtn = Button(self, text="Enter", bg="green", fg="black", width=8, height=3,
                       command=loginauth)
        okbtn.place(x=500, y=550)


class MainMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        frame = Frame(self, relief='raised', borderwidth=2)
        frame.pack(fill=BOTH, expand=YES)
        frame.pack_propagate(False)

        ######### Returns the Current user ID and populates the relevant
        ######### information onto the dashboard

        # Cuidobj = InputPin(parent,controller)
        # CUID = Cuidobj.return_Cuid()

        #################3 fUNCTION TO RETRIEVE ACCOUNT_NO FROM ATM SWIPE CLASS ########

        # insert_card_obj = InsertATM(parent, controller)
        # account_no_main = insert_card_obj.return_account_no()
        account_no_main = 2222
        # print(f"Within Main Menu the gotten account_no as : {account_no_main}")

        ############## Function to return values from the client to populate the Home page ######################3

        # def sqlcon():
        #     try:
        #         conn = sqlite3.connect('test.db')
        #         return conn
        #     except Error:
        #         print('Connection to database failed ' + str(Error))
        #
        # def retrieve_client_details(con):
        #     global N_id
        #     global User_ID
        #     global First_Name
        #     global Sur_Name
        #     idobj = InsertATM.return_id(InsertATM)
        #     N_id = idobj
        #     print(f"debug for national  id gives {idobj}")
        #     mycursor = con.cursor()
        #     query = "SELECT UserID,Sur_name, First_name from client where National_id=" + str(N_id)
        #     status = mycursor.execute(query)
        #
        #     if status:
        #         global Cuid
        #         validate = mycursor.fetchall()
        #         # print(validate[0])
        #         Cuid = validate[0]
        #
        #         print(f"login debug to check retrieval of userid for client which is  {Cuid}")
        #
        # test = sqlcon()
        # retrieve_client_details(test)
        ################################################### END of Function retrieve from Client table ######################

        username = Label(frame, width=51, text="username", font=("arial", 13, "bold"))
        username.place(x=300, y=22)
        user_id = Label(frame, width=15, height=3, text=f" ACC: {account_no_main}", font=("arial", 12, "bold"))
        user_id.place(x=277, y=22)

        mainLabel = Label(frame, width=20, text="Main Menu", font=("arial", 30, "bold"))
        mainLabel.place(x=200, y=70)

        Depositt = Button(frame, width=12, height=2, fg="white", bg="grey", relief=RAISED, text="Deposit",
                                  command=lambda: controller.show_frame(Deposit))
        Depositt.place(x=250, y=150)
        CheckBalance = Button(frame, width=12, height=2, fg="white", bg="grey", relief=RAISED, text="Check Balance",
                              command=lambda: controller.show_frame(CheckBalance))
        CheckBalance.place(x=500, y=150)

        Withdrawal = Button(frame, width=12, height=2, fg="white", bg="grey", relief=RAISED, text="Withdrawal",
                            command=lambda: controller.show_frame(Withdraw))
        Withdrawal.place(x=250, y=200)
        FastCash = Button(frame, width=12, height=2, fg="white", bg="grey", relief=RAISED, text="Fast Cash (200)")
        FastCash.place(x=500, y=200)

        TransferMoney = Button(frame, width=12, height=2, fg="white", bg="grey", relief=RAISED,
                               text="Transfer Money")
        TransferMoney.place(x=250, y=250)

        ### * pop up showing "Thank you for using Cheserem's Atm Services" #########
        Signout = Button(frame, height=2, width=12, fg="white", bg="green", relief=RAISED, text="Sign Out",
                         command=lambda: controller.show_frame(WelcomePage))
        Signout.place(x=500, y=250)


class Withdraw(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #
        # Hold onto a global reference for the root window
        global entry_2
        entry_2 = None
        count = 1
        amount = StringVar()

        # clear password field

        # function to input entry onto the entry
        def enternumber(x):
            global entry_2
            setval = StringVar()
            setval = str(x)
            print(setval)
            entry_2.insert(END, setval)

        def killwindow():
            pass

        # window.destroy()  # kill the root window

        def validate(
                inp):  #####Work on it so that it accepts only one dot and input starts from * LTR, and auto adds commas

            if inp.isdigit():
                return True
            elif inp == "":
                return True
            else:
                return False

        def withdrawconfirmation(inputamount):
            # loads the next page and validates the input

            pass

        def main():
            global entry_2
            global inputamount
            inputamount = StringVar()

            # pinobj = InsertATM(parent, controller)
            # compare = pinobj.return_account_no()
            # print(f"Debug to check if withdraw gets account_no {compare}")

            def cleartxtfield():
                global entry_2
                entry_2.delete(0, END)
                # inputamount.set("")

            def formattothousands():

                # ### Handle input of many points and return an error to the user or you can parse the input to only
                # allow one point to be input

                val = inputamount.get()
                f = float(val)
                print(locale.setlocale(locale.LC_ALL, ''))
                cash = locale.currency(f, grouping=True)

                inputamount.set(cash)

            entry_2 = Entry(self, textvariable=inputamount, width=64)
            entry_2.place(x=200, y=100)
            entry_2.focus()

            # isnum = lambda q:q.replace('.','',1).isdigit()
            # value = entry_1.get()
            # status = isnum(value)
            # print(status)
            rege = self.register(validate)
            entry_2.config(validate="key", validatecommand=(rege, '%P'))

            # def getcreds():
            #     # check if four digit entered and is not empty
            #     global amount
            #     amount = inputamount.get()
            #     print(amount)

            def funcbackspace():
                length = len(entry_2.get())
                entry_2.delete(length - 1, 'end')

            def goback():
                command = controller.show_frame(MainMenu)

                pass

            cancel = Button(self, width=8, height=3, text="Cancel", bg="red", fg="black", command=goback)
            cancel.place(x=220, y=150)

            clear = Button(self, text="Clear", bg="green", fg="white", width=8, height=3, command=cleartxtfield)
            clear.place(x=360, y=150)

            thousands = Button(self, width=8, height=3, text="Format", bg="red", fg="black",
                               command=formattothousands)
            thousands.place(x=600, y=150)

            backspace = Button(self, width=8, height=3, text="Backspace", bg="red", fg="black", command=funcbackspace)
            backspace.place(x=500, y=150)

            # ----number Buttons------
            btn_numbers = []
            for i in range(10):
                btn_numbers.append(
                    Button(self, width=8, height=3, text=str(i), bd=6, command=lambda x=i: enternumber(x)))
            btn_text = 1
            for i in range(0, 3):
                for j in range(0, 3):
                    btn_numbers[btn_text].place(x=220 + j * 140, y=250 + i * 100)
                    btn_text += 1

            btn_zero = Button(self, width=15, height=2, text='0', bd=5, command=lambda x=0: enternumber(x))
            btn_zero.place(x=330, y=550)

            #############################################3 Function to return amount

            """""""""
            addbutton(window, 220, 250,enterNumber)
            addbutton(window, 360, 250,enterNumber)
            addbutton(window, 500, 250,enterNumber)

            addbutton(window, 220, 350,enterNumber)
            addbutton(window, 360, 350,enterNumber)
            addbutton(window, 500, 350,enterNumber)

            addbutton(window, 220, 450,enterNumber)
            addbutton(window, 360, 450,enterNumber)
            addbutton(window, 500, 450,enterNumber)
        """

            dot = Button(self, text=".", bg="white", fg="black", width=8, height=3,
                         command=lambda x='.': enternumber(x))
            dot.place(x=500, y=550)
            okbtn = Button(self, text="Enter", bg="green", fg="black", width=12, height=6,
                           command=lambda: controller.show_frame(WithdrawConfirm))
            okbtn.place(x=600, y=500)

        """
            zero = Button(window, text="0", bg="black", fg="white", width=8, height=3)
            zero.place(x=360, y=550)
           """

        # Backspace = Button(window,text="Backspace",bg="black",fg="white",width=8,height=3)
        # Backspace.place(x=640,y=250)

        main()


class WithdrawConfirm(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # hold global reference to root window
        root = None
        lframe = None
        rframe = None
        lastbalance = None

        def addlabels(window, name, sidetopack):
            global root
            global lframe
            global rframe
            name_text = str(name)
            label = Label(window, text=name, bd=7, relief=GROOVE, height=5)
            label.pack(side=sidetopack)

        def main():
            global lastbalance
            global inputamount
            inputamount.set("")
            lastbalance = "Your Previous balance"
            prevbal = "Your Previous balance:"
            Withdrawamount = "Withdrawal amount:"
            newbalance = "Your new balance: "
            holdframe = Frame(self)
            bottom = Frame(self)
            lframe = Frame(holdframe)
            rframe = Frame(holdframe)
            addlabels(lframe, prevbal, LEFT)
            addlabels(lframe, Withdrawamount, LEFT)
            addlabels(lframe, newbalance, LEFT)
            lframe.pack(side=TOP)

            addlabels(rframe, prevbal, LEFT)
            addlabels(rframe, Withdrawamount, LEFT)
            addlabels(rframe, newbalance, LEFT)
            rframe.pack(side=BOTTOM)

            # * automatically redirect to the face recognition page for the animation and the actual 2 factor auth before money is withdrawn if
            # it fails " Authentication failed could not withdraw" Redirect to the page to confirm amount and then prompt if ready to scan face again
            ## if yes reauthenticate to a max of 5 times then terminate withdraw and return to the main menu

            Button(bottom, text="Print Reciept", fg='black', bg='green', font='times 18 bold', relief=RAISED, width=13,
                   height=2).pack(side=LEFT, padx=20)
            Button(bottom, text="Main Menu", fg='black', bg='brown', font='times 18 bold', relief=GROOVE, width=13,
                   height=2, command=lambda: controller.show_frame(MainMenu)).pack(side=LEFT, padx=20)
            bottom.pack(side=BOTTOM)

            holdframe.pack(side=TOP)

        main()


class Deposit(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text="Page one!!", font='times 15 bold').pack(pady=10, padx=10)
        Label(self, text="animation for the card to be inserted <event handler> [arduino]").pack()

        button1 = Button(self, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = Button(self, text="automatically redirect to Page Two when cash amount is read in",
                         command=lambda: controller.show_frame(DepositConfirm))
        button2.pack()


class DepositConfirm(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # hold global reference to root window
        root = None
        lframe = None
        rframe = None
        lastbalance = None

        def addlabels(window, name, sidetopack):
            global root
            global lframe
            global rframe
            name_text = str(name)
            label = Label(window, text=name, bd=7, relief=GROOVE, height=5)
            label.pack(side=sidetopack)

        def main():
            global lastbalance
            lastbalance = "Your Previous balance"
            prevbal = "Your Previous balance:"
            Withdrawamount = "Deposit amount:"
            newbalance = "Your new balance: "
            holdframe = Frame(self)
            bottom = Frame(self)
            lframe = Frame(holdframe)
            rframe = Frame(holdframe)
            addlabels(lframe, prevbal, LEFT)
            addlabels(lframe, Withdrawamount, LEFT)
            addlabels(lframe, newbalance, LEFT)
            lframe.pack(side=TOP)

            addlabels(rframe, prevbal, LEFT)
            addlabels(rframe, Withdrawamount, LEFT)
            addlabels(rframe, newbalance, LEFT)
            rframe.pack(side=BOTTOM)

            Button(bottom, text="Print Reciept", fg='black', bg='green', font='times 18 bold', relief=RAISED, width=13,
                   height=2).pack(side=LEFT, padx=20)
            Button(bottom, text="Main Menu", fg='black', bg='brown', font='times 18 bold', relief=GROOVE, width=13,
                   height=2, command=lambda: controller.show_frame(MainMenu)).pack(side=LEFT, padx=20)
            bottom.pack(side=BOTTOM)

            holdframe.pack(side=TOP)

        main()


class BalanceQuery(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


if __name__ == '__main__':
    app = SeaofBTCapp()
    app.title("United Bank")
    width = 1000
    height = 700
    screenwidth = app.winfo_screenwidth()
    screenheight = app.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    app.geometry(alignstr)
    # app.resizable(width=False, height=False)
    app.resizable(width=True, height=True)

    app.mainloop()
