# Generated by Django 3.2.21 on 2023-10-13 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20231013_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('Reservation', 'Reservation'), ('Terrace ticket', 'Terrace ticket'), ('Verranda ticket', 'Verranda ticket'), ('Suite ticket', 'Suite ticket'), ('VIP ticket', 'VIP ticket')], max_length=100, null=True),
        ),
    ]