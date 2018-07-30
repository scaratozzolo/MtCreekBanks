import tkinter as tk
from tkinter import ttk
from banks import *
from signature import signature, displaysig
from PIL import Image, ImageTk, ImageGrab
import pickle
import os

bar = None
fb = None
tkg = None
retail = None
bike = None
change = None
fanny = None

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)


def load():
    """
    Loads the type objects from pickles or creates new ones
    """

    global bar
    global fb
    global tkg
    global retail
    global bike
    global change
    global fanny

    if not os.path.exists('data'):
        os.makedirs('data')
        os.makedirs('data/bar')
        os.makedirs('data/fb')
        os.makedirs('data/tkg')
        os.makedirs('data/retail')
        os.makedirs('data/bike')
        os.makedirs('data/change')
        os.makedirs('data/fanny')
        signature("blank", "blank", datetime.now(), blank=True)

    try:
        with open("data/bar/bar.pickle", "rb") as f:
            bar = pickle.load(f)
    except:
        bar = Bar()

    try:
        with open("data/fb/fb.pickle", "rb") as f:
            fb = pickle.load(f)
    except:
        fb = FB()

    try:
        with open("data/tkg/tkg.pickle", "rb") as f:
            tkg = pickle.load(f)
    except:
        tkg = TKG()

    try:
        with open("data/retail/retail.pickle", "rb") as f:
            retail = pickle.load(f)
    except:
        retail = Retail()

    try:
        with open("data/bike/bike.pickle", "rb") as f:
            bike = pickle.load(f)
    except:
        bike = Bike()

    try:
        with open("data/change/change.pickle", "rb") as f:
            change = pickle.load(f)
    except:
        change = Change()

    try:
        with open("data/fanny/fanny.pickle", "rb") as f:
            fanny = pickle.load(f)
    except:
        fanny = Fanny()

def save():
    """Saves the type objects into a pickle"""

    with open("data/bar/bar.pickle", "wb") as f:
        pickle.dump(bar, f)

    with open("data/fb/fb.pickle", "wb") as f:
        pickle.dump(fb, f)

    with open("data/tkg/tkg.pickle", "wb") as f:
        pickle.dump(tkg, f)

    with open("data/retail/retail.pickle", "wb") as f:
        pickle.dump(retail, f)

    with open("data/bike/bike.pickle", "wb") as f:
        pickle.dump(bike, f)

    with open("data/change/change.pickle", "wb") as f:
        pickle.dump(change, f)

    with open("data/fanny/fanny.pickle", "wb") as f:
        pickle.dump(fanny, f)



def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()



