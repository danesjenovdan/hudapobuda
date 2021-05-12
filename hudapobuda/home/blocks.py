from django.utils.translation import gettext_lazy as _
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ExternalLinkBlock(blocks.StructBlock):
    style = blocks.ChoiceBlock(
        choices=[
            ('plain', 'Navaden'),
            ('button', 'Gumb'),
        ],
        label=_('Stil povezave'),
    )
    name = blocks.CharBlock(label=_('Ime'))
    url = blocks.URLBlock(label=_('Povezava'))

    class Meta:
        label = _('Zunanja povezava')
        icon = 'link'


class PageLinkBlock(blocks.StructBlock):
    style = blocks.ChoiceBlock(
        choices=[
            ('plain', 'Navaden'),
            ('button', 'Gumb'),
        ],
        label=_('Stil povezave'),
    )
    name = blocks.CharBlock(required=False, label=_('Ime'), help_text=_('Če je prazno se uporabi naslov strani.'))
    page = blocks.PageChooserBlock(label=_('Stran'))

    class Meta:
        label = _('Povezava do strani')
        icon = 'link'


class ContentBlock(blocks.StreamBlock):
    headline = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('description', blocks.TextBlock(required=False, label=_('Opis'))),
            ('image', ImageChooserBlock(required=False, label=_('Slika'))),
        ],
        label=_('Naslov'),
        template='home/blocks/headline.html',
        icon='title',
    )
    badge = blocks.StructBlock(
        [
            ('line_one', blocks.CharBlock(required=False, label=_('Prva vrstica'))),
            ('line_two', blocks.CharBlock(required=False, label=_('Druga vrstica'))),
        ],
        label=_('Značka'),
        template='home/blocks/badge.html',
        icon='pick',
    )
    rich_text = blocks.StreamBlock(
        [
            ('text', blocks.RichTextBlock(
                label=_('Besedilo'),
            )),
            ('table', TableBlock(
                label=_('Tabela'),
                template='home/blocks/table.html',
            )),
        ],
        label=_('Obogateno besedilo'),
        template='home/blocks/rich_text.html',
        icon='pilcrow',
    )
    share = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('facebook', blocks.URLBlock(label=_('Facebook'))),
            ('twitter', blocks.URLBlock(label=_('Twitter'))),
            ('mail', blocks.EmailBlock(label=_('Mail'))),
        ],
        label=_('Deli'),
        template='home/blocks/share.html',
        icon='title',
    )
    newsletter = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('description', blocks.CharBlock(label=_('Opis'))),
        ],
        label=_('Newsletter'),
        template='home/blocks/newsletter.html',
        icon='title',
    )
    triple_cards  = blocks.StructBlock(
         [
             ('title1', blocks.CharBlock(label=_('Naslov 1'))),
             ('description1', blocks.CharBlock(required=False, label=_('Opis 1'))),
             ('image1', ImageChooserBlock(label=_('Ikona 1'))),
             ('title2', blocks.CharBlock(label=_('Naslov 2'))),
             ('description2', blocks.CharBlock(required=False, label=_('Opis 2'))),
             ('image2', ImageChooserBlock(label=_('Ikona 2'))),
             ('title3', blocks.CharBlock(label=_('Naslov 3'))),
             ('description3', blocks.CharBlock(required=False, label=_('Opis 3'))),
             ('image3', ImageChooserBlock(label=_('Ikona 3'))),
         ],
         label=_('Tri kartice'),
         template='home/blocks/triple_cards.html',
         icon='title',
     )

    class Meta:
        label = _('Vsebina')
        icon = 'snippet'


class FormContentBlock(ContentBlock):
    form = blocks.StaticBlock(
        admin_text='Tukaj se bo vstavil obrazec, ki se ga lahko ureja spodaj.',
        label=_('Obrazec'),
        template='home/blocks/form.html',
        icon='form',
    )


class ColorSectionBlock(blocks.StructBlock):
    color = blocks.ChoiceBlock(
        choices=[
            ('white', 'Bela'),
            ('blue', 'Modra'),
            ('yellow', 'Rumena'),
            ('pink', 'Roza'),
        ],
        label=_('Barva'),
    )
    body = ContentBlock()

    class Meta:
        label = _('Vsebinski odsek z barvo')
        template = 'home/blocks/color_section.html'
        icon = 'snippet'


class FormColorSectionBlock(ColorSectionBlock):
    body = FormContentBlock()


class SectionBlock(blocks.StreamBlock):
    color_section = ColorSectionBlock()
    scrolling_banner = blocks.StructBlock(
        [('text', blocks.TextBlock(label=_('Besedilo')))],
        label=_('Drsna pasica'),
        template='home/blocks/scrolling_banner.html',
        icon='horizontalrule',
    )

    class Meta:
        label = _('Vsebinski odsek')
        template = 'home/blocks/section.html'
        icon = 'snippet'


class FormSectionBlock(SectionBlock):
    color_section = FormColorSectionBlock()
