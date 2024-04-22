from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    Categories = [
        ('Life', '生活'),
        ('Travel', '旅遊'),
        ('Office', '職場'),
        ('Sport', '運動'),
        ('Tech', '科技'),
        ('Other', '其他')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    image = models.ImageField(blank=True, default='default.jpg')
    content = models.TextField(blank=True)
    category = models.CharField(max_length=10, choices=Categories)
    tags = models.ManyToManyField(Tag)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return "({}) {}".format(self.author, self.title)

class Comment(models.Model):
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, on_delete=models.CASCADE)
     content = models.TextField(blank=True)
     date = models.DateTimeField(auto_now=True)

     def __str__(self):
        return "({}) comment on {}".format(self.author, self.post)
