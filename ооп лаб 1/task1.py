class Planken:
    def __int__(self, length: float, height: float, width: float): # TODO Написать 3 класса с документацией и аннотацией типов
        if not isinstance(length, (int, float)):
            raise TypeError
        if length < 0:
            raise ValueError
        self.length = length

        if not isinstance(height, (int, float)):
            raise TypeError
        if height < 0:
            raise ValueError
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError
        if width < 0:
            raise ValueError
        self.width = width

    def cut_planken(self, cut: (int, float)):
        """
        Отрезаем кусок доски.
        :param cut: Длина отрезаемого куска.
        Примеры:
        cut = Planken(100,10,50)
        cut.cut_planken(50)
        """
        if not isinstance(cut, (int, float)):
            raise TypeError
        if cut < 0:
            raise ValueError
        ...

    def is_planken(self):
        """
        Проверка соотношения сторон объекта на предмет, является ли он доской.
        :return:True / False.
        """
        ...

class Ticket:
    def __int__(self, business_class = float, econom_class = float):
        if not isinstance(business_class, (int, float)):
            raise TypeError
        if business_class < 0:
            raise ValueError
        self.business_class = business_class

        if not isinstance(econom_class, (int, float)):
            raise TypeError
        if econom_class < 0:
            raise ValueError
        self.econom_class = econom_class

    def buy_ticket(self, buy: (int, float)):
        """
        Проверяем хватит ли денег на несколько билетов бизнесс и эконом класса.
        :param buy: Общая доступная нам сумма.
        Примеры:
        buy = Ticket(50000, 30000)
        buy.buy_ticket(60000, 20000)
        :return: True / False.
        """
        if not isinstance(buy, (int, float)):
            raise TypeError
        if buy < 0:
            raise ValueError
        ...

    def amount_ticket(self, amount: int):
        """
        Проверяем хватит ли нам доступного количества билетов.
        :param amount: Количество билетов.
        Примеры:
        amount = Ticket(4, 2)
        amount.amount_ticket(4, 4)
        :return: True / False.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError
        if amount < 0:
            raise ValueError
        ...

class ButerbrodKolbasaSir:
    def __int__(self, amount = int, hleb = int, kolbasa = int, sir = int):
        if not isinstance(amount, int):
            raise TypeError
        if amount < 0:
            raise ValueError
        self.amount = amount
        if not isinstance(hleb, int):
            raise TypeError
        if hleb < 0:
            raise ValueError
        self.hleb = hleb
        if not isinstance(kolbasa, int):
            raise TypeError
        if kolbasa < 0:
            raise ValueError
        self.kolbasa = kolbasa
        if not isinstance(sir, int):
            raise TypeError
        if sir < 0:
            raise ValueError
        self.sir = sir

    def amount_ingridients(self, amount_i: int):
        """
        Проверяем хватит ли нам ингридиентов на бутерброд с колбасой и сыром.
        :param amount_i:Колиичество ингридиентов.
        :raise ValueError: Бутерброд не получится, если не хватит какого-то из ингридиентов.

        :return: Бутерброд получится
        """
        if not isinstance(amount_i, (int, float)):
            raise TypeError
        if amount_i < 0:
            raise ValueError
        ...

    def amount_sandwich(self, amount_s: int):
        """
        Проверяем на сколько бутербродов с колбасой и сыром нам хватит ингридиентов.
        :param amount_s: Количество бутербродов.
        :return: Количество бутербродов, на которых нам хватит ингридиентов.
        """
        if not isinstance(amount_s, (int, float)):
            raise TypeError
        if amount_s < 0:
            raise ValueError
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()# TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
