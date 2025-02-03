from typing import Any

from everysk.sdk.entities import CustomIndex

custom_indexes_query_list: list[Any] = [entity.custom_index for entity in self.script_inputs.custom_indexes]
custom_indexes_variant_list: list[str] = [entity.custom_index.variant for entity in self.inputs_info.custom_indexes]

custom_indexes: list[CustomIndex] = CustomIndex.script.fetch_multi(custom_indexes_query_list, custom_indexes_variant_list)
