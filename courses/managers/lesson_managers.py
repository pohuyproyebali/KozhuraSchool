from django.db import models


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

