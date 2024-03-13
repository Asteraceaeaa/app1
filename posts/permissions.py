

class AuthorPermissionsMixin:
  def has_permissions(self):
    return self.get_object().author == self.request.user
  
class ModerPermissionsMixin:
  def has_permissions(self):
    return self.request.user.groups.filter(name='mod').exists()