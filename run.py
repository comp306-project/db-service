from flask import Flask, jsonify
from app import cursor

app = Flask(__name__)

@app.route('/databases')
def databases():
    cursor.execute("SHOW DATABASES")
    result = [res[0].decode("utf-8") for res in cursor.fetchall()]
    return jsonify(result), 200

@app.route('/tables')
def tables():
    cursor.execute("SHOW TABLES")
    result = [res[0].decode('utf-8') for res in cursor.fetchall()]
    return jsonify(result), 200

@app.route('/tables/CIRCUITS')
def CIRCUITS():
    cursor.execute("SELECT * FROM CIRCUITS")
    result = {res[0] : [row for row in res[1:]] for res in cursor.fetchall()}
    return jsonify(result), 200



if __name__ == '__main__':
   app.run(host='0.0.0.0', port='5000', debug=True)