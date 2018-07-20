import tkinter as tk
from tkinter import ttk
from banks import *
import pickle

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

    try:
        with open("bar.pickle", "rb") as f:
            bar = pickle.load(f)
    except:
        bar = Bar()

    try:
        with open("fb.pickle", "rb") as f:
            fb = pickle.load(f)
    except:
        fb = FB()

    try:
        with open("tkg.pickle", "rb") as f:
            tkg = pickle.load(f)
    except:
        tkg = TKG()

    try:
        with open("retail.pickle", "rb") as f:
            retail = pickle.load(f)
    except:
        retail = Retail()

    try:
        with open("bike.pickle", "rb") as f:
            bike = pickle.load(f)
    except:
        bike = Bike()

    try:
        with open("change.pickle", "rb") as f:
            change = pickle.load(f)
    except:
        change = Change()

    try:
        with open("fanny.pickle", "rb") as f:
            fanny = pickle.load(f)
    except:
        fanny = Fanny()

def save():
    """Saves the type objects into a pickle"""

    with open("bar.pickle", "wb") as f:
        pickle.dump(bar, f)

    with open("fb.pickle", "wb") as f:
        pickle.dump(fb, f)

    with open("tkg.pickle", "wb") as f:
        pickle.dump(tkg, f)

    with open("retail.pickle", "wb") as f:
        pickle.dump(retail, f)

    with open("bike.pickle", "wb") as f:
        pickle.dump(bike, f)

    with open("change.pickle", "wb") as f:
        pickle.dump(change, f)

    with open("fanny.pickle", "wb") as f:
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
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for F in (StartPage, BarPage):

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

        barbutton = tk.Button(self, text="BAR", command=lambda: controller.show_frame(BarPage), height=4, width=10, font=("Verdana", 40, "bold"), background="cyan").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        fbbutton = tk.Button(self, text='FOOD & \nBEVERAGE', command=lambda: controller.show_frame(BarPage), height=4, width=10, font=("Verdana", 40, "bold"), background="blue").grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tkgbutton = tk.Button(self, text='TICKETING', command=lambda: controller.show_frame(BarPage), height=4, width=10, font=("Verdana", 40, "bold"), background="black", fg="white").grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        retailbutton = tk.Button(self, text='RETAIL', command=lambda: controller.show_frame(BarPage), height=4, width=10, font=("Verdana", 40, "bold"), background="#00ce03").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        bikebutton = tk.Button(self, text='BIKE', command=lambda: controller.show_frame(BarPage), height=4, width=10, font=("Verdana", 40, "bold"), background="red").grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        changebutton = tk.Button(self, text='CHANGE', command=lambda: controller.show_frame(BarPage), height=4, width=10, font=("Verdana", 40, "bold"), background="magenta").grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        fannybutton = tk.Button(self, text='FANNY\nPACK', command=lambda: controller.show_frame(BarPage), height=4, width=10, font=("Verdana", 40, "bold"), background="#7a7a7a").grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        exitbutton = tk.Button(self, text='EXIT', command=self.exitprogram, height=4, width=10, font=("Verdana", 40, "bold"), background="#7a7a7a").grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

        self.outinpark = tk.Label(self, text="Banks Out:\nBar: {}\nF&B: {}\nTicketing: {}\nRetail: {}\nBike: {}\nChange: {}\nFanny: {}".format((len(bar.signedout())), (len(fb.signedout())), (len(tkg.signedout())), (len(retail.signedout())), (len(bike.signedout())), (len(change.signedout())), (len(fanny.signedout()))), font=("Verdana", 20))
        self.outinpark.grid(row=0, column=3, padx=10, pady=10)
        self.inaudit = tk.Label(self, text="Banks In:\nBar: {}\nF&B: {}\nTicketing: {}\nRetail: {}\nBike: {}\nChange: {}\nFanny: {}".format((len(bar.madebanks())), (len(fb.madebanks())), (len(tkg.madebanks())), (len(retail.madebanks())), (len(bike.madebanks())), (len(change.madebanks())), (len(fanny.madebanks()))), font=("Verdana", 20))
        self.inaudit.grid(row=1, column=3, padx=10, pady=10)
        self.after(1000, self.updatestats)

    def updatestats(self):
        """Updates the bank in/out stats"""
        self.outinpark.config(text="Banks Out:\nBar: {}\nF&B: {}\nTicketing: {}\nRetail: {}\nBike: {}\nChange: {}\nFanny: {}".format((len(bar.signedout())), (len(fb.signedout())), (len(tkg.signedout())), (len(retail.signedout())), (len(bike.signedout())), (len(change.signedout())), (len(fanny.signedout()))))
        self.inaudit.config(text="Banks In:\nBar: {}\nF&B: {}\nTicketing: {}\nRetail: {}\nBike: {}\nChange: {}\nFanny: {}".format((len(bar.madebanks())), (len(fb.madebanks())), (len(tkg.madebanks())), (len(retail.madebanks())), (len(bike.madebanks())), (len(change.madebanks())), (len(fanny.madebanks()))))
        self.after(1000, self.updatestats)

    def exitprogram(self):
        """Function to properly exit program"""
        save()
        quit()

