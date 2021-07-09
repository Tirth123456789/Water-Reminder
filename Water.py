import time
from plyer import notification

if  __name__ == "__main__":
      notification.notify(
            title = "Please Drink Water",
            message = "The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men About 11.5 cups (2.7 liters) of fluids a day for women These recommendations cover fluids from water, other beverages and food.",
            app_icon = "this is your icon file path",
            timeout = 5
            )
