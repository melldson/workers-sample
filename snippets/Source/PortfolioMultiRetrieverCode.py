from typing import Any

from everysk.sdk.entities import Portfolio

portfolios_query_list: list[Any] = [entity.portfolio for entity in self.script_inputs.portfolios]
portfolios_variant_list: list[str] = [entity.portfolio.variant for entity in self.inputs_info.portfolios]
portfolios_workspace_list: list[str] = [entity.portfolio_workspace or self.workspace for entity in self.script_inputs.portfolios]

portfolios: list[Portfolio] = Portfolio.script.fetch_multi(portfolios_query_list, portfolios_variant_list, portfolios_workspace_list)
