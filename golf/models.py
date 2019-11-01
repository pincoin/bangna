import uuid

from django.conf import settings
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

    code = models.CharField(
        verbose_name=_('Golf club code'),
        max_length=255,
        unique=True,
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


class Booking(model_utils_models.SoftDeletableModel, model_utils_models.TimeStampedModel):
    SEASON_CHOICES = Choices(
        (0, 'low', _('Low season')),
        (1, 'high', _('High season')),
    )

    DAY_CHOICES = Choices(
        (0, 'weekday', _('Weekday')),
        (1, 'weekend', _('Weekend')),
    )

    SLOT_CHOICES = Choices(
        (0, 'morning', _('Morning')),
        (1, 'daytime', _('Daytime')),
        (2, 'twilight', _('Twilight')),
        (3, 'night', _('Night')),
    )

    HOLE_CHOICES = Choices(
        (0, 'eighteen', _('18 Holes')),
        (1, 'nine', _('9 Holes')),
        (2, 'twentyseven', _('27 Holes')),
        (3, 'thirtysix', _('36 Holes')),
    )

    STATUS_CHOICES = Choices(
        (0, 'order_opened', _('order opened')),
        (1, 'order_pending', _('order pending')),
        (2, 'payment_pending', _('payment pending')),
        (3, 'completed', _('order complete')),
        (4, 'offered', _('order offered')),
        (5, 'voided', _('order voided')),
        (6, 'refund_requested', _('refund requested')),
        (7, 'refund_pending', _('refund pending')),
        (8, 'refunded1', _('order refunded(original)')),  # original order
        (9, 'refunded2', _('order refunded(reverse)')),  # refund order
    )

    booking_uuid = models.UUIDField(
        verbose_name=_('UUID'),
        unique=True,
        default=uuid.uuid4,
        editable=False
    )

    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Requester'),
        db_index=True,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    round_date = models.DateField(
        verbose_name=_('Round day'),
        db_index=True,
    )

    pax = models.IntegerField(
        verbose_name=_('Pax'),
        default=4,
    )

    hole = models.IntegerField(
        verbose_name=_('No. of holes'),
        choices=HOLE_CHOICES,
        default=HOLE_CHOICES.eighteen,
        db_index=True,
    )

    green_fee_sales = models.DecimalField(
        verbose_name=_('Green fee sales'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
    )

    cart_fee_sales = models.DecimalField(
        verbose_name=_('Cart fee sales'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
    )

    caddie_fee_sales = models.DecimalField(
        verbose_name=_('Caddie fee sales'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
    )

    green_fee_pay_on_arrival = models.BooleanField(
        verbose_name=_('Green fee pay on arrival'),
        default=False,
        db_index=True,
    )

    cart_fee_pay_on_arrival = models.BooleanField(
        verbose_name=_('Cart fee pay on arrival'),
        default=False,
        db_index=True,
    )

    caddie_fee_pay_on_arrival = models.BooleanField(
        verbose_name=_('Caddie fee pay on arrival'),
        default=False,
        db_index=True,
    )

    green_fee_cost = models.DecimalField(
        verbose_name=_('Green fee cost'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
    )

    cart_fee_cost = models.DecimalField(
        verbose_name=_('Cart fee cost'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
    )

    cart_fee_deducted_from_deposit = models.IntegerField(
        verbose_name=_('Cart fee deducted from deposit'),
        default=0,
    )

    caddie_fee_cost = models.DecimalField(
        verbose_name=_('Caddie fee cost'),
        max_digits=11,
        decimal_places=2,
        help_text=_('THB'),
    )

    first_name = models.CharField(
        verbose_name=_('First name'),
        max_length=255,
    )

    last_name = models.CharField(
        verbose_name=_('Last name'),
        max_length=255,
    )

    fullname = models.CharField(
        verbose_name=_('Full name'),
        max_length=255,
    )

    memo = models.TextField(
        verbose_name=_('Memo'),
        blank=True,
        null=True,
    )

    season = models.IntegerField(
        verbose_name=_('High/Low Season'),
        choices=SEASON_CHOICES,
        default=SEASON_CHOICES.high,
        db_index=True,
    )

    day_of_week = models.IntegerField(
        verbose_name=_('Day of week'),
        choices=DAY_CHOICES,
        default=DAY_CHOICES.weekday,
        db_index=True,
    )

    slot = models.IntegerField(
        verbose_name=_('Time slot'),
        choices=SLOT_CHOICES,
        default=SLOT_CHOICES.morning,
        db_index=True,
    )

    status = models.IntegerField(
        verbose_name=_('Booking status'),
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES.order_opened,
        db_index=True,
    )

    class Meta:
        verbose_name = _('Booking')
        verbose_name_plural = _('Booking')

    def __str__(self):
        return '{}-{} {}'.format(self.booking_uuid, self.first_name, self.last_name)


class BookingTeeOff(model_utils_models.SoftDeletableModel, model_utils_models.TimeStampedModel):
    booking = models.ForeignKey(
        'golf.Booking',
        verbose_name=_('Booking'),
        db_index=True,
        on_delete=models.CASCADE,
    )

    tee_off_time = models.TimeField(
        verbose_name=_('Tee off time'),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Booking tee-off')
        verbose_name_plural = _('Booking tee-off')

    def __str__(self):
        return 'booking - {} / tee off - {}'.format(
            self.booking.booking_uuid, self.tee_off_time
        )
