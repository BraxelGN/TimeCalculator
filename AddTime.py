def add_time(start_time, duration, starting_day=None):
    # Obtener las horas y los minutos del tiempo de inicio
    start_hour, start_minute = map(int, start_time.split(":"))

    # Obtener las horas y los minutos de la duración
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Calcular el tiempo final sumando la duración
    end_minute = (start_minute + duration_minute) % 60
    carry_hour = (start_minute + duration_minute) // 60
    end_hour = (start_hour + duration_hour + carry_hour) % 24

    # Convertir el tiempo final al formato de 24 horas
    end_time = f"{end_hour:02d}:{end_minute:02d}"

    # Determinar el número de días después
    num_days_later = (start_hour + duration_hour + carry_hour) // 24

    # Determinar el día de la semana del tiempo final si se proporciona el día de inicio
    if starting_day:
        starting_day = starting_day.lower().capitalize()
        days_of_week = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
        starting_day_index = days_of_week.index(starting_day)
        end_day_index = (starting_day_index + num_days_later) % 7
        end_day = days_of_week[end_day_index]
        end_time += f", {end_day}"

    # Determinar si es el día siguiente o varios días después
    if num_days_later == 1:
        end_time += " (dia siguiente)"
    elif num_days_later > 1:
        end_time += f" ({num_days_later} dias despues)"

    return end_time

print(add_time("3:00 ", "3:10"))
print(add_time("11:30", "2:32", "Lunes"))
print(add_time("11:43", "00:20"))
print(add_time("10:10", "3:30"))
print(add_time("11:43", "24:20", "Martes"))
print(add_time("6:30", "205:12"))
