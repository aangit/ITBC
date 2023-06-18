# A program to track students' performance in exams. 
# For each student, we store their first name, last name, student ID, program code, 
# and all the courses they need to pass or have passed with grades ranging from 6 to 10. 
# For each assigned course, we know its name and unique course code.

# Based on the input data, the program should provide the following functionalities:
# a. Display all passed exams for a specific student.
# b. Calculate the average grade for a specific student.
# c. Retrieve data for the student(s) with the highest average grade.
# d. Retrieve data for the student(s) with the fewest passed exams.
# e. Display all students who have passed all exams in their assigned courses.
# f. Display the distribution of students by programs, in percentages.
# g. Display all students in a selected program.
# h. Retrieve data for the top-performing student in a selected program.
# i. Display all courses that no student has passed.
# j. Retrieve the course(s) with the highest average grade.

# Upon starting the program, display the main menu to the user with options a - j (which can be entered via the keyboard).
# After selecting an option, if necessary, prompt the user to enter data and display the desired results. 
# Then, show the main menu again.

studenti = [
    {"ime": "Milan",
     "prezime": "Belic",
     "indeks": "py200",
     "smer": "fizicka_hemija",
     "predmeti": [
         {"ocena": 10, "sifra": "bio", "status": True, "naziv": "hemija"},
         {"ocena": 9, "sifra": "bio", "status": True, "naziv": "nuklearna_fizika"},
         {"ocena": 5, "sifra": "bio", "status": False, "naziv": "matematika"}],
     },

    {"ime": "Sara",
     "prezime": "Ilic",
     "indeks": "py300",
     "smer": "enologija",
     "predmeti": [
         {"ocena": 10, "sifra": "bio", "status": True, "naziv": "bioprocesi"},
         {"ocena": 8, "sifra": "bio", "status": True, "naziv": "vinarstvo"}],
     },
    {
        "ime": "Marko",
        "prezime": "Markovic",
        "indeks": "py400",
        "smer": "enologija",
        "predmeti": [
            {"ocena": 7, "sifra": "bio", "status": True, "naziv": "bioprocesi"},
            {"ocena": 6, "sifra": "bio", "status": False, "naziv": "vinarstvo"}]
    }
]


def vrati_polozene_ispite(indeks, studenti):
    vrati_polozene = []
    for student in studenti:
        if student["indeks"] == indeks:
            for ispiti in student["predmeti"]:
                if ispiti["status"] == True:
                    vrati_polozene.append(ispiti)
            break
    return vrati_polozene


def polozeni_ispiti(indeks, studenti):
    student_ispiti = vrati_polozene_ispite(indeks, studenti)
    for ispiti in student_ispiti:
        print("Student sa indeksom", indeks, "je polozio ",
              ispiti["naziv"], "sa ocenom ", ispiti["ocena"])


def srednja_ocena(indeks, studenti):
    student_ispiti = vrati_polozene_ispite(indeks, studenti)
    suma = 0
    broj_polozenih = 0
    for ispiti in student_ispiti:
        suma += ispiti["ocena"]
        broj_polozenih += 1
    return suma/broj_polozenih


def najveca_prosecna(studenti):
    maks = 0
    for student in studenti:
        srednja = srednja_ocena(student["indeks"], studenti)
        if srednja > maks:
            maks = srednja
    return maks


def najmanje_polozenih(studenti):
    mini = 999
    lista = []
    for student in studenti:
        broj = len(vrati_polozene_ispite(student["indeks"], studenti))
        if broj < mini:
            mini = broj
    for student in studenti:
        broj = len(vrati_polozene_ispite(student["indeks"], studenti))
        if broj == mini: 
            lista.append(student)

        
    return lista


def student_polozio_ispite(student):
    for predmet in student["predmeti"]:
        if predmet["status"] == False:
            return False
    return True


def studenti_polozili_sve_ispite(studenti):
    lista_polozili_sve = []
    for student in studenti:
        if student_polozio_ispite(student):
            lista_polozili_sve.append(student)
    return lista_polozili_sve


def smer_raspodela(studenti):
    smer_recnik = {}
    broj_studenata = len(studenti)
    for student in studenti:
        if student["smer"] not in smer_recnik:
            smer_recnik[student["smer"]] = 1
        else:
            smer_recnik[student["smer"]] += 1

    for smer in smer_recnik:
        smer_recnik[smer] = round(smer_recnik[smer] * 100 / broj_studenata, 2)
    return smer_recnik


def studenti_na_smeru(smer, studenti):
    konacno = []
    for student in studenti:
        if student["smer"] == smer:
            konacno.append(student)
    return konacno


def najbolji_student(studenti):
    maks = 0
    for student in studenti:
        srednja = srednja_ocena(student["indeks"], studenti)
        if srednja > maks:
            maks = srednja
            maks_student = student
    return maks_student


