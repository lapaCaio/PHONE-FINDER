import phonenumbers
from test import number

from phonenumbers import geocoder
from phonenumbers import carrier

ch_nmber = phonenumbers.parse(number, "CH")  #get the location of phone number
print(geocoder.description_for_number(ch_nmber, "en"))

service_nmber = phonenumbers.parse(number, "RO")  #get the
print(carrier.name_for_number(service_nmber, "en"))
