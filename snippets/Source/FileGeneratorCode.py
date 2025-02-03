from everysk.core.object import BaseDict
from everysk.sdk.entities import File

file: File | BaseDict = self.script_inputs.file
storage_settings: BaseDict = self.script_inputs.storage_settings

file = File.script.storage(file, storage_settings)
