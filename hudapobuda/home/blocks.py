from django.utils.translation import gettext_lazy as _
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


DONATION_IDS = [
    (6, '6 - Pušča, na pomoč'),
    (7, '7 - Skupnostni studio, glas skupnosti'),
    (8, '8 - Zapišimo spomine')
]

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
            ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
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
            ('color', blocks.ChoiceBlock(
                choices=[
                    ('white', 'Bela'),
                    ('blue', 'Modra'),
                ],
                label=_('Barva'))
            ),
            ('position', blocks.ChoiceBlock(
                choices=[
                    ('left', 'Leva'),
                    ('center', 'Sredinska'),
                    ('right', 'Desna'),
                ],
                label=_('Poravnava'))
            ),
        ],
        label=_('Značka'),
        template='home/blocks/badge.html',
        icon='pick',
    )
    rich_text = blocks.StructBlock(
        [
            ('position', blocks.ChoiceBlock(
                choices=[
                    ('left', 'Leva'),
                    ('center', 'Sredinska'),
                    ('right', 'Desna'),
                ],
                label=_('Poravnava')
            )),
            ('aligned_text', blocks.StreamBlock(
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
        label=_('Gumbi za deljenje'),
        template='home/blocks/share.html',
        icon='title',
    )
    newsletter = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('description', blocks.CharBlock(label=_('Opis'))),
            ('checkbox_text', blocks.CharBlock(label=_('Checkbox tekst'))),
        ],
        label=_('Novičnik'),
        template='home/blocks/newsletter.html',
        icon='title',
    )
    double_cards  = blocks.StructBlock(
        [
            ('text1', blocks.CharBlock(label=_('Besedilo 1'))),
            ('image1', ImageChooserBlock(label=_('Ikona 1'))),
            ('text2', blocks.CharBlock(label=_('Besedilo 2'))),
            ('image2', ImageChooserBlock(label=_('Ikona 2'))),
        ],
        label=_('Dve kartici'),
        template='home/blocks/double_cards.html',
        icon='title',
    )
    triple_cards  = blocks.StructBlock(
        [
            ('title_big1', blocks.CharBlock(required=False, label=_('Naslov - velik 1'))),
            ('title_small1', blocks.CharBlock(required=False, label=_('Naslov - mali 1'))),
            ('description1', blocks.CharBlock(required=False, label=_('Opis 1'))),
            ('image1', ImageChooserBlock(label=_('Ikona 1'))),
            ('title_big2', blocks.CharBlock(required=False, label=_('Naslov - velik 2'))),
            ('title_small2', blocks.CharBlock(required=False, label=_('Naslov - mali 2'))),
            ('description2', blocks.CharBlock(required=False, label=_('Opis 2'))),
            ('image2', ImageChooserBlock(label=_('Ikona 2'))),
            ('title_big3', blocks.CharBlock(required=False, label=_('Naslov - velik 3'))),
            ('title_small3', blocks.CharBlock(required=False, label=_('Naslov - mali 3'))),
            ('description3', blocks.CharBlock(required=False, label=_('Opis 3'))),
            ('image3', ImageChooserBlock(label=_('Ikona 3'))),
        ],
        label=_('Tri kartice'),
        template='home/blocks/triple_cards.html',
        icon='title',
    )
    button_banner = blocks.StructBlock(
        [
            ('text', blocks.CharBlock(
                required=False,
                label=_('Besedilo'),
                help_text=_('Če je prazno se uporabi naslov strani (pri zunanji povezavi pa je obvezno).'),
            )),
            ('page', blocks.PageChooserBlock(
                required=False,
                label=_('Povezava do strani'),
            )),
            ('url', blocks.URLBlock(
                required=False,
                label=_('Zunanja povezava'),
                help_text=_('Če je prazno se uporabi povezava do strani.'),
            )),
        ],
        label=_('Gumb za preusmeritev'),
        template='home/blocks/button_banner.html',
        icon='title',
    )
    list = blocks.StructBlock(
        [
          ('title', blocks.CharBlock(label=_('Naslov'))),
          ('list', blocks.ListBlock(blocks.CharBlock(label=_('Element')))),
        ],
        label=_('Seznam'),
        template='home/blocks/list.html',
        icon='title',
    )
    qa_table = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('question', blocks.CharBlock(label=_('Vprašanje'))),
                ('answer', blocks.RichTextBlock(label=_('Odgovor'))),
            ],
            label=_('Vrstica'),
        ),
        label=_('Tabela z vprašanji in odgovori'),
        template='home/blocks/qa_table.html',
        icon='title',
    )
    initiative_boxes = blocks.StructBlock(
        [
            ('hide_donations', blocks.BooleanBlock(label=_('Skrij donacije?'), default=False, null=True, required=False)),
            ('card1', blocks.StructBlock([
                ('title', blocks.CharBlock(label=_('Ime pobude'))),
                ('page', blocks.PageChooserBlock(
                    label=_('Povezava do podstrani pobude'),
                )),
                ('image', ImageChooserBlock(label=_('Slika'))),
                ('author', blocks.CharBlock(label=_('Organizacija'))),
                ('author_url', blocks.URLBlock(
                    label=_('Povezava do organizacije'),
                )),
                ('description', blocks.CharBlock(label=_('Opis'))),
                ('button_text', blocks.CharBlock(label=_('Besedilo na gumbu'))),
                ('donation_ID', blocks.ChoiceBlock(label=_('ID donacijske kampanje'), choices=DONATION_IDS, required=True)),
            ],
            label=_('Prva kartica'),
            )),
            ('card2', blocks.StructBlock([
                ('title', blocks.CharBlock(label=_('Ime pobude'))),
                ('page', blocks.PageChooserBlock(
                    label=_('Povezava do podstrani pobude'),
                )),
                ('image', ImageChooserBlock(label=_('Slika'))),
                ('author', blocks.CharBlock(label=_('Organizacija'))),
                ('author_url', blocks.URLBlock(
                    label=_('Povezava do organizacije'),
                )),
                ('description', blocks.CharBlock(label=_('Opis'))),
                ('button_text', blocks.CharBlock(label=_('Besedilo na gumbu'))),
                ('donation_ID', blocks.ChoiceBlock(label=_('ID donacijske kampanje'), choices=DONATION_IDS, required=True)),
            ],
            label=_('Druga kartica'),
            )),
            ('card3', blocks.StructBlock([
                ('title', blocks.CharBlock(label=_('Ime pobude'))),
                ('page', blocks.PageChooserBlock(
                    label=_('Povezava do podstrani pobude'),
                )),
                ('image', ImageChooserBlock(label=_('Slika'))),
                ('author', blocks.CharBlock(label=_('Organizacija'))),
                ('author_url', blocks.URLBlock(
                    label=_('Povezava do organizacije'),
                )),
                ('description', blocks.CharBlock(label=_('Opis'))),
                ('button_text', blocks.CharBlock(label=_('Besedilo na gumbu'))),
                ('donation_ID', blocks.ChoiceBlock(label=_('ID donacijske kampanje'), choices=DONATION_IDS, required=True)),
            ],
            label=_('Tretja kartica'),
            ))
        ],
        label=_('Sekcija s pobudami'),
        template='home/blocks/initiatives_section.html',
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
