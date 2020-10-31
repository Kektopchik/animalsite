from docxtpl import DocxTemplate
"""
доделать когда будет бд
"""


def export_card_animal(path, number_a):
    card = DocxTemplate(path)
    context = {
        'animalcard': str(number_a),
        'date': str(number_a),
        'addresshelter': str(number_a),
        'company': str(number_a),
        'enclosurenumber': str(number_a),
        'age': str(number_a),
        'weight': str(number_a),
        'nickname': str(number_a),
        'gender': str(number_a),
        'breed': str(number_a),
        'color': str(number_a),
        'wool': str(number_a),
        'ears': str(number_a),
        'tail': str(number_a),
        'size': str(number_a),
        'specialsign': str(number_a),
        'character': str(number_a),
        'indmark': str(number_a),
        'datesteril': str(number_a),
        'placesteril': str(number_a),
        'nameveterinarian': str(number_a),
        'socialized': str(number_a),
        'order': str(number_a),
        'orderdate': str(number_a),
        'acttrapping': str(number_a),
        'actdate': str(number_a),
        'addresstrapping': str(number_a),
        'video': str(number_a),
        'legalentiny': str(number_a),
        'addresslegent': str(number_a),
        'phonelegent': str(number_a),
        'namelegent': str(number_a),
        'contactinformationentlefent': str(number_a),
        'individualname': str(number_a),
        'pasportseries': str(number_a),
        'pasportnumber': str(number_a),
        'issued': str(number_a),
        'issueddate': str(number_a),
        'registered': str(number_a),
        'contactindividual': str(number_a),
        'dateadmision': str(number_a),
        'actadmission': str(number_a),
        'datedeparture': str(number_a),
        'actdeparture': str(number_a),
        'namemaneger': str(number_a),
        'nameemloyee': str(number_a)
    }
    card.render(context)
    card.save("animal.docx")


"""export_card_animal("AnimalCard.docx", 2)"""
