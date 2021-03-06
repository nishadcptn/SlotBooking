# Generated by Django 3.2.6 on 2021-08-12 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='slots',
            fields=[
                ('slot', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'slots',
            },
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teachers.slots')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teachers.teacher')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
        migrations.CreateModel(
            name='attandance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('p_in', models.DateTimeField(auto_now_add=True)),
                ('p_out', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teachers.teacher')),
            ],
            options={
                'db_table': 'attandance',
            },
        ),
    ]
