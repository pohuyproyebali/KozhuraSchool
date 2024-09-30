from django.db import models


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
        units = {
            unit.id:
                {
                    'text': unit.text,
                    'speaker': f"{unit.speaker.name} {unit.speaker.profession}"
                } for unit in program_units_to_course}
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
