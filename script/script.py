from flask import Flask, render_template, request

app = Flask(__name__,
            template_folder="../public",
            static_folder="../assets")

# Main routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/script')
def calculator():
    return render_template('script.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        budget = float(request.form['revenu'])
        logement = float(request.form['logement'])
        nourriture = float(request.form['nourriture'])
        transport = float(request.form['transport'])
        epargne = float(request.form['epargne'])

        total_depenses = logement + nourriture + transport + epargne
        solde = budget - total_depenses

        if solde > 100:
            reaction = "👏 Yatta ! Tu gères ton argent comme un pro !"
            etat = "good"
        elif solde < 0:
            reaction = "⚠️ Oof… tu es dans le rouge !"
            etat = "danger"
        else:
            reaction = "😅 C’est serré…だけど walla"
            etat = "warning"

        return render_template('result.html',
                            budget=budget,
                            total_depenses=total_depenses,
                            solde=solde,
                            reaction=reaction,
                            etat=etat)

    except ValueError:
        return "Erreur : Veuillez entrer des nombres valides."

# Additional pages
@app.route('/about')
def about():
    return render_template('pages/about/about.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact/contact.html')

if __name__ == '__main__':
    app.run(debug=True)