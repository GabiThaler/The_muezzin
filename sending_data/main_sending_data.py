from sending_data.manager1 import manager1



class Main_sending_data:
    def Start_prosses_and_send_metadata(self):
        # מפעילים את המחלקה שמקבל את המטא דאטא ומטםל בזה

        sender = manager1.Manager()
        sender.get_sub()
