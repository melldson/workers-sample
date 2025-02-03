from typing import Any

from everysk.sdk.entities import CustomIndex

custom_indexes_query: Any = self.script_inputs.custom_indexes
custom_indexes_variant: str = self.inputs_info.custom_indexes.variant

custom_indexes: list[CustomIndex] = CustomIndex.script.fetch_list(custom_indexes_query, custom_indexes_variant)
