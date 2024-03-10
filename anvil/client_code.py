from ._anvil_designer import uploadTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class upload(uploadTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def file_loader_1_change(self, file, **event_args):
        result = anvil.server.call('classify_audio', file)

        bronchitis = result[0][0]
        commoncold = result[0][1]
        pertussis = result[0][2]
        pneumonia = result[0][3]
        normalcough = result[0][4]

        result_dictionary = {bronchitis: "Bronchitis", commoncold: "Common Cold", pertussis: "Whooping Cough", pneumonia: "Pneumonia", normalcough: "Normal Cough"}
        final_result = result_dictionary.get(max(result_dictionary))

        bronchitis_perc = bronchitis * 100
        commoncold_perc = commoncold * 100
        pertussis_perc = pertussis * 100
        pneumonia_perc = pneumonia * 100
        normalcough_perc = normalcough * 100

        bronchitis_result = "%.2f" % bronchitis_perc
        commoncold_result = "%.2f" % commoncold_perc
        pertussis_result = "%.2f" % pertussis_perc
        pneumonia_result = "%.2f" % pneumonia_perc
        normalcough_result = "%.2f" % normalcough_perc

        bronchitis_text = f'Bronchitis: {bronchitis_result}%'
        self.bronchitis_perc_label.text += bronchitis_text    
        commoncold_text = f'Common Cold: {commoncold_result}%'
        self.commoncold_perc_label.text += commoncold_text
        pertussis_text = f'Pertussis: {pertussis_result}%'
        self.pertussis_perc_label.text += pertussis_text
        pneumonia_text = f'Pneumonia: {pneumonia_result}%'
        self.pneumonia_perc_label.text += pneumonia_text
        normalcough_text = f'Normal Cough: {normalcough_result}%'
        self.normalcough_perc_label.text += normalcough_text

        if final_result == "Bronchitis":
            result_text = f"Your cough recording matches\nabout {bronchitis_result}% to bronchitis!"
            self.result_label.text += result_text
            prescription_text = "  Recommended treatment for bronchitis:\n  - Usually, you'll need nothing more than rest and plenty of fluids to treat the flu. But if you have a severe infection or are at higher risk of complications, your health care provider may prescribe an antiviral medication to treat the flu."
            self.prescription_label.text += prescription_text

        elif final_result == "Common Cold":
            result_text = f"Your cough recording matches\nabout {commoncold_result}% to the common cold!"
            self.result_label.text += result_text
            prescription_text = "  Recommended treatment for the common cold:\n  - Drink a lot of water.\n  - Rest is your best friend. Make sure to have lots of it.\n  - Also use a humidifier! Keeping the air moist helps loosen mucus!"
            self.prescription_label.text += prescription_text

        elif final_result == "Whooping Cough":
            result_text = f"Your cough recording matches\nabout {pertussis_result}% to whooping cough!"
            self.result_label.text += result_text
            prescription_text = "  Recommended treatment for whooping cough:\n  - Don't eat too much! Eating more than you can chew only strains your throat more! \n  - Wash your hands to avoid viruses.\n  - Drink water to avoid dehydation.\n  - Rest so you can recharge your stamina!"
            self.prescription_label.text += prescription_text 

        elif final_result == "Pneumonia":
            result_text = f"Your cough recording matches\nabout {pneumonia_result}% to pneumonia!"
            self.result_label.text += result_text
            prescription_text = "  Recommended treatment for pneumonia:\n  - Don't forget to drink a ton of water!\n  - Rest, rest, rest! Resting recharges your body's immune system.\n  - Prevent yourself from inhaling smoke. It can worsen your symptoms.\n  - And lastly, exercise your lungs! (e.g. walking, running, jumping) This can help give it a boost as you get better from pneumonia."
            self.prescription_label.text += prescription_text

        else:
            result_text = f"You are healthy!\nYour cough recording does not match any of the ailments."
            self.result_label.text += result_text
            prescription_text = "  Recommended treatment:\n  - Give yourself a pat on the back!\n  - And keep your body healthy and strong!"
            self.prescription_label.text += prescription_text
