from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class (e.g., 'fas fa-paint-brush')")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Project Categories"

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')
    description = models.TextField()
    client = models.CharField(max_length=200, blank=True)
    project_date = models.DateField()
    featured_image = models.ImageField(upload_to='projects/')
    image_1 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True, help_text="Live project URL if available")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_company = models.CharField(max_length=200, blank=True)
    client_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    testimonial = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client_name} - {self.testimonial[:50]}"
    
    class Meta:
        ordering = ['-created_at']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']

class About(models.Model):
    name = models.CharField(max_length=100, default="Your Name")
    title = models.CharField(max_length=200, default="Graphic Designer")
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)
    bio = models.TextField()
    experience_years = models.IntegerField(default=0)
    projects_completed = models.IntegerField(default=0)
    happy_clients = models.IntegerField(default=0)
    awards_won = models.IntegerField(default=0)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "About"
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(help_text="Skill percentage (0-100)")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('behance', 'Behance'),
        ('dribbble', 'Dribbble'),
        ('github', 'GitHub'),
        ('youtube', 'YouTube'),
    ]
    
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.platform