from behave import *

@then('Verify logo "https://uploads-ssl.webflow.com/5a44e540f6b9a40001be7bae/5a44f7fc80557a000179868e_Logo-New.svg" is here')
def vrf_logo_here(context):
    """
    https://uploads-ssl.webflow.com/5a44e540f6b9a40001be7bae/5a44f7fc80557a000179868e_Logo-New.svgt
    """
    context.app.main_page.vrf_logo_here()