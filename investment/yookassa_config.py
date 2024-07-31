from yookassa import Configuration, Settings

# Using Test data
Configuration.account_id = '431418'
Configuration.secret_key = 'test_uzaD6i1xSVuYRAe_aHCDS9Ns0sfFbmkcYFHEdGpfw2Y'

m = Settings.get_account_settings()

# print(dict(m))

# {
# 'account_id': '430271',
# 'fiscalization_enabled': False,
# 'payment_methods': ['yoo_money', 'bank_card'],
# 'status': 'enabled',
# 'test': True
# }


