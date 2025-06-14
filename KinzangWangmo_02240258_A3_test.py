"""
CSF101 Assignment 3 - Part B: Unit Tests
Author: Kinzang Wangmo
Student Number: 02240258
"""

import unittest
from KinzangWangmo_02240258_A3 import BankAccount, InvalidInputError, InvalidTransferError, topUpMobile

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Create test accounts before each test."""
        self.acc1 = BankAccount("Dupchu", 1000)  
        self.acc2 = BankAccount("Tshering", 500)     

    # === Test deposit ===
    def test_deposit_positive_amount(self):
        """Test depositing a positive amount updates the balance correctly."""
        self.acc1.deposit(100)
        self.assertEqual(self.acc1.get_balance(), 1100)

    def test_deposit_negative_amount(self):
        """Test depositing a negative amount raises ValueError."""
        with self.assertRaises(ValueError):
            self.acc1.deposit(-50)

    def test_deposit_zero_amount(self):
        """Test depositing zero amount raises ValueError."""
        with self.assertRaises(ValueError):
            self.acc1.deposit(0)

    # === Test withdraw ===
    def test_withdraw_valid(self):
        """Test withdrawing a valid amount updates the balance correctly."""
        self.acc1.withdraw(300)
        self.assertEqual(self.acc1.get_balance(), 700)

    def test_withdraw_insufficient_funds(self):
        """Test withdrawing more than balance raises ValueError."""
        with self.assertRaises(ValueError):
            self.acc2.withdraw(1000)

    def test_withdraw_negative_amount(self):
        """Test withdrawing a negative amount raises ValueError."""
        with self.assertRaises(ValueError):
            self.acc1.withdraw(-100)

    def test_withdraw_zero_amount(self):
        """Test withdrawing zero amount raises ValueError."""
        with self.assertRaises(ValueError):
            self.acc1.withdraw(0)

    # === Test transfer ===
    def test_transfer_valid(self):
        """Test transferring a valid amount updates both accounts correctly."""
        self.acc1.transfer(self.acc2, 200)
        self.assertEqual(self.acc1.get_balance(), 800)
        self.assertEqual(self.acc2.get_balance(), 700)

    def test_transfer_to_invalid_object(self):
        """Test transferring to a non-BankAccount object raises InvalidTransferError."""
        with self.assertRaises(InvalidTransferError):
            self.acc1.transfer("not an account", 100)

    def test_transfer_insufficient_funds(self):
        """Test transferring more than balance raises ValueError."""
        with self.assertRaises(ValueError):
            self.acc2.transfer(self.acc1, 1000)

    def test_transfer_zero_amount(self):
        """Test transferring zero amount raises ValueError."""
        with self.assertRaises(ValueError):
            self.acc1.transfer(self.acc2, 0)

    # === Test mobile top-up ===
    def test_topup_valid(self):
        """Test valid mobile top-up returns correct message."""
        result = topUpMobile("0412345678", 10)
        self.assertEqual(result, "Topped up Nu10.00 to 0412345678")

    def test_topup_invalid_phone(self):
        """Test invalid phone number raises InvalidInputError."""
        with self.assertRaises(InvalidInputError):
            topUpMobile("abc", 10)

    def test_topup_negative_amount(self):
        """Test negative top-up amount raises ValueError."""
        with self.assertRaises(ValueError):
            topUpMobile("0412345678", -5)

    def test_topup_minimum_phone_length(self):
        """Test phone number with exactly 8 digits works correctly."""
        result = topUpMobile("12345678", 10)
        self.assertEqual(result, "Topped up Nu10.00 to 12345678")

    # === Test get_balance ===
    def test_get_balance(self):
        """Test get_balance returns correct initial balance."""
        self.assertEqual(self.acc1.get_balance(), 1000)
        self.assertEqual(self.acc2.get_balance(), 500)

if __name__ == "__main__":
    unittest.main(verbosity=2) 