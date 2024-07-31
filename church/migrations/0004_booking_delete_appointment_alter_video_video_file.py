# Generated by Django 5.0.6 on 2024-07-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0003_video_delete_commercialvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('service', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='video/'),
        ),
    ]