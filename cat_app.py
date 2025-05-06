from flask import Flask, render_template, request, redirect, url_for
import os

# Make sure your template folder is named correctly and exists
app = Flask(__name__, template_folder='cat_templates')

# Temporary in-memory store for messages to God
god_messages = []

# Route for homepage
@app.route("/")
def cat_index():
    return render_template("cat_index.html")

# Form submission for "Talk to God"
@app.route("/talk_to_god", methods=["POST"])
def talk_to_god():
    user_message = request.form.get("message", "")
    if user_message:
        god_messages.append(f"Message from user: {user_message}")
    return redirect("/")

# "Talk to God" form page
@app.route("/talk_to_god_page")
def talk_to_god_page():
    return render_template("talk_to_god.html")

# View all submitted messages
@app.route("/view_messages")
def view_messages():
    return "<br>".join(god_messages) or "No messages yet."

# 🚨 Boss Fight page masquerading as form creation
@app.route("/cat_add", methods=["GET"])
def cat_add():
    return render_template("cat_add.html")

# Normal search form route
@app.route("/cat_search")
def cat_search():
    return render_template("cat_search.html")

# ⏳ The clock has spoken - time reveal page
@app.route("/timerevealed")
def time_revealed():
    return render_template("timerevealed.html")

if __name__ == "__main__":
    app.run(debug=True)
