from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        nom = request.form.get("nom")
        message = f"Bonjour {nom} 👋"

    return f"""
    <h1>Mon site en ligne</h1>
    <form method="POST">
        <input name="nom">
        <button>Envoyer</button>
    </form>
    <p>{message}</p>
    """

# ⚠️ IMPORTANT
app.run(host="0.0.0.0", port=10000)
