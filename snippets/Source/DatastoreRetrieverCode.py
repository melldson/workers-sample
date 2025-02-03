from typing import Any

from everysk.sdk.entities import Datastore

datastore_query: Any = self.script_inputs.datastore
datastore_variant: str = self.inputs_info.datastore.variant
datastore_workspace: str = self.script_inputs.datastore_workspace or self.workspace

datastore: Datastore = Datastore.script.fetch(datastore_query, datastore_variant, datastore_workspace)
