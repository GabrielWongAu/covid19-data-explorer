

valid_countries_names = [
    'Afghanistan', 'Albania', 'Algeria',
    'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize',
    'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana',
    'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
    'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)',
    'Congo (Kinshasa)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
    'Czech Republic', "Côte d'Ivoire", 'Denmark', 'Djibouti', 'Dominica',
    'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
    'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji',
    'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany',
    'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau',
    'Guyana', 'Haiti', 'Holy See (Vatican City State)', 'Honduras',
    'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of',
    'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
    'Kazakhstan', 'Kenya', 'Korea (South)', 'Kuwait', 'Kyrgyzstan',
    'Lao PDR', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
    'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao, SAR China',
    'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia',
    'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico',
    'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique',
    'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua',
    'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestinian Territory',
    'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland',
    'Portugal', 'Qatar', 'Republic of Kosovo', 'Romania',
    'Russian Federation', 'Rwanda', 'Réunion', 'Saint Kitts and Nevis',
    'Saint Lucia', 'Saint Vincent and Grenadines', 'San Marino',
    'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
    'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
    'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan',
    'Suriname', 'Swaziland', 'Sweden', 'Switzerland',
    'Syrian Arab Republic (Syria)', 'Taiwan, Republic of China', 'Tajikistan',
    'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo',
    'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine',
    'United Arab Emirates', 'United Kingdom', 'United States of America',
    'Uruguay', 'Uzbekistan', 'Venezuela (Bolivarian Republic)', 'Viet Nam',
    'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

valid_countries_code = [
    'AF', 'AL', 'DZ', 'AD', 'AO', 'AG', 'AR', 'AM',
    'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ',
    'BT', 'BO', 'BA', 'BW', 'BR', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM',
    'CA', 'CV', 'CF', 'TD', 'CL', 'CN', 'CO', 'KM', 'CG', 'CD', 'CR',
    'HR', 'CU', 'CY', 'CZ', 'CI', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG',
    'SV', 'GQ', 'ER', 'EE', 'ET', 'FJ', 'FI', 'FR', 'GA', 'GM', 'GE',
    'DE', 'GH', 'GR', 'GD', 'GT', 'GN', 'GW', 'GY', 'HT', 'VA', 'HN',
    'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IL', 'IT', 'JM', 'JP',
    'JO', 'KZ', 'KE', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR',
    'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML',
    'MT', 'MR', 'MU', 'MX', 'MD', 'MC', 'MN', 'ME', 'MA', 'MZ', 'MM',
    'NA', 'NP', 'NL', 'NZ', 'NI', 'NE', 'NG', 'NO', 'OM', 'PK', 'PS',
    'PA', 'PG', 'PY', 'PE', 'PH', 'PL', 'PT', 'QA', 'XK', 'RO', 'RU',
    'RW', 'RE', 'KN', 'LC', 'VC', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC',
    'SL', 'SG', 'SK', 'SI', 'SO', 'ZA', 'SS', 'ES', 'LK', 'SD', 'SR',
    'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TT',
    'TN', 'TR', 'UG', 'UK', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VE',
    'VN', 'EH', 'YE', 'ZM', 'ZW']

valid_slugs = [
    'afghanistan', 'albania', 'algeria', 'andorra', 'angola',
    'antigua-and-barbuda', 'argentina', 'armenia', 'australia', 'austria',
    'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus',
    'belgium', 'belize', 'benin', 'bhutan', 'bolivia',
    'bosnia-and-herzegovina', 'botswana', 'brazil', 'brunei',
    'bulgaria', 'burkina-faso', 'burundi', 'cambodia', 'cameroon', 'canada',
    'cape-verde', 'central-african-republic', 'chad', 'chile', 'china',
    'colombia', 'comoros', 'congo-brazzaville', 'congo-kinshasa',
    'costa-rica', 'croatia', 'cuba', 'cyprus', 'czech-republic',
    'cote-divoire', 'denmark', 'djibouti', 'dominica', 'dominican-republic',
    'ecuador', 'egypt', 'el-salvador', 'equatorial-guinea', 'eritrea',
    'estonia', 'ethiopia', 'fiji', 'finland', 'france', 'gabon',
    'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada',
    'guatemala', 'guinea', 'guinea-bissau', 'guyana', 'haiti',
    'holy-see-vatican-city-state', 'honduras', 'hungary', 'iceland', 'india',
    'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 'jamaica',
    'japan', 'jordan', 'kazakhstan', 'kenya', 'korea-south', 'kuwait',
    'kyrgyzstan', 'lao-pdr', 'latvia', 'lebanon', 'lesotho', 'liberia',
    'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'macao-sar-china',
    'macedonia', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali',
    'malta', 'mauritania', 'mauritius', 'mexico', 'moldova', 'monaco',
    'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar', 'namibia',
    'nepal', 'netherlands', 'new-zealand', 'nicaragua', 'niger', 'nigeria',
    'norway', 'oman', 'pakistan', 'palestine', 'panama', 'papua-new-guinea',
    'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar',
    'kosovo', 'romania', 'russia', 'rwanda', 'réunion',
    'saint-kitts-and-nevis', 'saint-lucia',
    'saint-vincent-and-the-grenadines',
    'san-marino', 'sao-tome-and-principe', 'saudi-arabia', 'senegal',
    'serbia', 'seychelles', 'sierra-leone', 'singapore', 'slovakia',
    'slovenia', 'somalia', 'south-africa', 'south-korea', 'south korea',
    'south-sudan', 'spain', 'sri-lanka', 'sudan', 'suriname', 'swaziland',
    'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania',
    'thailand', 'timor-leste', 'togo', 'trinidad-and-tobago', 'tunisia',
    'turkey', 'uganda', 'ukraine', 'united-arab-emirates', 'united-kingdom',
    'united kingdom', 'united-states', 'united states', 'uruguay',
    'uzbekistan', 'venezuela', 'vietnam', 'western-sahara', 'yemen',
    'zambia', 'zimbabwe']


# function to determine whether country input is a valid API request.
# country input is checked with valid_countries_names,
# valid_countries_code, valid_slugs lists.
def validate_country_input(country_name_or_code: str) -> bool:
    country_name_or_code_lower = country_name_or_code.lower()
    country_name_or_code_upper = country_name_or_code.upper()

    if (country_name_or_code_lower in valid_slugs) or  \
            (country_name_or_code_upper in valid_countries_code) or \
            (country_name_or_code in valid_countries_names):
        return True
    else:
        return False


# function to validate whether user input is Y or N
def validate_data_explorer_restart(input: str) -> bool:
    input_lower = input.upper()

    if input_lower == "Y" or input_lower == "y":
        return True
    if input_lower == "N" or input_lower == "n":
        return False


valid_menu_options = ["1", "2", "3", "4"]


# function to validate whether menu selection input is a valid menu
# selection (1, 2, 3 or 4). if not, return false.
def validate_menu_selection(menu_input: str) -> str:
    if menu_input in valid_menu_options:
        validate_menu_selection = menu_input
        return validate_menu_selection
    else:
        return False
