# from viewer import View
# from model import Model

class Controller:
    def __init__(self, model, view):
        self.model  = model
        self.view   = view

        

    def update_dict(self, entries):
        try:
            self.model.update_dict(entries)

        except:
            print("Updaten des dict nicht möglich")

    def start_Tracking(self):
        try:
            self.model.start_Tracking()
            print("Succes, Tracking started")

        except:
            print("Tracking kann nicht gestartet werden")

    def stop_Tracking(self):

        try:
            self.model.stop_Tracking()
            print("Succes, Tracking stopped")

        except:
            print("Tracking kann nicht gestoppt werden")

    def get_Heatmap(self, nameHeatmap):
        try:
            if nameHeatmap == "Heatmap Bewegung":
                return self.model.calculate_heatmap(self.model.dataMovement)
            elif nameHeatmap == "Heatmap Klicks":
                return self.model.calculate_heatmap(self.model.dataClicks)
        except:
            print("Zugriff auf Heatmap nicht möglich" + nameHeatmap)

    def save_DataToCSV(self, nameDataset):
        """
        Save the email
        :param name Dataset:
        :return:
        """
        try:
            # self.model.nameDataset = nameDataset
            self.model.save_DataToCSV(self.model.dataMovement, nameDataset)
            #self.view.show_success(f'The email {email} saved!')
            print("Speichern erfolgreich!")

        except ValueError as error:
            # show an error message
            #self.view.show_error(error)

            print("Speichern nicht möglich")

