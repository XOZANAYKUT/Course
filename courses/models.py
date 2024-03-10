from django.db import models
from django.contrib.auth.models import User

DURATION_CHOICES = (
    ('short_term', 'Short-term'),
    ('long_term', 'Long-term')
)

STATUS_CHOICES = (
    (0, "Draft"),
    (1, "Published")
)
class Course(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL Tag")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courses_posts", default=1
    )  # Varsayılan olarak, kullanıcı kimliği 1 olan bir kullanıcıyı ata.
    content = models.TextField(verbose_name="Course Content")
    date = models.DateField(verbose_name="Course Date")
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES, verbose_name="Course Duration")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="Status")
    excerpt = models.TextField(blank=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title