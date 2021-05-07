# Generated by Django 3.1.10 on 2021-05-07 17:51

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0005_auto_20210507_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StreamBlock([('color_section', wagtail.core.blocks.StructBlock([('color', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'Bela'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('pink', 'Roza')], label='Barva')), ('body', wagtail.core.blocks.StreamBlock([('headline', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.TextBlock(label='Opis', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Slika', required=False))], label='Naslov', template='home/blocks/headline.html')), ('badge', wagtail.core.blocks.StructBlock([('line_one', wagtail.core.blocks.CharBlock(label='Prva vrstica', required=False)), ('line_two', wagtail.core.blocks.CharBlock(label='Druga vrstica', required=False))], label='Značka', template='home/blocks/badge.html')), ('rich_text', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(label='Besedilo')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Tabela', template='home/blocks/table.html'))], label='Obogateno besedilo', template='home/blocks/rich_text.html'))]))])), ('scrolling_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(label='Besedilo'))], label='Drsna pasica', template='home/blocks/scrolling_banner.html'))]))], default='', verbose_name='Vsebina'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Slika'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Podnaslov'),
        ),
        migrations.CreateModel(
            name='MetaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('meta_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
