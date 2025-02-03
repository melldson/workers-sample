from typing import Any

from everysk.sdk.entities import Portfolio

portfolio_query: Any = self.script_inputs.portfolio
portfolio_variant: str = self.inputs_info.portfolio.variant
portfolio_workspace: str = self.script_inputs.portfolio_workspace or self.workspace

portfolio: Portfolio = Portfolio.script.fetch(portfolio_query, portfolio_variant, portfolio_workspace)
