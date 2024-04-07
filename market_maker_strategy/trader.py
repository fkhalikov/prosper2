
from common.datamodel import OrderDepth, TradingState, Order
from typing import List
import string

class Trader:
    
    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

        # Orders to be placed on exchange matching engine
        result = {}
        for product in state.order_depths:
            order_depth: OrderDepth = state.order_depths[product]
            orders: List[Order] = []
            
            acceptable_bid_price = self.calculate_acceptable_bid_price(order_depth, state.position.get(product, 0))
            acceptable_ask_price = self.calculate_acceptable_ask_price(order_depth, state.position.get(product, 0))
            
            # Place a buy order slightly below the best ask to provide liquidity
            if len(order_depth.sell_orders) != 0:
                best_ask = min(order_depth.sell_orders.keys())
                bid_price = max(acceptable_bid_price, best_ask - 1)  # Ensure bid is below best ask
                orders.append(Order(product, bid_price, 1))  # Example quantity of 1
            
            # Place a sell order slightly above the best bid to provide liquidity
            if len(order_depth.buy_orders) != 0:
                best_bid = max(order_depth.buy_orders.keys())
                ask_price = min(acceptable_ask_price, best_bid + 1)  # Ensure ask is above best bid
                orders.append(Order(product, ask_price, -1))  # Example quantity of 1
            
            result[product] = orders
    
        traderData = "Updated Trader Data"
        conversions = 0
        return result, conversions, traderData
    
    def calculate_acceptable_bid_price(self, order_depth: OrderDepth, current_position: int):
        # Simple strategy to calculate bid based on the best ask in the market and inventory
        if order_depth.sell_orders:
            best_ask = min(order_depth.sell_orders.keys())
            # Adjust bid based on inventory; more conservative if high inventory
            bid_adjustment = 1 if current_position < 100 else 2
            return best_ask - bid_adjustment
        return 10  # Fallback bid price if no sell orders
    
    def calculate_acceptable_ask_price(self, order_depth: OrderDepth, current_position: int):
        # Simple strategy to calculate ask based on the best bid in the market and inventory
        if order_depth.buy_orders:
            best_bid = max(order_depth.buy_orders.keys())
            # Adjust ask based on inventory; more conservative if low inventory
            ask_adjustment = 1 if current_position > 50 else 2
            return best_bid + ask_adjustment
        return 20  # Fallback ask price if no buy orders