def najbolji_na_smeru(smer, studenti):
    smer_studenti = studenti_na_smeru(smer, studenti)
    return najbolji_student(smer_studenti)


def nije_polozeno(predmet, student):
    lista_neka = []
    for ispiti in studenti:
        if ispiti["status"] != True:
            lista_neka.append(ispiti["naziv"])
    return lista_neka


def proveri_indeks(indeks, studenti):
    for student in studenti:
        if student["indeks"] == indeks:
            return True
    return False


def proveri_smer(smer, studenti):
    for student in studenti:
        if student["smer"] == smer:
            return True
    return False


def teski_predmeti(studenti):
    nova_lista = []
    polozeni_ispiti = set()
    nepolozeni_ispiti = set()
    for student in studenti:
        lista_predmeta = student["predmeti"]
        for predmet in lista_predmeta:
            if predmet["status"] == False:
                nepolozeni_ispiti.add(predmet["naziv"])
            else:
                polozeni_ispiti.add(predmet["naziv"])
    for ispit in nepolozeni_ispiti:
        if ispit not in polozeni_ispiti:
            nova_lista.append(ispit)
    return nova_lista


def najveci_prosek_predmeta(studenti):
    prosek_dict = {}
    ispiti_lista = []
    nazivi_predmeta = set()
    for student in studenti:
        lista_predmeta = student["predmeti"]
        for predmet in lista_predmeta:
            if predmet["status"]:
                ispiti_lista.append(predmet)
                nazivi_predmeta.add(predmet["naziv"])

    for ime in nazivi_predmeta:
        suma = 0
        brojac = 0
        for ispit in ispiti_lista:
            if ispit["naziv"] == ime:
                brojac += 1
                suma += ispit["ocena"]
        prosek_dict[ime] = suma / brojac
    maksi = 0
    maksi_predmet = " "
    for i in prosek_dict:
        if prosek_dict[i] > maksi:
            maksi = prosek_dict[i]
            maksi_predmet = i
    return maksi_predmet


izbor = ""
print("Za spisak polozenih ispita odredjenog studenta, pritisnite a")
print("Za prosecnu ocenu odredjenog studenta, pristisnite b")
print("Za studenta sa najvecom prosecnom ocenom, pristisnite c")
print("Za podatke studenta sa najmanje polozenih ispita, pristisnite d")
print("Za podatke svih studenta koji su položili sve ispite na predmetima koji su im dodeljeni, pristisnite e")
print("Za raspodele studenata po smerovima, u procentima, pristisnite f")
print("Za sve studente na odabranom smeru, pristisnite g")
print("Za najboljeg studenta na odabranom smeru, pristisnite h")
print("Za sve predmete koji nije položio niti jedan student, pristisnite i")
print("Za predmet sa najvećom prosečnom ocenom, pristisnite j")
while izbor != "Kraj programa":
    izbor = input(
        "Unesite zeljenu opciju, od a do j, a za kraj programa, unesite Kraj programa.")
    if izbor == "a":
        a = input("unesite broj indeksa studenta")
        while not proveri_indeks(a, studenti):
            a = input("unesite broj indeksa studenta")
        polozeni_ispiti(a, studenti)
    elif izbor == "b":
        b = input("unesite broj indeksa studenta")
        while not proveri_indeks(b, studenti):
            b = input("unesite broj indeksa studenta ")
        print(srednja_ocena(b, studenti))
    elif izbor == "c":
        print(najveca_prosecna(studenti))
    elif izbor == "d":
        s = najmanje_polozenih(studenti)
        for student in s:
            print(f"{student['ime']} {student['prezime']}")
    elif izbor == "e":
        s = studenti_polozili_sve_ispite(studenti)
        for student in s:
            print(f"{student['ime']} {student['prezime']}")
    elif izbor == "f":
        s = smer_raspodela(studenti)
        for i in s:
            print(f"{i} {s[i]}")
    elif izbor == "g":
        g = input("unesite smer ")
        while not proveri_smer(g, studenti):
            g = input("unesite smer ")
        s = studenti_na_smeru(g, studenti)
        for student in s:
            print(f"{student['ime']} {student['prezime']}")
    elif izbor == "h":
        h = input("unesite smer")
        while not proveri_smer(h, studenti):
            h = input("unesite smer ")
        s = najbolji_na_smeru(h, studenti) 
        print(f"{s['ime']} {s['prezime']}")
    elif izbor == "i":
        for predmet in teski_predmeti(studenti):
            print(predmet)
    elif izbor == "j":
        print(najveci_prosek_predmeta(studenti))
    else:
        print("Vrednost nevalidna. Unesite vrednost od a do j.")