from typing import Any

from everysk.sdk.entities import Portfolio

portfolios_query: Any = self.script_inputs.portfolios
portfolios_variant: str = self.inputs_info.portfolios.variant
portfolios_workspace: str = self.script_inputs.portfolios_workspace or self.workspace

portfolio: list[Portfolio] = Portfolio.script.fetch_list(portfolios_query, portfolios_variant, portfolios_workspace)
