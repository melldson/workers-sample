from typing import Any

from everysk.sdk.entities import File

files_query: Any = self.script_inputs.files
files_variant: str = self.inputs_info.files.variant
files_workspace: str = self.script_inputs.files_workspace or self.workspace

file: list[File] = File.script.fetch_list(files_query, files_variant, files_workspace)
