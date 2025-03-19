from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return f"Nama: {name}, Email: {email}"
    return '''
        <h2>Masukkan Nama dan Email</h2>
        <form method="POST">
            <label for="name">Nama:</label>
            <input type="text" id="name" name="name" required>
            <br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <br><br>
            <button type="submit">Kirim</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
