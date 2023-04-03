import app
import json
import unittest


class TestLoanApplication(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        app.create_tables()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(json.loads(response.data), {'message': 'Welcome to the loan application API!'})

    def test_apply_loan(self):
        data = {'borrower_name': 'John Doe', 'loan_amount': 5000, 'repayment_term': 12}
        response = self.app.post('/apply', data=json.dumps(data), content_type='application/json')
        self.assertEqual(json.loads(response.data), {'message': 'Loan application submitted successfully!'})

    def tearDown(self):
        conn = app.sqlite3.connect(app.DATABASE)
        cur = conn.cursor()
        cur.execute('DROP TABLE loans')
        conn.commit()
        conn.close()


if __name__ == '__main__':
    unittest.main()
