import time

import numpy as np

from database import delete_db, init_db, save_measurement


def generate_data(t):
    # Oxymeter
    spo2 = np.random.normal(97.5, 0.4)
    heart_rate = 75 + 5 * np.sin(t / 10) + np.random.normal(0, 1)

    # Barometer
    pressure = 1013 + 2 * np.sin(t / 30) + np.random.normal(0, 0.1)

    # Accelerometer
    accel_x = 0.3 * np.sin(t) + np.random.normal(0, 0.1)
    accel_y = 0.3 * np.cos(t) + np.random.normal(0, 0.1)
    accel_z = 9.81 + 0.5 * np.sin(t / 2) + np.random.normal(0, 0.1)

    return {
        "spo2": spo2,
        "heart_rate": heart_rate,
        "pressure": pressure,
        "accel_x": accel_x,
        "accel_y": accel_y,
        "accel_z": accel_z
    }


def main():
    delete_db()
    init_db()
    print("Starting sensor simulator...")

    start = time.time()

    while True:
        t = time.time() - start

        data = generate_data(t)
        save_measurement(data)

        print(data)

        time.sleep(1)


if __name__ == "__main__":
    main()
