from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class Company(models.Model):
    """ Модель для компаний """
    name = models.CharField(max_length=100)
    video_link = models.CharField(max_length=250)
    main_text = models.CharField(max_length=450)
    secondary_text = models.CharField(max_length=450)
    logo = models.ImageField(upload_to='course_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class CourseQueryset(models.QuerySet):
    def speaker_of_this_course(self, speakers_to_course):
        speakers = {
            speaker.speaker.id: {
                'name': speaker.speaker.name,
                'profession': speaker.speaker.profession,
                'image': speaker.speaker.image.url if speaker.speaker.image else None,
            }
            for speaker in speakers_to_course
        }
        return speakers

    def program_units_of_this_course(self, program_units_to_course):
        units = {unit.id: unit.text for unit in program_units_to_course}
        return units

    def about_block_of_this_course(self, about_block_to_course):
        about_blocks = {
            block.id: {
                'block_name': block.block_name,
                'block_text': block.block_text,
            }
            for block in about_block_to_course
        }
        return about_blocks

    def skills_from_process_of_this_course(self, skills_to_course):
        skills = {
            skill.id: {
                'name': skill.name,
                'image': skill.image.url if skill.image else None,
                'about': skill.about
            }
            for skill in skills_to_course
        }
        return skills


class CourseManager(models.Manager):
    def get_queryset(self):
        return CourseQueryset(self.model)

    def speaker_of_this_course(self, speakers_to_course):
        return self.get_queryset().speaker_of_this_course(speakers_to_course)

    def program_units_of_this_course(self, program_units_to_course):
        return self.get_queryset().program_units_of_this_course(program_units_to_course)

    def about_block_of_this_course(self, about_blocks_to_course):
        return self.get_queryset().about_block_of_this_course(about_blocks_to_course)

    def skills_from_process_of_this_course(self, skills_to_course):
        return self.get_queryset().skills_from_process_of_this_course(skills_to_course)


class Course(models.Model):
    """ Модель для курсов """
    name = models.CharField(max_length=100)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, related_name='courses')
    about = models.TextField()
    skills = models.TextField()
    preview_image = models.ImageField(upload_to='course_images/', blank=True)
    image = models.ImageField(upload_to='course_images/', blank=True)

    objects = models.Manager()
    course_manager = CourseManager()

    def __str__(self):
        return self.name


class User(AbstractUser):
    """ Модель для пользователя """
    phone = models.CharField(max_length=100)


class Skill(models.Model):
    """ Модель для навыков получаемых в ходе прохождения курса """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/', blank=True)
    about = models.TextField()
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='skills_from_process')

    def __str__(self):
        return self.name


class LessonQueryset(models.QuerySet):
    def text_of_this_lesson(self, text_to_this_lesson):
        text = {
            text_unit.id:
                {
                    "text": text_unit.text,
                    "images": {
                        "image": image.url for image in text_unit.image_to_text_lesson.all()
                    },
                    "answers": {
                        answer.id: {
                            "answer": answer.answer,
                            "right": answer.right
                        } for answer in text_unit.answer_to_text.all()
                    }
                } for text_unit in text_to_this_lesson
        }
        return text

    def video_link_to_this_lesson(self, video_link_to_this_lesson):
        units = {video.id: video.text for video in video_link_to_this_lesson}
        return units


class LessonManager(models.Manager):
    def get_queryset(self):
        return LessonQueryset(self.model)

    def text_of_this_lesson(self, text_to_this_lesson):
        return self.get_queryset().text_of_this_lesson(text_to_this_lesson)

    def video_link_to_this_lesson(self, video_link_to_this_lesson):
        return self.get_queryset().video_link_to_this_lesson(video_link_to_this_lesson)


class Lesson(models.Model):
    """ Модель для уроков в конкретном курсе """
    name = models.CharField(max_length=100)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='lessons')

    objects = models.Manager()
    lesson_manager = LessonManager()

    def __str__(self):
        return f'{self.name} {self.course}'


class VideoToLesson(models.Model):
    """ Модель для видеоуроков """
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, related_name='video_to_lesson')
    video = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class TextToLesson(models.Model):
    """ Модель для текстовых уроков """
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, related_name='text_to_lesson')
    text = models.TextField()
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ImageToTextLesson(models.Model):
    """ Модель для изображений в уроке """
    text_lesson = models.ForeignKey(to=TextToLesson, on_delete=models.CASCADE, related_name='image_to_text_lesson')
    image = models.ImageField(upload_to='course_images/', blank=True)

    def __str__(self):
        return 'изображение для' + self.text_lesson.name


class LessonToUser(models.Model):
    """ Модель для соединения уроков с пользователем и отметки выполнения """
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, related_name='users_to_lesson')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='lesson_to_user')

    def __str__(self):
        return f'{self.user.username} - {self.lesson}'


class CourseToUser(models.Model):
    """ Модель для соединения различных курсов с конкретным пользователем """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.user.username + ' - ' + self.course.name


class Speaker(models.Model):
    """ Модель для спикеров """
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/', blank=True)
    on_main_page = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.profession}, отображение на гланой {self.on_main_page}'


class SpeakerToCourse(models.Model):
    """ Модель для привязки различных спикеров к конкретному курсу """
    speaker = models.ForeignKey(to=Speaker, on_delete=models.CASCADE, related_name='courses')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='speakers')

    class Meta:
        unique_together = (('speaker', 'course'),)

    def __str__(self):
        return self.speaker.name + ' - ' + self.course.name


class ProgramUnit(models.Model):
    """ Модель для этапов программы конкретного курса """
    text = models.TextField()
    speaker = models.ForeignKey(to=Speaker, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='program_units')

    def __str__(self):
        return self.text


class AnswerToText(models.Model):
    """ Модель для выбора ответа у теста """
    text = models.ForeignKey(to=TextToLesson, on_delete=models.CASCADE, related_name='answer_to_text')
    answer = models.TextField()
    right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class AboutCourse(models.Model):
    """ Модель для блоков о курсе """
    block_name = models.CharField(max_length=100)
    block_text = models.TextField()
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='about_block')

    def __str__(self):
        return self.block_name


class SpeakerToLesson(models.Model):
    """ Модель для связки спикеров с уроками """
    speaker = models.ForeignKey(to=Speaker, on_delete=models.CASCADE)
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, related_name='speaker_to_lesson')

    def __str__(self):
        return f'{self.speaker.name} - {self.lesson}'
