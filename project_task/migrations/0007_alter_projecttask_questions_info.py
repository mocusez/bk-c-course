# Generated by Django 3.2.4 on 2022-04-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project_task", "0006_alter_projecttask_students_visible"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projecttask",
            name="questions_info",
            field=models.JSONField(
                blank=True, null=True, verbose_name="题目相关信息(id,顺序,分值等)"
            ),
        ),
    ]
