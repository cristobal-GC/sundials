
import math



class Sundial:
    
    type_of   = 'vertical'
    latitude  = 40.38709185162298    # degrees
    longitude = -3.701860979530921  # degrees; only required for OFFICIAL TIME

    def set_latitude(self,new_latitude):
        self.latitude = new_latitude
        print("New latitude set to",self.latitude)

    def set_longitude(self,new_longitude):
        self.longitude = new_longitude
        print("New longitude set to",self.longitude)




def fun_delta(N):
    '''
    This function provides the sun declination as a function of the day of the year.

    Inputs:
        N : integer. Is the day of the year
            1   : 01/Ene 
            80  : 21/Mar
            172 : 21/Jun
            264 : 21/Sep
            355 : 21/Dic
            365 : 31/Dic
    
    Outputs: 
        delta [rad]: is the sun declination 
    '''

    delta_deg = -23.45*math.cos( (N+10)*360/365*(math.pi/180) )
    delta = math.radians(delta_deg) 

    return delta





