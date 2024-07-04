from django.db import models


class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='idea_images/', default='idea_images/no_idea.jpg')
    status = models.ForeignKey("IdeaStatus", on_delete=models.CASCADE, default=1)
    co_author = models.ManyToManyField('user.User', through='partnership.CoAuthor', related_name='coauthored_ideas')
    investors = models.ManyToManyField('user.User', through='investment.Investor', related_name='investors_ideas')


# class IdeaImages(models.Model):
#     idea = models.ForeignKey(Idea, related_name='images', on_delete=models.CASCADE)
#     image2 = models.ImageField(upload_to='idea_images/', default='idea_images/no_idea.jpg')

    def __str__(self):
        return (f"{self.title}/{self.category}/{self.author}")

    def comments_count(self):
        return self.comments.count()



class Likes(models.Model):

    idea = models.ForeignKey(Idea, verbose_name='Idea', on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', verbose_name='User', on_delete=models.CASCADE)


class DisLikes(models.Model):

    idea = models.ForeignKey(Idea, verbose_name='Idea', on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', verbose_name='User', on_delete=models.CASCADE)


class IdeaStatus(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    updated_by = models.ForeignKey('user.User', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status