from presidents_db import PresidentsDatabase
from flask import Flask

flaskapp = Flask(__name__)

presidents_db = PresidentsDatabase()

def president_page(body):
    return f"""
        <html>
        <head><title>President's Database</title></head>
        <body>{body}</body>
        </html>
        """

@flaskapp.route("/")
def list_presidents():
    presidents_list = ""
    for president in presidents_db.presidents:
        presidents_list += f"""
            <li><a href="/president/{president.name}">{president}</li>
        """
    
    return president_page(f"<ol>{presidents_list}</ol>")

@flaskapp.route("/president/<president_name>")
def president(president_name):
    for president in presidents_db.presidents:
        if president_name == president.name:
            return president_page(f"""
            <p>
                {president.name} served {president.duration.days} days.
                He was elected by the {president.party} party.
                His vice president was {president.vice_president}.
            </p>""")
    # No president found
    return f"<p>No president named {president_name}</p>"

if __name__ == "__main__":
    presidents_db.open()
    presidents_db.load_presidents()
    presidents_db.close()
    flaskapp.run()