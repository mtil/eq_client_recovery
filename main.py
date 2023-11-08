import functions
import time

functions.kill_clients_all()

functions.client_launch()

#pulse
pulse = True
while pulse:
    print("Pulse Started.")
    time.sleep(10)
    if functions.client_alive_check('Blue') == False:
        print("Blue client not found.")
        # functions.kill_clients()
        functions.client_launch_single('Blue')
        time.sleep(10)

    if functions.client_alive_check('Green') == False:
        print("Green client not found.")
        # functions.kill_clients()
        functions.client_launch_single('Green')
        time.sleep(10)

    functions.error_window()

time.sleep(3)


