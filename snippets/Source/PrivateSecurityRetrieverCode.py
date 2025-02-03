from typing import Any

from everysk.sdk.entities import PrivateSecurity

private_security_query: Any = self.script_inputs.private_security
private_security_variant: str = self.inputs_info.private_security.variant

private_security: PrivateSecurity = PrivateSecurity.script.fetch(private_security_query, private_security_variant)
