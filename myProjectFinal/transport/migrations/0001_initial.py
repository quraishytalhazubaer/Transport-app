# Generated by Django 4.0.2 on 2022-05-15 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Air',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_name', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('Class', models.CharField(max_length=20)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('rem', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Air_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('airid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('air_name', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=30)),
                ('To', models.CharField(max_length=30)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled'), ('P', 'paid')], default='B', max_length=11)),
                ('paymentstatus', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid'), ('D', 'Completed')], default='U', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('From', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('R', 'Requested'), ('C', 'Cancelled'), ('D', 'Completed')], default='R', max_length=11)),
                ('paymentstatus', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid')], default='U', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('Class', models.CharField(max_length=20)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('rem', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Bus_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('busid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('bus_name', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=30)),
                ('To', models.CharField(max_length=30)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled'), ('P', 'paid')], default='B', max_length=11)),
                ('paymentstatus', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid'), ('D', 'Completed')], default='U', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('From', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('R', 'Requested'), ('C', 'Cancelled'), ('D', 'Completed')], default='R', max_length=11)),
                ('paymentstatus', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid')], default='U', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='CNG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('From', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('R', 'Requested'), ('C', 'Cancelled'), ('D', 'Completed')], default='R', max_length=11)),
                ('paymentstatus', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid')], default='U', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122)),
                ('message', models.TextField()),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Launch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_name', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('Class', models.CharField(max_length=20)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('rem', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Launch_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('launchid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('launch_name', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=30)),
                ('To', models.CharField(max_length=30)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled'), ('P', 'paid')], default='B', max_length=11)),
                ('paymentstatus', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid'), ('D', 'Completed')], default='U', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Microbus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('From', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('R', 'Requested'), ('C', 'Cancelled'), ('D', 'Completed')], default='R', max_length=11)),
                ('paymentstatus', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid')], default='U', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Resetpass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122)),
                ('history', models.CharField(max_length=12)),
                ('dateused', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('Class', models.CharField(max_length=20)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('rem', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Train_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('trainid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('train_name', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=30)),
                ('To', models.CharField(max_length=30)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=11)),
                ('paymentstatus', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid'), ('D', 'Completed')], default='U', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('fname', models.CharField(max_length=200, null=True)),
                ('lname', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=13, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='static/ImageUpload/img200.png', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]