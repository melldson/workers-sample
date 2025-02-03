from everysk.core.object import BaseDict
from everysk.sdk.entities import CustomIndex

custom_index: CustomIndex | BaseDict = self.script_inputs.custom_index
storage_settings: BaseDict = self.script_inputs.storage_settings

custom_index = CustomIndex.script.storage(custom_index, storage_settings)
