import sqlite3
import os
from flask import Flask, render_template, request, url_for, flash, redirect, abort
from dotenv import load_dotenv
from json import loads

# Load .env file
load_dotenv()

# Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['HOST'] = os.environ.get('HOST')
app.config['PORT'] = os.environ.get('PORT')

# Functions
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_tag(tag_epc):
    conn = get_db_connection()
    tag = conn.execute('SELECT * FROM tags WHERE epc = ?', (tag_epc,)).fetchone()
    conn.close()
    if tag is None:
        abort(404)
    return tag

def search_tags(field='epc',query=None):
    conn = get_db_connection()
    if query is None or query.strip() == "":
        tags = conn.execute('SELECT * FROM tags').fetchall()
    else:
        query = '%{}%'.format(query)
        query_string = 'SELECT * FROM tags WHERE {} LIKE ?'.format(field)
        tags = conn.execute(query_string, (query,)).fetchall()
    conn.close()
    if tags is None:
        abort(404)
    return tags

# Routes
@app.route('/')
def index():
    field = request.args.get('field', None)
    query = request.args.get('search', None)
    tags = search_tags(field, query)
    if query != "" and len(tags) == 0:
        flash('No results')
    return render_template('index.html', tags=tags)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        epc = request.form['epc']
        title = request.form['title']
        comment = request.form['comment']

        if not epc:
            flash('EPC required')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO tags (epc, title, comment, original_register) VALUES (?, ?, ?, ?)', (epc, title, comment, 'user'))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<string:epc>/edit/', methods=('GET', 'POST'))
def edit(epc=None):
    if epc is None:
        flash('Must have EPC to edit')
    else:
        tag = get_tag(epc)

        if request.method == 'POST':
            epc = request.form['epc']
            title = request.form['title']
            comment = request.form['comment']

            conn = get_db_connection()
            conn.execute('UPDATE tags SET title = ?, comment = ? WHERE epc = ?', (title, comment, epc))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

        return render_template('edit.html', tag=tag)

@app.route('/<string:epc>/delete/', methods=('POST',))
def delete(epc):
    tag = get_tag(epc)
    conn = get_db_connection()
    conn.execute('DELETE FROM tags WHERE epc = ?', (epc,))
    conn.commit()
    conn.close()
    flash('"{}" successfully deleted'.format(tag['epc']))
    return redirect(url_for('index'))

@app.route('/publish/', methods=('POST',))
def publish():
    if not request.is_json:
        abort(400)
    else:
        jdata = loads(request.data)
        tag_list = list(set([tag['epc'] for tag in jdata['tag_reads'] ]))
        app.logger.info('Url: %s', request.url)
        app.logger.info('Reader: %s', jdata['reader_name'])
        app.logger.info('Reader Mac: %s', jdata['mac_address'])

        for tag in tag_list:
            conn = get_db_connection()
            conn.execute('INSERT OR IGNORE INTO tags (epc, original_register) VALUES (?, ?)', (tag, jdata['reader_name']))
            conn.execute('UPDATE tags SET last_register = ? WHERE epc = ?', (jdata['reader_name'], tag))
            conn.commit()
            conn.close()

        return 'OK\n'

if __name__ == '__main__':
    app.run()