# Generated by Django 2.2.6 on 2019-10-20 17:51

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='Holiday name')),
                ('holiday', models.DateField(db_index=True, verbose_name='Holiday day')),
                ('country', models.IntegerField(choices=[(1, 'Thailand'), (2, 'South Korea'), (3, 'Japan'), (4, 'China')], db_index=True, default=1, verbose_name='Country code')),
            ],
            options={
                'verbose_name': 'Holiday',
                'verbose_name_plural': 'Holidays',
                'unique_together': {('holiday', 'country')},
            },
        ),
    ]