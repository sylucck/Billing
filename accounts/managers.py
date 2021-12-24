from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, name, password=None, is_active=True, is_staff=False, is_superuser=False):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('Users Email must be set')
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError('Users must have a name')
        user_obj = self.model(
            email = self.normalize_email(email),
            name = name
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.superuser = is_superuser
        user_obj.active = is_active
        user_obj.save(using=self.db)
        return user_obj

    def create_staffuser(self, email, name, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            name,
            password=password,
            is_staff=True
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            name,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        
        user.save(using=self._db)
        return user
