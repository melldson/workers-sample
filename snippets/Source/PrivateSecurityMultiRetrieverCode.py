from typing import Any

from everysk.sdk.entities import PrivateSecurity

private_securities_query_list: list[Any] = [entity.private_security for entity in self.script_inputs.private_securities]
private_securities_variant_list: list[str] = [entity.private_security.variant for entity in self.inputs_info.private_securities]

private_securities: list[PrivateSecurity] = PrivateSecurity.script.fetch_multi(private_securities_query_list, private_securities_variant_list)
