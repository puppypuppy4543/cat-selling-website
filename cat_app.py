from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__, template_folder='cat_templates')

# Temporary in-memory store for user messages
god_messages = []

# Route for homepage
@app.route("/")
def cat_index():
    return render_template("cat_index.html")

# Route for "Talk to God" form submission
@app.route("/talk_to_god", methods=["POST"])
def talk_to_god():
    user_message = request.form.get("message", "")
    if user_message:
        god_messages.append(f"Message from user: {user_message}")
    return redirect("/")  # Redirect back to the homepage

# Route for the "Talk to God" page
@app.route("/talk_to_god_page")
def talk_to_god_page():
    return render_template("talk_to_god.html")

# Route to view all messages
@app.route("/view_messages")
def view_messages():
    return "<br>".join(god_messages) or "No messages yet."

# ⚠️ This now shows the BOSS FIGHT, not the old form!
@app.route("/cat_add", methods=["GET"])
def cat_add():
    return render_template("cat_add.html")

# Route for searching counseling forms (still normal)
@app.route("/cat_search")
def cat_search():
    return render_template("cat_search.html")

if __name__ == "__main__":
    app.run(debug=True)
