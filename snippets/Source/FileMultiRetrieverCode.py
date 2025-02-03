from typing import Any

from everysk.sdk.entities import File

files_query_list: list[Any] = [entity.file for entity in self.script_inputs.files]
files_variant_list: list[str] = [entity.file.variant for entity in self.inputs_info.files]
files_workspace_list: list[str] = [entity.file_workspace or self.workspace for entity in self.script_inputs.files]

files: list[File] = File.script.fetch_multi(files_query_list, files_variant_list, files_workspace_list)
