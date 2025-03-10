from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    """Manager for custom User model with token handling."""

    def create_user(self, username, password=None):
        """Create and return a regular user with default tokens."""
        if not username:
            raise ValueError("A username is required")
        
        user = self.model(username=username.lower())  # Normalize username
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """Create and return a superuser with admin permissions."""
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model supporting authentication and token tracking."""
    username = models.CharField(max_length=50, unique=True)
    tokens = models.IntegerField(default=4000)  # Default tokens for new users
    is_staff = models.BooleanField(default=False)  # Enables Django admin login
    is_superuser = models.BooleanField(default=False)  # Admin privileges

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Check if user has a specific permission."""
        return self.is_superuser

    def has_module_perms(self, app_label):
        """Check if user has permissions to view the module."""
        return self.is_superuser


class Chat(models.Model):
    """Model to store chat messages between users and AI."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.username} at {self.timestamp}"
