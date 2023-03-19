from flask import Flask, render_template, request

app = Flask(__name__)

web_notes = []

@app.route('/web', methods=["GET", "POST"])
def web_server():
    note = request.args.get("note")
    web_notes.append(note)
    return render_template("web_server.html", notes=web_notes)


app_notes = []    

@app.route('/app', methods=["GET", "POST"])
def app_server():
    note = request.args.get("note")
    app_notes.append(note)
    return render_template("app_server.html", notes=app_notes)    


if __name__ == '__main__':
    app.run(debug=True)