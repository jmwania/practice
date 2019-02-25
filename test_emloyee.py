import unittest
from employee import Employee 

class TestEmployee(unittest.TestCase):
    # Testing mail

    def test_email(self):
        emp_1 = Employee('Josphat', 'Mwania', 50000)
        emp_2 = Employee('Fred', 'Munyao', 60000)

        self.assertEqual(emp_1.email, 'Josphat.Mwania@email.com')
        self.assertEqual(emp_2.email, 'Fred.MUnyao@email.com')

        emp_1.first = 'Josphat'
        emp_2.first = 'Fred'
        



if __name__ == '__main__':
    unittest.main()