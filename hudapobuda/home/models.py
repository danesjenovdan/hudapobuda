import sys

import requests
from django import forms
from django.conf import settings
from django.db import models
from django.forms import fields, widgets
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel, ObjectList,
                                         StreamFieldPanel, TabbedInterface)
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.contrib.forms.models import (FORM_FIELD_CHOICES, AbstractForm,
                                          AbstractFormField)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from .blocks import (ExternalLinkBlock, FormSectionBlock, PageLinkBlock,
                     SectionBlock)


@register_setting(icon='cog')
class MetaSettings(BaseSetting):
    header_links = StreamField([
        ('page_link', PageLinkBlock()),
        ('external_link', ExternalLinkBlock()),
    ])

    link_tab_panels = [
        StreamFieldPanel('header_links'),
    ]

    facebook = models.URLField(
        null=True,
        blank=True,
    )
    twitter = models.URLField(
        null=True,
        blank=True,
    )
    instagram = models.URLField(
        null=True,
        blank=True,
    )
    youtube = models.URLField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )

    social_tab_panels = [
        FieldPanel('facebook'),
        FieldPanel('twitter'),
        FieldPanel('instagram'),
        FieldPanel('youtube'),
        FieldPanel('email'),
    ]

    meta_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    meta_description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    meta_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    meta_tab_panels = [
        FieldPanel('meta_title'),
        FieldPanel('meta_description'),
        ImageChooserPanel('meta_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(link_tab_panels, heading='Seznam povezav'),
        ObjectList(social_tab_panels, heading='Socialna omrežja'),
        ObjectList(meta_tab_panels, heading='Meta opisi'),
    ])

    class Meta:
        verbose_name = 'Meta nastavitve'


class HomePage(Page):
    subtitle = models.CharField(
        verbose_name=_('Podnaslov'),
        max_length=255,
        null=True,
        blank=True,
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Slika'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body = StreamField(
        [('section', SectionBlock())],
        verbose_name=_('Vsebina'),
        default='',
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = []


class ContentPage(Page):
    body = StreamField(
        [('section', SectionBlock())],
        verbose_name=_('Vsebina'),
        default='',
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class StaticHeading(forms.Widget):
    pass


class CustomFormBuilder(FormBuilder):
    def create_static_heading_field(self, field, options):
        options['required'] = False
        print(options)
        return forms.CharField(widget=StaticHeading, **options)


class FormField(AbstractFormField):
    # extend the built in field type choices
    CHOICES = FORM_FIELD_CHOICES + (('static_heading', 'Statični naslov'),)
    # override the field_type field with extended choices
    field_type = models.CharField(verbose_name=_('field type'), max_length=16, choices=CHOICES)

    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractForm):
    body = StreamField(
        [('section', FormSectionBlock())],
        verbose_name=_('Vsebina'),
        default='',
    )
    landing_body = StreamField(
        [('section', SectionBlock())],
        verbose_name=_('Vsebina po oddaji obrazca'),
        default='',
    )

    content_panels = AbstractForm.content_panels + [
        StreamFieldPanel('body'),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label=_('Polja obrazca')),
        StreamFieldPanel('landing_body'),
    ]

    form_builder = CustomFormBuilder

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for name, field in form.fields.items():
            # add type to widget for template to access
            setattr(field.widget, 'widget_type', field.widget.__class__.__name__)

            if form.is_bound and form.errors.get(name, None):
                css_classes = field.widget.attrs.get('class', '').split()
                css_classes.append('is-invalid')
                field.widget.attrs.update({'class': ' '.join(css_classes)})

            if isinstance(field.widget, (widgets.TextInput, widgets.Textarea, widgets.NumberInput, widgets.EmailInput)):
                css_classes = field.widget.attrs.get('class', '').split()
                css_classes.append('form-control')
                field.widget.attrs.update({'class': ' '.join(css_classes)})

            if isinstance(field.widget, widgets.Textarea):
                field.widget.attrs.pop('cols', None)
                field.widget.attrs.update({'rows': '6'})

            if isinstance(field.widget, (widgets.CheckboxInput, widgets.CheckboxSelectMultiple, widgets.RadioSelect)):
                css_classes = field.widget.attrs.get('class', '').split()
                css_classes.append('form-check-input')
                field.widget.attrs.update({'class': ' '.join(css_classes)})

        return form

    def process_form_submission(self, form):
        submission = super().process_form_submission(form)

        email_field_name = None
        for name, field in form.fields.items():
            if isinstance(field, fields.EmailField):
                email_field_name = name
                break

        email = None
        if email_field_name:
            email = submission.get_data().get(email_field_name, None)

        if email and settings.PODPRI_SEND_EMAIL_TOKEN:
            try:
                response = requests.post(
                    'https://podpri.djnd.si/api/send-email/',
                    data={
                        'email': email,
                        'email_template_id': 515,
                    },
                    headers={
                        'Authorization': settings.PODPRI_SEND_EMAIL_TOKEN,
                    }
                )
                if response.status_code != requests.codes.ok:
                    print(f'SEND MAIL FAILED. status_code={response.status_code}')
            except:
                print(f'SEND MAIL FAILED. exception={sys.exc_info()[0]}')

        return submission
