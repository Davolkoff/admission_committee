from django.db import models


# класс, отвечающий за страницы, на которых отображаются кнопки
class Pages(models.Model):
    page_id = models.IntegerField('Id страницы')
    name = models.CharField('Название страницы', max_length=60, default="")

    def __str__(self):
        return f"{self.page_id}. {self.name}"


# класс, определяющий, что написано на кнопках и что они делают
class MenuButtons(models.Model):
    button_id = models.IntegerField('Id кнопки')
    page = models.ForeignKey(Pages, on_delete=models.CASCADE, verbose_name="Страница с кнопкой", related_name="page")
    text = models.CharField("Текст кнопки", max_length=60, default="")
    print_file = models.CharField("Файл для печати", max_length=60, default="-")
    redirect_page = models.ForeignKey(Pages, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Страница переадресации", related_name="redirect_page")

    class Meta:
        unique_together = ('button_id', 'page')

    def __str__(self):
        return f"{self.text} | Страница: {self.page.name}"


# класс, отвечающий за талончики
class Tickets(models.Model):
    ticket_id = models.IntegerField("Номер талона")
    question = models.CharField("Вопрос", max_length=60)
    taken = models.BooleanField("Принят в работу", default=False)

    def __str__(self):
        return f"{self.ticket_id}. {self.question}"


# класс, определяюший операторов, обрабатывающих запросы
class Operators(models.Model):
    window_number = models.IntegerField("Номер окна")
    current_ticket = models.ForeignKey(Tickets, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="Текущий посетитель")

    def __str__(self):
        return f"Окно номер {self.window_number}"

# class ExpertTickets(models.Model):
#     ticket_id = models.IntegerField("Номер талона")
#     question = models.CharField("Вопрос", max_length=60)
#     taken = models.BooleanField("Принят в работу", default=False)

#     def __str__(self):
#         return f"{self.ticket_id}. {self.question}"
    
class Experts(models.Model):
    window_number = models.IntegerField("Номер окна")
    current_ticket = models.ForeignKey(Tickets, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="Текущий посетитель")

    def __str__(self):
        return f"Окно номер {self.window_number}"
