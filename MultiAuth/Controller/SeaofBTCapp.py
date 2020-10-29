# from Imports.env_imports import *
from tkinter import *

from UI_Layouts.BalanceQuery.BalanceQuery import BalanceQuery
from UI_Layouts.Deposit.Deposit import Deposit
from UI_Layouts.DepositConfirm.Deposit_Confirm import DepositConfirm
from UI_Layouts.FaceAuth.Face_Auth import FaceAuth, FaceAuth2
from UI_Layouts.InputPin.InputPin import InputPin
from UI_Layouts.InsertAtm.Inser_Atm import InsertATM, InsertATM2
from UI_Layouts.MainMenu.MainMenu import MainMenu
from UI_Layouts.New_User.New_User import New_User
from UI_Layouts.Register.Register import Register_new_user
from UI_Layouts.Welcome.Welcome import WelcomePage
from UI_Layouts.WithdrawConfirm.Withdraw_Confirm import WithdrawConfirm


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
                BalanceQuery, Register_new_user, New_User):  # ,PageThree,PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(DepositConfirm)

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
