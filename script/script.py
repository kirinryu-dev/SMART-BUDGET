from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="../public", static_folder="../assets")

@app.route('/')
def index():
    return render_template('script.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        revenu = int(request.form['revenu'])
        logement = int(request.form['logement'])
        nourriture = int(request.form['nourriture'])
        transport = int(request.form['transport'])
        epargne = int(request.form['epargne'])

        total_depenses = logement + nourriture + transport + epargne
        solde = revenu - total_depenses

        if solde > 100:
            message = "👏 Yatta ! Tu gères ton argent comme un pro ! all green!（＾∀＾●）ﾉｼ"
            status = "green"
        elif solde < 0:
            message = "⚠️ Oof… tu es dans le rouge ! ！yabai! aka desu !!"
            status = "red"
        else:
            message = "😅 C’est serré…だけど"
            status = "orange"

        return f"""
        <link rel="stylesheet" href="../assets/css/script.css">
        <h1>Résultat</h1>
        <p>Solde restant : <strong>{solde}€</strong></p>
        <p class="{status}">{message}</p>
        <a href="/">Retour</a>
        """

    except ValueError:
        return "<p>Erreur : Veuillez entrer des nombres valides.</p>"

if __name__ == '__main__':
    app.run(debug=True)

    from flask import Flask, render_template, request

@app.route('/result', methods=['POST'])
def result():
    budget = float(request.form['budget'])
    logement = float(request.form['logement'])
    nourriture = float(request.form['nourriture'])
    transport = float(request.form['transport'])
    epargne = float(request.form['epargne'])

    total_depenses = logement + nourriture + transport + epargne
    solde = budget - total_depenses

    if solde > 100:
        reaction = "👏 Yatta ! Tu gères ton argent comme un pro ! all green!（＾∀＾●）ﾉｼ"
        etat = "good"
    elif solde < 0:
        reaction = "⚠️ Oof… tu es dans le rouge ! ！yabai! aka desu !!"
        etat = "danger"
    else:
        reaction = "😅 C’est serré…だけど walla"
        etat = "warning"

    return render_template('result.html',
        budget=budget,
        total_depenses=total_depenses,
        solde=solde,
        reaction=reaction,
        etat=etat
    )

