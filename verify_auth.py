from django.contrib.auth import get_user_model
from auction.forms import UserSignupForm

User = get_user_model()

# Test 1: Create User via Form
print("Testing User Creation via Form...")
form_data = {
    'username': 'testuser_debug',
    'user_type': 'bidder',
    'password1': 'TestPass123!',
    'password2': 'TestPass123!'
}

# Note: In the view, the form is initialized with POST data
# UserSignupForm inherits from UserCreationForm, which handles password1/2 in 'clean' or 'save'
# but wait, UserCreationForm expects password1/2 to be in the form fields.
# My fix REMOVED password1/2 from Meta.fields.
# Does UserCreationForm automatically add them? Yes, in its __init__.
# BUT, if I explicitly define Meta.fields in UserSignupForm it might override?
# Let's check if the form is valid.

form = UserSignupForm(data=form_data)
if form.is_valid():
    print("Form is VALID.")
    try:
        user = form.save()
        print(f"User created: {user.username} (ID: {user.id})")
        
        # Test 2: Check Auctioner flag
        if not user.is_auctioner:
            print("User is correctly marked as bidder (is_auctioner=False)")
        else:
            print("ERROR: User incorrectly marked as auctioner")
            
    except Exception as e:
        print(f"ERROR Saving User: {e}")
else:
    print("Form is INVALID.")
    print(form.errors)

# Cleanup
if 'user' in locals():
    user.delete()
    print("Test User Deleted.")
