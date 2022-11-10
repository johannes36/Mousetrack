class Controller:
    def __init__(self, model, view):
        self.model  = model
        self.view   = view

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

    def save_DataToCSV(self, nameDataset):
        """
        Save the email
        :param name Dataset:
        :return:
        """
        try:

            # save the model
            # self.model.nameDataset = nameDataset
            self.model.save_DataToCSV(self.model.dataMovement, nameDataset)

            # show a success message
            #self.view.show_success(f'The email {email} saved!')
            print("Speichern erfolgreich!")

        except ValueError as error:
            # show an error message
            #self.view.show_error(error)

            print("Speichern nicht möglich")