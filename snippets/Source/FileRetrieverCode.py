from typing import Any

from everysk.sdk.entities import File

file_query: Any = self.script_inputs.file
file_variant: str = self.inputs_info.file.variant
file_workspace: str = self.script_inputs.file_workspace or self.workspace

file: File = File.script.fetch(file_query, file_variant, file_workspace)
