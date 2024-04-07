from market_maker_strategy.trader import Trader
from market_maker_strategy.mock_state import mock_trading_state

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