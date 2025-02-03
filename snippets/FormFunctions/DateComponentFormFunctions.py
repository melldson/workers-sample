def is_single_date(*args):
    form_data = args[0]
    _WORKER_TAB_NAME_ = form_data.get('_WORKER_TAB_NAME_', {})
    date_mode = _WORKER_TAB_NAME_.get('date_mode', {})
    date_mode_select = date_mode.get('select', {})
    date_mode_value = date_mode_select.get('value', '')
    return date_mode_value == 'single_date'

def is_date_interval(*args):
    form_data = args[0]
    _WORKER_TAB_NAME_ = form_data.get('_WORKER_TAB_NAME_', {})
    date_mode = _WORKER_TAB_NAME_.get('date_mode', {})
    date_mode_select = date_mode.get('select', {})
    date_mode_value = date_mode_select.get('value', '')
    return date_mode_value == 'date_interval'
