from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class Company(models.Model):
    """ Модель для компаний """
    name = models.CharField(max_length=100)
    video_link = models.CharField(max_length=250)
    main_text = models.CharField(max_length=450)
    secondary_text = models.CharField(max_length=450)
    logo = models.ImageField(upload_to='course_images/')

    def __str__(self):
        return self.name


class Course(models.Model):
    """ Модель для курсов """
    name = models.CharField(max_length=100)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    about = models.TextField()
    skills = models.TextField()
    preview_image = models.ImageField(upload_to='course_images/')
    image = models.ImageField(upload_to='course_images/')

    def __str__(self):
        return self.name


class User(AbstractUser):
    """ Модель для пользователя """
    phone = models.CharField(max_length=100)


class Skill(models.Model):
    """ Модель для навыков получаемых в ходе прохождения курса """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/')
    about = models.TextField()
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """ Модель для уроков в конкретном курсе """
    name = models.CharField(max_length=100)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.course}'


class VideoToLesson(models.Model):
    """ Модель для видеоуроков """
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE)
    video = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class TextToLesson(models.Model):
    """ Модель для текстовых уроков """
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE)
    text = models.TextField()
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ImageToTextLesson(models.Model):
    """ Модель для изображений в уроке """
    text_lesson = models.ForeignKey(to=TextToLesson, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course_images/')

    def __str__(self):
        return 'изображение для' + self.text_lesson.name


class LessonToUser(models.Model):
    """ Модель для соединения уроков с пользователем и отметки выполнения """
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.lesson}'


class CourseToUser(models.Model):
    """ Модель для соединения различных курсов с конкретным пользователем """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' - ' + self.course.name


class Speaker(models.Model):
    """ Модель для спикеров """
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/')

    def __str__(self):
        return self.name


class SpeakerToCourse(models.Model):
    """ Модель для привязки различных спикеров к конкретному курсу """
    speaker = models.ForeignKey(to=Speaker, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.speaker.name + ' - ' + self.course.name


class ProgramUnit(models.Model):
    """ Модель для этапов программы конкретного курса """
    text = models.TextField()
    speaker = models.ForeignKey(to=Speaker, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class AnswerToText(models.Model):
    """ Модель для выбора ответа у теста """
    text = models.ForeignKey(to=TextToLesson, on_delete=models.CASCADE)
    answer = models.TextField()
    right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class AboutCourse(models.Model):
    """ Модель для блоков о курсе """
    block_name = models.CharField(max_length=100)
    block_text = models.TextField()
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.block_name
