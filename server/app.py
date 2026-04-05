import os
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.json
    name = data.get('name')
    initial_balance = float(data.get('initial_balance', 0))
    acc_num = "".join([str(random.randint(0, 9)) for _ in range(10)])

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts (name, account_number, balance) VALUES (%s, %s, %s)", 
                   (name, acc_num, initial_balance))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Success", "account": {"name": name, "account_number": acc_num}})

@app.route('/accounts', methods=['GET'])
def list_accounts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM accounts ORDER BY id DESC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/transactions', methods=['POST'])
def handle_transaction():
    data = request.json
    acc_num = data.get('account_number')
    amount = float(data.get('amount'))
    t_type = data.get('type')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (acc_num,))
    acc = cursor.fetchone()
    
    if not acc: return jsonify({"error": "Not found"}), 404
    
    current_bal = float(acc['balance'])
    if t_type == 'withdraw' and current_bal < amount:
        return jsonify({"error": "Insufficient funds"}), 400
    
    new_bal = current_bal + amount if t_type == 'deposit' else current_bal - amount
    
    cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (new_bal, acc_num))
    cursor.execute("INSERT INTO transactions (account_number, amount, type) VALUES (%s, %s, %s)", 
                   (acc_num, amount, t_type))
    
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Success"})

@app.route('/transactions/<acc_num>', methods=['GET'])
def get_history(acc_num):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM transactions WHERE account_number = %s ORDER BY created_at DESC", (acc_num,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True, port=5000)