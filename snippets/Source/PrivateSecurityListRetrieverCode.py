from typing import Any

from everysk.sdk.entities import PrivateSecurity

private_securities_query: Any = self.script_inputs.private_securities
private_securities_variant: str = self.inputs_info.private_securities.variant

private_securities: list[PrivateSecurity] = PrivateSecurity.script.fetch_list(private_securities_query, private_securities_variant)
