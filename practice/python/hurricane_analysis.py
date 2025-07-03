# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded'
           , '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B'
           , '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B'
           , '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


def convert_damages_data(damages):
    """Convert damages data from string to float and return converted data as a list."""
    conversion = {"M": 1000000,
                "B": 1000000000}

    updated_damages = list()
    for damage in damages:
        if damage == "Damages not recorded":
          updated_damages.append(damage)
        if damage.find('M') != -1:
          updated_damages.append(float(damage[0:damage.find('M')])*conversion["M"])
        if damage.find('B') != -1:
          updated_damages.append(float(damage[0:damage.find('B')])*conversion["B"])
    return updated_damages

# test function by updating damages
updated_damages = convert_damages_data(damages)
print(updated_damages)

