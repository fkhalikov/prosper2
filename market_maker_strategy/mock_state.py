
from common.datamodel import TradingState, OrderDepth, Listing, Trade, Observation
from typing import Dict, List

def mock_trading_state() -> TradingState:
    # Updated mock data for a passive market making strategy
    traderData = 'Initial Data for Market Making'
    timestamp = 123456789
    listings = {'ExampleSymbol': Listing('ExampleSymbol', 'ExampleProduct', 'ExampleDenomination')}
    
    # Updated sample order depth with buy and sell orders
    order_depths = {'ExampleProduct': OrderDepth()}
    # Adding sample buy orders - price: quantity
    order_depths['ExampleProduct'].buy_orders = {
        95: 10,  # Price: 95, Quantity: 10
        90: 20   # Price: 90, Quantity: 20
    }
    # Adding sample sell orders - price: quantity
    order_depths['ExampleProduct'].sell_orders = {
        105: 15,  # Price: 105, Quantity: 15
        110: 25   # Price: 110, Quantity: 25
    }
    
    # Own trades example
    own_trades = {'ExampleSymbol': [Trade('ExampleSymbol', 100, 10, 'BuyerID', 'SellerID', 123456789)]}
    # Market trades example
    market_trades = {'ExampleSymbol': [Trade('ExampleSymbol', 110, 5, 'BuyerID', 'SellerID', 123456789)]}
    # Position adjusted for market making
    position = {'ExampleProduct': 50}  # Starting with 50 units
    observations = Observation({}, {})
    
    # Create and return the TradingState object with updated mock data
    return TradingState(
        traderData=traderData,
        timestamp=timestamp,
        listings=listings,
        order_depths=order_depths,
        own_trades=own_trades,
        market_trades=market_trades,
        position=position,
        observations=observations
    )
