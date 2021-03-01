from django.db import models

status_choices = (
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, null=False, blank=False)
    text_for_detailed = models.TextField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=100, default='new', choices=status_choices, blank=False)
    pub_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(self.id, self.description, self.text_for_detailed, self.status)

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = "задачи"
