class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Write a function that provides an efficient look up of whether the user is in a group.
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # looking for user in get_users and get_name methods in Group class
    name = group.get_name()
    users = group.get_users()
    
    if user in users or user == name:
        return True
    else:
        # getting details of groups from get_groups method in Group class
        groups = group.get_groups()
        for group in groups:
            return is_user_in_group(user, group) # calling function recursively
        return False

##### Test Cases #####
print('Test Case 1:')
print(is_user_in_group('sub_child_user', parent))  
# would return True
print('\n')

print('Test Case 2:')
print(is_user_in_group('', child))
# would return False
print('\n')

print('Test Case 3:')
print(is_user_in_group('child', child))
# would return True
print('\n')

print('Test Case 4:')
print(is_user_in_group('sub_child_user', sub_child))
# would return True