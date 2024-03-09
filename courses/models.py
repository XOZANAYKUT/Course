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

REVIEW_CHOICES = (
    (1, "Excellent"),
    (2, "Good"),
    (3, "Average"),
    (4, "Poor"),
    (5, "Very Poor")
)

class Course(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL Tag")
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses", verbose_name="Instructor")
    description = models.TextField(verbose_name="Course Description")
    content = models.TextField(verbose_name="Course Content")
    date = models.DateField(verbose_name="Course Date")
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES, verbose_name="Course Duration")
    review = models.IntegerField(choices=REVIEW_CHOICES, verbose_name="Course Rating")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="Status")
    category = models.CharField(max_length=100, verbose_name="Category")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title