from behave import *

@then('Verify phone "{phone}" is here')
def vrf_phn_here(context, phone):
    """
    Verify phone "+1 718-576-1406" is here
    """
    context.app.main_page.vrf_phn_here(phone)