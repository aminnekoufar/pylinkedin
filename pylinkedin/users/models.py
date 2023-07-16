from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, BooleanField, CharField, DateField, ForeignKey, ImageField, Model, TextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for pylinkedin.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    location = CharField(max_length=255)
    gender = CharField(max_length=20)
    avatar = ImageField(upload_to="avatars/", null=True, blank=True)
    is_verified = BooleanField(default=False)

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})


class Education(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name="education")
    institution = CharField(max_length=255)
    degree = CharField(max_length=100)
    field_of_study = CharField(max_length=100)
    start_date = DateField()
    end_date = DateField()
    description = TextField()

    def __str__(self):
        return f"{self.field_of_study}: {self.degree}"
