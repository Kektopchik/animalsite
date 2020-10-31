from docxtpl import DocxTemplate
import sqlite3


def create_data(path, card):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    query = f"SELECT * from mainapp_animals where record_card = '{card}'"
    cursor.execute(query)
    result = cursor.fetchall()
    dat = []
    for d in range(46):
        dat.append("")
    dat[0] = result[0][1]
    dat[5] = result[0][3]
    dat[6] = result[0][4]
    dat[7] = result[0][5]
    dat[8] = result[0][6]
    dat[9] = result[0][7]
    dat[10] = result[0][8]
    dat[11] = result[0][9]
    dat[12] = result[0][10]
    dat[13] = result[0][11]
    dat[14] = result[0][12]
    dat[15] = result[0][13]
    dat[4] = result[0][14]
    print(dat)
    return dat


def create_card_animal(path, data):
    card = DocxTemplate(path)
    context = {
        'animalcard': str(data[0]),
        'date': str(data[1]),
        'addresshelter': str(data[2]),
        'company': str(data[3]),
        'area': str(data[4]),
        'age': str(data[5]),
        'weight': str(data[6]),
        'nickname': str(data[7]),
        'gender': str(data[8]),
        'breed': str(data[9]),
        'color': str(data[10]),
        'wool': str(data[11]),
        'ears': str(data[12]),
        'tail': str(data[13]),
        'size': str(data[14]),
        'specialsign': str(data[15]),
        'character': str(data[16]),
        'indmark': str(data[17]),
        'datesteril': str(data[18]),
        'placesteril': str(data[19]),
        'nameveterinarian': str(data[20]),
        'socialized': str(data[21]),
        'order': str(data[22]),
        'orderdate': str(data[23]),
        'acttrapping': str(data[24]),
        'actdate': str(data[25]),
        'addresstrapping': str(data[26]),
        'video': str(data[27]),
        'legalentiny': str(data[28]),
        'addresslegent': str(data[29]),
        'phonelegent': str(data[30]),
        'namelegent': str(data[31]),
        'contactinformationentlefent': str(data[32]),
        'individualname': str(data[33]),
        'pasportseries': str(data[34]),
        'pasportnumber': str(data[35]),
        'issued': str(data[36]),
        'issueddate': str(data[37]),
        'registered': str(data[38]),
        'contactindividual': str(data[39]),
        'dateadmision': str(data[40]),
        'actadmission': str(data[41]),
        'datedeparture': str(data[42]),
        'actdeparture': str(data[43]),
        'namemaneger': str(data[44]),
        'nameemloyee': str(data[45])
    }
    card.render(context)
    card.save("animal.docx")



create_card_animal("AnimalCard.docx", create_data("..\db_new.sqlite", '1633з-20'))

