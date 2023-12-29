def build_profile(first, last, **user_info):
    """The double asterisks before the parameter **user_info cause Python to create
a dictionary called user_info containing all the extra name-value pairs the
function receives (as many as user gives)."""
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)