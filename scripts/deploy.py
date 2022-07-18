from aiohttp import TraceDnsCacheHitParams
from brownie import FundMe, network, config, MockV3Aggregator
from psutil import STATUS_DEAD
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def checkvals():
    fund_me = FundMe[-1]
    ethprice = fund_me.getPrice()
    print(f"Price of ETH is set at...{ethprice} with length of {len(str(ethprice))}")
    mockdata = MockV3Aggregator[-1]
    answer = mockdata.latestRoundData()[1]
    print(f"v3aggre latest price is ...{answer} with length of {len(str(answer))}")
    fee = fund_me.getEntranceFee()
    print(f"Price of fee is ...{fee} with length of {len(str(fee))}")


def main():
    deploy_fund_me()
    checkvals()
