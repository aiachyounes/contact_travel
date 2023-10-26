{
    'name': 'Voyage', #Nom du module/ le nom technique du module c'est le nom du dossier qui contien le code
    'version': '1.0',
    'description': 'Voyage',
    'summary': '',
    'author': 'Aiach Hamrioui Younes',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base'
    ],
    'data': [ #Ici on met tout les views du system priority pour les fichiers de securité
        'security/ir.model.access.csv',
        'views/voyage_view.xml',
    ],
    'demo': [
        ''
    ],
    'auto_install': False,
    'application': False,
    'assets': {
        
    }
}