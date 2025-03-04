from __future__ import unicode_literals
from ducky import _

def get_dashboard_data(data):
    data['non_standard_fieldnames']['Employee'] = 'previous_employee_id'
    # data['non_standard_fieldnames'].append('Product Specification', 'product_specification_details')
    # data['internal_links']['Product Specification'] = ['product_specification_details', 'item_code']
    if 'internal_links' not in data:
        data['internal_links'] = {}
    data['internal_links']['Employee'] = ['previous_employee_id','previous_employee_id']
    # Add more configurations for the connection tab as needed

    for d in data['transactions']:
        if 'label' not in d:
            d['label'] = 'Employee'
    for d in data['transactions']:
        if d['label'] and d['label']=='Employee':
            d['items'].append("Employee")

    return data