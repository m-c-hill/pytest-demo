import logging

from errors import InsufficientFundsError, NegativeDepositError, NegativeWithdrawalError

logger = logging.getLogger(__name__)


class BankAccount:
    def __init__(self, balance: float = 0):
        self.balance = balance

    def get_balance(self) -> float:
        """
        Return the current balance of the account
        """
        return self.balance

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account
        """
        if amount < 0:
            raise NegativeDepositError(amount)
        self.balance += amount
        logger.info(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount) -> None:
        """
        Withdraw money from the account
        """
        if amount <= 0:
            raise NegativeWithdrawalError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(amount)
        self.balance -= amount
        logger.info(f"Withdrew {amount}. New balance is {self.balance}")
