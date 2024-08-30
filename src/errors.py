class BankAccountException(Exception):
    def __init__(self, message: str, amount: float = None):
        super().__init__(message)
        self.amount = amount


class InsufficientFundsError(BankAccountException):
    def __init__(self, amount):
        super().__init__(f"Insufficient funds. Attempted to withdraw: {amount}", amount)


class NegativeDepositError(BankAccountException):
    def __init__(self, amount):
        super().__init__(
            f"Deposit amount must be positive - {amount} is invalid", amount
        )


class NegativeWithdrawalError(BankAccountException):
    def __init__(self, amount):
        super().__init__(
            f"Withdrawal amount must be positive - {amount} is invalid", amount
        )
