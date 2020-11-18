from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Отправитель", related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Получатель", related_name='recipient')
    message = models.TextField("Сообщение")
    pub_date = models.DateTimeField('Дата сообщения', auto_now_add=True)

    def __str__(self):
        return self.message

