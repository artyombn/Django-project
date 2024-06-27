from django.contrib.auth.mixins import UserPassesTestMixin


class GroupRequiredMixin(UserPassesTestMixin):
    group_name = None

    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            if isinstance(self.group_name, list):
                return user.groups.filter(name__in=self.group_name).exists() or user.is_staff
            else:
                    return user.groups.filter(name=self.group_name).exists() or user.is_staff
        return False