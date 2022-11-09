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