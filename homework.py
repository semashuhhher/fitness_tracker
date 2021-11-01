class InfoMessage:

    def __init__(self, training_type: str, duration: float,
                 distance: float, speed: float, calories: float) -> None:
        self.training_type = training_type
        self.duration = round(duration, 3)
        self.distance = round(distance, 3)
        self.speed = round(speed, 3)
        self.calories = round(calories, 3)

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.; '
                f'Дистанция: {self.distance} км; '
                f'Ср. скорость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}.')


class Training:

    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self, action: int, duration: float, weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        distance = self.get_distance()
        average_speed = distance / self.duration
        return average_speed

    def get_spent_calories(self) -> float:
        pass

    def show_training_info(self) -> InfoMessage:
        info = InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories(),
                           )
        return info


class Running(Training):
    LEN_STEP = 0.65

    def get_spent_calories(self):
        average_speed = self.get_mean_speed()
        coeff_calorie_1 = (18 * average_speed - 20) * \
            self.weight / self.M_IN_KM * self.duration
        return coeff_calorie_1


class SportsWalking(Training):

    def __init__(self, action: int, duration: float,
                 weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    LEN_STEP = 0.65

    def get_spent_calories(self):
        average_speed = self.get_mean_speed()
        coeff_calorie_2 = (0.035 * self.weight +
                           (average_speed**2 // self.height) *
                           0.029 * self.weight) * self.duration
        return coeff_calorie_2


class Swimming(Training):

    LEN_STEP = 1.38

    def __init__(self, action: int, duration: float, weight: float,
                 length_pool: float, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        average_speed_pool = self.length_pool * \
            self.count_pool / self.M_IN_KM / self.duration
        return average_speed_pool

    def get_spent_calories(self):
        average_speed = self.get_mean_speed()
        coeff_calorie_3 = (average_speed + 1.1) * 2 * self.weight
        return coeff_calorie_3


def read_package(workout_type, data):
    classification = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking,
    }
    return classification[workout_type](*data)


def main(training: Training):
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
