# Generated by Django 4.2.5 on 2023-09-29 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('SALARY', 'SALARY'), ('BUSSINESS', 'BUSSINESS'), ('SIDE-HUSTLE', 'SIDE-HUSTLE'), ('OTHERS', 'OTHERS')], max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.DeleteModel(
            name='Expenses',
        ),
    ]
