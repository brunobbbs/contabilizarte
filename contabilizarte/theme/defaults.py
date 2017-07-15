from mezzanine.conf import register_setting

register_setting(
    name='SITE_TITLE',
    label='Site title',
    editable=False,
    default=u'Contabilizarte',
)

register_setting(
    name='SITE_TAGLINE',
    label='Site tagline',
    editable=False,
    default=u'Uma maneira divertida de aprender contabilidade',
)
