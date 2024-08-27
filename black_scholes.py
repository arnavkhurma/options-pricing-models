""" 
    European option pricing using Black-Scholes Model

    Assumptions:
    1. Contracts can be exercised only on maturity date.
    2. Underlying stock does not pay divident during the lifetime of the contract
    3. Volatility and Risk-free-rate are constant until maturity
    4. Lognormal distribution of underlying returns.
"""
from scipy.stats import norm
import numpy as np

class BlackScholes():

    def __init__(self, underlying_price, strike_price, time_to_maturity, risk_free_rate, sigma):
            """
            Initialize variables used to price calls and puts

            @param underlying_price current underlying spot price
            @param strike_price current strike price for the options contract
            @param time_to_maturity contract maturity date
            @param risk_free_rate return on risk-free assets (T-Bills), assumed to be constant till maturity
            @param sigma standard deviation of the asset's log returns (underlying volatility)
            
            """
            self.underlying = underlying_price
            self.strike = strike_price
            self.time = time_to_maturity
            self.risk_free_rate = risk_free_rate
            self.sigma = sigma

    def d_one(self):
        return (np.log(self.underlying / self.strike) + (self.risk_free_rate + 0.5 * self.sigma ** 2) * self.time) / (self.sigma * np.sqrt(self.time))
    
    def d_two(self):
        return (np.log(self.underlying / self.strike) + (self.risk_free_rate - 0.5 * self.sigma ** 2) * self.time) / (self.sigma * np.sqrt(self.time))

    def calculate_call_price(self):
        """
        CALL OPTION      
        Calculates d1 and d2, and then uses those inputs to price the call option
        """
        d1 = self.d_one()
        d2 = self.d_two()
        price = (self.underlying * norm.cdf(d1, 0.0, 1.0) - self.strike * np.exp(-self.risk_free_rate * self.time) * norm.cdf(d2, 0.0, 1.0))
        return price
    
    def calculate_put_price(self):
        """
        PUT OPTION
        Calculates d1 and d2, and then uses those inputs to price the put option
        """
        d1 = self.d_one()
        d2 = self.d_two()
        return (self.strike * np.exp(-self.risk_free_rate * self.time) * norm.cdf(-d2, 0.0, 1.0) - self.underlying * norm.cdf(-d1, 0.0, 1.0))
    
    def printStats(self):
        print("Underlying Price: ", self.underlying)
        print("Strike Price: ", self.strike)
        print("Time to Maturity: ", self.time)
        print("Risk Free Rate: ", self.risk_free_rate)
        print("Sigma: ", self.sigma)

        print("Call Option Price: ", self.calculate_call_price())
        print("Put Option Price: ", self.calculate_put_price())

    # Calculate Greeks
    def delta(self, type): 
        if type == "C":
            return norm.cdf(self.d_one())
        elif type == "P":
            return norm.cdf(self.d_one()) - 1
        else:
            return None
        
    def gamma(self):
        return norm.pdf(self.d_one()) / (self.underlying * self.sigma * np.sqrt(self.time))

    def theta(self, type):
        a = (-self.underlying * norm.pdf(self.d_one()) * self.sigma) / (2 * np.sqrt(self.time))
        if type == "C":
            b = self.risk_free_rate * self.strike * np.exp(-self.risk_free_rate * self.time) * norm.cdf(self.d_two())
            return (a - b) * 0.01
        elif type == "P":
            b = self.risk_free_rate * self.strike * np.exp(-self.risk_free_rate * self.time) * norm.cdf(-self.d_two())
            return (a + b) * 0.01
        else:
            return None
        
    def vega(self):
        return (self.underlying * norm.pdf(self.d_one()) * np.sqrt(self.time) * 0.01)

    def rho(self, type):
        if type == "C":
            return (self.strike * self.time * np.exp(-self.risk_free_rate * self.time) * norm.cdf(self.d_two()) * 0.01)
        elif type == "P":
            return -(self.strike * self.time * np.exp(-self.risk_free_rate * self.time) * norm.cdf(-self.d_two()) * 0.01)
        else:
            return None