#TODO: update errors so they don't overlap

class BarPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label = tk.Label(self, text="BAR BANKS", font=("Verdana", 40)).grid()

        signoutbutton = tk.Button(self, text='SIGN OUT', command=self.signoutbank, height=4, width=10, font=("Verdana", 40, "bold"), background="#ff002a").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        signinbutton = tk.Button(self, text='SIGN IN', command=self.signinbank, height=4, width=10, font=("Verdana", 40, "bold"), background="#f9f21b").grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        returnbutton = tk.Button(self, text='RETURN', command=self.returnbank, height=4, width=10, font=("Verdana", 40, "bold"), background="#00ce03").grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        currentbankinfobutton = tk.Button(self, text="CURRENT\nBANK INFO", command=self.currentbankinfo, height=4, width=10, font=("Verdana", 40, "bold"), background="cyan").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        makebankbutton = tk.Button(self, text='MAKE BANK', command=self.makebank, height=4, width=10, font=("Verdana", 40, "bold"), background="#ff00ee").grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        managelocbutton = tk.Button(self, text="MANAGE\nLOCATIONS", command=self.managelocs, height=4, width=10, font=("Verdana", 40, "bold"), background="#0c00ff").grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        testbutton = tk.Button(self, text="MANAGE\nBANKS", command=self.managebanks, height=4, width=10, font=("Verdana", 40, "bold"), background="#8c00ff").grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        banklogbutton = tk.Button(self, text="BANK LOG", command=self.banklog, height=4, width=10, font=("Verdana", 40, "bold"), background="#c896ff").grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        backbutton = tk.Button(self, text="BACK", command=lambda: controller.show_frame(StartPage), height=4, width=10, font=("Verdana", 40, "bold"), background="#7a7a7a").grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

        # testbutton = tk.Button(self, text="SECRET\nTESTING", command=self.managebanks, height=4, width=10, font=("Verdana", 40, "bold"), background="black", fg="white").grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

        self.barstats = tk.Label(self, text="Bar Banks Out: {}\n\nBar Banks In Audit: {}".format(len(bar.signedout()), len(bar.madebanks())), font=("Verdana", 20))
        self.barstats.grid(row=0, column=3, padx=10, pady=10)
        self.after(1000, self.updatestats)

    def updatestats(self):
        """Updates the bank in/out stats"""
        self.barstats.config(text="Bar Banks Out: {}\n\nBar Banks In Audit: {}".format(len(bar.signedout()), len(bar.madebanks())))
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
        notesentry = tk.Entry(popup, font=("Verdana", 20))
        notesentry.grid(row=3, column=1, padx=10, pady=10)

        close = tk.Button(popup, text="CLOSE", font=("Verdana", 20), command = popup.destroy).grid(row=4, column=0, padx=10, pady=10)
        submitbutton = tk.Button(popup, text="SUBMIT", font=("Verdana", 20), command = lambda: submit(nameentry.get(), locvar.get(), madevar.get(), notesentry.get())).grid(row=4, column=1, padx=10, pady=10)

        def submit(name, location, number, notes):
            if name == "" or name == " ":
                errorlabel = tk.Label(popup, text="Error: Please enter a name", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
            elif location == "" or location == " ":
                errorlabel = tk.Label(popup, text="Error: Please select a location", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
            elif number == "" or number == " ":
                errorlabel = tk.Label(popup, text="Error: Please select a bank number", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
            else:
                success, status = bar.signout(name, location, number.split("#")[-1], notes)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel = tk.Label(popup, text="Error: Please select a bank number", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 1:
                    errorlabel = tk.Label(popup, text="Error: That bank is out", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 2:
                    errorlabel = tk.Label(popup, text="Error: That bank is not signed in", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 3:
                    errorlabel = tk.Label(popup, text="Error: That bank is not returned", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)

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

        def submit(name, number):
            if name == "":
                errorlabel = tk.Label(popup, text="Error: Please enter a name", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
            elif number == "":
                errorlabel = tk.Label(popup, text="Error: Please select a bank number", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
            else:
                success, status = bar.signin(name, number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel = tk.Label(popup, text="Error: Please select a bank number", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 1:
                    errorlabel = tk.Label(popup, text="Error: That bank is not out", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 2:
                    errorlabel = tk.Label(popup, text="Error: That bank is already signed in", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 3:
                    errorlabel = tk.Label(popup, text="Error: That bank is returned", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)

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

        def submit(number):
            if number == "":
                errorlabel = tk.Label(popup, text="Error: Please select a bank number", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
            else:
                success, status = bar.returnbank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel = tk.Label(popup, text="Error: Please select a bank number", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 1:
                    errorlabel = tk.Label(popup, text="Error: That bank is not signed in", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 2:
                    errorlabel = tk.Label(popup, text="Error: That bank is already returned", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 3:
                    errorlabel = tk.Label(popup, text="Error: That bank is not out", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)

        popup.mainloop()


    def makebank(self):
        """Popup for making bar bank"""
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

        def submit(number, amount):
            if number == "":
                errorlabel = tk.Label(popup, text="Error: Please enter a bank number", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
            elif amount == "":
                success, status = bar.makebank(number.split("#")[-1])
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel = tk.Label(popup, text="Error: That bank does not exist", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 1:
                    errorlabel = tk.Label(popup, text="Error: That bank is not returned", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 2:
                    errorlabel = tk.Label(popup, text="Error: That bank is already made", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)

            else:
                success, status = bar.makebank(number.split("#")[-1], amount)
                if success:
                    popup.destroy()
                    save()
                elif status == 0:
                    errorlabel = tk.Label(popup, text="Error: That bank does not exist", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 1:
                    errorlabel = tk.Label(popup, text="Error: That bank is not returned", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 2:
                    errorlabel = tk.Label(popup, text="Error: That bank is already made", fg="red", font=("Verdana", 10)).grid(row=5, column=1, padx=10, pady=10)

        popup.mainloop()

    def currentbankinfo(self):
        """Popup for showing bank info"""

        popup = tk.Tk()
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

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=3, column=1, padx=10, pady=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=4, column=1, padx=10, pady=10)

        def refresh():
            try:
                infoout.config(text="")
                infoin.config(text="")
                returninfo.config(text="")
            except:
                pass

        def submit(number):
            refresh()
            closebutton.destroy()

            if number == "":
                errorlabel = tk.Label(popup, text="Error: Please enter a bank number", fg="red", font=("Verdana", 10)).grid(row=2, column=1, padx=10, pady=10)
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
                    okaybutton = tk.Button(popup, text="OKAY", command=popup.destroy, font=("Verdana", 20)).grid(row=5, column=1, padx=10, pady=10)
                elif status == 0:
                    errorlabel = tk.Label(popup, text="Error: That bank does not exist", fg="red", font=("Verdana", 10)).grid(row=2, column=1, padx=10, pady=10)

        popup.mainloop()

    def banklog(self):
        """Popup for showing bank info"""

        popup = tk.Tk()
        popup.wm_title("Bar Bank Logs")

        banknumlabel = tk.Label(popup, text="Bank #: ", font=("Verdana", 20)).grid(row=0, column=0, padx=10, pady=10)
        banks = bar.returnedbanks()
        bankvar = tk.StringVar(popup)
        bankvar.set("")
        bankdrop = tk.OptionMenu(popup, bankvar, *banks, command = lambda x: submit(bankvar.get()))
        bankdrop.config(font=("Verdana", 20), width= 20)
        bankdrop.grid(row=0, column=1, padx=10, pady=10)

        datelabel = tk.Label(popup, text="Date: ", font=("Verdana", 20)).grid(row=1, column=0, padx=10, pady=10)
        datevar = tk.StringVar(popup)
        datevar.set("")

        signoutlabel = tk.Label(popup, text="Sign Out: ", font=("Verdana", 20)).grid(row=2, column=0, padx=10, pady=10)
        infoout = tk.Label(popup, font=("Verdana", 20))
        infoout.grid(row=2, column=1, padx=10, pady=10)

        signinlabel = tk.Label(popup, text="Sign In: ", font=("Verdana", 20)).grid(row=3, column=0, padx=10, pady=10)
        infoin = tk.Label(popup, font=("Verdana", 20))
        infoin.grid(row=3, column=1, padx=10, pady=10)

        returnlabel = tk.Label(popup, text="Returned: ", font=("Verdana", 20)).grid(row=4, column=0, padx=10, pady=10)
        returninfo = tk.Label(popup, font=("Verdana", 20))
        returninfo.grid(row=4, column=1, padx=10, pady=10)

        closebutton = tk.Button(popup, text="CLOSE", command=popup.destroy, font=("Verdana", 20)).grid(row=5, column=0, padx=10, pady=10)
        okaybutton = tk.Button(popup, text="OKAY", command=popup.destroy, font=("Verdana", 20)).grid(row=5, column=1, padx=10, pady=10)

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
                errorlabel = tk.Label(popup, text="Error: Please enter a bank number", fg="red", font=("Verdana", 10)).grid(row=2, column=1, padx=10, pady=10)
            else:
                success, status = bar.banklog(number.split("#")[-1])
                if success:

                    def submit2(date):
                        try:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}\nNotes: {}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"], status[date]["Notes"]))
                        except:
                            infoout.config(text="Name: {}\nTime: {}\nLocation: {}\nAmount: ${}".format(status[date]["Name_Out"], status[date]["Time_Out"], status[date]["Location"], status[date]["Amount"]))

                        infoin.config(text="Name: {}\nTime: {}".format(status[date]["Name_In"], status[date]["Time_In"]))
                        returninfo.config(text="Returned: {}".format(status[date]["Returned_Time"]))

                    dates = [i for i in status]
                    datevar.set("")
                    datesdrop = tk.OptionMenu(popup, datevar, *dates, command = lambda x: submit2(datevar.get()))
                    datesdrop.config(font=("Verdana", 20), width= 20)
                    datesdrop.grid(row=1, column=1, padx=10, pady=10)

                elif status == 0:
                    errorlabel = tk.Label(popup, text="Error: That bank does not exist", fg="red", font=("Verdana", 10)).grid(row=2, column=1, padx=10, pady=10)

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

        def refresh():
            bankdrop.children['menu'].delete(0, "end")
            for bank in bar.banks():
                bankdrop.children['menu'].add_command(label=bank, command=lambda opt=bank: bankvar.set(opt))
            bankvar.set("")

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



app = Tracking()
app.geometry("1920x1080")
app.mainloop()