class Tracking(tk.Tk):

    def __init__(self, *args, **kwargs):

        load()
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Mountain Creek Bank Tacking System")

        container = tk.Frame(self)
        container.pack(side="top", expand = True)


        self.frames = {}

        for F in (StartPage, BarPage, FBPage, TKGPage, RetailPage, BikePage, ChangePage, FannyPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        barbutton = tk.Button(self, text="BAR", command=lambda: controller.show_frame(BarPage), height=2, width=10, font=("Verdana", 35, "bold"), background="cyan").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        fbbutton = tk.Button(self, text='FOOD & \nBEVERAGE', command=lambda: controller.show_frame(FBPage), height=2, width=10, font=("Verdana", 35, "bold"), background="blue").grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tkgbutton = tk.Button(self, text='TICKETING', command=lambda: controller.show_frame(TKGPage), height=2, width=10, font=("Verdana", 35, "bold"), background="black", fg="white").grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        retailbutton = tk.Button(self, text='RETAIL', command=lambda: controller.show_frame(RetailPage), height=2, width=10, font=("Verdana", 35, "bold"), background="#00ce03").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        bikebutton = tk.Button(self, text='BIKE', command=lambda: controller.show_frame(BikePage), height=2, width=10, font=("Verdana", 35, "bold"), background="red").grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        changebutton = tk.Button(self, text='CHANGE', command=lambda: controller.show_frame(ChangePage), height=2, width=10, font=("Verdana", 35, "bold"), background="magenta").grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        fannybutton = tk.Button(self, text='FANNY\nPACK', command=lambda: controller.show_frame(FannyPage), height=2, width=10, font=("Verdana", 35, "bold"), background="#f9f21b").grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        exitbutton = tk.Button(self, text='EXIT', command=self.exitprogram, height=2, width=10, font=("Verdana", 35, "bold"), background="#7a7a7a").grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        self.outinpark = tk.Label(self, text="Banks Out:\nBar: {}\nF&B: {}\nTicketing: {}\nRetail: {}\nBike: {}\nChange: {}\nFanny: {}".format((len(bar.signedout())), (len(fb.signedout())), (len(tkg.signedout())), (len(retail.signedout())), (len(bike.signedout())), (len(change.signedout())), (len(fanny.signedout()))), font=("Verdana", 20))
        self.outinpark.grid(row=3, column=0, padx=10, pady=10)

        devby = tk.Label(self, text="Developed by Scott Caratozzolo", font=("Verdana", 10)).grid(row=3, column=1, padx=10, pady=10, sticky="s")

        self.inaudit = tk.Label(self, text="Banks In:\nBar: {}\nF&B: {}\nTicketing: {}\nRetail: {}\nBike: {}\nChange: {}\nFanny: {}".format((len(bar.madebanks())), (len(fb.madebanks())), (len(tkg.madebanks())), (len(retail.madebanks())), (len(bike.madebanks())), (len(change.madebanks())), (len(fanny.madebanks()))), font=("Verdana", 20))
        self.inaudit.grid(row=3, column=2, padx=10, pady=10)
        self.after(1000, self.updatestats)

    def updatestats(self):
        """Updates the bank in/out stats"""
        self.outinpark.config(text="Banks Out:\nBar: {}\nF&B: {}\nTicketing: {}\nRetail: {}\nBike: {}\nChange: {}\nFanny: {}".format((len(bar.signedout())), (len(fb.signedout())), (len(tkg.signedout())), (len(retail.signedout())), (len(bike.signedout())), (len(change.signedout())), (len(fanny.signedout()))))
        self.inaudit.config(text="Banks In:\nBar: {}\nF&B: {}\nTicketing: {}\nRetail: {}\nBike: {}\nChange: {}\nFanny: {}".format((len(bar.madebanks())), (len(fb.madebanks())), (len(tkg.madebanks())), (len(retail.madebanks())), (len(bike.madebanks())), (len(change.madebanks())), (len(fanny.madebanks()))))
        self.after(1000, self.updatestats)

    def exitprogram(self):
        """Function to properly exit program"""

        def yes():
            save()
            popup.destroy()
            quit()

        def no():
            save()
            popup.destroy()

        popup= tk.Tk()
        question = tk.Label(popup, text = "Are you sure?", font = ("Verdana", 20)).grid(row=0, column=0, sticky ="nw", padx=10, pady=10, columnspan=2)
        yesbutton = tk.Button(popup, text="YES", font = ("Verdana", 20), command = yes).grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        nobutton = tk.Button(popup, text="NO", font = ("Verdana", 20), command = no).grid(row=1, column=1, padx=10, pady=10, sticky="nw")

        windowWidth = popup.winfo_reqwidth()
        windowHeight = popup.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        positionRight = int(popup.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(popup.winfo_screenheight()/2 - windowHeight/2)

        # Positions the window in the center of the page.
        popup.geometry("+{}+{}".format(positionRight, positionDown))

        popup.mainloop()

class BarPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BAR", font=("Verdana", 40)).grid(row=0, column=1, padx=10, pady=10)

        signoutbutton = tk.Button(self, text='SIGN OUT', command=self.signoutbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff002a").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        signinbutton = tk.Button(self, text='SIGN IN', command=self.signinbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#f9f21b").grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        returnbutton = tk.Button(self, text='RETURN', command=self.returnbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#00ce03").grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        currentbankinfobutton = tk.Button(self, text="CURRENT\nBANK INFO", command=self.currentbankinfo, height=2, width=10, font=("Verdana", 35, "bold"), background="cyan").grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        makebankbutton = tk.Button(self, text='MAKE BANK', command=self.makebank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff00ee").grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        managelocbutton = tk.Button(self, text="MANAGE\nLOCATIONS", command=self.managelocs, height=2, width=10, font=("Verdana", 35, "bold"), background="#0c00ff").grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        testbutton = tk.Button(self, text="MANAGE\nBANKS", command=self.managebanks, height=2, width=10, font=("Verdana", 35, "bold"), background="#8c00ff").grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        banklogbutton = tk.Button(self, text="BANK LOG", command=self.banklog, height=2, width=10, font=("Verdana", 35, "bold"), background="#c896ff").grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        backbutton = tk.Button(self, text="BACK", command=lambda: controller.show_frame(StartPage), height=2, width=10, font=("Verdana", 35, "bold"), background="#7a7a7a").grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        # testbutton = tk.Button(self, text="SECRET\nTESTING", command=self.managebanks, height=4, width=10, font=("Verdana", 40, "bold"), background="black", fg="white").grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

        self.barstatsout = tk.Label(self, text="Banks Out: {}".format(len(bar.signedout())), font=("Verdana", 20))
        self.barstatsout.grid(row=4, column=0, padx=10, pady=10, sticky="sew")

        self.barstatsin = tk.Label(self, text="Banks In Audit: {}".format(len(bar.madebanks())), font=("Verdana", 20))
        self.barstatsin.grid(row=4, column=2, padx=10, pady=10, sticky="sew")

        self.after(1000, self.updatestats)

    def updatestats(self):
        """Updates the bank in/out stats"""
        self.barstatsout.config(text="Banks Out: {}".format(len(bar.signedout())))
        self.barstatsin.config(text="Banks In Audit: {}".format(len(bar.madebanks())))
        self.after(1000, self.updatestats)

    def signoutbank(self):
        """Popup for bar sign out"""
        popup = tk.Tk()
        popup.wm_title("Sign Out Bar Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        locationlabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        barlocs = bar.locations()
        if len(barlocs) == 0:
            barlocs = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locsdrop = tk.OptionMenu(popup, locvar, *barlocs)
        locsdrop.config(font=("Verdana", 20), width= 20)
        locsdrop.grid(row=1, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        barmade = bar.madebanks()
        if len(barmade) == 0:
            barmade = [""]
        madevar = tk.StringVar(popup)
        madevar.set("")
        madedrop = tk.OptionMenu(popup, madevar, *barmade)
        madedrop.config(font=("Verdana", 20), width= 20)
        madedrop.grid(row=2, column=1, padx=10, pady=10)

        noteslabel = tk.Label(popup, text="Notes: ", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        notesentry = tk.Text(popup, font=("Verdana", 20), height=4, width=22)
        notesentry.grid(row=3, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), locvar.get(), madevar.get(), notesentry.get("1.0", "end"))).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, location, number, notes):
            if name == "" or name == " ":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif location == "" or location == " ":
                errorlabel.config(text="Error: Please select a location", fg="red")
            elif number == "" or number == " ":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = bar.signout(name, location, number.split("#")[-1], notes)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")

        popup.mainloop()

    def signinbank(self):
        """Popup for bar sign in"""
        popup = tk.Tk()
        popup.wm_title("Sign In Bar Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        barout = bar.signedout()
        if len(barout) == 0:
            barout = [" "]
        outvar = tk.StringVar(popup)
        outvar.set("")
        outdrop = tk.OptionMenu(popup, outvar, *barout)
        outdrop.config(font=("Verdana", 20), width= 20)
        outdrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), outvar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, fg="red", font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, number):
            if name == "":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = bar.signin(name, number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is returned", fg="red")

        popup.mainloop()

    def returnbank(self):
        """Popup for bar return"""
        popup = tk.Tk()
        popup.wm_title("Return Bar Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        barin = bar.notreturnedbanks()
        if len(barin) == 0:
            barin = [" "]
        invar = tk.StringVar(popup)
        invar.set("")
        indrop = tk.OptionMenu(popup, invar, *barin)
        indrop.config(font=("Verdana", 20), width= 20)
        indrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(invar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number):
            if number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = bar.returnbank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already returned", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not out", fg="red")

        popup.mainloop()

    def makebank(self):
        """Popup for making bar bank""" ## TODO: Dont close on submit, update list
        popup = tk.Tk()
        popup.wm_title("Make Bar Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        returnedbanks = bar.returnedbanks()
        if len(returnedbanks) == 0:
            returnedbanks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *returnedbanks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        amountlabel = tk.Label(popup, text="Amount: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        amountentry = tk.Entry(popup, font=("Verdana", 20))
        amountentry.grid(row=1, column=1, padx=10, pady=10)
        amountentry.insert(0, "350")

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get(), amountentry.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number, amount):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            elif amount == "":
                success, status = bar.makebank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

            else:
                success, status = bar.makebank(number.split("#")[-1], amount)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

        popup.mainloop()

    def currentbankinfo(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()
            closebutton.destroy()

            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = bar.signoutinfo(number.split("#")[-1])
                if success:
                    try:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"], status["Notes"]))
                    except:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"]))

                    infoin.config(text="Name: {}\nTime: {}".format(status["Name_In"], status["Time_In"]))


                    try:
                        returninfo.config(text="{}\nTime: {}".format(status["Returned"], status["Returned_Time"]))
                    except:
                        returninfo.config(text="{}".format(status["Returned"]))


                    imgout = ImageTk.PhotoImage(Image.open("data/bar/{}-{}-{}/bar-{}-{}-{}.png".format(status["Time_Out"].month, status["Time_Out"].day, status["Time_Out"].year, number.split("#")[-1], status["Time_Out"].hour, status["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                    sigoutcanvas.image = imgout
                    sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                    try:
                        imgin = ImageTk.PhotoImage(Image.open("data/bar/{}-{}-{}/bar-{}-{}-{}.png".format(status["Time_In"].month, status["Time_In"].day, status["Time_In"].year, number.split("#")[-1], status["Time_In"].hour, status["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
                    except:
                        imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)

                    editbutton = tk.Button(popup, text="EDIT", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=0, padx=10, pady=10) #TODO
                    okaybutton = tk.Button(popup, text="OKAY", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Current Bar Bank Info")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = bar.banks()
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20))
        closebutton.grid(row=1, column=0, padx=10, pady=10)
        # submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get()))
        # submitbutton.grid(row=1, column=1, padx=10, pady=10)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=2, column=1, padx=10, pady=10)



        popup.mainloop()

    def banklog(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = bar.banklog(number.split("#")[-1])
                if success:

                    def submit2(date):
                        try:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"], status[date]["Notes"]))
                        except:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"]))

                        infoin.config(text="Name: {}\nTime: {}".format(status[date]["Name_In"], status[date]["Time_In"]))
                        returninfo.config(text="Time: {}".format(status[date]["Returned_Time"]))

                        imgout = ImageTk.PhotoImage(Image.open("data/bar/{}-{}-{}/bar-{}-{}-{}.png".format(status[date]["Time_Out"].month, status[date]["Time_Out"].day, status[date]["Time_Out"].year, number.split("#")[-1], status[date]["Time_Out"].hour, status[date]["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigoutcanvas.image = imgout
                        sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                        imgin = ImageTk.PhotoImage(Image.open("data/bar/{}-{}-{}/bar-{}-{}-{}.png".format(status[date]["Time_In"].month, status[date]["Time_In"].day, status[date]["Time_In"].year, number.split("#")[-1], status[date]["Time_In"].hour, status[date]["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)


                    dates = [i for i in status]
                    dates = dates[::-1]
                    datevar.set("")
                    datesdrop = tk.OptionMenu(popup, datevar, *dates, command = lambda x: submit2(datevar.get()))
                    datesdrop.config(font=("Verdana", 20), width= 20)
                    datesdrop.grid(row=1, column=1, padx=10, pady=10)

                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Bar Bank Logs")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = bar.returnedbanks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        datelabel = tk.Label(popup, text="Date: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        datevar = tk.StringVar(popup)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10, pady=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10, pady=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)

        popup.mainloop()

    def managebanks(self):
        """Popup for adding/removing bar banks"""
        popup = tk.Tk()
        popup.wm_title("Add Bar Bank")

        banklabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        bankentry = tk.Entry(popup, font=("Verdana", 20))
        bankentry.grid(row=1, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=2, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: add(bankentry.get())).grid(row=3, column=0, padx=10, pady=10)


        def add(number):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = bar.addbank(number)
                if success:
                    errorlabel.config(text="Successfully added bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That bank already exists", fg="red")


        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        banks = bar.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=1, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=2, column=1, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: remove(bankvar.get())).grid(row=3, column=1, padx=10, pady=10)

        def remove(number):
            if number == "":
                errorlabel2.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = bar.removebank(number.split("#")[-1])
                if success:
                    errorlabel2.config(text="Successfully removed bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel2.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel2.config(text="Error: That bank is already made", fg="red")

        def refresh():
            bankdrop.children['menu'].delete(0, "end")
            for bank in bar.banks():
                bankdrop.children['menu'].add_command(label=bank, command=lambda opt=bank: bankvar.set(opt))
            bankvar.set("")

            bankentry.delete(0, 'end')

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        popup.mainloop()

    def managelocs(self):
        """Popup for adding and removing locations"""
        popup = tk.Tk()
        popup.wm_title("Manage Bar Locations")


        def add(location):

            if location == "" or location == " ":
                errorlabel.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = bar.addlocation(location)
                if success:
                    errorlabel.config(text="Successfully added location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That location already exists", fg="red")

        def remove(location):
            if location == "" or location == " ":
                errorlabel2.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = bar.removelocation(location)
                if success:
                    errorlabel2.config(text="Successfully removed location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That location does not exist", fg="red")


        def refresh():
            locdrop.children['menu'].delete(0, "end")
            for loc in bar.locations():
                locdrop.children['menu'].add_command(label=loc, command=lambda opt=loc: locvar.set(opt))
            locvar.set("")

            locationentry.delete(0, 'end')

        locationaddlabel = tk.Label(popup, text="Location Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        locationentry = tk.Entry(popup, font=("Verdana", 20))
        locationentry.grid(row=1, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="ADD", font=("Verdana", 20), command = lambda: add(locationentry.get())).grid(row=2, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=3, column=0, padx=10, pady=10)

        locationremovelabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        locations = bar.locations()
        if len(locations) == 0:
            locations = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locdrop = tk.OptionMenu(popup, locvar, *locations)
        locdrop.config(font=("Verdana", 20), width= 20)
        locdrop.grid(row=1, column=1, padx=10, pady=10)

        submitbutton2 = tk.Button(popup, text="REMOVE", font=("Verdana", 20), command = lambda: remove(locvar.get())).grid(row=2, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=3, column=1, padx=10, pady=10)


        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)



        refresh()
        popup.mainloop()

class FBPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="F&B", font=("Verdana", 40)).grid(row=0, column=1, padx=10, pady=10)

        signoutbutton = tk.Button(self, text='SIGN OUT', command=self.signoutbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff002a").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        signinbutton = tk.Button(self, text='SIGN IN', command=self.signinbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#f9f21b").grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        returnbutton = tk.Button(self, text='RETURN', command=self.returnbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#00ce03").grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        currentbankinfobutton = tk.Button(self, text="CURRENT\nBANK INFO", command=self.currentbankinfo, height=2, width=10, font=("Verdana", 35, "bold"), background="cyan").grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        makebankbutton = tk.Button(self, text='MAKE BANK', command=self.makebank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff00ee").grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        managelocbutton = tk.Button(self, text="MANAGE\nLOCATIONS", command=self.managelocs, height=2, width=10, font=("Verdana", 35, "bold"), background="#0c00ff").grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        testbutton = tk.Button(self, text="MANAGE\nBANKS", command=self.managebanks, height=2, width=10, font=("Verdana", 35, "bold"), background="#8c00ff").grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        banklogbutton = tk.Button(self, text="BANK LOG", command=self.banklog, height=2, width=10, font=("Verdana", 35, "bold"), background="#c896ff").grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        backbutton = tk.Button(self, text="BACK", command=lambda: controller.show_frame(StartPage), height=2, width=10, font=("Verdana", 35, "bold"), background="#7a7a7a").grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        # testbutton = tk.Button(self, text="SECRET\nTESTING", command=self.managebanks, height=4, width=10, font=("Verdana", 40, "bold"), background="black", fg="white").grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

        self.fbstatsout = tk.Label(self, text="Banks Out: {}".format(len(fb.signedout())), font=("Verdana", 20))
        self.fbstatsout.grid(row=4, column=0, padx=10, pady=10, sticky="sew")

        self.fbstatsin = tk.Label(self, text="Banks In Audit: {}".format(len(fb.madebanks())), font=("Verdana", 20))
        self.fbstatsin.grid(row=4, column=2, padx=10, pady=10, sticky="sew")

        self.after(1000, self.updatestats)

    def updatestats(self):
        """Updates the bank in/out stats"""
        self.fbstatsout.config(text="Banks Out: {}".format(len(fb.signedout())))
        self.fbstatsin.config(text="Banks In Audit: {}".format(len(fb.madebanks())))
        self.after(1000, self.updatestats)

    def signoutbank(self):
        """Popup for fb sign out"""
        popup = tk.Tk()
        popup.wm_title("Sign Out F&B Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        locationlabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        fblocs = fb.locations()
        if len(fblocs) == 0:
            fblocs = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locsdrop = tk.OptionMenu(popup, locvar, *fblocs)
        locsdrop.config(font=("Verdana", 20), width= 20)
        locsdrop.grid(row=1, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        fbmade = fb.madebanks()
        if len(fbmade) == 0:
            fbmade = [""]
        madevar = tk.StringVar(popup)
        madevar.set("")
        madedrop = tk.OptionMenu(popup, madevar, *fbmade)
        madedrop.config(font=("Verdana", 20), width= 20)
        madedrop.grid(row=2, column=1, padx=10, pady=10)

        noteslabel = tk.Label(popup, text="Notes: ", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        notesentry = tk.Text(popup, font=("Verdana", 20), height=4, width=22)
        notesentry.grid(row=3, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), locvar.get(), madevar.get(), notesentry.get("1.0", "end"))).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, location, number, notes):
            if name == "" or name == " ":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif location == "" or location == " ":
                errorlabel.config(text="Error: Please select a location", fg="red")
            elif number == "" or number == " ":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = fb.signout(name, location, number.split("#")[-1], notes)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")

        popup.mainloop()

    def signinbank(self):
        """Popup for fb sign in"""
        popup = tk.Tk()
        popup.wm_title("Sign In F&B Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        fbout = fb.signedout()
        if len(fbout) == 0:
            fbout = [" "]
        outvar = tk.StringVar(popup)
        outvar.set("")
        outdrop = tk.OptionMenu(popup, outvar, *fbout)
        outdrop.config(font=("Verdana", 20), width= 20)
        outdrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), outvar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, fg="red", font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, number):
            if name == "":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = fb.signin(name, number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is returned", fg="red")

        popup.mainloop()

    def returnbank(self):
        """Popup for fb return"""
        popup = tk.Tk()
        popup.wm_title("Return F&B Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        fbin = fb.notreturnedbanks()
        if len(fbin) == 0:
            fbin = [" "]
        invar = tk.StringVar(popup)
        invar.set("")
        indrop = tk.OptionMenu(popup, invar, *fbin)
        indrop.config(font=("Verdana", 20), width= 20)
        indrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(invar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number):
            if number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = fb.returnbank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already returned", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not out", fg="red")

        popup.mainloop()

    def makebank(self):
        """Popup for making fb bank"""
        popup = tk.Tk()
        popup.wm_title("Make F&B Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        returnedbanks = fb.returnedbanks()  #Check unmade banks rather than returned
        if len(returnedbanks) == 0:
            returnedbanks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *returnedbanks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        amountlabel = tk.Label(popup, text="Amount: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        amountentry = tk.Entry(popup, font=("Verdana", 20))
        amountentry.grid(row=1, column=1, padx=10, pady=10)
        amountentry.insert(0, "350")

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get(), amountentry.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number, amount):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            elif amount == "":
                success, status = fb.makebank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

            else:
                success, status = fb.makebank(number.split("#")[-1], amount)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

        popup.mainloop()

    def currentbankinfo(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()

            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = fb.signoutinfo(number.split("#")[-1])
                if success:
                    closebutton.destroy()
                    try:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"], status["Notes"]))
                    except:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"]))

                    infoin.config(text="Name: {}\nTime: {}".format(status["Name_In"], status["Time_In"]))


                    try:
                        returninfo.config(text="{}\nTime: {}".format(status["Returned"], status["Returned_Time"]))
                    except:
                        returninfo.config(text="{}".format(status["Returned"]))


                    imgout = ImageTk.PhotoImage(Image.open("data/fb/{}-{}-{}/fb-{}-{}-{}.png".format(status["Time_Out"].month, status["Time_Out"].day, status["Time_Out"].year, number.split("#")[-1], status["Time_Out"].hour, status["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                    sigoutcanvas.image = imgout
                    sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                    try:
                        imgin = ImageTk.PhotoImage(Image.open("data/fb/{}-{}-{}/fb-{}-{}-{}.png".format(status["Time_In"].month, status["Time_In"].day, status["Time_In"].year, number.split("#")[-1], status["Time_In"].hour, status["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
                    except:
                        imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)

                    editbutton = tk.Button(popup, text="EDIT", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=0, padx=10, pady=10) #TODO
                    okaybutton = tk.Button(popup, text="OKAY", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Current F&B Bank Info")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = fb.banks()
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20))
        closebutton.grid(row=1, column=0, padx=10, pady=10)
        # submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get()))
        # submitbutton.grid(row=1, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)


        popup.mainloop()

    def banklog(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = fb.banklog(number.split("#")[-1])
                if success:

                    def submit2(date):
                        try:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"], status[date]["Notes"]))
                        except:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"]))

                        infoin.config(text="Name: {}\nTime: {}".format(status[date]["Name_In"], status[date]["Time_In"]))
                        returninfo.config(text="Time: {}".format(status[date]["Returned_Time"]))

                        imgout = ImageTk.PhotoImage(Image.open("data/fb/{}-{}-{}/fb-{}-{}-{}.png".format(status[date]["Time_Out"].month, status[date]["Time_Out"].day, status[date]["Time_Out"].year, number.split("#")[-1], status[date]["Time_Out"].hour, status[date]["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigoutcanvas.image = imgout
                        sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                        imgin = ImageTk.PhotoImage(Image.open("data/fb/{}-{}-{}/fb-{}-{}-{}.png".format(status[date]["Time_In"].month, status[date]["Time_In"].day, status[date]["Time_In"].year, number.split("#")[-1], status[date]["Time_In"].hour, status[date]["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)


                    dates = [i for i in status]
                    dates = dates[::-1]
                    datevar.set("")
                    datesdrop = tk.OptionMenu(popup, datevar, *dates, command = lambda x: submit2(datevar.get()))
                    datesdrop.config(font=("Verdana", 20), width= 20)
                    datesdrop.grid(row=1, column=1, padx=10, pady=10)

                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("F&B Bank Logs")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = fb.returnedbanks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        datelabel = tk.Label(popup, text="Date: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        datevar = tk.StringVar(popup)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10, pady=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10, pady=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)

        popup.mainloop()

    def managebanks(self):
        """Popup for adding/removing bar banks"""
        popup = tk.Tk()
        popup.wm_title("Add F&B Bank")

        banklabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        bankentry = tk.Entry(popup, font=("Verdana", 20))
        bankentry.grid(row=1, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=2, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: add(bankentry.get())).grid(row=3, column=0, padx=10, pady=10)


        def add(number):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = fb.addbank(number)
                if success:
                    errorlabel.config(text="Successfully added bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That bank already exists", fg="red")


        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        banks = fb.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=1, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=2, column=1, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: remove(bankvar.get())).grid(row=3, column=1, padx=10, pady=10)

        def remove(number):
            if number == "":
                errorlabel2.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = fb.removebank(number.split("#")[-1])
                if success:
                    errorlabel2.config(text="Successfully removed bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel2.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel2.config(text="Error: That bank is already made", fg="red")

        def refresh():
            bankdrop.children['menu'].delete(0, "end")
            for bank in fb.banks():
                bankdrop.children['menu'].add_command(label=bank, command=lambda opt=bank: bankvar.set(opt))
            bankvar.set("")

            bankentry.delete(0, 'end')

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        popup.mainloop()

    def managelocs(self):
        """Popup for adding and removing locations"""
        popup = tk.Tk()
        popup.wm_title("Manage F&B Locations")


        def add(location):

            if location == "" or location == " ":
                errorlabel.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = fb.addlocation(location)
                if success:
                    errorlabel.config(text="Successfully added location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That location already exists", fg="red")

        def remove(location):
            if location == "" or location == " ":
                errorlabel2.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = fb.removelocation(location)
                if success:
                    errorlabel2.config(text="Successfully removed location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That location does not exist", fg="red")


        def refresh():
            locdrop.children['menu'].delete(0, "end")
            for loc in fb.locations():
                locdrop.children['menu'].add_command(label=loc, command=lambda opt=loc: locvar.set(opt))
            locvar.set("")

            locationentry.delete(0, 'end')

        locationaddlabel = tk.Label(popup, text="Location Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        locationentry = tk.Entry(popup, font=("Verdana", 20))
        locationentry.grid(row=1, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="ADD", font=("Verdana", 20), command = lambda: add(locationentry.get())).grid(row=2, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=3, column=0, padx=10, pady=10)

        locationremovelabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        locations = fb.locations()
        if len(locations) == 0:
            locations = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locdrop = tk.OptionMenu(popup, locvar, *locations)
        locdrop.config(font=("Verdana", 20), width= 20)
        locdrop.grid(row=1, column=1, padx=10, pady=10)

        submitbutton2 = tk.Button(popup, text="REMOVE", font=("Verdana", 20), command = lambda: remove(locvar.get())).grid(row=2, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=3, column=1, padx=10, pady=10)


        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)



        refresh()
        popup.mainloop()

class TKGPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="TICKETING", font=("Verdana", 40)).grid(row=0, column=1, padx=10, pady=10)

        signoutbutton = tk.Button(self, text='SIGN OUT', command=self.signoutbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff002a").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        signinbutton = tk.Button(self, text='SIGN IN', command=self.signinbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#f9f21b").grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        returnbutton = tk.Button(self, text='RETURN', command=self.returnbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#00ce03").grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        currentbankinfobutton = tk.Button(self, text="CURRENT\nBANK INFO", command=self.currentbankinfo, height=2, width=10, font=("Verdana", 35, "bold"), background="cyan").grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        makebankbutton = tk.Button(self, text='MAKE BANK', command=self.makebank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff00ee").grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        managelocbutton = tk.Button(self, text="MANAGE\nLOCATIONS", command=self.managelocs, height=2, width=10, font=("Verdana", 35, "bold"), background="#0c00ff").grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        testbutton = tk.Button(self, text="MANAGE\nBANKS", command=self.managebanks, height=2, width=10, font=("Verdana", 35, "bold"), background="#8c00ff").grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        banklogbutton = tk.Button(self, text="BANK LOG", command=self.banklog, height=2, width=10, font=("Verdana", 35, "bold"), background="#c896ff").grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        backbutton = tk.Button(self, text="BACK", command=lambda: controller.show_frame(StartPage), height=2, width=10, font=("Verdana", 35, "bold"), background="#7a7a7a").grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        # testbutton = tk.Button(self, text="SECRET\nTESTING", command=self.managebanks, height=4, width=10, font=("Verdana", 40, "bold"), background="black", fg="white").grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

        self.tkgstatsout = tk.Label(self, text="Banks Out: {}".format(len(tkg.signedout())), font=("Verdana", 20))
        self.tkgstatsout.grid(row=4, column=0, padx=10, pady=10, sticky="sew")

        self.tkgstatsin = tk.Label(self, text="Banks In Audit: {}".format(len(tkg.madebanks())), font=("Verdana", 20))
        self.tkgstatsin.grid(row=4, column=2, padx=10, pady=10, sticky="sew")

        self.after(1000, self.updatestats)

    def updatestats(self):
        """Updates the bank in/out stats"""
        self.tkgstatsout.config(text="Banks Out: {}".format(len(tkg.signedout())))
        self.tkgstatsin.config(text="Banks In Audit: {}".format(len(tkg.madebanks())))
        self.after(1000, self.updatestats)

    def signoutbank(self):
        """Popup for tkg sign out"""
        popup = tk.Tk()
        popup.wm_title("Sign Out Ticketing Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        locationlabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        tkglocs = tkg.locations()
        if len(tkglocs) == 0:
            tkglocs = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locsdrop = tk.OptionMenu(popup, locvar, *tkglocs)
        locsdrop.config(font=("Verdana", 20), width= 20)
        locsdrop.grid(row=1, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        tkgmade = tkg.madebanks()
        if len(tkgmade) == 0:
            tkgmade = [""]
        madevar = tk.StringVar(popup)
        madevar.set("")
        madedrop = tk.OptionMenu(popup, madevar, *tkgmade)
        madedrop.config(font=("Verdana", 20), width= 20)
        madedrop.grid(row=2, column=1, padx=10, pady=10)

        noteslabel = tk.Label(popup, text="Notes: ", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        notesentry = tk.Text(popup, font=("Verdana", 20), height=4, width=22)
        notesentry.grid(row=3, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), locvar.get(), madevar.get(), notesentry.get("1.0", "end"))).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, location, number, notes):
            if name == "" or name == " ":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif location == "" or location == " ":
                errorlabel.config(text="Error: Please select a location", fg="red")
            elif number == "" or number == " ":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = tkg.signout(name, location, number.split("#")[-1], notes)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")

        popup.mainloop()

    def signinbank(self):
        """Popup for tkg sign in"""
        popup = tk.Tk()
        popup.wm_title("Sign In Ticketing Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        tkgout = tkg.signedout()
        if len(tkgout) == 0:
            tkgout = [" "]
        outvar = tk.StringVar(popup)
        outvar.set("")
        outdrop = tk.OptionMenu(popup, outvar, *tkgout)
        outdrop.config(font=("Verdana", 20), width= 20)
        outdrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), outvar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, fg="red", font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, number):
            if name == "":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = tkg.signin(name, number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is returned", fg="red")

        popup.mainloop()

    def returnbank(self):
        """Popup for tkg return"""
        popup = tk.Tk()
        popup.wm_title("Return Ticketing Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        tkgin = tkg.notreturnedbanks()
        if len(tkgin) == 0:
            tkgin = [" "]
        invar = tk.StringVar(popup)
        invar.set("")
        indrop = tk.OptionMenu(popup, invar, *tkgin)
        indrop.config(font=("Verdana", 20), width= 20)
        indrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(invar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number):
            if number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = tkg.returnbank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already returned", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not out", fg="red")

        popup.mainloop()

    def makebank(self):
        """Popup for making tkg bank"""
        popup = tk.Tk()
        popup.wm_title("Make Ticketing Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        returnedbanks = tkg.returnedbanks()  #Check unmade banks rather than returned
        if len(returnedbanks) == 0:
            returnedbanks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *returnedbanks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        amountlabel = tk.Label(popup, text="Amount: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        amountentry = tk.Entry(popup, font=("Verdana", 20))
        amountentry.grid(row=1, column=1, padx=10, pady=10)
        amountentry.insert(0, "350")

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get(), amountentry.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number, amount):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            elif amount == "":
                success, status = tkg.makebank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

            else:
                success, status = tkg.makebank(number.split("#")[-1], amount)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

        popup.mainloop()

    def currentbankinfo(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()
            closebutton.destroy()

            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = tkg.signoutinfo(number.split("#")[-1])
                if success:
                    try:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"], status["Notes"]))
                    except:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"]))

                    infoin.config(text="Name: {}\nTime: {}".format(status["Name_In"], status["Time_In"]))


                    try:
                        returninfo.config(text="{}\nTime: {}".format(status["Returned"], status["Returned_Time"]))
                    except:
                        returninfo.config(text="{}".format(status["Returned"]))


                    imgout = ImageTk.PhotoImage(Image.open("data/tkg/{}-{}-{}/tkg-{}-{}-{}.png".format(status["Time_Out"].month, status["Time_Out"].day, status["Time_Out"].year, number.split("#")[-1], status["Time_Out"].hour, status["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                    sigoutcanvas.image = imgout
                    sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                    try:
                        imgin = ImageTk.PhotoImage(Image.open("data/tkg/{}-{}-{}/tkg-{}-{}-{}.png".format(status["Time_In"].month, status["Time_In"].day, status["Time_In"].year, number.split("#")[-1], status["Time_In"].hour, status["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
                    except:
                        imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)

                    editbutton = tk.Button(popup, text="EDIT", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=0, padx=10, pady=10) #TODO
                    okaybutton = tk.Button(popup, text="OKAY", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Current Ticketing Bank Info")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = tkg.banks()
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20))
        closebutton.grid(row=1, column=0, padx=10, pady=10)
        # submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get()))
        # submitbutton.grid(row=1, column=1, padx=10, pady=10)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=2, column=1, padx=10, pady=10)



        popup.mainloop()

    def banklog(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)

            except:
                pass

        def submit(number):
            refresh()
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = tkg.banklog(number.split("#")[-1])
                if success:

                    def submit2(date):
                        try:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"], status[date]["Notes"]))
                        except:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"]))

                        infoin.config(text="Name: {}\nTime: {}".format(status[date]["Name_In"], status[date]["Time_In"]))
                        returninfo.config(text="Time: {}".format(status[date]["Returned_Time"]))

                        imgout = ImageTk.PhotoImage(Image.open("data/tkg/{}-{}-{}/tkg-{}-{}-{}.png".format(status[date]["Time_Out"].month, status[date]["Time_Out"].day, status[date]["Time_Out"].year, number.split("#")[-1], status[date]["Time_Out"].hour, status[date]["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigoutcanvas.image = imgout
                        sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                        imgin = ImageTk.PhotoImage(Image.open("data/tkg/{}-{}-{}/tkg-{}-{}-{}.png".format(status[date]["Time_In"].month, status[date]["Time_In"].day, status[date]["Time_In"].year, number.split("#")[-1], status[date]["Time_In"].hour, status[date]["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)


                    dates = [i for i in status]
                    dates = dates[::-1]
                    datevar.set("")
                    datesdrop = tk.OptionMenu(popup, datevar, *dates, command = lambda x: submit2(datevar.get()))
                    datesdrop.config(font=("Verdana", 20), width= 20)
                    datesdrop.grid(row=1, column=1, padx=10, pady=10)

                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Ticketing Bank Logs")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = tkg.returnedbanks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        datelabel = tk.Label(popup, text="Date: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        datevar = tk.StringVar(popup)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10, pady=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10, pady=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)

        popup.mainloop()

    def managebanks(self):
        """Popup for adding/removing bar banks"""
        popup = tk.Tk()
        popup.wm_title("Add Ticketing Bank")

        banklabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        bankentry = tk.Entry(popup, font=("Verdana", 20))
        bankentry.grid(row=1, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=2, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: add(bankentry.get())).grid(row=3, column=0, padx=10, pady=10)


        def add(number):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = tkg.addbank(number)
                if success:
                    errorlabel.config(text="Successfully added bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That bank already exists", fg="red")


        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        banks = tkg.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=1, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=2, column=1, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: remove(bankvar.get())).grid(row=3, column=1, padx=10, pady=10)

        def remove(number):
            if number == "":
                errorlabel2.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = tkg.removebank(number.split("#")[-1])
                if success:
                    errorlabel2.config(text="Successfully removed bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel2.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel2.config(text="Error: That bank is already made", fg="red")

        def refresh():
            bankdrop.children['menu'].delete(0, "end")
            for bank in tkg.banks():
                bankdrop.children['menu'].add_command(label=bank, command=lambda opt=bank: bankvar.set(opt))
            bankvar.set("")

            bankentry.delete(0, 'end')

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        popup.mainloop()

    def managelocs(self):
        """Popup for adding and removing locations"""
        popup = tk.Tk()
        popup.wm_title("Manage Ticketing Locations")


        def add(location):

            if location == "" or location == " ":
                errorlabel.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = tkg.addlocation(location)
                if success:
                    errorlabel.config(text="Successfully added location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That location already exists", fg="red")

        def remove(location):
            if location == "" or location == " ":
                errorlabel2.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = tkg.removelocation(location)
                if success:
                    errorlabel2.config(text="Successfully removed location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That location does not exist", fg="red")


        def refresh():
            locdrop.children['menu'].delete(0, "end")
            for loc in tkg.locations():
                locdrop.children['menu'].add_command(label=loc, command=lambda opt=loc: locvar.set(opt))
            locvar.set("")

            locationentry.delete(0, 'end')

        locationaddlabel = tk.Label(popup, text="Location Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        locationentry = tk.Entry(popup, font=("Verdana", 20))
        locationentry.grid(row=1, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="ADD", font=("Verdana", 20), command = lambda: add(locationentry.get())).grid(row=2, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=3, column=0, padx=10, pady=10)

        locationremovelabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        locations = tkg.locations()
        if len(locations) == 0:
            locations = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locdrop = tk.OptionMenu(popup, locvar, *locations)
        locdrop.config(font=("Verdana", 20), width= 20)
        locdrop.grid(row=1, column=1, padx=10, pady=10)

        submitbutton2 = tk.Button(popup, text="REMOVE", font=("Verdana", 20), command = lambda: remove(locvar.get())).grid(row=2, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=3, column=1, padx=10, pady=10)


        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)



        refresh()
        popup.mainloop()

class RetailPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="RETAIL", font=("Verdana", 40)).grid(row=0, column=1, padx=10, pady=10)

        signoutbutton = tk.Button(self, text='SIGN OUT', command=self.signoutbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff002a").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        signinbutton = tk.Button(self, text='SIGN IN', command=self.signinbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#f9f21b").grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        returnbutton = tk.Button(self, text='RETURN', command=self.returnbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#00ce03").grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        currentbankinfobutton = tk.Button(self, text="CURRENT\nBANK INFO", command=self.currentbankinfo, height=2, width=10, font=("Verdana", 35, "bold"), background="cyan").grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        makebankbutton = tk.Button(self, text='MAKE BANK', command=self.makebank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff00ee").grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        managelocbutton = tk.Button(self, text="MANAGE\nLOCATIONS", command=self.managelocs, height=2, width=10, font=("Verdana", 35, "bold"), background="#0c00ff").grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        testbutton = tk.Button(self, text="MANAGE\nBANKS", command=self.managebanks, height=2, width=10, font=("Verdana", 35, "bold"), background="#8c00ff").grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        banklogbutton = tk.Button(self, text="BANK LOG", command=self.banklog, height=2, width=10, font=("Verdana", 35, "bold"), background="#c896ff").grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        backbutton = tk.Button(self, text="BACK", command=lambda: controller.show_frame(StartPage), height=2, width=10, font=("Verdana", 35, "bold"), background="#7a7a7a").grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        # testbutton = tk.Button(self, text="SECRET\nTESTING", command=self.managebanks, height=4, width=10, font=("Verdana", 40, "bold"), background="black", fg="white").grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

        self.retailstatsout = tk.Label(self, text="Banks Out: {}".format(len(retail.signedout())), font=("Verdana", 20))
        self.retailstatsout.grid(row=4, column=0, padx=10, pady=10, sticky="sew")

        self.retailstatsin = tk.Label(self, text="Banks In Audit: {}".format(len(retail.madebanks())), font=("Verdana", 20))
        self.retailstatsin.grid(row=4, column=2, padx=10, pady=10, sticky="sew")

        self.after(1000, self.updatestats)

    def updatestats(self):
        """Updates the bank in/out stats"""
        self.retailstatsout.config(text="Banks Out: {}".format(len(retail.signedout())))
        self.retailstatsin.config(text="Banks In Audit: {}".format(len(retail.madebanks())))
        self.after(1000, self.updatestats)

    def signoutbank(self):
        """Popup for retail sign out"""
        popup = tk.Tk()
        popup.wm_title("Sign Out Retail Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        locationlabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        retaillocs = retail.locations()
        if len(retaillocs) == 0:
            retaillocs = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locsdrop = tk.OptionMenu(popup, locvar, *retaillocs)
        locsdrop.config(font=("Verdana", 20), width= 20)
        locsdrop.grid(row=1, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        retailmade = retail.madebanks()
        if len(retailmade) == 0:
            retailmade = [""]
        madevar = tk.StringVar(popup)
        madevar.set("")
        madedrop = tk.OptionMenu(popup, madevar, *retailmade)
        madedrop.config(font=("Verdana", 20), width= 20)
        madedrop.grid(row=2, column=1, padx=10, pady=10)

        noteslabel = tk.Label(popup, text="Notes: ", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        notesentry = tk.Text(popup, font=("Verdana", 20), height=4, width=22)
        notesentry.grid(row=3, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), locvar.get(), madevar.get(), notesentry.get("1.0", "end"))).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, location, number, notes):
            if name == "" or name == " ":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif location == "" or location == " ":
                errorlabel.config(text="Error: Please select a location", fg="red")
            elif number == "" or number == " ":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = retail.signout(name, location, number.split("#")[-1], notes)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")

        popup.mainloop()

    def signinbank(self):
        """Popup for retail sign in"""
        popup = tk.Tk()
        popup.wm_title("Sign In Retail Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        retailout = retail.signedout()
        if len(retailout) == 0:
            retailout = [" "]
        outvar = tk.StringVar(popup)
        outvar.set("")
        outdrop = tk.OptionMenu(popup, outvar, *retailout)
        outdrop.config(font=("Verdana", 20), width= 20)
        outdrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), outvar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, fg="red", font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, number):
            if name == "":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = retail.signin(name, number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is returned", fg="red")

        popup.mainloop()

    def returnbank(self):
        """Popup for retail return"""
        popup = tk.Tk()
        popup.wm_title("Return Retail Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        retailin = retail.notreturnedbanks()
        if len(retailin) == 0:
            retailin = [" "]
        invar = tk.StringVar(popup)
        invar.set("")
        indrop = tk.OptionMenu(popup, invar, *retailin)
        indrop.config(font=("Verdana", 20), width= 20)
        indrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(invar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number):
            if number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = retail.returnbank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already returned", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not out", fg="red")

        popup.mainloop()

    def makebank(self):
        """Popup for making retail bank"""
        popup = tk.Tk()
        popup.wm_title("Make Retail Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        returnedbanks = retail.returnedbanks()  #Check unmade banks rather than returned
        if len(returnedbanks) == 0:
            returnedbanks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *returnedbanks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        amountlabel = tk.Label(popup, text="Amount: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        amountentry = tk.Entry(popup, font=("Verdana", 20))
        amountentry.grid(row=1, column=1, padx=10, pady=10)
        amountentry.insert(0, "350")

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get(), amountentry.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number, amount):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            elif amount == "":
                success, status = retail.makebank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

            else:
                success, status = retail.makebank(number.split("#")[-1], amount)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

        popup.mainloop()

    def currentbankinfo(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()


            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = retail.signoutinfo(number.split("#")[-1])
                if success:
                    closebutton.destroy()
                    try:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"], status["Notes"]))
                    except:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"]))

                    infoin.config(text="Name: {}\nTime: {}".format(status["Name_In"], status["Time_In"]))


                    try:
                        returninfo.config(text="{}\nTime: {}".format(status["Returned"], status["Returned_Time"]))
                    except:
                        returninfo.config(text="{}".format(status["Returned"]))


                    imgout = ImageTk.PhotoImage(Image.open("data/retail/{}-{}-{}/retail-{}-{}-{}.png".format(status["Time_Out"].month, status["Time_Out"].day, status["Time_Out"].year, number.split("#")[-1], status["Time_Out"].hour, status["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                    sigoutcanvas.image = imgout
                    sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                    try:
                        imgin = ImageTk.PhotoImage(Image.open("data/retail/{}-{}-{}/retail-{}-{}-{}.png".format(status["Time_In"].month, status["Time_In"].day, status["Time_In"].year, number.split("#")[-1], status["Time_In"].hour, status["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
                    except:
                        imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)

                    editbutton = tk.Button(popup, text="EDIT", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=0, padx=10, pady=10) #TODO
                    okaybutton = tk.Button(popup, text="OKAY", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Current Retail Bank Info")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = retail.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20))
        closebutton.grid(row=1, column=0, padx=10, pady=10)
        # submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get()))
        # submitbutton.grid(row=1, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)

        popup.mainloop()

    def banklog(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = retail.banklog(number.split("#")[-1])
                if success:

                    def submit2(date):
                        try:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"], status[date]["Notes"]))
                        except:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"]))

                        infoin.config(text="Name: {}\nTime: {}".format(status[date]["Name_In"], status[date]["Time_In"]))
                        returninfo.config(text="Time: {}".format(status[date]["Returned_Time"]))

                        imgout = ImageTk.PhotoImage(Image.open("data/retail/{}-{}-{}/retail-{}-{}-{}.png".format(status[date]["Time_Out"].month, status[date]["Time_Out"].day, status[date]["Time_Out"].year, number.split("#")[-1], status[date]["Time_Out"].hour, status[date]["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigoutcanvas.image = imgout
                        sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                        imgin = ImageTk.PhotoImage(Image.open("data/retail/{}-{}-{}/retail-{}-{}-{}.png".format(status[date]["Time_In"].month, status[date]["Time_In"].day, status[date]["Time_In"].year, number.split("#")[-1], status[date]["Time_In"].hour, status[date]["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)


                    dates = [i for i in status]
                    dates = dates[::-1]
                    datevar.set("")
                    datesdrop = tk.OptionMenu(popup, datevar, *dates, command = lambda x: submit2(datevar.get()))
                    datesdrop.config(font=("Verdana", 20), width= 20)
                    datesdrop.grid(row=1, column=1, padx=10, pady=10)

                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Retail Bank Logs")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = retail.returnedbanks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        datelabel = tk.Label(popup, text="Date: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        datevar = tk.StringVar(popup)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10, pady=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10, pady=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)

        popup.mainloop()

    def managebanks(self):
        """Popup for adding/removing bar banks"""
        popup = tk.Tk()
        popup.wm_title("Add Retail Bank")

        banklabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        bankentry = tk.Entry(popup, font=("Verdana", 20))
        bankentry.grid(row=1, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=2, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: add(bankentry.get())).grid(row=3, column=0, padx=10, pady=10)


        def add(number):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = retail.addbank(number)
                if success:
                    errorlabel.config(text="Successfully added bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That bank already exists", fg="red")


        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        banks = retail.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=1, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=2, column=1, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: remove(bankvar.get())).grid(row=3, column=1, padx=10, pady=10)

        def remove(number):
            if number == "":
                errorlabel2.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = retail.removebank(number.split("#")[-1])
                if success:
                    errorlabel2.config(text="Successfully removed bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel2.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel2.config(text="Error: That bank is already made", fg="red")

        def refresh():
            bankdrop.children['menu'].delete(0, "end")
            for bank in retail.banks():
                bankdrop.children['menu'].add_command(label=bank, command=lambda opt=bank: bankvar.set(opt))
            bankvar.set("")

            bankentry.delete(0, 'end')

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        popup.mainloop()

    def managelocs(self):
        """Popup for adding and removing locations"""
        popup = tk.Tk()
        popup.wm_title("Manage Retail Locations")


        def add(location):

            if location == "" or location == " ":
                errorlabel.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = retail.addlocation(location)
                if success:
                    errorlabel.config(text="Successfully added location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That location already exists", fg="red")

        def remove(location):
            if location == "" or location == " ":
                errorlabel2.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = retail.removelocation(location)
                if success:
                    errorlabel2.config(text="Successfully removed location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That location does not exist", fg="red")


        def refresh():
            locdrop.children['menu'].delete(0, "end")
            for loc in retail.locations():
                locdrop.children['menu'].add_command(label=loc, command=lambda opt=loc: locvar.set(opt))
            locvar.set("")

            locationentry.delete(0, 'end')

        locationaddlabel = tk.Label(popup, text="Location Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        locationentry = tk.Entry(popup, font=("Verdana", 20))
        locationentry.grid(row=1, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="ADD", font=("Verdana", 20), command = lambda: add(locationentry.get())).grid(row=2, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=3, column=0, padx=10, pady=10)

        locationremovelabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        locations = retail.locations()
        if len(locations) == 0:
            locations = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locdrop = tk.OptionMenu(popup, locvar, *locations)
        locdrop.config(font=("Verdana", 20), width= 20)
        locdrop.grid(row=1, column=1, padx=10, pady=10)

        submitbutton2 = tk.Button(popup, text="REMOVE", font=("Verdana", 20), command = lambda: remove(locvar.get())).grid(row=2, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=3, column=1, padx=10, pady=10)


        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)



        refresh()
        popup.mainloop()

class BikePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BIKE", font=("Verdana", 40)).grid(row=0, column=1, padx=10, pady=10)

        signoutbutton = tk.Button(self, text='SIGN OUT', command=self.signoutbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff002a").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        signinbutton = tk.Button(self, text='SIGN IN', command=self.signinbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#f9f21b").grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        returnbutton = tk.Button(self, text='RETURN', command=self.returnbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#00ce03").grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        currentbankinfobutton = tk.Button(self, text="CURRENT\nBANK INFO", command=self.currentbankinfo, height=2, width=10, font=("Verdana", 35, "bold"), background="cyan").grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        makebankbutton = tk.Button(self, text='MAKE BANK', command=self.makebank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff00ee").grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        managelocbutton = tk.Button(self, text="MANAGE\nLOCATIONS", command=self.managelocs, height=2, width=10, font=("Verdana", 35, "bold"), background="#0c00ff").grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        testbutton = tk.Button(self, text="MANAGE\nBANKS", command=self.managebanks, height=2, width=10, font=("Verdana", 35, "bold"), background="#8c00ff").grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        banklogbutton = tk.Button(self, text="BANK LOG", command=self.banklog, height=2, width=10, font=("Verdana", 35, "bold"), background="#c896ff").grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        backbutton = tk.Button(self, text="BACK", command=lambda: controller.show_frame(StartPage), height=2, width=10, font=("Verdana", 35, "bold"), background="#7a7a7a").grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        # testbutton = tk.Button(self, text="SECRET\nTESTING", command=self.managebanks, height=4, width=10, font=("Verdana", 40, "bold"), background="black", fg="white").grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

        self.bikestatsout = tk.Label(self, text="Banks Out: {}".format(len(bike.signedout())), font=("Verdana", 20))
        self.bikestatsout.grid(row=4, column=0, padx=10, pady=10, sticky="sew")

        self.bikestatsin = tk.Label(self, text="Banks In Audit: {}".format(len(bike.madebanks())), font=("Verdana", 20))
        self.bikestatsin.grid(row=4, column=2, padx=10, pady=10, sticky="sew")

        self.after(1000, self.updatestats)

    def updatestats(self):
        """Updates the bank in/out stats"""
        self.bikestatsout.config(text="Banks Out: {}".format(len(bike.signedout())))
        self.bikestatsin.config(text="Banks In Audit: {}".format(len(bike.madebanks())))
        self.after(1000, self.updatestats)

    def signoutbank(self):
        """Popup for bike sign out"""
        popup = tk.Tk()
        popup.wm_title("Sign Out Bike Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        locationlabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        bikelocs = bike.locations()
        if len(bikelocs) == 0:
            bikelocs = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locsdrop = tk.OptionMenu(popup, locvar, *bikelocs)
        locsdrop.config(font=("Verdana", 20), width= 20)
        locsdrop.grid(row=1, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        bikemade = bike.madebanks()
        if len(bikemade) == 0:
            bikemade = [""]
        madevar = tk.StringVar(popup)
        madevar.set("")
        madedrop = tk.OptionMenu(popup, madevar, *bikemade)
        madedrop.config(font=("Verdana", 20), width= 20)
        madedrop.grid(row=2, column=1, padx=10, pady=10)

        noteslabel = tk.Label(popup, text="Notes: ", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        notesentry = tk.Text(popup, font=("Verdana", 20), height=4, width=22)
        notesentry.grid(row=3, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), locvar.get(), madevar.get(), notesentry.get("1.0", "end"))).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, location, number, notes):
            if name == "" or name == " ":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif location == "" or location == " ":
                errorlabel.config(text="Error: Please select a location", fg="red")
            elif number == "" or number == " ":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = bike.signout(name, location, number.split("#")[-1], notes)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")

        popup.mainloop()

    def signinbank(self):
        """Popup for bike sign in"""
        popup = tk.Tk()
        popup.wm_title("Sign In Bike Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        bikeout = bike.signedout()
        if len(bikeout) == 0:
            bikeout = [" "]
        outvar = tk.StringVar(popup)
        outvar.set("")
        outdrop = tk.OptionMenu(popup, outvar, *bikeout)
        outdrop.config(font=("Verdana", 20), width= 20)
        outdrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), outvar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, fg="red", font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, number):
            if name == "":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = bike.signin(name, number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is returned", fg="red")

        popup.mainloop()

    def returnbank(self):
        """Popup for bike return"""
        popup = tk.Tk()
        popup.wm_title("Return Bike Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        bikein = bike.notreturnedbanks()
        if len(bikein) == 0:
            bikein = [" "]
        invar = tk.StringVar(popup)
        invar.set("")
        indrop = tk.OptionMenu(popup, invar, *bikein)
        indrop.config(font=("Verdana", 20), width= 20)
        indrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(invar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number):
            if number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = bike.returnbank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already returned", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not out", fg="red")

        popup.mainloop()

    def makebank(self):
        """Popup for making bike bank"""
        popup = tk.Tk()
        popup.wm_title("Make Bike Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        returnedbanks = bike.returnedbanks()  #Check unmade banks rather than returned
        if len(returnedbanks) == 0:
            returnedbanks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *returnedbanks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        amountlabel = tk.Label(popup, text="Amount: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        amountentry = tk.Entry(popup, font=("Verdana", 20))
        amountentry.grid(row=1, column=1, padx=10, pady=10)
        amountentry.insert(0, "350")

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get(), amountentry.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number, amount):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            elif amount == "":
                success, status = bike.makebank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

            else:
                success, status = bike.makebank(number.split("#")[-1], amount)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

        popup.mainloop()

    def currentbankinfo(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()

            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = bike.signoutinfo(number.split("#")[-1])
                if success:
                    closebutton.destroy()
                    try:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"], status["Notes"]))
                    except:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"]))

                    infoin.config(text="Name: {}\nTime: {}".format(status["Name_In"], status["Time_In"]))


                    try:
                        returninfo.config(text="{}\nTime: {}".format(status["Returned"], status["Returned_Time"]))
                    except:
                        returninfo.config(text="{}".format(status["Returned"]))


                    imgout = ImageTk.PhotoImage(Image.open("data/bike/{}-{}-{}/bike-{}-{}-{}.png".format(status["Time_Out"].month, status["Time_Out"].day, status["Time_Out"].year, number.split("#")[-1], status["Time_Out"].hour, status["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                    sigoutcanvas.image = imgout
                    sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                    try:
                        imgin = ImageTk.PhotoImage(Image.open("data/bike/{}-{}-{}/bike-{}-{}-{}.png".format(status["Time_In"].month, status["Time_In"].day, status["Time_In"].year, number.split("#")[-1], status["Time_In"].hour, status["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
                    except:
                        imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png").resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)

                    editbutton = tk.Button(popup, text="EDIT", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=0, padx=10, pady=10) #TODO
                    okaybutton = tk.Button(popup, text="OKAY", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Current Bike Bank Info")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = bike.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20))
        closebutton.grid(row=1, column=0, padx=10, pady=10)
        # submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get()))
        # submitbutton.grid(row=1, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)


        popup.mainloop()

    def banklog(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = bike.banklog(number.split("#")[-1])
                if success:

                    def submit2(date):
                        try:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"], status[date]["Notes"]))
                        except:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"]))

                        infoin.config(text="Name: {}\nTime: {}".format(status[date]["Name_In"], status[date]["Time_In"]))
                        returninfo.config(text="Time: {}".format(status[date]["Returned_Time"]))

                        imgout = ImageTk.PhotoImage(Image.open("data/bike/{}-{}-{}/bike-{}-{}-{}.png".format(status[date]["Time_Out"].month, status[date]["Time_Out"].day, status[date]["Time_Out"].year, number.split("#")[-1], status[date]["Time_Out"].hour, status[date]["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigoutcanvas.image = imgout
                        sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                        imgin = ImageTk.PhotoImage(Image.open("data/bike/{}-{}-{}/bike-{}-{}-{}.png".format(status[date]["Time_In"].month, status[date]["Time_In"].day, status[date]["Time_In"].year, number.split("#")[-1], status[date]["Time_In"].hour, status[date]["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)


                    dates = [i for i in status]
                    dates = dates[::-1]
                    datevar.set("")
                    datesdrop = tk.OptionMenu(popup, datevar, *dates, command = lambda x: submit2(datevar.get()))
                    datesdrop.config(font=("Verdana", 20), width= 20)
                    datesdrop.grid(row=1, column=1, padx=10, pady=10)

                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Bike Bank Logs")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = bike.returnedbanks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        datelabel = tk.Label(popup, text="Date: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        datevar = tk.StringVar(popup)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10, pady=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10, pady=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)

        popup.mainloop()

    def managebanks(self):
        """Popup for adding/removing bar banks"""
        popup = tk.Tk()
        popup.wm_title("Add Bike Bank")

        banklabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        bankentry = tk.Entry(popup, font=("Verdana", 20))
        bankentry.grid(row=1, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=2, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: add(bankentry.get())).grid(row=3, column=0, padx=10, pady=10)


        def add(number):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = bike.addbank(number)
                if success:
                    errorlabel.config(text="Successfully added bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That bank already exists", fg="red")


        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        banks = bike.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=1, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=2, column=1, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: remove(bankvar.get())).grid(row=3, column=1, padx=10, pady=10)

        def remove(number):
            if number == "":
                errorlabel2.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = bike.removebank(number.split("#")[-1])
                if success:
                    errorlabel2.config(text="Successfully removed bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel2.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel2.config(text="Error: That bank is already made", fg="red")

        def refresh():
            bankdrop.children['menu'].delete(0, "end")
            for bank in bike.banks():
                bankdrop.children['menu'].add_command(label=bank, command=lambda opt=bank: bankvar.set(opt))
            bankvar.set("")

            bankentry.delete(0, 'end')

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        popup.mainloop()

    def managelocs(self):
        """Popup for adding and removing locations"""
        popup = tk.Tk()
        popup.wm_title("Manage Bike Locations")


        def add(location):

            if location == "" or location == " ":
                errorlabel.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = bike.addlocation(location)
                if success:
                    errorlabel.config(text="Successfully added location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That location already exists", fg="red")

        def remove(location):
            if location == "" or location == " ":
                errorlabel2.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = bike.removelocation(location)
                if success:
                    errorlabel2.config(text="Successfully removed location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That location does not exist", fg="red")


        def refresh():
            locdrop.children['menu'].delete(0, "end")
            for loc in bike.locations():
                locdrop.children['menu'].add_command(label=loc, command=lambda opt=loc: locvar.set(opt))
            locvar.set("")

            locationentry.delete(0, 'end')

        locationaddlabel = tk.Label(popup, text="Location Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        locationentry = tk.Entry(popup, font=("Verdana", 20))
        locationentry.grid(row=1, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="ADD", font=("Verdana", 20), command = lambda: add(locationentry.get())).grid(row=2, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=3, column=0, padx=10, pady=10)

        locationremovelabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        locations = bike.locations()
        if len(locations) == 0:
            locations = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locdrop = tk.OptionMenu(popup, locvar, *locations)
        locdrop.config(font=("Verdana", 20), width= 20)
        locdrop.grid(row=1, column=1, padx=10, pady=10)

        submitbutton2 = tk.Button(popup, text="REMOVE", font=("Verdana", 20), command = lambda: remove(locvar.get())).grid(row=2, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=3, column=1, padx=10, pady=10)


        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)



        refresh()
        popup.mainloop()

class ChangePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CHANGE", font=("Verdana", 40)).grid(row=0, column=1, padx=10, pady=10)

        signoutbutton = tk.Button(self, text='SIGN OUT', command=self.signoutbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff002a").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        signinbutton = tk.Button(self, text='SIGN IN', command=self.signinbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#f9f21b").grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        returnbutton = tk.Button(self, text='RETURN', command=self.returnbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#00ce03").grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        currentbankinfobutton = tk.Button(self, text="CURRENT\nBANK INFO", command=self.currentbankinfo, height=2, width=10, font=("Verdana", 35, "bold"), background="cyan").grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        makebankbutton = tk.Button(self, text='MAKE BANK', command=self.makebank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff00ee").grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        managelocbutton = tk.Button(self, text="MANAGE\nLOCATIONS", command=self.managelocs, height=2, width=10, font=("Verdana", 35, "bold"), background="#0c00ff").grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        testbutton = tk.Button(self, text="MANAGE\nBANKS", command=self.managebanks, height=2, width=10, font=("Verdana", 35, "bold"), background="#8c00ff").grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        banklogbutton = tk.Button(self, text="BANK LOG", command=self.banklog, height=2, width=10, font=("Verdana", 35, "bold"), background="#c896ff").grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        backbutton = tk.Button(self, text="BACK", command=lambda: controller.show_frame(StartPage), height=2, width=10, font=("Verdana", 35, "bold"), background="#7a7a7a").grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        # testbutton = tk.Button(self, text="SECRET\nTESTING", command=self.managebanks, height=4, width=10, font=("Verdana", 40, "bold"), background="black", fg="white").grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

        self.changestatsout = tk.Label(self, text="Banks Out: {}".format(len(change.signedout())), font=("Verdana", 20))
        self.changestatsout.grid(row=4, column=0, padx=10, pady=10, sticky="sew")

        self.changestatsin = tk.Label(self, text="Banks In Audit: {}".format(len(change.madebanks())), font=("Verdana", 20))
        self.changestatsin.grid(row=4, column=2, padx=10, pady=10, sticky="sew")

        self.after(1000, self.updatestats)

    def updatestats(self):
        """Updates the bank in/out stats"""
        self.changestatsout.config(text="Banks Out: {}".format(len(change.signedout())))
        self.changestatsin.config(text="Banks In Audit: {}".format(len(change.madebanks())))
        self.after(1000, self.updatestats)

    def signoutbank(self):
        """Popup for change sign out"""
        popup = tk.Tk()
        popup.wm_title("Sign Out Change Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        locationlabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        changelocs = change.locations() # TODO: all locations
        if len(changelocs) == 0:
            changelocs = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locsdrop = tk.OptionMenu(popup, locvar, *changelocs)
        locsdrop.config(font=("Verdana", 20), width= 20)
        locsdrop.grid(row=1, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        changemade = change.madebanks()
        if len(changemade) == 0:
            changemade = [""]
        madevar = tk.StringVar(popup)
        madevar.set("")
        madedrop = tk.OptionMenu(popup, madevar, *changemade)
        madedrop.config(font=("Verdana", 20), width= 20)
        madedrop.grid(row=2, column=1, padx=10, pady=10)

        noteslabel = tk.Label(popup, text="Notes: ", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        notesentry = tk.Text(popup, font=("Verdana", 20), height=4, width=22)
        notesentry.grid(row=3, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), locvar.get(), madevar.get(), notesentry.get("1.0", "end"))).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, location, number, notes):
            if name == "" or name == " ":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif location == "" or location == " ":
                errorlabel.config(text="Error: Please select a location", fg="red")
            elif number == "" or number == " ":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = change.signout(name, location, number.split("#")[-1], notes)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")

        popup.mainloop()

    def signinbank(self):
        """Popup for change sign in"""
        popup = tk.Tk()
        popup.wm_title("Sign In Change Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        changeout = change.signedout()
        if len(changeout) == 0:
            changeout = [" "]
        outvar = tk.StringVar(popup)
        outvar.set("")
        outdrop = tk.OptionMenu(popup, outvar, *changeout)
        outdrop.config(font=("Verdana", 20), width= 20)
        outdrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), outvar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, fg="red", font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, number):
            if name == "":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = change.signin(name, number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is returned", fg="red")

        popup.mainloop()

    def returnbank(self):
        """Popup for change return"""
        popup = tk.Tk()
        popup.wm_title("Return Change Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        changein = change.notreturnedbanks()
        if len(changein) == 0:
            changein = [" "]
        invar = tk.StringVar(popup)
        invar.set("")
        indrop = tk.OptionMenu(popup, invar, *changein)
        indrop.config(font=("Verdana", 20), width= 20)
        indrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(invar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number):
            if number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = change.returnbank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already returned", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not out", fg="red")

        popup.mainloop()

    def makebank(self):
        """Popup for making change bank"""
        popup = tk.Tk()
        popup.wm_title("Make Change Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        returnedbanks = change.returnedbanks()  #Check unmade banks rather than returned
        if len(returnedbanks) == 0:
            returnedbanks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *returnedbanks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        amountlabel = tk.Label(popup, text="Amount: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        amountentry = tk.Entry(popup, font=("Verdana", 20))
        amountentry.grid(row=1, column=1, padx=10, pady=10)
        amountentry.insert(0, "500")

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get(), amountentry.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number, amount):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            elif amount == "":
                success, status = change.makebank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

            else:
                success, status = change.makebank(number.split("#")[-1], amount)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

        popup.mainloop()

    def currentbankinfo(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()

            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = change.signoutinfo(number.split("#")[-1])
                if success:
                    closebutton.destroy()
                    try:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"], status["Notes"]))
                    except:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"]))

                    infoin.config(text="Name: {}\nTime: {}".format(status["Name_In"], status["Time_In"]))


                    try:
                        returninfo.config(text="{}\nTime: {}".format(status["Returned"], status["Returned_Time"]))
                    except:
                        returninfo.config(text="{}".format(status["Returned"]))


                    imgout = ImageTk.PhotoImage(Image.open("data/change/{}-{}-{}/change-{}-{}-{}.png".format(status["Time_Out"].month, status["Time_Out"].day, status["Time_Out"].year, number.split("#")[-1], status["Time_Out"].hour, status["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                    sigoutcanvas.image = imgout
                    sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                    try:
                        imgin = ImageTk.PhotoImage(Image.open("data/change/{}-{}-{}/change-{}-{}-{}.png".format(status["Time_In"].month, status["Time_In"].day, status["Time_In"].year, number.split("#")[-1], status["Time_In"].hour, status["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
                    except:
                        imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)

                    editbutton = tk.Button(popup, text="EDIT", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=0, padx=10, pady=10) #TODO
                    okaybutton = tk.Button(popup, text="OKAY", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Current Change Bank Info")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = change.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20))
        closebutton.grid(row=1, column=0, padx=10, pady=10)
        # submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get()))
        # submitbutton.grid(row=1, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)


        popup.mainloop()

    def banklog(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = change.banklog(number.split("#")[-1])
                if success:

                    def submit2(date):
                        try:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"], status[date]["Notes"]))
                        except:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"]))

                        infoin.config(text="Name: {}\nTime: {}".format(status[date]["Name_In"], status[date]["Time_In"]))
                        returninfo.config(text="Time: {}".format(status[date]["Returned_Time"]))

                        imgout = ImageTk.PhotoImage(Image.open("data/change/{}-{}-{}/change-{}-{}-{}.png".format(status[date]["Time_Out"].month, status[date]["Time_Out"].day, status[date]["Time_Out"].year, number.split("#")[-1], status[date]["Time_Out"].hour, status[date]["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigoutcanvas.image = imgout
                        sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                        imgin = ImageTk.PhotoImage(Image.open("data/change/{}-{}-{}/change-{}-{}-{}.png".format(status[date]["Time_In"].month, status[date]["Time_In"].day, status[date]["Time_In"].year, number.split("#")[-1], status[date]["Time_In"].hour, status[date]["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)


                    dates = [i for i in status]
                    dates = dates[::-1]
                    datevar.set("")
                    datesdrop = tk.OptionMenu(popup, datevar, *dates, command = lambda x: submit2(datevar.get()))
                    datesdrop.config(font=("Verdana", 20), width= 20)
                    datesdrop.grid(row=1, column=1, padx=10, pady=10)

                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Change Bank Logs")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = change.returnedbanks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        datelabel = tk.Label(popup, text="Date: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        datevar = tk.StringVar(popup)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10, pady=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10, pady=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)

        popup.mainloop()

    def managebanks(self):
        """Popup for adding/removing bar banks"""
        popup = tk.Tk()
        popup.wm_title("Add Change Bank")

        banklabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        bankentry = tk.Entry(popup, font=("Verdana", 20))
        bankentry.grid(row=1, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=2, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: add(bankentry.get())).grid(row=3, column=0, padx=10, pady=10)


        def add(number):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = change.addbank(number)
                if success:
                    errorlabel.config(text="Successfully added bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That bank already exists", fg="red")


        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        banks = change.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=1, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=2, column=1, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: remove(bankvar.get())).grid(row=3, column=1, padx=10, pady=10)

        def remove(number):
            if number == "":
                errorlabel2.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = change.removebank(number.split("#")[-1])
                if success:
                    errorlabel2.config(text="Successfully removed bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel2.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel2.config(text="Error: That bank is already made", fg="red")

        def refresh():
            bankdrop.children['menu'].delete(0, "end")
            for bank in change.banks():
                bankdrop.children['menu'].add_command(label=bank, command=lambda opt=bank: bankvar.set(opt))
            bankvar.set("")

            bankentry.delete(0, 'end')

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        popup.mainloop()

    def managelocs(self):
        """Popup for adding and removing locations"""
        popup = tk.Tk()
        popup.wm_title("Manage Change Locations")


        def add(location):

            if location == "" or location == " ":
                errorlabel.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = change.addlocation(location)
                if success:
                    errorlabel.config(text="Successfully added location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That location already exists", fg="red")

        def remove(location):
            if location == "" or location == " ":
                errorlabel2.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = change.removelocation(location)
                if success:
                    errorlabel2.config(text="Successfully removed location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That location does not exist", fg="red")


        def refresh():
            locdrop.children['menu'].delete(0, "end")
            for loc in change.locations():
                locdrop.children['menu'].add_command(label=loc, command=lambda opt=loc: locvar.set(opt))
            locvar.set("")

            locationentry.delete(0, 'end')

        locationaddlabel = tk.Label(popup, text="Location Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        locationentry = tk.Entry(popup, font=("Verdana", 20))
        locationentry.grid(row=1, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="ADD", font=("Verdana", 20), command = lambda: add(locationentry.get())).grid(row=2, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=3, column=0, padx=10, pady=10)

        locationremovelabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        locations = change.locations()
        if len(locations) == 0:
            locations = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locdrop = tk.OptionMenu(popup, locvar, *locations)
        locdrop.config(font=("Verdana", 20), width= 20)
        locdrop.grid(row=1, column=1, padx=10, pady=10)

        submitbutton2 = tk.Button(popup, text="REMOVE", font=("Verdana", 20), command = lambda: remove(locvar.get())).grid(row=2, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=3, column=1, padx=10, pady=10)


        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)



        refresh()
        popup.mainloop()

class FannyPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="FANNY", font=("Verdana", 40)).grid(row=0, column=1, padx=10, pady=10)

        signoutbutton = tk.Button(self, text='SIGN OUT', command=self.signoutbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff002a").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        signinbutton = tk.Button(self, text='SIGN IN', command=self.signinbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#f9f21b").grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        returnbutton = tk.Button(self, text='RETURN', command=self.returnbank, height=2, width=10, font=("Verdana", 35, "bold"), background="#00ce03").grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        currentbankinfobutton = tk.Button(self, text="CURRENT\nBANK INFO", command=self.currentbankinfo, height=2, width=10, font=("Verdana", 35, "bold"), background="cyan").grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        makebankbutton = tk.Button(self, text='MAKE BANK', command=self.makebank, height=2, width=10, font=("Verdana", 35, "bold"), background="#ff00ee").grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        managelocbutton = tk.Button(self, text="MANAGE\nLOCATIONS", command=self.managelocs, height=2, width=10, font=("Verdana", 35, "bold"), background="#0c00ff").grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        testbutton = tk.Button(self, text="MANAGE\nBANKS", command=self.managebanks, height=2, width=10, font=("Verdana", 35, "bold"), background="#8c00ff").grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        banklogbutton = tk.Button(self, text="BANK LOG", command=self.banklog, height=2, width=10, font=("Verdana", 35, "bold"), background="#c896ff").grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        backbutton = tk.Button(self, text="BACK", command=lambda: controller.show_frame(StartPage), height=2, width=10, font=("Verdana", 35, "bold"), background="#7a7a7a").grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        # testbutton = tk.Button(self, text="SECRET\nTESTING", command=self.managebanks, height=4, width=10, font=("Verdana", 40, "bold"), background="black", fg="white").grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

        self.fannystatsout = tk.Label(self, text="Banks Out: {}".format(len(fanny.signedout())), font=("Verdana", 20))
        self.fannystatsout.grid(row=4, column=0, padx=10, pady=10, sticky="sew")

        self.fannystatsin = tk.Label(self, text="Banks In Audit: {}".format(len(fanny.madebanks())), font=("Verdana", 20))
        self.fannystatsin.grid(row=4, column=2, padx=10, pady=10, sticky="sew")

        self.after(1000, self.updatestats)

    def updatestats(self):
        """Updates the bank in/out stats"""
        self.fannystatsout.config(text="Banks Out: {}".format(len(fanny.signedout())))
        self.fannystatsin.config(text="Banks In Audit: {}".format(len(fanny.madebanks())))
        self.after(1000, self.updatestats)

    def signoutbank(self):
        """Popup for fanny sign out"""
        popup = tk.Tk()
        popup.wm_title("Sign Out Fanny Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        locationlabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        fannylocs = fanny.locations()
        if len(fannylocs) == 0:
            fannylocs = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locsdrop = tk.OptionMenu(popup, locvar, *fannylocs)
        locsdrop.config(font=("Verdana", 20), width= 20)
        locsdrop.grid(row=1, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        fannymade = fanny.madebanks()
        if len(fannymade) == 0:
            fannymade = [""]
        madevar = tk.StringVar(popup)
        madevar.set("")
        madedrop = tk.OptionMenu(popup, madevar, *fannymade)
        madedrop.config(font=("Verdana", 20), width= 20)
        madedrop.grid(row=2, column=1, padx=10, pady=10)

        noteslabel = tk.Label(popup, text="Notes: ", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        notesentry = tk.Text(popup, font=("Verdana", 20), height=4, width=22)
        notesentry.grid(row=3, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), locvar.get(), madevar.get(), notesentry.get("1.0", "end"))).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, location, number, notes):
            if name == "" or name == " ":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif location == "" or location == " ":
                errorlabel.config(text="Error: Please select a location", fg="red")
            elif number == "" or number == " ":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = fanny.signout(name, location, number.split("#")[-1], notes)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")

        popup.mainloop()

    def signinbank(self):
        """Popup for fanny sign in"""
        popup = tk.Tk()
        popup.wm_title("Sign In Fanny Bank")

        namelabel = tk.Label(popup, text="Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        nameentry = tk.Entry(popup, font=("Verdana", 20))
        nameentry.grid(row=0, column=1, padx=10, pady=10)

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        fannyout = fanny.signedout()
        if len(fannyout) == 0:
            fannyout = [" "]
        outvar = tk.StringVar(popup)
        outvar.set("")
        outdrop = tk.OptionMenu(popup, outvar, *fannyout)
        outdrop.config(font=("Verdana", 20), width= 20)
        outdrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), outvar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, fg="red", font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(name, number):
            if name == "":
                errorlabel.config(text="Error: Please enter a name", fg="red")
            elif number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = fanny.signin(name, number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not out", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already signed in", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is returned", fg="red")

        popup.mainloop()

    def returnbank(self):
        """Popup for fanny return"""
        popup = tk.Tk()
        popup.wm_title("Return Fanny Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        fannyin = fanny.notreturnedbanks()
        if len(fannyin) == 0:
            fannyin = [" "]
        invar = tk.StringVar(popup)
        invar.set("")
        indrop = tk.OptionMenu(popup, invar, *fannyin)
        indrop.config(font=("Verdana", 20), width= 20)
        indrop.grid(row=1, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(invar.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number):
            if number == "":
                errorlabel.config(text="Error: Please select a bank number", fg="red")
            else:
                success, status = fanny.returnbank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: Please select a bank number", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not signed in", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already returned", fg="red")
                elif status == 3:
                    errorlabel.config(text="Error: That bank is not out", fg="red")

        popup.mainloop()

    def makebank(self):
        """Popup for making fanny bank"""
        popup = tk.Tk()
        popup.wm_title("Make Fanny Bank")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        returnedbanks = fanny.returnedbanks()  #Check unmade banks rather than returned
        if len(returnedbanks) == 0:
            returnedbanks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *returnedbanks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        amountlabel = tk.Label(popup, text="Amount: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        amountentry = tk.Entry(popup, font=("Verdana", 20))
        amountentry.grid(row=1, column=1, padx=10, pady=10)
        amountentry.insert(0, "350")

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get(), amountentry.get())).grid(row=4, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=5, column=1, padx=10, pady=10)

        def submit(number, amount):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            elif amount == "":
                success, status = fanny.makebank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

            else:
                success, status = fanny.makebank(number.split("#")[-1], amount)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel.config(text="Error: That bank is already made", fg="red")

        popup.mainloop()

    def currentbankinfo(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")
            except:
                pass

        def submit(number):
            refresh()

            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = fanny.signoutinfo(number.split("#")[-1])
                if success:
                    closebutton.destroy()
                    try:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"], status["Notes"]))
                    except:
                        infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status["Name_Out"], status["Time_Out"], status["Location"], status["Amount"]))

                    infoin.config(text="Name: {}\nTime: {}".format(status["Name_In"], status["Time_In"]))


                    try:
                        returninfo.config(text="{}\nTime: {}".format(status["Returned"], status["Returned_Time"]))
                    except:
                        returninfo.config(text="{}".format(status["Returned"]))


                    imgout = ImageTk.PhotoImage(Image.open("data/fanny/{}-{}-{}/fanny-{}-{}-{}.png".format(status["Time_Out"].month, status["Time_Out"].day, status["Time_Out"].year, number.split("#")[-1], status["Time_Out"].hour, status["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                    sigoutcanvas.image = imgout
                    sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                    try:
                        imgin = ImageTk.PhotoImage(Image.open("data/fanny/{}-{}-{}/fanny-{}-{}-{}.png".format(status["Time_In"].month, status["Time_In"].day, status["Time_In"].year, number.split("#")[-1], status["Time_In"].hour, status["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
                    except:
                        imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)

                    editbutton = tk.Button(popup, text="EDIT", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=0, padx=10, pady=10) #TODO
                    okaybutton = tk.Button(popup, text="OKAY", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)
                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Current Fanny Bank Info")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = fanny.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20))
        closebutton.grid(row=1, column=0, padx=10, pady=10)
        # submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(bankvar.get()))
        # submitbutton.grid(row=1, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)


        popup.mainloop()

    def banklog(self):
        """Popup for showing bank info"""

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")

                imgout = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigoutcanvas.image = imgout
                sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                imgin = ImageTk.PhotoImage(Image.open("data/blanksignature.png"))
                sigincanvas.image = imgin
                sigincanvas.create_image(20, 20, anchor="nw", image=imgin)
            except:
                pass

        def submit(number):
            refresh()
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = fanny.banklog(number.split("#")[-1])
                if success:

                    def submit2(date):
                        try:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"], status[date]["Notes"]))
                        except:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"]))

                        infoin.config(text="Name: {}\nTime: {}".format(status[date]["Name_In"], status[date]["Time_In"]))
                        returninfo.config(text="Time: {}".format(status[date]["Returned_Time"]))

                        imgout = ImageTk.PhotoImage(Image.open("data/fanny/{}-{}-{}/fanny-{}-{}-{}.png".format(status[date]["Time_Out"].month, status[date]["Time_Out"].day, status[date]["Time_Out"].year, number.split("#")[-1], status[date]["Time_Out"].hour, status[date]["Time_Out"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigoutcanvas.image = imgout
                        sigoutcanvas.create_image(20, 20, anchor="nw", image=imgout)

                        imgin = ImageTk.PhotoImage(Image.open("data/fanny/{}-{}-{}/fanny-{}-{}-{}.png".format(status[date]["Time_In"].month, status[date]["Time_In"].day, status[date]["Time_In"].year, number.split("#")[-1], status[date]["Time_In"].hour, status[date]["Time_In"].minute)).resize((500,110), Image.ANTIALIAS))
                        sigincanvas.image = imgin
                        sigincanvas.create_image(20, 20, anchor="nw", image=imgin)


                    dates = [i for i in status]
                    dates = dates[::-1]
                    datevar.set("")
                    datesdrop = tk.OptionMenu(popup, datevar, *dates, command = lambda x: submit2(datevar.get()))
                    datesdrop.config(font=("Verdana", 20), width= 20)
                    datesdrop.grid(row=1, column=1, padx=10, pady=10)

                elif status == 0:
                    errorlabel.config(text="Error: That bank does not exist", fg="red")


        popup = tk.Toplevel()
        popup.wm_title("Fanny Bank Logs")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = fanny.returnedbanks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 15))
        errorlabel.grid(row=1, column=1, padx=10, pady=10)

        datelabel = tk.Label(popup, text="Date: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        datevar = tk.StringVar(popup)

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        # signatureoutlabel = tk.Label(popup, text = "Sign Out Signature:", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        sigoutcanvas = tk.Canvas(popup, width = 500, height = 130)
        sigoutcanvas.grid(row=3, column=1, padx=10, pady=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=4, column=1, padx=10, pady=10)

        # signatureinlabel = tk.Label(popup, text = "Sign In Signature:", font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        sigincanvas = tk.Canvas(popup, width = 500, height = 130)
        sigincanvas.grid(row=5, column=1, padx=10, pady=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=6, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=6, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20)).grid(row=7, column=1, padx=10, pady=10)

        popup.mainloop()

    def managebanks(self):
        """Popup for adding/removing bar banks"""
        popup = tk.Tk()
        popup.wm_title("Add Fanny Bank")

        banklabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        bankentry = tk.Entry(popup, font=("Verdana", 20))
        bankentry.grid(row=1, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=2, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: add(bankentry.get())).grid(row=3, column=0, padx=10, pady=10)


        def add(number):
            if number == "":
                errorlabel.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = fanny.addbank(number)
                if success:
                    errorlabel.config(text="Successfully added bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That bank already exists", fg="red")


        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        banks = fanny.banks()
        if len(banks) == 0:
            banks = [" "]
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks)
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=1, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=2, column=1, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: remove(bankvar.get())).grid(row=3, column=1, padx=10, pady=10)

        def remove(number):
            if number == "":
                errorlabel2.config(text="Error: Please enter a bank number", fg="red")
            else:
                success, status = fanny.removebank(number.split("#")[-1])
                if success:
                    errorlabel2.config(text="Successfully removed bank", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That bank does not exist", fg="red")
                elif status == 1:
                    errorlabel2.config(text="Error: That bank is not returned", fg="red")
                elif status == 2:
                    errorlabel2.config(text="Error: That bank is already made", fg="red")

        def refresh():
            bankdrop.children['menu'].delete(0, "end")
            for bank in fanny.banks():
                bankdrop.children['menu'].add_command(label=bank, command=lambda opt=bank: bankvar.set(opt))
            bankvar.set("")

            bankentry.delete(0, 'end')

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        popup.mainloop()

    def managelocs(self):
        """Popup for adding and removing locations"""
        popup = tk.Tk()
        popup.wm_title("Manage Fanny Locations")


        def add(location):

            if location == "" or location == " ":
                errorlabel.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = fanny.addlocation(location)
                if success:
                    errorlabel.config(text="Successfully added location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel.config(text="Error: That location already exists", fg="red")

        def remove(location):
            if location == "" or location == " ":
                errorlabel2.config(text="Error: Please enter a location", fg="red")
            else:
                success, status = fanny.removelocation(location)
                if success:
                    errorlabel2.config(text="Successfully removed location", fg="blue")
                    save()
                    refresh()
                elif status == 0:
                    errorlabel2.config(text="Error: That location does not exist", fg="red")


        def refresh():
            locdrop.children['menu'].delete(0, "end")
            for loc in fanny.locations():
                locdrop.children['menu'].add_command(label=loc, command=lambda opt=loc: locvar.set(opt))
            locvar.set("")

            locationentry.delete(0, 'end')

        locationaddlabel = tk.Label(popup, text="Location Name: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        locationentry = tk.Entry(popup, font=("Verdana", 20))
        locationentry.grid(row=1, column=0, padx=10, pady=10)

        submitbutton = tk.Button(popup, text="ADD", font=("Verdana", 20), command = lambda: add(locationentry.get())).grid(row=2, column=0, padx=10, pady=10)

        errorlabel = tk.Label(popup, font=("Verdana", 10))
        errorlabel.grid(row=3, column=0, padx=10, pady=10)

        locationremovelabel = tk.Label(popup, text="Location: ", font=("Verdana", 20)).grid(row=0, column=1, padx=10, pady=10)
        locations = fanny.locations()
        if len(locations) == 0:
            locations = [" "]
        locvar = tk.StringVar(popup)
        locvar.set("")
        locdrop = tk.OptionMenu(popup, locvar, *locations)
        locdrop.config(font=("Verdana", 20), width= 20)
        locdrop.grid(row=1, column=1, padx=10, pady=10)

        submitbutton2 = tk.Button(popup, text="REMOVE", font=("Verdana", 20), command = lambda: remove(locvar.get())).grid(row=2, column=1, padx=10, pady=10)

        errorlabel2 = tk.Label(popup, font=("Verdana", 10))
        errorlabel2.grid(row=3, column=1, padx=10, pady=10)


        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command=popup.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        refresh()
        popup.mainloop()



app = Tracking()
# app.geometry("1920x1080")
app.mainloop()
