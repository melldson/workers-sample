from typing import Any

from everysk.sdk.entities import CustomIndex

custom_index_query: Any = self.script_inputs.custom_index
custom_index_variant: str = self.inputs_info.custom_index.variant

custom_index: CustomIndex = CustomIndex.script.fetch(custom_index_query, custom_index_variant)
