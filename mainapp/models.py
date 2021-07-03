from django.db import models




# ---------------------Support--models------------------------
class Item(models.Model):

    title=models.CharField(max_length=100,verbose_name="Название предмета")
    
    def __str__(self):
        return self.title
    

class Benchmark(models.Model):

    title=models.CharField(max_length=1000,verbose_name="Название критерия")
    points=models.PositiveIntegerField(verbose_name="Максимальное кол-во баллов")

    def __str__(self):
        return self.title

class Material(models.Model):

    title=models.CharField(unique=True,max_length=100,verbose_name="Название материала")
    text=models.TextField(verbose_name="Текст материала")
    imgMaterial=models.ImageField(upload_to="imgForMaterials",blank=True,null=True,verbose_name="Картинка для материала")

    def __str__(self):
        return self.title

class Category(models.Model):

    title=models.CharField(unique=True,max_length=100,verbose_name='Название тэга')
    material=models.ForeignKey(Material,verbose_name="Материал к категории задания",blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#---------------------------Main--Models---------------------------
class Number(models.Model):

    categorys=models.ManyToManyField(Category,verbose_name="Категории")
    title=models.CharField(max_length=100,unique=True)
    number=models.PositiveIntegerField(unique=True,verbose_name="Номер задания")
    points=models.PositiveIntegerField(default=1,verbose_name="Количество баллов за выполненное задание")
    benchmarks=models.ManyToManyField(Benchmark,blank=True,verbose_name="Критерии (Только для 2-ой части!)")
    item=models.ForeignKey(Item,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.title}"


class Question(models.Model):

    number=models.ForeignKey(Number,on_delete=models.CASCADE,verbose_name="Номер задания")
    categorys=models.ForeignKey(Category,verbose_name="Категория",on_delete=models.CASCADE)
    difficult=models.PositiveIntegerField(verbose_name="Сложность задания по 10-ти бальной шкале")
    introduction=models.TextField(blank=True,verbose_name="Текст к заданию")
    firstAsk=models.TextField(verbose_name="Первый вопрос")
    secondAsk=models.TextField(blank=True,verbose_name="Второй вопрос")
    thirdAsk=models.TextField(blank=True,verbose_name="Третий вопрос")
    imgForAsk=models.ImageField(blank=True,null=True,upload_to="imgForAsk",verbose_name="Картинка для вопроса")

    imgForAns=models.ImageField(blank=True,null=True,upload_to="imgForAns",verbose_name="Картинка для ответа")
    fistInstruction=models.TextField(verbose_name="инструкция к первому вопросу")
    secondInstuction=models.TextField(blank=True,verbose_name="инструкция к второму вопросу")
    thirdIntroduction=models.TextField(blank=True,verbose_name="инструкция к третьему вопросу")

    firstAnswer=models.CharField(max_length=100,verbose_name="Ответ на первый вопрос")
    secondAnwer=models.CharField(max_length=100,blank=True,verbose_name="Ответ на второй вопрос")
    thirdAnswer=models.CharField(max_length=100,blank=True,verbose_name="Ответ на третий вопрос")

    addition=models.TextField(verbose_name="Примечание",blank=True)
    source=models.CharField(max_length=100,verbose_name="Название источника",blank=True)
    source_link=models.TextField(verbose_name="Ссылка на источник",blank=True)

    def __str__(self):
        return f"{self.number} - {self.introduction}"

class Variant(models.Model):

    variantNumber=models.PositiveIntegerField(unique=True,verbose_name="Номер варианта")
    questions=models.ManyToManyField(Question,verbose_name="Задания, которые будут в этом варианте")
    item=models.ForeignKey(Item,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.variantNumber}"
