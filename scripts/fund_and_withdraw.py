from brownie import FundMe
from scripts.helpful_scripts import get_account
from web3 import Web3


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    eth_price = Web3.fromWei(fund_me.getPrice(), "ether") / 10000000000
    print(f"The Price of Ether is {eth_price}")
    print(f"The Current entry fee is {entrance_fee}")
    print(f"Funding...{entrance_fee+entrance_fee}")
    fund_me.fund({"from": account, "value:": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
