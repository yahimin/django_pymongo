from django.db import migrations, models

class Migration(migrations.Migration):
    
    initial = True
    
    dependencies = []
    
    operations = [
        migrations.CreateModel(
            name='SampleDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_id', models.CharField(max_length=30)),
                ('common_name', models.CharField(max_length=30)),
                ('scientific_name', models.CharField(max_length=30)),
                ('available', models.CharField(max_length=2)),
                ('category', models.CharField(max_length=7)),
            ]
        )
    ]