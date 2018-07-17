from banks import *
import pickle

global bar, fb, tkg, retail, bike, change, fanny

def load():
    """
    Loads the type objects from pickles or creates new ones
    """

    global bar, fb, tkg, retail, bike, change, fanny
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




if __name__ == "__main__":
    load()

    bar.addbank("202")
    bar.addbank("203")
    bar.addbank("204")
    #
    # bar.signout("scott", "beach", "202", "Parking")
    # bar.signin("scott", "202")
    # bar.returnbank("202")
    # bar.makebank("202")
    # out = bar.signedout()
    # signin = bar.signedin()
    # returned = bar.returnedbanks()
    # made = bar.madebanks()
    # print(out, signin, returned, made)
    print(len(bar.banks()))
    bar.removebank("203")
    print(len(bar.banks()))

    save()
