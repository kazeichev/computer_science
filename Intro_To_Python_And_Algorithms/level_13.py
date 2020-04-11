def Unmanned(l, n, track):
    path = 1
    summery_time = 1
    traffic_lights = generate_traffic_lights(track)

    while path < l:
        traffic_lights_data = traffic_lights.get(path)

        if traffic_lights_data and is_red_light(summery_time, traffic_lights_data):
            summery_time += 1
            continue

        path += 1
        summery_time += 1

    return summery_time


def generate_traffic_lights(track):
    result = dict()

    for i in track:
        result[i[0]] = [i[1], i[2]]

    return result


def is_red_light(summery_time, traffic_lights_data):
    light = 0

    while summery_time > 0:
        if summery_time < traffic_lights_data[light]:
            break

        summery_time = summery_time - traffic_lights_data[light]
        light = 1 if light == 0 else 0

    return False if light == 1 else True
