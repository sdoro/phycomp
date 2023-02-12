from spike import PrimeHub

hub = PrimeHub()

message = 'Hello World'
x = 5
y = 6

hub.light_matrix.show_image('HAPPY')
hub.light_matrix.write(message)
hub.light_matrix.write(x/y)
