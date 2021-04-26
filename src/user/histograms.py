def get_gre_histogram(array):
    
    histogram = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0
    }

    for item in array:
        if item >= 130 and item < 135:
            histogram['1'] += 1
        elif item >= 135 and item < 140:
            histogram['2'] += 1
        elif item >= 140 and item < 145:
            histogram['3'] += 1
        elif item >= 145 and item < 150:
            histogram['4'] += 1
        elif item >= 150 and item < 155:
            histogram['5'] += 1
        elif item >= 155 and item < 160:
            histogram['6'] += 1
        elif item >= 160 and item < 165:
            histogram['7'] += 1
        else:
            histogram['8'] += 1
    

    return histogram



def get_toefl_histogram(array):
    histogram = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0
    }

    for item in array:
        if item >= 0 and item < 15:
            histogram['1'] += 1
        elif item >= 15 and item < 30:
            histogram['2'] += 1
        elif item >= 30 and item < 45:
            histogram['3'] += 1
        elif item >= 45 and item < 60:
            histogram['4'] += 1
        elif item >= 60 and item < 75:
            histogram['5'] += 1
        elif item >= 75 and item < 90:
            histogram['6'] += 1
        elif item >= 90 and item < 105:
            histogram['7'] += 1
        else:
            histogram['8'] += 1
    
    return histogram



def get_gpa_histogram(array):
    histogram = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0
    }

    for item in array:
        if item >= 0 and item < 0.5:
            histogram['1'] += 1
        elif item >= 0.5 and item < 1.0:
            histogram['2'] += 1
        elif item >= 1.0 and item < 1.5:
            histogram['3'] += 1
        elif item >= 1.5 and item < 2.0:
            histogram['4'] += 1
        elif item >= 2.0 and item < 2.5:
            histogram['5'] += 1
        elif item >= 2.5 and item < 3.0:
            histogram['6'] += 1
        elif item >= 3.0 and item < 3.5:
            histogram['7'] += 1
        else:
            histogram['8'] += 1
            
    return histogram
