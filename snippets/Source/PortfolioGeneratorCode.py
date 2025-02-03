from everysk.core.object import BaseDict
from everysk.sdk.entities import Portfolio

portfolio: Portfolio | BaseDict = self.script_inputs.portfolio
storage_settings: BaseDict = self.script_inputs.storage_settings

portfolio = Portfolio.script.storage(portfolio, storage_settings)
