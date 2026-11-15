"""
Resources used to write this code:
John Yang 2018, "Static Websites with Frozen Flask", 
accessed 14 November 2026, <https://john-b-yang.github.io/flask-website/>

json — JSON encoder and decoder 2026, Python Software Foundation, 
accessed 15 November 2026, <https://docs.python.org/3/library/json.html>
"""

import os
import json

from flask import Flask, render_template


file_directory = os.path.dirname(__name__)
page_content_dir = os.path.join(file_directory, "page_content")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about.html")
def about():
    education_file_dir = os.path.join(page_content_dir, "education.json")
    with open(education_file_dir, mode="r", encoding="utf8") as education_json:
        education_info = json.load(education_json)

    experience_file_dir = os.path.join(page_content_dir, "experience.json")
    with open(experience_file_dir, mode="r", encoding="utf8") as experience_json:
        experience_info = json.load(experience_json)

    skills_file_dir = os.path.join(page_content_dir, "skills.json")
    with open(skills_file_dir, mode="r", encoding="utf8") as skills_json:
        skills_info = json.load(skills_json)

    return render_template(
        "about.html",
        education_info=education_info,
        experience_info=experience_info,
        skills_dict=skills_info
    )


@app.route("/projects.html")
def projects():
    projects_file_dir = os.path.join(page_content_dir, "projects.json")
    with open(projects_file_dir, mode="r", encoding="utf8") as projects_json:
        projects_list = json.load(projects_json)

    return render_template("projects.html", projects_list=projects_list)


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/tr/")
def index_tr():
    return render_template("tr/index.html")


@app.route("/tr/about.html")
def about_tr():
    education_file_dir = os.path.join(page_content_dir, "education_tr.json")
    with open(education_file_dir, mode="r", encoding="utf8") as education_json:
        education_info = json.load(education_json)

    experience_file_dir = os.path.join(page_content_dir, "experience_tr.json")
    with open(experience_file_dir, mode="r", encoding="utf8") as experience_json:
        experience_info = json.load(experience_json)

    skills_file_dir = os.path.join(page_content_dir, "skills_tr.json")
    with open(skills_file_dir, mode="r", encoding="utf8") as skills_json:
        skills_info = json.load(skills_json)
    
    return render_template(
        "tr/about.html",
        education_info=education_info,
        experience_info=experience_info,
        skills_dict=skills_info
    )


@app.route("/tr/projects.html")
def projects_tr():
    projects_file_dir = os.path.join(page_content_dir, "projects_tr.json")
    with open(projects_file_dir, mode="r", encoding="utf8") as projects_json:
        projects_list = json.load(projects_json)

    return render_template("tr/projects.html", projects_list=projects_list)


@app.route("/tr/contact.html")
def contact_tr():
    return render_template("tr/contact.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
