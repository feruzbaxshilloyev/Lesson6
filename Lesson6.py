from collections import namedtuple

'''
def masala1():
    car = namedtuple('Car', ('brand', 'model', 'year', 'price'))

    mashinalar = [
        car('Tesla', 'Model 3', 2021, 50000),
        car('Toyota', 'corolla', 2022, 20000),
        car('BMW', 'i7', 2022, 105000),
        car('Kia', 'K5', 2019, 25000)
    ]

    print([i for i in mashinalar if i.year > 2020])

masala1()



def masala2():
    player = namedtuple('Player', ('name', 'position', 'score', 'asist'))

    oyinchilar = [
        player('Mbappe', 'CF', 14, 3),
        player('Vini jr', 'LW', 14, 10),
        player('Rodrygo', 'RW', 8, 5),
        player('Bellingham', 'AM', 7, 4),
        player('Valverde', 'CM', 5, 2),
        player('Arda Guler', 'RW', 1, 2)
    ]
    def ball():
        for i in oyinchilar:
            print(i.score + i.asist)
    a = ball()
    
    print(max(oyinchilar, key=a))

masala2()


def masala3():
    book = namedtuple('Book', ('title', 'author', 'year', 'price'))

    kitoblar = [
        book('ikki eshik orasi', 'Tohir Malik', 2013, 10),
        book('Sariq devni minib', 'Xudoyberdi, Toxtaboyev', 2012, 8),
        book('Men', 'Duman', 2017, 15),
        book('Yashirin Dunyo', 'Shayx Muhammad Sodiq Muhammad Yusuf', 2016, 20)
    ]

    e = [i.price for i in kitoblar if i.year >= 2015]
    return f"Kitoblar narxi: ${sum(e)}"

print(masala3())



def masala4():
    ishchi = namedtuple('Ishchi', ('name', 'salary', 'expirence'))

    ishchilar = [
        ishchi('Abror', 2000, 3),
        ishchi('Ali', 3000, 4),
        ishchi('Vali', 4000, 6),
        ishchi('Guli', 6000, 8)
    ]
    a = ishchilar[0]
    for i in ishchilar:
        if a.salary < i.salary:
            a = i

    return a

print(masala4())


def masala5():
    sport_team = namedtuple('Sport', ('Team', 'point'))

    teams = [
        sport_team('Real Madrid', 40),
        sport_team('Barcelona', 38),
        sport_team('Atletiko Madrid', 41),
        sport_team('Atletik Bilbao', 36)
    ]
    a = teams[0]
    for i in teams:
        if a.point < i.point:
            a = i
    return a

print(masala5())


def masala6():

    weather = namedtuple('Weather', ('city', 'temperature', 'humidity'))

    a = [
        weather('Toshkent', -1, 20),
        weather('Bukhara', -3, 30),
        weather('Doha', 35, 2)
    ]
    b = a[0]
    for i in a:
        if b.temperature < i.temperature:
            b = i
    return b

print(masala6())



def masala7():
    student = namedtuple("Student", ('name', 'math_score', 'english_score'))

    talabalar = [
        student('Feruz', 5, 3),
        student('Javohir', 4, 4),
        student('Ogabek', 3, 5),
        student('Diyor', 3, 3)
    ]

    a = talabalar[0]
    for i in talabalar:
        if a.math_score < i.math_score:
            a = i
    return a

print(masala7())


student = namedtuple('student', ('ismi', 'yoshi', 'kursi'))

talabalar = [student('Feruz', 20, 3),
            student('Feruzjon', 19, 3),
            student('Isfandiyor', 19, 2),
             student('Diyor', 18, 2)]
s = 0
for i in talabalar:
    s += i.yoshi
print(s / len(talabalar))


c = namedtuple('car', ('nom', 'yil'))

cars = [
    c('nexia 2', 2008),
    c('damas', 1996),
    c('cobalt', 2013),
    c('nexia 3', 2017)
]

r = []
for i in cars:
    if i.yil < 2010:
        r.append(i._replace(nom = f"{i.nom} x"))
    else:
        r.append(i)
print(r)
'''
