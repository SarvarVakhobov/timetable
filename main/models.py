from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    course_id = models.CharField(max_length=20, blank=True, null=True)
    first_year = models.IntegerField(default=2022)
    last_year = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.last_year = self.first_year + 4

        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.course_id)
    

class Teachers(models.Model):
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.full_name = self.last_name+'. '+self.first_name[:1].title()+'. '+self.father_name[:1].title()+'.'

        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.full_name)
    


class Subjects(models.Model):
    sub_id = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_id = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    

class Lesson(models.Model):
    PARA = (
        ('1', '1'),        
        ('2', '2'),        
        ('3', '3'),        
        ('4', '4'),        
        ('5', '5'),        
        ('6', '6'),        
    )
    HAFTA_KUNLARI = (
        ('dushanba', 'dushanba'),        
        ('seshanba', 'seshanba'),        
        ('chorshanba', 'chorshanba'),        
        ('payshanba', 'payshanba'),        
        ('juma', 'juma'),        
        ('shanba', 'shanba'),        
    )
    TYPE = (
        ('Amaliy','Amaliy'),
        ('Ma\'ruza','Ma\'ruza'),
        ('Seminar','Seminar'),
        ('Laboratoriya','Laboratoriya'),
    )
    TIME = ['8:30', '10:00', '11:30', '2:00', '3:30', '5:00']

    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, related_name='lesson', null=True,)
    teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=20, choices=TYPE, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    week_day = models.CharField(max_length=20, choices=HAFTA_KUNLARI, default=HAFTA_KUNLARI[0][0], null=True)
    para = models.CharField(max_length=5, choices=PARA, null=True)
    time = models.CharField(max_length=10, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.time = self.TIME[int(self.para)-1]

        return super().save(*args, **kwargs)
    

    def __str__(self):
        return str(self.week_day+" "+self.para+" "+" "+str(self.subject)+" "+self.type+" "+self.teacher.last_name+" "+str(self.course))
