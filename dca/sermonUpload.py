sermons = [
    {
        'driveLink': 'https://drive.google.com/file/d/1vU0XaaKlLNJtKVa3PAuE1OGEGb_MMU2F/view?usp=sharing',
        'preacher': 'Dcn. Tobi Akapo',
        'sermonTitle': 'The Effects of Light',
        'sermonDate': '30th January, 2022',
    },
]


def convertToExportLink(driveLink):
    driveLink = driveLink.split('/d/')
    driveLink = driveLink[1]
    driveLink = driveLink.split('/')
    driveLink = driveLink[0]
    return driveLink


sqlScript = "INSERT INTO `sermons` (`entryIndex`, `driveLink`, `preacher`, `sermonTitle`, `sermonDate`) VALUES"
entryIndex = 34
for sermon in sermons:
    driveLink = sermon['driveLink']
    driveLink = convertToExportLink(driveLink)
    sermon['driveLink'] = 'http://docs.google.com/uc?export=open&id={}'.format(
        driveLink)
    sqlScript += "('{}', '{}', '{}', '{}', '{}'),".format(
        entryIndex, sermon['driveLink'], sermon['preacher'], sermon['sermonTitle'], sermon['sermonDate'],
    )
    entryIndex += 1

sqlScript = sqlScript[:len(sqlScript) - 1]
sqlScript += ';'
print(sqlScript)
