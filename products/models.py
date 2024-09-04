from django.db import models


class AbstractModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(AbstractModel):
    view_count = models.IntegerField(default=0)


class SearchTag(AbstractModel):
    pass


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.movies.count()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(SearchTag)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def search_tags(self):
        return [tag.name for tag in self.all()]

    def rating(self):
        return 0


STAR_CHOICES = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=STAR_CHOICES, default=4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='all_reviews')

    def __str__(self):
        return self.text
