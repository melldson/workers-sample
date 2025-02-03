def storage_mode_create(*args):
    form_data = args[0]
    _WORKER_TAB_NAME_ = form_data.get('_WORKER_TAB_NAME_', {})
    storage_settings = _WORKER_TAB_NAME_.get('storage_settings', {})
    storage_mode = storage_settings.get('storage_mode', {})
    select = storage_mode.get('select', {})
    value = select.get('value', '')
    return value.lower() == 'create'

def storage_mode_update(*args):
    form_data = args[0]
    _WORKER_TAB_NAME_ = form_data.get('_WORKER_TAB_NAME_', {})
    storage_settings = _WORKER_TAB_NAME_.get('storage_settings', {})
    storage_mode = storage_settings.get('storage_mode', {})
    select = storage_mode.get('select', {})
    value = select.get('value', '')
    return value.lower() == 'create_or_update'

def storage_mode_transient(*args):
    form_data = args[0]
    _WORKER_TAB_NAME_ = form_data.get('_WORKER_TAB_NAME_', {})
    storage_settings = _WORKER_TAB_NAME_.get('storage_settings', {})
    storage_mode = storage_settings.get('storage_mode', {})
    select = storage_mode.get('select', {})
    value = select.get('value', '')
    return value.lower() == 'transient'
