# Generated by Django 3.2 on 2023-09-29 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('golosApp', '0003_rename_candidateform_canditeform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Golos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golosApp.canditeform')),
            ],
            options={
                'verbose_name': 'Голоса',
                'verbose_name_plural': 'Голос',
            },
        ),
    ]