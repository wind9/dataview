from db import db_session, MarketInfo


if __name__ == '__main__':
    market_info = MarketInfo()
    result = db_session.query(MarketInfo.price).filter(MarketInfo.brand=='塔牌').first()
    print(result)
