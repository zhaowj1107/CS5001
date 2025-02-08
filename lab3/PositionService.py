# this is a class! we'll learn what a class is in Week 10 or so
class PositionService:

    # there can be only one of these PositionServices
    singleton = None

    # this is the code that runs when we make a Position Service
    def __init__(self):
        # Position Service has an x, which is set to 0
        self.x = 0
        # Position Service has an y, which is set to 0
        self.y = 0
        # the 'visible' variable is set to False by default
        self.position_is_set = False

    # this code makes sure we only have one Position Service at a time
    @classmethod
    def get_instance(cls):
        if PositionService.singleton == None:
            PositionService.singleton = PositionService()
        return PositionService.singleton

# these are the methods/functions we can call with dot
# notation with our PositionService

def record_position_x( x ):
    instance = PositionService.get_instance()
    instance.x = x

def record_position_y( y ):
    instance = PositionService.get_instance()
    instance.y = y

def record_position(x, y):
    instance = PositionService.get_instance()
    instance.x = x
    instance.y = y

def get_position_x():
    instance = PositionService.get_instance()
    return instance.x

def get_position_y():
    instance = PositionService.get_instance()
    return instance.y

def check_if_position_is_set():
    instance = PositionService.get_instance()
    return instance.position_is_set

def change_status_of_set_position(status ):
    instance = PositionService.get_instance()
    instance.position_is_set = status
