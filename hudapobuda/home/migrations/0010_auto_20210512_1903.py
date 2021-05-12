# Generated by Django 3.1.10 on 2021-05-12 17:03

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0009_auto_20210507_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StreamBlock([('color_section', wagtail.core.blocks.StructBlock([('color', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'Bela'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('pink', 'Roza')], label='Barva')), ('body', wagtail.core.blocks.StreamBlock([('headline', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.TextBlock(label='Opis', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Slika', required=False))], icon='title', label='Naslov', template='home/blocks/headline.html')), ('badge', wagtail.core.blocks.StructBlock([('line_one', wagtail.core.blocks.CharBlock(label='Prva vrstica', required=False)), ('line_two', wagtail.core.blocks.CharBlock(label='Druga vrstica', required=False))], icon='pick', label='Značka', template='home/blocks/badge.html')), ('rich_text', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(label='Besedilo')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Tabela', template='home/blocks/table.html'))], icon='pilcrow', label='Obogateno besedilo', template='home/blocks/rich_text.html')), ('share', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('facebook', wagtail.core.blocks.URLBlock(label='Facebook')), ('twitter', wagtail.core.blocks.URLBlock(label='Twitter')), ('mail', wagtail.core.blocks.EmailBlock(label='Mail'))], icon='title', label='Gumbi za deljenje', template='home/blocks/share.html')), ('newsletter', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.CharBlock(label='Opis'))], icon='title', label='Newsletter', template='home/blocks/newsletter.html')), ('double_cards', wagtail.core.blocks.StructBlock([('text1', wagtail.core.blocks.CharBlock(label='Besedilo 1')), ('image1', wagtail.images.blocks.ImageChooserBlock(label='Ikona 1')), ('text2', wagtail.core.blocks.CharBlock(label='Besedilo 2')), ('image2', wagtail.images.blocks.ImageChooserBlock(label='Ikona 2'))], icon='title', label='Dve kartici', template='home/blocks/double_cards.html')), ('triple_cards', wagtail.core.blocks.StructBlock([('title_big1', wagtail.core.blocks.CharBlock(label='Naslov - velik 1', required=False)), ('title_small1', wagtail.core.blocks.CharBlock(label='Naslov - mali 1', required=False)), ('description1', wagtail.core.blocks.CharBlock(label='Opis 1', required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(label='Ikona 1')), ('title_big2', wagtail.core.blocks.CharBlock(label='Naslov - velik 2', required=False)), ('title_small2', wagtail.core.blocks.CharBlock(label='Naslov - mali 2', required=False)), ('description2', wagtail.core.blocks.CharBlock(label='Opis 2', required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(label='Ikona 2')), ('title_big3', wagtail.core.blocks.CharBlock(label='Naslov - velik 3', required=False)), ('title_small3', wagtail.core.blocks.CharBlock(label='Naslov - mali 3', required=False)), ('description3', wagtail.core.blocks.CharBlock(label='Opis 3', required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(label='Ikona 3'))], icon='title', label='Tri kartice', template='home/blocks/triple_cards.html')), ('button_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Če je prazno se uporabi naslov strani (pri zunanji povezavi pa je obvezno).', label='Besedilo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(label='Povezava do strani', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Če je prazno se uporabi povezava do strani.', label='Zunanja povezava', required=False))], icon='title', label='Gumb za preusmeritev', template='home/blocks/button_banner.html')), ('list', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Element')))], icon='title', label='Seznam', template='home/blocks/list.html')), ('form', wagtail.core.blocks.static_block.StaticBlock(admin_text='Tukaj se bo vstavil obrazec, ki se ga lahko ureja spodaj.', icon='form', label='Obrazec', template='home/blocks/form.html'))]))])), ('scrolling_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(label='Besedilo'))], icon='horizontalrule', label='Drsna pasica', template='home/blocks/scrolling_banner.html'))]))], default='', verbose_name='Vsebina')),
                ('landing_body', wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StreamBlock([('color_section', wagtail.core.blocks.StructBlock([('color', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'Bela'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('pink', 'Roza')], label='Barva')), ('body', wagtail.core.blocks.StreamBlock([('headline', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.TextBlock(label='Opis', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Slika', required=False))], icon='title', label='Naslov', template='home/blocks/headline.html')), ('badge', wagtail.core.blocks.StructBlock([('line_one', wagtail.core.blocks.CharBlock(label='Prva vrstica', required=False)), ('line_two', wagtail.core.blocks.CharBlock(label='Druga vrstica', required=False))], icon='pick', label='Značka', template='home/blocks/badge.html')), ('rich_text', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(label='Besedilo')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Tabela', template='home/blocks/table.html'))], icon='pilcrow', label='Obogateno besedilo', template='home/blocks/rich_text.html')), ('share', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('facebook', wagtail.core.blocks.URLBlock(label='Facebook')), ('twitter', wagtail.core.blocks.URLBlock(label='Twitter')), ('mail', wagtail.core.blocks.EmailBlock(label='Mail'))], icon='title', label='Gumbi za deljenje', template='home/blocks/share.html')), ('newsletter', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.CharBlock(label='Opis'))], icon='title', label='Newsletter', template='home/blocks/newsletter.html')), ('double_cards', wagtail.core.blocks.StructBlock([('text1', wagtail.core.blocks.CharBlock(label='Besedilo 1')), ('image1', wagtail.images.blocks.ImageChooserBlock(label='Ikona 1')), ('text2', wagtail.core.blocks.CharBlock(label='Besedilo 2')), ('image2', wagtail.images.blocks.ImageChooserBlock(label='Ikona 2'))], icon='title', label='Dve kartici', template='home/blocks/double_cards.html')), ('triple_cards', wagtail.core.blocks.StructBlock([('title_big1', wagtail.core.blocks.CharBlock(label='Naslov - velik 1', required=False)), ('title_small1', wagtail.core.blocks.CharBlock(label='Naslov - mali 1', required=False)), ('description1', wagtail.core.blocks.CharBlock(label='Opis 1', required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(label='Ikona 1')), ('title_big2', wagtail.core.blocks.CharBlock(label='Naslov - velik 2', required=False)), ('title_small2', wagtail.core.blocks.CharBlock(label='Naslov - mali 2', required=False)), ('description2', wagtail.core.blocks.CharBlock(label='Opis 2', required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(label='Ikona 2')), ('title_big3', wagtail.core.blocks.CharBlock(label='Naslov - velik 3', required=False)), ('title_small3', wagtail.core.blocks.CharBlock(label='Naslov - mali 3', required=False)), ('description3', wagtail.core.blocks.CharBlock(label='Opis 3', required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(label='Ikona 3'))], icon='title', label='Tri kartice', template='home/blocks/triple_cards.html')), ('button_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Če je prazno se uporabi naslov strani (pri zunanji povezavi pa je obvezno).', label='Besedilo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(label='Povezava do strani', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Če je prazno se uporabi povezava do strani.', label='Zunanja povezava', required=False))], icon='title', label='Gumb za preusmeritev', template='home/blocks/button_banner.html')), ('list', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Element')))], icon='title', label='Seznam', template='home/blocks/list.html'))]))])), ('scrolling_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(label='Besedilo'))], icon='horizontalrule', label='Drsna pasica', template='home/blocks/scrolling_banner.html'))]))], default='', verbose_name='Vsebina po oddaji obrazca')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StreamBlock([('color_section', wagtail.core.blocks.StructBlock([('color', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'Bela'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('pink', 'Roza')], label='Barva')), ('body', wagtail.core.blocks.StreamBlock([('headline', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.TextBlock(label='Opis', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Slika', required=False))], icon='title', label='Naslov', template='home/blocks/headline.html')), ('badge', wagtail.core.blocks.StructBlock([('line_one', wagtail.core.blocks.CharBlock(label='Prva vrstica', required=False)), ('line_two', wagtail.core.blocks.CharBlock(label='Druga vrstica', required=False))], icon='pick', label='Značka', template='home/blocks/badge.html')), ('rich_text', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(label='Besedilo')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Tabela', template='home/blocks/table.html'))], icon='pilcrow', label='Obogateno besedilo', template='home/blocks/rich_text.html')), ('share', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('facebook', wagtail.core.blocks.URLBlock(label='Facebook')), ('twitter', wagtail.core.blocks.URLBlock(label='Twitter')), ('mail', wagtail.core.blocks.EmailBlock(label='Mail'))], icon='title', label='Gumbi za deljenje', template='home/blocks/share.html')), ('newsletter', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.CharBlock(label='Opis'))], icon='title', label='Newsletter', template='home/blocks/newsletter.html')), ('double_cards', wagtail.core.blocks.StructBlock([('text1', wagtail.core.blocks.CharBlock(label='Besedilo 1')), ('image1', wagtail.images.blocks.ImageChooserBlock(label='Ikona 1')), ('text2', wagtail.core.blocks.CharBlock(label='Besedilo 2')), ('image2', wagtail.images.blocks.ImageChooserBlock(label='Ikona 2'))], icon='title', label='Dve kartici', template='home/blocks/double_cards.html')), ('triple_cards', wagtail.core.blocks.StructBlock([('title_big1', wagtail.core.blocks.CharBlock(label='Naslov - velik 1', required=False)), ('title_small1', wagtail.core.blocks.CharBlock(label='Naslov - mali 1', required=False)), ('description1', wagtail.core.blocks.CharBlock(label='Opis 1', required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(label='Ikona 1')), ('title_big2', wagtail.core.blocks.CharBlock(label='Naslov - velik 2', required=False)), ('title_small2', wagtail.core.blocks.CharBlock(label='Naslov - mali 2', required=False)), ('description2', wagtail.core.blocks.CharBlock(label='Opis 2', required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(label='Ikona 2')), ('title_big3', wagtail.core.blocks.CharBlock(label='Naslov - velik 3', required=False)), ('title_small3', wagtail.core.blocks.CharBlock(label='Naslov - mali 3', required=False)), ('description3', wagtail.core.blocks.CharBlock(label='Opis 3', required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(label='Ikona 3'))], icon='title', label='Tri kartice', template='home/blocks/triple_cards.html')), ('button_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Če je prazno se uporabi naslov strani (pri zunanji povezavi pa je obvezno).', label='Besedilo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(label='Povezava do strani', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Če je prazno se uporabi povezava do strani.', label='Zunanja povezava', required=False))], icon='title', label='Gumb za preusmeritev', template='home/blocks/button_banner.html')), ('list', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Element')))], icon='title', label='Seznam', template='home/blocks/list.html'))]))])), ('scrolling_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(label='Besedilo'))], icon='horizontalrule', label='Drsna pasica', template='home/blocks/scrolling_banner.html'))]))], default='', verbose_name='Vsebina'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StreamBlock([('color_section', wagtail.core.blocks.StructBlock([('color', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'Bela'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('pink', 'Roza')], label='Barva')), ('body', wagtail.core.blocks.StreamBlock([('headline', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.TextBlock(label='Opis', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Slika', required=False))], icon='title', label='Naslov', template='home/blocks/headline.html')), ('badge', wagtail.core.blocks.StructBlock([('line_one', wagtail.core.blocks.CharBlock(label='Prva vrstica', required=False)), ('line_two', wagtail.core.blocks.CharBlock(label='Druga vrstica', required=False))], icon='pick', label='Značka', template='home/blocks/badge.html')), ('rich_text', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(label='Besedilo')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Tabela', template='home/blocks/table.html'))], icon='pilcrow', label='Obogateno besedilo', template='home/blocks/rich_text.html')), ('share', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('facebook', wagtail.core.blocks.URLBlock(label='Facebook')), ('twitter', wagtail.core.blocks.URLBlock(label='Twitter')), ('mail', wagtail.core.blocks.EmailBlock(label='Mail'))], icon='title', label='Gumbi za deljenje', template='home/blocks/share.html')), ('newsletter', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.CharBlock(label='Opis'))], icon='title', label='Newsletter', template='home/blocks/newsletter.html')), ('double_cards', wagtail.core.blocks.StructBlock([('text1', wagtail.core.blocks.CharBlock(label='Besedilo 1')), ('image1', wagtail.images.blocks.ImageChooserBlock(label='Ikona 1')), ('text2', wagtail.core.blocks.CharBlock(label='Besedilo 2')), ('image2', wagtail.images.blocks.ImageChooserBlock(label='Ikona 2'))], icon='title', label='Dve kartici', template='home/blocks/double_cards.html')), ('triple_cards', wagtail.core.blocks.StructBlock([('title_big1', wagtail.core.blocks.CharBlock(label='Naslov - velik 1', required=False)), ('title_small1', wagtail.core.blocks.CharBlock(label='Naslov - mali 1', required=False)), ('description1', wagtail.core.blocks.CharBlock(label='Opis 1', required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(label='Ikona 1')), ('title_big2', wagtail.core.blocks.CharBlock(label='Naslov - velik 2', required=False)), ('title_small2', wagtail.core.blocks.CharBlock(label='Naslov - mali 2', required=False)), ('description2', wagtail.core.blocks.CharBlock(label='Opis 2', required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(label='Ikona 2')), ('title_big3', wagtail.core.blocks.CharBlock(label='Naslov - velik 3', required=False)), ('title_small3', wagtail.core.blocks.CharBlock(label='Naslov - mali 3', required=False)), ('description3', wagtail.core.blocks.CharBlock(label='Opis 3', required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(label='Ikona 3'))], icon='title', label='Tri kartice', template='home/blocks/triple_cards.html')), ('button_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Če je prazno se uporabi naslov strani (pri zunanji povezavi pa je obvezno).', label='Besedilo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(label='Povezava do strani', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Če je prazno se uporabi povezava do strani.', label='Zunanja povezava', required=False))], icon='title', label='Gumb za preusmeritev', template='home/blocks/button_banner.html')), ('list', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Element')))], icon='title', label='Seznam', template='home/blocks/list.html'))]))])), ('scrolling_banner', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(label='Besedilo'))], icon='horizontalrule', label='Drsna pasica', template='home/blocks/scrolling_banner.html'))]))], default='', verbose_name='Vsebina'),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.formpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]