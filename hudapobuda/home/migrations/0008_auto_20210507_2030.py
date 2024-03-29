# Generated by Django 3.1.10 on 2021-05-07 18:30

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
        ('home', '0007_auto_20210507_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_links', wagtail.core.fields.StreamField([('page', wagtail.core.blocks.PageChooserBlock())])),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Meta nastavitve',
            },
        ),
        migrations.AddField(
            model_name='contentpage',
            name='body',
            field=wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StreamBlock([('color_section', wagtail.core.blocks.StructBlock([('color', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'Bela'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('pink', 'Roza')], label='Barva')), ('body', wagtail.core.blocks.StreamBlock([('headline', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.TextBlock(label='Opis', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Slika', required=False))], icon='title', label='Naslov', template='home/blocks/headline.html')), ('badge', wagtail.core.blocks.StructBlock([('line_one', wagtail.core.blocks.CharBlock(label='Prva vrstica', required=False)), ('line_two', wagtail.core.blocks.CharBlock(label='Druga vrstica', required=False))], icon='pick', label='Značka', template='home/blocks/badge.html')), ('rich_text', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(label='Besedilo')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Tabela', template='home/blocks/table.html'))], icon='pilcrow', label='Obogateno besedilo', template='home/blocks/rich_text.html'))]))])), ('scrolling_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(label='Besedilo'))], icon='horizontalrule', label='Drsna pasica', template='home/blocks/scrolling_banner.html'))]))], default='', verbose_name='Vsebina'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StreamBlock([('color_section', wagtail.core.blocks.StructBlock([('color', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'Bela'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('pink', 'Roza')], label='Barva')), ('body', wagtail.core.blocks.StreamBlock([('headline', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.TextBlock(label='Opis', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Slika', required=False))], icon='title', label='Naslov', template='home/blocks/headline.html')), ('badge', wagtail.core.blocks.StructBlock([('line_one', wagtail.core.blocks.CharBlock(label='Prva vrstica', required=False)), ('line_two', wagtail.core.blocks.CharBlock(label='Druga vrstica', required=False))], icon='pick', label='Značka', template='home/blocks/badge.html')), ('rich_text', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(label='Besedilo')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Tabela', template='home/blocks/table.html'))], icon='pilcrow', label='Obogateno besedilo', template='home/blocks/rich_text.html'))]))])), ('scrolling_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(label='Besedilo'))], icon='horizontalrule', label='Drsna pasica', template='home/blocks/scrolling_banner.html'))]))], default='', verbose_name='Vsebina'),
        ),
        migrations.DeleteModel(
            name='GlobalSiteSettings',
        ),
    ]
