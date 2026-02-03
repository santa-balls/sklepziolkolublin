from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/kategoria/zioła")
def kategoria_ziola():
    produkty = [
        {"nazwa": "Damian", "opis": "Zioło lecznicze", "obraz": "damian.jpg"},
        {"nazwa": "Melisa", "opis": "Zioło do herbaty", "obraz": "melisa.jpg"},
        {"nazwa": "Dziewanna", "opis": "Roślina lecznicza", "obraz": "dziewanna.jpg"}
    ]
    return render_template("kategoria.html", nazwa="Zioła", produkty=produkty)

@app.route("/kategoria/kwiaty")
def kategoria_kwiaty():
    produkty = [
        {"nazwa": "Pelargonia", "opis": "Klasyka balkonowa", "obraz": "pelargonia.jpg"},
        {"nazwa": "Petunia/Surfinia", "opis": "Kwita obficie całe lato", "obraz": "petunia.jpg"},
        {"nazwa": "Begonia", "opis": "Łatwa w uprawie", "obraz": "begonia.jpg"},
        {"nazwa": "Aksamitka", "opis": "Popularna na rabaty", "obraz": "aksamitka.jpg"},
        {"nazwa": "Szałwia błyszcząca", "opis": "", "obraz": "szalwia.jpg"},
        {"nazwa": "Lobelia przylądkowa", "opis": "", "obraz": "lobelia.jpg"},
        {"nazwa": "Werbena", "opis": "", "obraz": "werbena.jpg"},
        {"nazwa": "Floksy", "opis": "Bylina", "obraz": "floksy.jpg"},
        {"nazwa": "Irysy", "opis": "Bylina", "obraz": "irysy.jpg"},
        {"nazwa": "Hortensja", "opis": "Krzew kwitnący całe lato", "obraz": "hortensja.jpg"},
        {"nazwa": "Róża", "opis": "Popularny symbol miłości", "obraz": "roza.jpg"},
        {"nazwa": "Tulipan", "opis": "Klasyczny kwiat wiosenny", "obraz": "tulipan.jpg"},
        {"nazwa": "Goździk", "opis": "", "obraz": "gozdzik.jpg"},
        {"nazwa": "Lawenda", "opis": "Modna roślina do kompozycji florystycznych", "obraz": "lawenda.jpg"},
        {"nazwa": "Słonecznik", "opis": "Łatwy w uprawie, efektowny", "obraz": "slonecznik.jpg"},
        {"nazwa": "Lewkonia", "opis": "", "obraz": "lewkonia.jpg"},
        {"nazwa": "Aster chiński", "opis": "", "obraz": "aster.jpg"},
        {"nazwa": "Cynia wytworna", "opis": "", "obraz": "cynia.jpg"},
        {"nazwa": "Eustoma", "opis": "", "obraz": "eustoma.jpg"},
        {"nazwa": "Lwia paszcza", "opis": "", "obraz": "lwia_paszca.jpg"},
        {"nazwa": "Jeżówka", "opis": "Bylina, dobra do kompozycji", "obraz": "jezowka.jpg"},
        {"nazwa": "Rudbekia", "opis": "Bylina", "obraz": "rudbekia.jpg"},
        {"nazwa": "Len ozdobny", "opis": "", "obraz": "len.jpg"}
    ]
    return render_template("kategoria.html", nazwa="Kwiaty", produkty=produkty)

if __name__ == "__main__":
    app.run(debug=True)
