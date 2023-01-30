from django.db import models

# Create your models here.


from django_extensions.db.models import TimeStampedModel
from django.utils import timezone
from datetime import datetime

class Task(TimeStampedModel):
    """Задачи"""
    """1 В каждой задаче есть название, говорящее о том, что нужно сделать, 
    например, "купить в магазине новый утюг". 
    2 В каждой задаче есть отметка выполнена она или нет (по умолчанию     не выполнена). 
    3 4 У каждой задачи есть дата и время создания, дата и время завершения. 
    Время завершения задачи проставляется в момент проставления галочки о завершении задачи. 
    Время завершения задачи убирается (становится null) в момент снятия галочки о завершении задачи."""
    # objects = AnnotatedManager()  # переопределение объекта Cart.objects.
    # При любой выборке из таблицы вызовется метод get_queryset() определенный внутри AnnotatedManager

    name = models.CharField(max_length=64, help_text="Описание задачи")
    is_active = models.BooleanField(default=True, help_text="Активна ли задача")
    timestamp_created = models.DateTimeField(auto_now_add=True, help_text="Дата создания задачи")
    timestamp_closed = models.DateTimeField(blank=True, null=True, help_text="Дата завершения задачи")

    def __str__(self):
        """переопределение строкового представления задачи"""
        return f"Task {self.id}:{self.name}|created:{self.timestamp_created}|closed:{self.timestamp_closed}"

    def save(self, *args, **kwargs) -> None:
        """Переопределение сохранения.
        Убирается время завершения задачи, если ставится статус "не завершено".
        Если ставится статус "завершено", время завершения становится текущим.
        """
        if self.is_active :
            self.timestamp_closed = None
        else:
            # if not self.timestamp_closed:
            self.timestamp_closed = datetime.now()
        # print("aaa")
        return super().save(*args, **kwargs)

        # def save(self, *args, **kwargs) -> None:
        # """Переопределение сохранения.

    # Убирается галочка активности корзины если нет привязанного пользователя.
    # """
    # if self.user is None and self.is_active:
    #     self.is_active = False
    # return super().save(*args, **kwargs)
