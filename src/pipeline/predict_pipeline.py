import sys
import pandas as pd
from src.utils import load_object
from src.exception import CustomException

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)
            predictions = model.predict(data_scaled)

            return predictions

        except Exception as e:
            raise CustomException(e, sys) from e


class CustomData:
    def __init__(
        self,
        area: float,
        bedrooms: int,
        bathrooms: int,
        stories: int,
        parking: int,
        mainroad: str,
        guestroom: str,
        basement: str,
        hotwaterheating: str,
        airconditioning: str,
        prefarea: str,
        furnishingstatus: str
    ):
        self.area = area
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.stories = stories
        self.parking = parking
        self.mainroad = mainroad
        self.guestroom = guestroom
        self.basement = basement
        self.hotwaterheating = hotwaterheating
        self.airconditioning = airconditioning
        self.prefarea = prefarea
        self.furnishingstatus = furnishingstatus

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "area": [self.area],
                "bedrooms": [self.bedrooms],
                "bathrooms": [self.bathrooms],
                "stories": [self.stories],
                "parking": [self.parking],
                "mainroad": [self.mainroad],
                "guestroom": [self.guestroom],
                "basement": [self.basement],
                "hotwaterheating": [self.hotwaterheating],
                "airconditioning": [self.airconditioning],
                "prefarea": [self.prefarea],
                "furnishingstatus": [self.furnishingstatus]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys) from e
