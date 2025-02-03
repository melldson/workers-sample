from typing import Any

from everysk.sdk.entities import Datastore

datastores_query_list: list[Any] = [entity.datastore for entity in self.script_inputs.datastores]
datastores_variant_list: list[str] = [entity.datastore.variant for entity in self.inputs_info.datastores]
datastores_workspace_list: list[str] = [entity.datastore_workspace or self.workspace for entity in self.script_inputs.datastores]

datastores: list[Datastore] = Datastore.script.fetch_multi(datastores_query_list, datastores_variant_list, datastores_workspace_list)
