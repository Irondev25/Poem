# Generated by Django 2.0.2 on 2018-04-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title for the poem.', max_length=50)),
                ('poet', models.CharField(help_text='Enter the poet/author name.', max_length=50)),
                ('slug', models.SlugField(help_text='User for url config', max_length=63)),
                ('poem', models.TextField()),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='poem',
            unique_together={('title', 'poet')},
        ),
    ]
