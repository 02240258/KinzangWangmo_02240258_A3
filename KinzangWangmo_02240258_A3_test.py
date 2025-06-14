import unittest
from KinzangWangmo_02240258_A3 import BankAccount, topUpMobile, InvalidInputError, InvalidTransferError

class TestBankingApp(unittest.TestCase):

    def setUp(self):
        self.acc1 = BankAccount("Kinzang", 1000)
        self.acc2 = BankAccount("Tandin", 500)

    # 1. Unusual user input
    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.acc1.deposit(-100)

    def test_zero_withdrawal(self):
        with self.assertRaises(ValueError):
            self.acc1.withdraw(0)

    def test_non_digit_phone_number(self):
        with self.assertRaises(InvalidInputError):
            topUpMobile("abcd123", 100)

    def test_short_phone_number(self):
        with self.assertRaises(InvalidInputError):
            topUpMobile("12345", 100)

    # 2. Invalid usage of application functions
    def test_transfer_to_non_account(self):
        with self.assertRaises(InvalidTransferError):
            self.acc1.transfer("not_a_bank_account", 100)

    def test_transfer_more_than_balance(self):
        with self.assertRaises(ValueError):
            self.acc1.transfer(self.acc2, 2000)

    def test_topup_negative_amount(self):
        with self.assertRaises(ValueError):
            topUpMobile("12345678", -50)

    # 3. Testing individual main methods
    def test_valid_deposit(self):
        self.acc1.deposit(200)
        self.assertEqual(self.acc1.get_balance(), 1200)

    def test_valid_withdraw(self):
        self.acc1.withdraw(300)
        self.assertEqual(self.acc1.get_balance(), 700)

    def test_valid_transfer(self):
        self.acc1.transfer(self.acc2, 400)
        self.assertEqual(self.acc1.get_balance(), 600)
        self.assertEqual(self.acc2.get_balance(), 900)

    def test_valid_topup(self):
        result = topUpMobile("12345678", 50)
        self.assertEqual(result, "Topped up Nu50.00 to 12345678")

if __name__ == "__main__":
    unittest.main()
