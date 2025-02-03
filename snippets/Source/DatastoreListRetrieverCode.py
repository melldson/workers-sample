from typing import Any

from everysk.sdk.entities import Datastore

datastores_query: Any = self.script_inputs.datastores
datastores_variant: str = self.inputs_info.datastores.variant
datastores_workspace: str = self.script_inputs.datastores_workspace or self.workspace

datastores: list[Datastore] = Datastore.script.fetch_list(datastores_query, datastores_variant, datastores_workspace)
