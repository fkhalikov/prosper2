from tutorial import Trader
from datamodel import TradingState, OrderDepth, Listing, Trade, Observation
from typing import Dict, List

def mock_trading_state() -> TradingState:
    # Mock data for demonstration; replace with real data as necessary
    traderData = 'Initial Data'
    timestamp = 123456789
    listings = {'ExampleSymbol': Listing('ExampleSymbol', 'ExampleProduct', 'ExampleDenomination')}
    
    # Sample order depth with buy and sell orders
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
    
    own_trades = {'ExampleSymbol': [Trade('ExampleSymbol', 100, 10, 'BuyerID', 'SellerID', 123456789)]}
    market_trades = {'ExampleSymbol': [Trade('ExampleSymbol', 110, 5, 'BuyerID', 'SellerID', 123456789)]}
    position = {'ExampleProduct': 100}
    observations = Observation({}, {})
    
    # Create and return the TradingState object
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

def main():
    # Instantiate the Trader
    trader = Trader()
    
    # Create a mock TradingState
    state = mock_trading_state()
    
    # Execute the Trader's run method with the mock TradingState
    result, conversions, traderData = trader.run(state)
    
    # Output the results
    print(f"Orders: {result}")
    print(f"Conversions: {conversions}")
    print(f"Trader Data: {traderData}")

if __name__ == "__main__":
    main()
