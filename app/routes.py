from flask import render_template, redirect, url_for, send_file
from app import app
from app.forms import RepoForm
from src.data_processing import process_repositories, save_data_to_excel
from flask import send_from_directory
import os


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RepoForm()
    if form.validate_on_submit():
        repo_url = form.repo_url.data
        repositories_data = process_repositories([repo_url])
        save_data_to_excel(repositories_data)
        filename = f"contributors_{repo_url.split('/')[-1]}.xlsx"
        filepath = os.path.join('data', filename)
        return send_file(filepath, as_attachment=True)
    return render_template('index.html', form=form)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'data'), filename, as_attachment=True)
