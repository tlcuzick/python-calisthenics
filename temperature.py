def convert_c_to_f(temp):
    new_temp = (temp * (9.0/5.0)) + 32.0    
    print('{} degrees C = {} degrees F'.format(temp, new_temp))

convert_c_to_f(37)

def convert_f_to_c(temp):
    new_temp = (temp - 32.0) * (5.0/9.0)
    print('{} degrees F = {} degrees C'.format(temp, new_temp))

convert_f_to_c(72)
