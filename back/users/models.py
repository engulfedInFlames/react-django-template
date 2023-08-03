from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from timestamps.models import Timestamp


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        if email is None:
            raise ValueError("이메일을 반드시 입력해야 합니다")

        if password is None:
            raise ValueError("비밀번호를 반드시 입력해야 합니다")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(
    AbstractBaseUser,
    Timestamp,
):
    class UserTypeChoices(models.TextChoices):
        GITHUB = ("github", "깃허브")
        GOOGLE = ("google", "구글")
        NORMAL = ("normal", "일반")

    username = None
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    email_verified = models.BooleanField(default=False)
    nickname = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    avatar = models.URLField(
        null=True,
        blank=True,
    )
    user_type = models.CharField(
        choices=UserTypeChoices.choices,
        max_length=20,
        default="NORMAL",
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
