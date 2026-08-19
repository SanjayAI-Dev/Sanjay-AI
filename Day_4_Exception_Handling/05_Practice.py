# 05_Practice
class PaymentError(Exception):
    """Base payment exception."""


class AccountNotFoundError(PaymentError):
    """Raised when an account is missing."""


class InsufficientBalanceError(PaymentError):
    """Raised when the balance is insufficient."""


class InvalidPaymentAmountError(PaymentError):
    """Raised for invalid payment amounts."""


class PaymentFailedError(PaymentError):
    """Raised when payment processing fails."""


class PaymentAccount:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance


class PaymentProcessor:
    def __init__(self):
        self.accounts = {
            "ACC1001": PaymentAccount("ACC1001", 5000),
            "ACC1002": PaymentAccount("ACC1002", 2000),
        }

    def process_payment(self, account_id, amount):
        if account_id not in self.accounts:
            raise AccountNotFoundError(
                f"Account {account_id} not found."
            )

        if amount <= 0:
            raise InvalidPaymentAmountError(
                "Payment amount must be positive."
            )

        account = self.accounts[account_id]

        if amount > account.balance:
            raise InsufficientBalanceError(
                "Insufficient account balance."
            )

        if amount > 10000:
            raise PaymentFailedError(
                "Payment rejected by payment gateway."
            )

        account.balance -= amount

        return True


def main():
    processor = PaymentProcessor()

    try:
        account_id = input("Enter account ID: ").strip()
        amount = float(input("Enter payment amount: "))

        processor.process_payment(account_id, amount)

    except ValueError:
        print("Please enter a valid numeric amount.")

    except AccountNotFoundError as error:
        print(f"Account error: {error}")

    except InvalidPaymentAmountError as error:
        print(f"Amount error: {error}")

    except InsufficientBalanceError as error:
        print(f"Balance error: {error}")

    except PaymentFailedError as error:
        print(f"Payment error: {error}")

    else:
        print("Payment successful.")

    finally:
        print("Payment processing completed.")


if __name__ == "__main__":
    main()

