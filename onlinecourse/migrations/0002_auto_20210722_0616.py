# Generated by Django 3.1.3 on 2021-07-22 06:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='is_Correct',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='question_id',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='question',
            name='lesson_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(),
        ),
    ]