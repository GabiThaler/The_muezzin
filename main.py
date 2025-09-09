from processing_metadata.manager import manager
from sending_data.manager1 import manager1


# מפעילים את התייקיה שלוקח את הקובץ בונה את המאטא דאטא ושולח
prosser=manager.Manager()
prosser.prosses_and_send_metadata()


# מפעילים את המחלקה שמקבל את המטא דאטא ומטםל בזה

sender = manager1.Manager()
sender.get_sub()

