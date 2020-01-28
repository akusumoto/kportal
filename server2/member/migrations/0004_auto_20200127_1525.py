# Generated by Django 3.0.2 on 2020-01-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20200127_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='part',
            field=models.CharField(choices=[('vn1', '1st Violin'), ('vn2', '2nd Violin'), ('va', 'Viola'), ('vc', 'Cello'), ('cb', 'Contrabass'), ('fl', 'Flute'), ('cl', 'Clarinet'), ('sax', 'Saxophone'), ('ob', 'Oboe'), ('fg', 'Fagotto'), ('tp', 'Trumpet'), ('tb', 'Trombone'), ('tu', 'Tuba'), ('gt', 'Guiter'), ('pf', 'Piano'), ('syn', 'Synchesizer'), ('bs', 'Electric Bass'), ('cho-sp', 'Chorus Soprano'), ('cho-al', 'Chorus Alto'), ('cho-tn', 'Chorus Tennor'), ('cho-bs', 'Chorus Bass'), ('cond', 'Conductor'), ('staff', 'Staff')], default='staff', max_length=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('active', '在籍中'), ('rest', '休団中'), ('left', '退団'), ('ghost', '幽霊団員')], default='active', max_length=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('adult', '社会人'), ('student', '学生')], default='adult', max_length=7),
        ),
    ]
