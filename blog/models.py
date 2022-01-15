from django.conf import settings
from django.db import models
from django.utils import timezone

# Definindo que o modelo trata-se de um objeto
# "Class" -> indica que está sendo definido um objeto 
# "Post" -> nome do modelo (pode ser qualquer um)
# "models.Model" -> indica que é um modelo Django (será armazenado no banco de dados)

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #models.ForeignKey -> link para outro modelo
    title = models.CharField(max_length=200) #models.CharField -> um texto com caracteres limitados
    text = models.TextField() #models.TextField -> texto sem limitação de caracteres 
    created_date = models.DateTimeField(default=timezone.now) #models.DateTimeField -> data e hora
    published_date = models.DateTimeField(blank=True, null=True) 

# def -> função/método  
# IMPORTANTE: def e def __str__(self) sempre são endentados dentro de "Class"
# TODOS OS MÉTODOS SÃO ENDENTADOS DENTRO DA CLASSE (CLASS)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
