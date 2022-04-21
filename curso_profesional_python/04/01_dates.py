from datetime import datetime

if '__main__' == __name__:
    my_time = datetime.now()
    print(my_time)
    
    my_str = my_time.strftime('%d/%m/%Y')
    print(f'LATAM Format: ', my_str)
    
    my_str = my_time.strftime('%m/%d/%Y')
    print(f'US Format: ', my_str)
    
    my_str = my_time.strftime('%Y')
    print(f'We are at year: ', my_str)
    