# Generated by Django 2.2.8 on 2022-02-28 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('tutoring', '0001_initial'), ('tutoring', '0002_auto_20210122_0002'), ('tutoring', '0003_auto_20210128_0050'), ('tutoring', '0004_auto_20210202_0210'), ('tutoring', '0005_auto_20210902_2254'), ('tutoring', '0006_auto_20210907_0154'), ('tutoring', '0007_auto_20220127_1958')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coursesemester', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.IntegerField(choices=[(12, '12pm'), (13, '1pm'), (14, '2pm'), (15, '3pm'), (16, '4pm'), (20, '8pm'), (21, '9pm')])),
                ('day', models.IntegerField(choices=[(1, 'Mon'), (2, 'Tue'), (3, 'Wed'), (4, 'Thu'), (5, 'Fri')])),
                ('timeslot_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TutorCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cory_preference', models.IntegerField(default=0, null=True)),
                ('soda_preference', models.IntegerField(default=1, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursesemester.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('adjacent_pref', models.IntegerField(default=0)),
                ('num_assignments', models.IntegerField(default=2)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CoursePreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.IntegerField(default=-1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.TutorCourse')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.Tutor')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=255)),
                ('room_num', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutoring.Room')),
                ('slot_id', models.IntegerField(default=0)),
                ('timeslot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutoring.TimeSlot')),
                ('tutors', models.ManyToManyField(to='tutoring.Tutor')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlotPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.TimeSlot')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.Tutor')),
                ('preference', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RoomPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.IntegerField(default=0)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.Room')),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.TimeSlot')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.Tutor')),
            ],
        ),
    ]