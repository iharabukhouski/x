#     if 'aliexpress' in x.lower():

#         return 'aliexpress'

#     if 'ALIPAY' in x:

#         return 'aliexpress'

#     if 'github' in x.lower():

#         return 'github'

#     if 'anthropic' in x.lower():

#         return 'anthropic'

#     if 'crocs' in x.lower():

#         return 'crocs'

#     if 'rei.com' in x.lower():

#         return 'rei'

#     if 'nike.com' in x.lower():

#         return 'nike'

#     if 'openai' in x.lower():

#         return 'openai'

#     if 'uplift desk' in x.lower():

#         return 'uplift desk'

#     if 'barbon\'s barbershop' in x.lower():

#         return 'barbons barbershop'

MAP = {
    # chase
    'Payment Thank You': 'payment',
    # bofa
    'Online payment from': 'payment',

    'Amazon.com': 'amazon',
    'AMAZON': 'amazon',
    'AMZN': 'amazon',
    'Chase Travel': 'chase travel',
    'AMAZON MKTPL': 'amazon',
    'AMAZON RETA': 'amazon',
    'JOSEPH WANG': 'joseph wang',
    'GOLDS GYM': 'golds gym',
    'AMAZON MKTPL': 'amazon',
    'AMAZON MKTPL': 'amazon',
    'AMAZON MKTPL': 'amazon',
    'AMAZON MKTPL': 'amazon',
    'AMAZON MKTPL': 'amazon',
    'AMAZON MKTPL': 'amazon',
    'AMAZON MKTPL': 'amazon',
    'FOREIGN TRANSACTION FEE': 'foreign transaction fee',
    'WEIRDO': 'valeria',
    'EXXON': 'exxon',
    'CVS': 'cvs',
    'BTOD.COM': 'btod',
    'PETER ATTIA': 'peter attia',
    'MICROSOFT': 'microsoft',
    'WARBY PARKER': 'warby parker',
    'Patreon': 'patreon',
    'NIVA DENTAL': 'niva dental',
    'ADVANCED SMILES DENTAL': 'advanced smiles dental',
    'PARKFAMILYDENTAL': 'park family dental',
    'Wikimedia': 'wikipedia',
    'H-E-B': 'heb',
    'ANTHROPIC': 'anthropic',
    'CROCS': 'crocs',
    'ALIPAY': 'aliexpress',
    'GITHUB': 'github',
    'IKEA': 'ikea',
    
}

def process(row):

    description = row['description'].lower()

    for key in MAP.keys():

        if key in row['description']:

            description = MAP[key]

            row['description'] = description

    return row

def process_merchant(
    str,
):

    description = str.lower()

    for key in MAP.keys():

        if key in str:

            description = MAP[key]

        return description
