from everysk.core.object import BaseDict
from everysk.sdk.entities import PrivateSecurity

private_security: PrivateSecurity | BaseDict = self.script_inputs.private_security
storage_settings: BaseDict = self.script_inputs.storage_settings

private_security = PrivateSecurity.script.storage(private_security, storage_settings)
