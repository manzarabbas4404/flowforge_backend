import uuid
from django.db import models
from django.utils.text import slugify
from django.db.transaction import atomic
from django.core.exceptions import ValidationError
from organization.model_managers import ActiveOrganizationManager
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


def no_digit_name(value):
    if value.isdigit():
        raise ValidationError("Organization name cannot be numbers only.")


class Organization(models.Model):

    objects = models.Manager()
    active_orgs = ActiveOrganizationManager()

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, null=False, editable=False
    )
    name = models.CharField(
        null=False, max_length=255, unique=True, validators=[no_digit_name]
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["slug", "name"])]
        ordering = ["name"]
        verbose_name = "Organization"

    def clean(self):
        if len(self.name) < 2:
            raise ValidationError(
                "Organization name must be at least 3 characters long."
            )

    @property
    def created_at_formatted(self):
        if self.created_at is None:
            return ""
        return self.created_at.strftime("%d.%m.%Y")

    @atomic
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class OrganizationDisplay(Organization):
    class Meta:
        proxy = True
        ordering = ["-created_at"]
        verbose_name = "Organization Display"

    def short_name(self):
        return self.name[:10]


class OrganizationMember(models.Model):
    ROLE_CHOICES = (
        ("owner", "Owner"),
        ("admin", "Admin"),
        ("member", "Member"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="member")
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="member",
    )
    organization = models.ForeignKey(
        Organization,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Organization",
    )
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "organization"],
                name="unique_user_organization_membership",
            )
        ]
        verbose_name = "Organization Member"

    def __str__(self):
        return f"{self.user} - {self.organization} ({self.role})"

    def is_owner(self):
        return self.role == "owner"

    def can_manage_projects(self):
        return self.role in ["owner", "admin"]

    def can_manage_members(self):
        return self.role == "owner"
