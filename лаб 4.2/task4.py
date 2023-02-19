class Traffic:
    def __init__(self, traffic_volume: (int, float), traffic_consumption: (int, float)):
        """
        Создание базового класса "Трафик"
        :param traffic_volume: объем трафика
        :param traffic_consumption: расход траффика (Мб) в 1 с
        """
        self._traffic_volume = None  # protected: не изменяется при не использовании мобильной сети
        self._init_traffic_volume(traffic_volume)
        self._traffic_consumption = None  # protected: константа при фоновом использовании
        self._init_traffic_consumption(traffic_consumption)

    def __str__(self) -> str:
        return f"Трафик: объем трафика {self.traffic_volume} (Мб), расход трафика {self.traffic_consumption} (Мб/с)."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(traffic_volume={self.traffic_volume},traffic_consumption={self.traffic_consumption})"

    def _init_traffic_volume(self, traffic_volume: (int, float)) -> None:
        """
        Инициализация атрибута _traffic_volume:
        Protected: используется только при инициализации экземпляра класса
        :param traffic_volume: текущий использованый трафик
        """
        if not isinstance(traffic_volume, (int, float)):
            raise TypeError('Объем трафика должен быть типа int или float')
        if traffic_volume < 0:
            raise ValueError('Объем трафика должен быть не меньше 0')
        self._traffic_volume = traffic_volume

    def _init_traffic_consumption(self, traffic_consumption: (int, float)) -> None:
        """
        Инициализация атрибута _traffic_consumption:
        Protected: используется только при инициализации экземпляра класса
        :param traffic_consumption: расход трафика (Мб) в 1
        """
        if not isinstance(traffic_consumption, (int, float)):
            raise TypeError('Расход трафика должнен быть типа int или float')
        if traffic_consumption <= 0:
            raise ValueError('Расход трафика должнен быть больше 0')
        self._traffic_consumption = traffic_consumption

    @property
    def traffic_volume(self) -> (int, float):
        """
        Используем getter для атрибута _traffic_volume (не setter: protected атрибут)
        """
        return self._traffic_volume

    @property
    def traffic_consumption(self) -> (int, float):
        """
        Используем getter для атрибута _traffic_consumption (не setter: protected атрибут)
        """
        return self._traffic_consumption

    def fill_traffic(self, added_traffic: (int, float)) -> None:
        """
        Докупить Гб - увеличить объем трафика, который мы можем использовать
        :param added_traffic: объем добавляемого трафика
        """
        if not isinstance(added_traffic, (int, float)):
            raise TypeError('Объем добавляемого трафика должен быть типа int или float')
        if added_traffic < 0:
            raise ValueError('Объем добавляемого трафика должен быть не меньше 0')
        self._traffic_volume += added_traffic

    def spent_traffic(self, downloading_volume: (int, float)) -> None:
        """
        Определить объем потраченного трафика во время скачивания приложения
        :param downloading_volume: объем загрузки
        """
        if not isinstance(downloading_volume, (int, float)):
            raise TypeError('Объем загрузки должен быть типа int или float')
        if downloading_volume < 0:
            raise ValueError('Объем загрузки должен быть не меньше 0')
        ...


class Video(Traffic):
    def __init__(self, traffic_volume: (int, float), traffic_consumption: (int, float), number_of_video: int):
        """
        Создание дочернего класса "Мотоцикл с коляской", унаследован от класса "Мотоцикл"
        :param traffic_volume: объем доступного трафика
        :param traffic_consumption: расход трафика (Мб) в 1 с
        :param number_of_video: количество просмотренных видео
        """
        super().__init__(traffic_volume, traffic_consumption)
        self._number_of_video = None  # protected: количество в один сеанс
        self._init_number_of_video(number_of_video)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(traffic_amount={self.traffic_volume},traffic_consumption={self.traffic_consumption}," \
               f"video={self._number_of_video})"

    def _init_number_of_video(self, number_of_video: int) -> None:
        """
        Инициализация атрибута number_of_video - количество видео за сеанс
        Protected: используется только при инициализации экземпляра класса
        :param number_of_video: количество просмотренных видео
        """
        if not isinstance(number_of_video, int):
            raise TypeError('Количество просмотренных видео int')
        if number_of_video <= 0:
            raise ValueError('Количество просмотренных видео 0')
        self._number_of_video = number_of_video

    @property
    def seats(self) -> int:
        """
        Используем getter для атрибута number_of_video (не setter: protected атрибут)
        """
        return self._number_of_video

    def spent_traffic(self, downloading_volume: (int, float)) -> None:
        """
        Определить объем загрузки во время просматривания видео
        Перегрузка метода базового класса ввиду того, что просматриваем видео
        :param downloading_volume: объем загрузки
        """
        if not isinstance(downloading_volume, (int, float)):
            raise TypeError('Объем загрузки должен быть типа int или float')
        if downloading_volume < 0:
            raise ValueError('Объем загрузки должен быть не меньше 0')
        ...

if __name__ == "__main__":
    # Write your solution here
    pass
