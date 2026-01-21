from django.db import models


class Movies(models.Model):
    name_movie = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie/')
    description = models.TextField()

    JENRE_MOVIE = (
        ("Боевик", "Боевик"),
        ("Драма", "Драма"),
        ("Фантастика", "Фантастика"),
        ("Ужасы", "Ужасы"),
        ("Триллер", "Триллер"),
        ("Документальное", "Документальное")
    )

    jenre_movies = models.CharField(
        max_length=100,
        choices=JENRE_MOVIE,
        default="Боевик"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_movie


class Reviews(models.Model):
    choice_movie = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE,
        related_name="review"
    )

    MARKS = (
        ("🌟", "🌟"),
        ("🌟🌟", "🌟🌟"),
        ("🌟🌟🌟", "🌟🌟🌟"),
        ("🌟🌟🌟🌟", "🌟🌟🌟🌟"),
        ("🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟")
    )

    marks = models.CharField(
        max_length=100,
        choices=MARKS,
        default="🌟"
    )

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_movie} : {self.marks}'