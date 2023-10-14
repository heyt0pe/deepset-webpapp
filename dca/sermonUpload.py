sermons = [
    {
        'driveLink': 'https://drive.google.com/file/d/1IrIYPe9bYBIaBVfOWQDc3bB92lOFeVLU/view?usp=drive_link',
        'preacher': 'Rev. Olubusayo Folarin',
        'sermonTitle': 'Need for Speed (Delay)',
        'sermonDate': '2023-09-17 00:00:00',
    },
    {
        'driveLink': 'https://drive.google.com/file/d/1wSAx9JKcWJbge6VDgDF7bq9ykPxQ6pbI/view?usp=sharing',
        'preacher': 'Rev. Olubusayo Folarin',
        'sermonTitle': 'Heaven on Earth',
        'sermonDate': '2023-10-01 00:00:00',
    },
    {
        'driveLink': 'https://drive.google.com/file/d/1IFos5bkcJZMKxInMEYMwzfdRHIXj8wIi/view?usp=sharing',
        'preacher': 'Rev. Olubusayo Folarin',
        'sermonTitle': 'The Power of Forgiveness',
        'sermonDate': '2023-10-08 00:00:00',
    },
]


def convertToExportLink(driveLink):
    driveLink = driveLink.split('/d/')
    driveLink = driveLink[1]
    driveLink = driveLink.split('/')
    driveLink = driveLink[0]
    return driveLink


sqlScript = "INSERT INTO `sermons` (`sermonId`, `sermon`, `preacher`, `title`, `date`) VALUES"
entryIndex = 87
for sermon in sermons:
    entryIndex += 1
    driveLink = sermon['driveLink']
    driveLink = convertToExportLink(driveLink)
    sermon['driveLink'] = 'http://docs.google.com/uc?export=open&id={}'.format(
        driveLink)
    sqlScript += "('{}', '{}', '{}', '{}', '{}'),".format(
        entryIndex, sermon['driveLink'], sermon['preacher'], sermon['sermonTitle'], sermon['sermonDate'],
    )
    

sqlScript = sqlScript[:len(sqlScript) - 1]
sqlScript += ';'
print(sqlScript)
