"""
This module contains unit tests for the BankAccount class.

It has been created to demonstrate the following pytest features:

- Assertions
- Fixtures
- Marking
- Parametrization
- Caplog
- Exception testing
"""

import logging

import pytest

from bank_account import BankAccount
from errors import InsufficientFundsError, NegativeDepositError, NegativeWithdrawalError

# =================
#  Fixtures
# =================


@pytest.fixture
def bank_account() -> BankAccount:
    return BankAccount(balance=100)


# =================
#  Unit Tests
# =================

# ========== Test Initial Balance ===========


@pytest.mark.balance
def test_initial_balance(bank_account):
    assert bank_account.get_balance() == 100


# ========== Test Depositing ===========


@pytest.mark.deposit
def test_deposit(bank_account, caplog):
    with caplog.at_level(logging.INFO):
        bank_account.deposit(50)

    assert bank_account.get_balance() == 150
    assert "Deposited 50. New balance is 150" in caplog.text


@pytest.mark.deposit
def test_deposit_negative_amount(bank_account):
    with pytest.raises(NegativeDepositError) as err:
        bank_account.deposit(-50)

    assert "Deposit amount must be positive" in str(err.value)
    assert "-50 is invalid" in str(err.value)


# ========== Test Withdrawing ===========


@pytest.mark.withdraw
@pytest.mark.parametrize(
    "withdraw_amount, expected_balance", [(20, 80), (50, 50), (100, 0)]
)
def test_withdraw(bank_account, withdraw_amount, expected_balance, caplog):
    with caplog.at_level(logging.INFO):
        bank_account.withdraw(withdraw_amount)
    assert bank_account.get_balance() == expected_balance


@pytest.mark.withdraw
def test_withdraw_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFundsError) as err:
        bank_account.withdraw(200)

    assert "Insufficient funds. Attempted to withdraw: 200" in str(err.value)


# ========== Test Currency ===========


@pytest.mark.currency
@pytest.mark.skip(reason="Currency feature not yet supported")
def test_get_currency(bank_account):
    assert bank_account.get_currency() == "GBP"
