from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils import models  as model_utils_models


class Holiday(model_utils_models.TimeStampedModel):
    COUNTRY_CHOICES = Choices(
        (1, 'thailand', _('Thailand')),
        (2, 'south_korea', _('South Korea')),
        (3, 'japan', _('Japan')),
        (4, 'china', _('China')),
    )

    title = models.CharField(
        verbose_name=_('Holiday name'),
        max_length=255,
    )

    holiday = models.DateField(
        verbose_name=_('Holiday date'),
        db_index=True,
    )

    country = models.IntegerField(
        verbose_name=_('Country code'),
        choices=COUNTRY_CHOICES,
        default=COUNTRY_CHOICES.thailand,
        db_index=True,
    )

    class Meta:
        verbose_name = _('Holiday')
        verbose_name_plural = _('Holidays')

        unique_together = ('holiday', 'country')

    def __str__(self):
        return '{} {} {}'.format(self.title, self.holiday, self.country)


class GolfClub(model_utils_models.TimeStampedModel):
    HOLE_CHOICES = Choices(
        (0, 'eighteen', _('18 Holes')),
        (1, 'nine', _('9 Holes')),
        (2, 'twentyseven', _('27 Holes')),
        (3, 'thirtysix', _('36 Holes')),
    )

    COUNTRY_CHOICES = Choices(
        (1, 'thailand', _('Thailand')),
        (2, 'south_korea', _('South Korea')),
        (3, 'japan', _('Japan')),
        (4, 'china', _('China')),
    )

    title = models.CharField(
        verbose_name=_('Golf club name'),
        max_length=255,
    )

    phone = models.CharField(
        verbose_name=_('Phone number'),
        max_length=16,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=255,
        blank=True,
        null=True,
    )

    website = models.URLField(
        verbose_name=_('Website'),
        max_length=255,
        blank=True,
        null=True,
    )

    hole = models.IntegerField(
        verbose_name=_('No. of holes'),
        choices=HOLE_CHOICES,
        default=HOLE_CHOICES.eighteen,
        db_index=True,
    )

    cart_fee = models.DecimalField(
        verbose_name=_('Cart fee'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
    )

    caddie_fee = models.DecimalField(
        verbose_name=_('Caddie fee'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
    )

    high_season = models.IntegerField(
        verbose_name=_('High season'),
        default=0x0C03,  # b'110000000011'
    )

    max_high_weekday = models.PositiveIntegerField(
        verbose_name=_('Max # of High/Weekday'),
        default=0,
    )

    max_high_weekend = models.PositiveIntegerField(
        verbose_name=_('Max # of High/Weekend'),
        default=0,
    )

    max_low_weekday = models.PositiveIntegerField(
        verbose_name=_('Max # of Low/Weekday'),
        default=0,
    )

    max_low_weekend = models.PositiveIntegerField(
        verbose_name=_('Max # of Low/Weekend'),
        default=0,
    )

    country = models.IntegerField(
        verbose_name=_('Country code'),
        choices=COUNTRY_CHOICES,
        default=COUNTRY_CHOICES.thailand,
        db_index=True,
    )

    class Meta:
        verbose_name = _('Golf club')
        verbose_name_plural = _('Golf clubs')

    def __str__(self):
        return '{} {} {}'.format(self.title, self.email, self.phone)
