def memorize(function):
    # TODO пиши тут
    a = {}
    def weight_speed(weight, speed):
        kesh = ()
        kesh_1 = function(weight, speed)
        a[(weight, speed)] = kesh_1
        kesh = (kesh_1, a)
        return kesh
    return weight_speed


# эту часть НЕ трогать
@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия"""
    return (weight * speed ** 2)/2
