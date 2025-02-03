from everysk.core.object import BaseDict
from everysk.sdk.entities import Datastore

datastore: Datastore | BaseDict = self.script_inputs.datastore
storage_settings: BaseDict = self.script_inputs.storage_settings

datastore = Datastore.script.storage(datastore, storage_settings)
