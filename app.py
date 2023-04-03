from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DATABASE = 'loan_application.db'


def create_tables():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS loans
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     borrower_name TEXT NOT NULL,
                     loan_amount INTEGER NOT NULL,
                     repayment_term INTEGER NOT NULL,
                     status TEXT NOT NULL);''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the loan application API!'})


@app.route('/apply', methods=['POST'])
def apply_loan():
    data = request.get_json()
    borrower_name = data['borrower_name']
    loan_amount = data['loan_amount']
    repayment_term = data['repayment_term']
    status = 'pending'
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute('INSERT INTO loans (borrower_name, loan_amount, repayment_term, status) VALUES (?, ?, ?, ?)',
                    (borrower_name, loan_amount, repayment_term, status))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Loan application submitted successfully!'})
    except:
        return jsonify({'error': 'An error occurred while submitting the loan application.'})


if __name__ == '__main__':
    create_tables()
    app.run()
