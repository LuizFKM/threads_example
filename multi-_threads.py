
import threading

def calc_square(numbers):
    print('Calculate square numbers: ')
    for i in numbers:
        
        print('square: {}'.format(str(i * i)))

def calc_cube(numbers):
    print('Calculate cube numbers: ')
    for i in numbers:
        
        print('cube: {}'.format(str(i*i*i)))

if __name__ == '__main__':
    arr = [2,3,8,9] #compartilhando o mesmo objeto dentro de 2 threads diferentes.
    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Main thread HERE!!!')
    print('Successes!')