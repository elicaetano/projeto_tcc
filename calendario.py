import os
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'calendario'
app.config['MYSQL_DATABASE_DB'] = 'db'
#app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('formulario.html')


@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    etapa = request.form['etapa']
    local = request.form['local']
    data = request.form['data']

    if etapa and local and data:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tbl_calendario (etapa,local,) VALUES (%s, %s, %s)', (etapa,local,data))
        conn.commit()
    return render_template('formulario.html')


@app.route('/listar', methods=['POST', 'GET'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select etapa,local,data from tbl_calendario')
    data = cursor.fetchall()
    conn.commit()
    return render_template('lista.html', datas=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)

