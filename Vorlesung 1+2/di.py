class Werkzeug: # Oberklasse
    def benutze(self):
        pass

class Schaufel(Werkzeug): # Unterklasse: Schaufel ist ein Werkzeug
    def benutze(self):
        print("...graben...")

class Spaten(Werkzeug):
    def benutze(self):
        print("...hacken...")

class Bagger(Werkzeug):
    def benutze(self):
        print("...baggern...")

class Knecht:
    def __init__(self):
        self.werkzeug = None

    # Dependency Injection
    def gibWerkzeug(self, werkzeug: Werkzeug):
        self.werkzeug = werkzeug

    def benutzeWerkzeug(self):
        self.werkzeug.benutze()

schaufel = Schaufel()
spaten = Spaten()
hein = Knecht()
piet = Knecht()
hein.gibWerkzeug(schaufel)
hein.benutzeWerkzeug()
piet.gibWerkzeug(spaten)
piet.benutzeWerkzeug()