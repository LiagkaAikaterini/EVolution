# -*- coding: utf-8 -*-

from google.colab import drive
drive.mount('/gdrive')
import os
os.listdir('/gdrive/My Drive')
path='/gdrive/My Drive/'

filename = "/gdrive/My Drive/Colab Notebooks/electric_vehicles_data.json"
import json
with open(filename) as f:
  data = json.load(f)
company_names1=[]
for i in range(0,len(data['data'])):
  company_names1.append(data['data'][i]['brand'])
myset=set(company_names1)
company_names1=list(myset)

!pip install randomuser

pip install passlib

#Function to produce random datatimes
import random
from random import randrange
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


from datetime import datetime

d1 = datetime.strptime('1/1/2018 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

!pip install bcrypt

from randomuser import RandomUser
import hashlib
import bcrypt
from passlib.hash import sha512_crypt

# Generate a single user
user = RandomUser()

class Car_Owner:
  username=""
  email=""
  phone=""
  password=""
  points=0
  price_to_pay=0
  hashed_password =""
  sessionID =0


class Energy_Supplier:
  id=""
  company_name=""
  is_user=""
  username=""
  email=""
  phone=""
  password=""
  hashed_password =""
  whatamI = 1
  sessionID =0
class Payment:
  id=""
  value_paid=""
  payment_way=""
  data_time=""
  points_used=""
  car_owner_username=""
  bank_id=""

class Bank:
  id=""
  name=""

class Car_Manufacturer:
  id=""
  company_name=""
  is_user=""
  username=""
  password=""
  email=""
  phone=""
  hashed_password =""
  whatamI = 0
  sessionID =0

user_list = RandomUser.generate_users(100)
energy_suppliers=['Harz Energie','BS Energie','EV Energy Group (FCN)','eVgo Network','EVS Energieversorgung Sylt','Evway','EWB','EWI Energiewerke Isernhagen','Fenie Energía (Spain)','FLOW Charging','FORTISIS','GardaUno','Gnrgy','GoCharge (IE)','Greenflux']
car_manufacturers=[Car_Manufacturer() for i in range(len(company_names1))]
car_owners = [Car_Owner() for i in range(len(user_list))]
energy_supplier=[Energy_Supplier() for i in range(len(energy_suppliers))]
payment=[Payment() for i in range(len(car_owners))]
banks=[Bank() for i in range(0,4)]

bank=['City Union Bank','Federal Bank','Union Bank','National Bank']

for i in range(0,4):
  banks[i].id=i+1
  banks[i].name=bank[i]



j=0
for i in user_list:
  car_owners[j].username=i.get_username()
  car_owners[j].email=i.get_email()
  car_owners[j].password=i.get_password()
  car_owners[j].hashed_password  = sha512_crypt.encrypt(car_owners[j].password,rounds=1000)
  car_owners[j].phone=i.get_phone()
  car_owners[j].points=random.randint(0,10000)
  car_owners[j].sessionID =0
  #car_owners[j].price_to_pay=random.randint(0,1000)/10
  j=j+1

user_list = RandomUser.generate_users(len(energy_suppliers))
j=0
for i in user_list:
  energy_supplier[j].id=j+1
  energy_supplier[j].username=i.get_username() ############## insert from datafiles ???????????
  energy_supplier[j].email=i.get_email()
  energy_supplier[j].password=i.get_password()
  salt = bcrypt.gensalt()
  energy_supplier[j].hashed_password = sha512_crypt.encrypt(energy_supplier[j].password,rounds=1000)
  energy_supplier[j].phone=i.get_phone()
  energy_supplier[j].is_user=random.randint(0,1)
  energy_supplier[j].company_name = energy_suppliers[j]
  energy_supplier[j].whatamI = 1
  energy_supplier[j].sessionID =0
  j=j+1





user_list1 = RandomUser.generate_users(len(car_manufacturers))
for j in range(len(car_manufacturers)):
  car_manufacturers[j].id=j+1
  car_manufacturers[j].company_name=company_names1[j]
  car_manufacturers[j].is_user=random.randint(0,1)
  car_manufacturers[j].username=user_list1[j].get_username()
  car_manufacturers[j].password=user_list1[j].get_password()
  salt = bcrypt.gensalt()
  car_manufacturers[j].hashed_password =  sha512_crypt.encrypt(car_manufacturers[j].password,rounds=1000)
  car_manufacturers[j].email=user_list1[j].get_email()
  car_manufacturers[j].phone=user_list1[j].get_phone()
  car_manufacturers[j].whatamI = 0
  car_manufacturers[j].sessionID = 0

def pick_random(start,end):
  return random.randint(start,end-1)

"""# Car Generator"""

import random
from random import randint


def plate_gen():
  numbers='0123456789'

  L1=chr(randint(65,90))
  L2=chr(randint(65,90))
  L3=chr(randint(65,90))

  N1=random.choice(numbers)
  N2=random.choice(numbers)
  N3=random.choice(numbers)

  s=L1+L2+L3+"-"+N1+N2+N3
  return s

filename = "/gdrive/My Drive/Colab Notebooks/electric_vehicles_data.json"
import json

class car:
    ID=""
    model=""
    Car_Manufacturercompany_name=""
    Car_Ownerusername = ""
    usable_battery_size=""
    plates=""
    ac_charger=""
    dc_charger=""

class charger_type:
  ID=""
  type_=""
  phases=""
  fast_charging=""
  port=""

class has:
  Charger_TypeID=""
  CarID=""



with open(filename) as f:
  data = json.load(f)


  cars=[car() for i in range(len(data['data']))]

  for i in range(0,len(data['data'])):
      cars[i].ID=data['data'][i]['id']
      cars[i].model=data['data'][i]['model']
      # cars[i].Car_Manufacturercompany_name=data['data'][i]['brand']
      for j in car_manufacturers:
        if(data['data'][i]['brand'] == j.company_name):
          cars[i].Car_Manufacturercompany_name = j.id

      cars[i].usable_battery_size=data['data'][i]['usable_battery_size']
      cars[i].ac_charger=data['data'][i]['ac_charger']
      cars[i].dc_charger=data['data'][i]['dc_charger']
      cars[i].plates=plate_gen()

  user_set=set()
  for i in car_owners:
    if i in user_set:
      print("user already in set")
    user_set.add(i.username)
  j=0
  while (1):
    if (j>=len(cars)):
      break
    if (user_set):
      cars[j].Car_Ownerusername=user_set.pop()
      print("owner: "+cars[j].Car_Ownerusername)
      j+=1
      print(j)
    else:
      for i in car_owners:
        user_set.add(i.username)


  charger_ports_ac=set()
  charger_ports_dc=set()
  ac_phases=set()

  for i in range(0,len(data['data'])):
    if (cars[i].ac_charger):
      for j in range(0, len(cars[i].ac_charger['ports'])):
        charger_ports_ac.add(cars[i].ac_charger['ports'][j])
      ac_phases.add(cars[i].ac_charger['usable_phases'])
    if (cars[i].dc_charger):
      for j in range(0, len(cars[i].dc_charger['ports'])):
        charger_ports_dc.add(cars[i].dc_charger['ports'][j])
  # print(charger_ports_ac)
  # print(charger_ports_dc)
  # print(ac_phases)

  charger_types=[]
  id_inc=0
  for i in range (1,4):
    new_type=charger_type()
    charger_types.append(new_type)
    charger_types[id_inc].ID=id_inc+1
    charger_types[id_inc].type_='AC'
    charger_types[id_inc].phases=i
    charger_types[id_inc].port='type1'
    id_inc+=1

  for i in range (1,4):
    new_type=charger_type()
    charger_types.append(new_type)
    charger_types[id_inc].ID=id_inc+1
    charger_types[id_inc].type_='AC'
    charger_types[id_inc].phases=id_inc
    charger_types[id_inc].port='type2'
    id_inc+=1


  for i in range (len(charger_ports_dc)):
    new_type=charger_type()
    charger_types.append(new_type)
    charger_types[id_inc].ID=id_inc+1
    charger_types[id_inc].type_='DC'
    charger_types[id_inc].phases=0
    charger_types[id_inc].port=list(charger_ports_dc)[i]
    id_inc+=1

  # for i in range (0, len(charger_types)):
  #   print(charger_types[i].ID, charger_types[i].type_, charger_types[i].phases, charger_types[i].port)

  def get_charger_type (type_, phases, port):
    if (type_=='AC' and phases==1 and port=='type1'):
      return 1
    if (type_=='AC' and phases==2 and port=='type1'):
      return 2
    if (type_=='AC' and phases==3 and port=='type1'):
      return 3
    if (type_=='AC' and phases==1 and port=='type2'):
      return 4
    if (type_=='AC' and phases==2 and port=='type2'):
      return 5
    if (type_=='AC' and phases==3 and port=='type2'):
      return 6
    if (type_=='DC' and phases==0 and port=='tesla_ccs'):
      return 7
    if (type_=='DC' and phases==0 and port=='ccs'):
      return 8
    if (type_=='DC' and phases==0 and port=='chademo'):
      return 9
    if (type_=='DC' and phases==0 and port=='tesla_suc'):
      return 10

  has_relations=[]

  for i in range (0, len(data['data'])):
    if (cars[i].ac_charger):
      for j in range(0, len(cars[i].ac_charger['ports'])):
        temp=has()
        temp.Charger_TypeID=get_charger_type('AC', cars[i].ac_charger['usable_phases'], cars[i].ac_charger['ports'][j])
        temp.CarID=cars[i].ID
        has_relations.append(temp)
    if (cars[i].dc_charger):
      for j in range(0, len(cars[i].dc_charger['ports'])):
        temp=has()
        temp.Charger_TypeID=get_charger_type('DC', 0, cars[i].dc_charger['ports'][j])
        temp.CarID=cars[i].ID
        has_relations.append(temp)

month_to_number = {'Jan':1,
'Feb' : 2,
'Mar' : 3,
'Apr' : 4,
'May' : 5,
'Jun' : 6,
'Jul' : 7,
'Aug' : 8,
'Sep' : 9,
'Oct' : 10,
'Nov' : 11,
'Dec' : 12}

"""# Let's generate Charging Data"""

def its_a_date(date_str):
  my_date = datetime.strptime(date_str.split(" ",1)[0], "%d/%m/%Y").date()
  my_hour =  datetime.strftime(datetime.strptime(date_str.split(" ",1)[1], "%I:%M %p"),"%H:%M")
  return(str(my_date)+" "+str(my_hour))

import random
from datetime import datetime
protocols = ["OSCP","OCPP","PWM","LIN"]
def generate_total_km(car):

  events =dict()
  dates=[]
  for i in charging_events:
    if i.car_id == car:
      if i.total_km >0:
        events[i.date] = i.total_km
        dates.append(i.date)
  if(len(dates)>0):
    max = dates[0]
    for x, y in events.items():
      if(x>max and y!=0):
        max =x
    rand_km = random.randint(events[max],2000000)
    diff = events[max]
  else:
    diff = random.randint(0,2000000)
    rand_km = random.randint(diff,2000000)
  return [rand_km,diff]
def return_rand_car(owner):
  car_list=[]

  for i in cars:
    if i.Car_Ownerusername ==owner:
      car_list.append(i.ID)
  if (len(car_list)>1):
    return car_list[random.randint(0,len(car_list)-1)]
  else:
    if(len(car_list) ==0):
      print ("\n "+owner)
    return car_list[0]
def convert_td(timestamp_string):
  return str(int(timestamp_string[5:7]))+"/"+str(month_to_number[timestamp_string[8:11]])+"/"+str(timestamp_string[12:16]+" "+datetime.strptime(timestamp_string[17:22], "%H:%M").strftime("%I:%M %p"))


class Charging:
  def __init__(self, js_dat):
    self.id = js_dat["_id"]
    self.connection_time = js_dat["connectionTime"]
    self.disconnection_time = js_dat["disconnectTime"]
    self.done_charging_time=js_dat["doneChargingTime"]
    self.kWh_delivered = js_dat["kWhDelivered"]
    #self.date = js_dat["sessionID"].split("_")[4][0:10]
    self.date = convert_td(js_dat["connectionTime"])
    self.sessid = js_dat["sessionID"]
    self.Car_Ownerusername = car_owners[pick_random(0,len(car_owners))].username
    self.car_id = return_rand_car(self.Car_Ownerusername)
    self.stationID = js_dat["stationID"]
    self.position = js_dat["spaceID"]
    self.battery_percent_begin = random.randint(0, 100)
    self.battery_percent_end = random.randint(self.battery_percent_begin, 100)
    self.total_km=0
    self.km_between_charges=0
    self.protocol = random.choice(protocols)
    self.supplierID = ""
    self.charging_price =0
    self.still_owed = 0
  def print_charging(self):
    print("id: "+str(self.id)+" date: "+self.date+" connection time: "+str(self.connection_time)+" done_charging_time "+str(self.done_charging_time)+" kWh_delivered "+str(self.kWh_delivered)+" date: "+str(self.date) + " Car_Ownerusername "+str(self.Car_Ownerusername)+" stationID: "+ str(self.stationID)+" battery percent begin "+str(self.battery_percent_begin)+" battery percent end: "+str(self.battery_percent_end)+" car id: "+self.car_id+" total km: "+str(self.total_km)+" between: "+str(self.km_between_charges)+" protocol "+self.protocol)


filename = "/gdrive/My Drive/Colab Notebooks/acn_data/caltech_acndata_sessions_33month.json"
with open(filename) as f:
  data = json.load(f)
  counter = 0
  charging_events =[]
  for i in data["_items"]:
    charger = Charging(i)
    charging_events.append(charger)
    #charger.print_charging()
print(len(charging_events))
cars_visited = set()
for i in charging_events:
  if i.car_id not in cars_visited:
    cars_visited.add(i.car_id)
  dates = []
  events = dict()
  dates.append(its_a_date(i.date))
  events[its_a_date(i.date)] = i
  for j in charging_events:
    if j.car_id ==i.car_id and j.date != i.date:
      my_date = its_a_date(j.date)
      dates.append(my_date)
      events[my_date] = j
  counter = 0
  dates = sorted(dates,reverse=False)
  while counter<len(dates):
    if counter ==0:
      events[dates[counter]].km_between_charges = 0
      events[dates[counter]].total_km = random.randint(0,600)
      prev = events[dates[counter]]
    else:
      try:
        events[dates[counter]].total_km = random.randint(prev.total_km,600+prev.total_km)
      except:
        print("Errot "+str(events[dates[counter]]))
      events[dates[counter]].km_between_charges = events[dates[counter]].total_km - prev.total_km
      prev = events[dates[counter]]
    counter +=1

"""# Let's generate Station and Charging Position Data

---


"""

class station:
  ID=""
  euro_per_kWh=""
  payment_types=""
  is_active=""
  address_info=""
  country=""
  postal_code=""
  operator=""
  def print_station(self):
    print("id: "+str(self.ID)+" euro per kwh: "+str(self.euro_per_kWh)+" payment types: "+str(self.payment_types)+" is active: "+str(self.is_active)+" address info: "+str(self.address_info)+" country: "+self.country+" postal_code"+self.postal_code)

class charging_position:
  active=""
  taken=""
  stationID=""
  name=""
  operator=""
  supplierID=""
  def print_charging_position(self):
    print("active: "+str(self.active)+" taken: "+str(self.taken)+" StationID: "+str(self.stationID)+"  name: "+self.name+" supplier id:"+str(self.supplierID))

!pip install names

def generate_random_name(oc_set):
  letters = ["A","B","C"]
  while 1:
    first = random.choice(letters)
    second = random.choice(letters)
    num = random.randint(100,999)
    fin = first+second+"-"+str(num)
    if fin not in oc_set:
      break
  return fin
  #επί της ουσίας πριν υπήρχαν πολλά charging events για την ίδια θέση,ωστόσο εμείς κρατούσαμε μόνο ένα. Επομένως, σε μεταγενέστερες επαναλήψεις απλά "κόβαμε" το event
  #αν βλέπαμε ότι έχει γίνει στον ίδιο σταθμό και space. Τώρα, αν βρω ίδιο όνομα σταθμού και space παράγω νέο όνομα space και ενημερώνω αντίστοιχα την αντίστοιχη τιμή
  #στον πίνακα των events

def create_charg(station,name):
    station_ids.add(station)
    temp=charging_position()
    temp.operator=names.get_full_name()
    temp.active=random.randint(0,1)
    temp.supplierID = (random.choice(energy_supplier)).id
    if(temp.active == 0):
      temp.taken = 0
    else:
      temp.taken=random.randint(0,1)
    temp.stationID=i.stationID
    temp.name=name
    charging_positions.append(temp)

import names
station_ids=set()
charging_positions=[]
filename2 = "/gdrive/My Drive/Colab Notebooks/charging_points_europe_json/poi.json"
#print(len(charging_events))
charg_dict = dict()
with open(filename2) as f2:

  #lu  = RandomUser.generate_users(len(charging_events)) + RandomUser.generate_users(len(charging_events)) +RandomUser.generate_users(len(charging_events))+RandomUser.generate_users(len(charging_events))+RandomUser.generate_users(len(charging_events))+RandomUser.generate_users(3117)
  #lu  = RandomUser.generate_users(1)
  #print(len(lu))
  charg_pos = set()
  charg_name = set()
  for i in charging_events:
    if(i.stationID,i.position) in charg_pos:
      if len(charg_dict[i.stationID]["pos"])<10:
        i.position = generate_random_name(charg_name)
        charg_pos.add((i.stationID,i.position))
        charg_name.add(i.position)
        charg_dict[i.stationID]["prev"] = 0
        charg_dict[i.stationID]["pos"].append(i.position)
        create_charg(i.stationID,i.position)
        charg_dict[i.stationID][i.position] = 1
      else:
          if charg_dict[i.stationID]["prev"] >=10:
            charg_dict[i.stationID]["prev"]=0
          y=charg_dict[i.stationID]["pos"][charg_dict[i.stationID]["prev"]]
          i.position =y
          charg_dict[i.stationID][y] +=1

          charg_dict[i.stationID]["prev"]+=1
    else:
      if i.stationID not in station_ids:
        station_ids.add(i.stationID)
      charg_dict[i.stationID] = dict()
      charg_dict[i.stationID]["pos"]=[]
      charg_dict[i.stationID][i.position] = 1
      charg_pos.add((i.stationID,i.position))
      charg_name.add(i.position)
      charg_dict[i.stationID]["pos"].append(i.position)
      create_charg(i.stationID,i.position)


  for x in station_ids:
    print(charg_dict[x]["pos"])
    for y in charg_dict[x]["pos"]:
      print (charg_dict[x][y])

  stations=[]
  payment_types=['Cash', "Pos", "Credit_note", "Pay_later_in_app"]

  for id in station_ids:
    #l1= RandomUser.generate_users(1)
    temp=station()
    temp.ID=id
    temp.euro_per_kWh=random.uniform(0.069, 0.399 )
    temp.operator=names.get_full_name()
    temp.payment_types="Cash"+","+"Pos"+","+"Pay_later_in_app"
    bit=random.randint(0,1)
    if (bit):
      temp.payment_types=temp.payment_types+","+"Credit_note"
    temp.is_active=1
    stations.append(temp)



  poi_data = []
  for line in open(filename2, 'r'):
    poi_data.append(json.loads(line))

  for i in range (0, len(stations)):
    stations[i].address_info=poi_data[i]['AddressInfo']['Title']
    if (poi_data[i]['AddressInfo']['AddressLine1']):
      stations[i].address_info=stations[i].address_info+" "+poi_data[i]['AddressInfo']['AddressLine1']
    if (poi_data[i]['AddressInfo']['AddressLine2']):
      stations[i].address_info=stations[i].address_info+" "+poi_data[i]['AddressInfo']['AddressLine2']
    if poi_data[i]['AddressInfo']['Town']:
        stations[i].address_info=stations[i].address_info+" "+poi_data[i]['AddressInfo']['Town']
    if poi_data[i]['AddressInfo']['StateOrProvince']:
      stations[i].address_info=stations[i].address_info+" "+poi_data[i]['AddressInfo']['StateOrProvince']
    if poi_data[i]['AddressInfo']['Postcode']:
      stations[i].postal_code=poi_data[i]['AddressInfo']['Postcode']
    stations[i].country=poi_data[i]['AddressInfo']['Country']['Title']

#for i in stations:
 # i.print_station()
#print("NEW")
#for j in charging_positions:
 # j.print_charging_position()

"""# Let's define supplier id for each charging event"""

for k in charging_events:
  for m in charging_positions:
    if(k.position == m.name and k.stationID == m.stationID):
      k.supplierID = m.supplierID
      break
  #print(k.supplierID)

"""# Let's define charging_price for wach charging event"""

for k in charging_events:
  for m in stations:
    if(k.stationID == m.ID):
      #print(float(m.euro_per_kWh)*float(k.kWh_delivered))
      k.charging_price = float(m.euro_per_kWh)*float(k.kWh_delivered)
      k.still_owed = float(m.euro_per_kWh)*float(k.kWh_delivered)
      break
  #print (k.charging_price)

for k in charging_events:
  for m in car_owners:
    if(k.Car_Ownerusername == m.username):
      m.price_to_pay += k.charging_price
      #print (m.price_to_pay)

'''
class pays_up:
  PaymentID = ""
  ChargingID = ""
pays_up_relations = []
J=0
payments=[]
for k in car_owners:
  print("to_p long before: "+ str(k.price_to_pay))
  amount=random.randint(int(k.price_to_pay/5), int(k.price_to_pay))
  totalsum=0   #το ποσο που εχουμε εξοφλισει μεσω πληρωμων για τον χρηστη μεχρι αυτη τη στιγμη
  left_from_amount = amount
  for j in range(0,random.randint(1,10)):  #θα κανω το πολυ δεκα πληρωμες για το ποσο που θελω να εξοφλισω για αυτο τον χρηστη
    money=random.randint(int(left_from_amount/5), left_from_amount)  #επιλεγω ποσο για την πρωτη πληρωμη
    amount=amount-money   #για τις υπολοιπες πληρωμες μενει το υπολοιπο
    #totalsum=totalsum - amount  #ποσο που εχω πληρωσει μεχρι τωρα
    #totalsum = totalsum +money
    temp=Payment()  #φτιαχνω την πληρωμη μου
    temp.id=J   #πρεπει να αρχικοποιησω τα πεδια ολα
    temp.value_paid=money
    temp.car_owner_username=k.username
    #εδω και τα υπολοιπα στοιχεια
    amount_left=money  #τι ποσο απο αυτο που θελω να εξοφλει η πληρωμη αυτη εχω εξοφλισει μεχρι τωρα
    for m in charging_events:  #ψαχνω φορτισεις να συνδεσω με την πληρωμη
      if (m.Car_Ownerusername==k.username):  #με νοιαζουν μονο οι φορτισεις που εχω για τον συγκεκριμενο χρηστη
        if (m.still_owed==0):   #αν η φορτιση αυτη ειναι ηδη εξοφλημενη ψαχνω την επομενη
          #print("hello")
          continue;

        if (amount_left>m.still_owed):  #αν στην φορτιση μενει ενα ποσο για εξοφλιση, μικροτετο απο το ποσο που μου μενει να εξοφλισω σε αυτην την πλρωμη:
          totalsum +=m.still_owed
          print("still: "+str(m.still_owed))
          amount_left=amount_left-m.still_owed  #χρησιμοποιω ολο το ποσο της φορτισης και μου μενει ακομα καμποσο να εξοφλισω
          m.still_owed=0   #η φορτιση εξοφληθηκε
          obj=pays_up()   #συσχετιση πληρωμης με την συγκεκριμενη φορτιση
          obj.PaymentID=temp.id
          obj.ChargingID=m.id
          pays_up_relations.append(obj)
        else:   #ενναλακτικα το μη εξοφλημενο ποσο της φορτισης ειναι μεγαλυτερο απο αυτο που μου μενει για την πληρωμη αυτη
          totalsum += amount_left
          print("left: "+ str(amount_left))
          m.still_owed=m.still_owed-amount_left   #θα μεινει ενα μερος της φορτισης μη εξοφλημενο
          amount_left=0   #εχω τελειωσει με ολο το ποσο για την παρουσα πληρωμη
          obj=pays_up()   #συσχετιση πληρωμης φορτισης
          obj.PaymentID=temp.id
          obj.ChargingID=m.id
          pays_up_relations.append(obj)
      if (amount_left==0):   #αν εχω εξοφλησει ολο το ποσο που ηθελα για την παρουσα πληρωμη δεν χρειαζεται να ψαξω αλλες φορτισεις
        break;
      #totalsum+=money-amount_left #εχω μολις τελειωσει με το ποσο που επελεξα για την πρωτη μου πληρωμη, αρα το προσθετω στο συνολικο ποσο που εχω εξοφλισει μεχρι τωρα
      #print(totalsum)
    payments.append(temp)   #προσθετω και την πληρωμη μου στις πληρωμες
    J=J+1  #το επομενο id για την επομενη πληρωμη
    if (amount==0): #αν το ποσο που μενει σε σχεση με το αρχικο ποσο που θελω να εξοφλισω για αυτον τον χρηστη ειναι 0 τοτε δε χρειαζεται να φτιαξω αλλες πληρωμες
      break
    print("to_p before: "+ str(k.price_to_pay))
    k.price_to_pay-=totalsum  #εχω τελειωσει με οσες πληρωμες επελεξα να κανω για αυτον τον χρηστη,ισως ομως να μην επελεξα αρκετες με το randint για να εξοφλισω ολο το ποσο του, χρωσταει ακομα οσα χρωσταγε μειον οσα καταφερα να εξοφλισω με πληρωμες
    print("to_p after: "+ str(k.price_to_pay))
    print("total: "+ str(totalsum))
'''

'''
for i in car_owners:
  print(i.username)
  for j in payments:
    if(i.username == j.car_owner_username):
      print(str(j.id)+" "+str(j.value_paid))
'''

'''
for k in car_owners:
  tot = 0
  lot =0
  for m in charging_events:
    if(k.username == m.Car_Ownerusername):
      tot += m.charging_price
  for j in payments:
     if(k.username == j.car_owner_username):
      lot += j.value_paid
  print (str(tot)+" "+str(lot)+" "+str(k.price_to_pay))
'''

class in_program_with:
  monthly_charge=""
  discount=""
  Car_Ownerusername=""
  Energy_SupplierID=""

in_program_with_relations=[]

for i in car_owners:
  a=random.randint(0,1)
  if a:
    supplier=random.choice(energy_supplier)
    temp=in_program_with()
    temp.Car_Ownerusername=i.username
    temp.Energy_SupplierID=supplier.id
    b=random.randint(0,1)
    if b:
      temp.discount=random.randint(3,20)
      temp.monthly_charge=-1
    else:
      temp.monthly_charge=random.randint(100,1000)
      temp.discount=-1
    in_program_with_relations.append(temp)

# for i in in_program_with_relations:
#   print(i.monthly_charge, i.discount, i.Energy_SupplierID)
#   print(i.Car_Ownerusername)

# print(len(in_program_with_relations))

class supports:
  Charger_TypeID=""
  StationID=""

supports_relations=[]
sup_rel = set()
for i in stations:
  carid_set=set()
  for j in charging_events:
    if (i.ID==j.stationID):
      carid_set.add(j.car_id)
  for a in carid_set:
    for k in has_relations:
      if (k.CarID==a):
        if(k.Charger_TypeID,i.ID) not in sup_rel:
          sup_rel.add((k.Charger_TypeID,i.ID))
          temp=supports()
          temp.Charger_TypeID=k.Charger_TypeID
          temp.StationID=i.ID
          supports_relations.append(temp)

class Evaluates:
  car_owner=""
  station_id =""
  evaluation =""
  def print_evaluation(self):
    print("car_owner: "+ self.car_owner+" station id: "+str(self.station_id)+" evaluation: "+str(self.evaluation))
evaluations=[]
ev_set = set()
for i in car_owners:
  l=random.randint(0,40)
  for j in range(0,l):
    l2 = random.randint(0,len(stations)-1)
    if(i.username,stations[l2].ID) not in ev_set:

      temp = Evaluates()
      temp.car_owner = i.username
      temp.station_id = stations[l2].ID
      temp.evaluation = random.randint(0,10)
      evaluations.append(temp)
      ev_set.add((i.username,stations[l2].ID))

payment_ways=['Cash','Visa','MasterCard','American Express','Paypal','Discover Network']
class pays_up:
  PaymentID = ""
  ChargingID = ""
pays_up_relations = []
J=0
for k in car_owners:
  for m in charging_events:
    if k.username == m.Car_Ownerusername:
      a = random.randint(0,1)
      if a:
        temp=Payment()  #φτιαχνω την πληρωμη μου
        temp.id=J+1   #πρεπει να αρχικοποιησω τα πεδια ολα
        temp.value_paid=m.charging_price
        temp.car_owner_username=k.username
        temp.points_used = random.randint(0,200)
        temp.payment_way = random.choice(payment_ways)
        temp.bank_id = random.randint(1,4)
        if(J<100):
          print("id: "+str(temp.id))
        b = random.randint(0,1)
        if b:
          temp.data_time = m.date
        else:
          d1 = datetime.strptime(m.date, '%d/%m/%Y %I:%M %p')
          d2 = datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')
          temp.data_time = random_date(d1,d2)

        m.still_owed=0
        k.price_to_pay -= temp.value_paid
        obj = pays_up()
        obj.ChargingID= m.id
        obj.PaymentID=temp.id
        pays_up_relations.append(obj)
        payment.append(temp)
        J+=1
# for i in range(0,200):
#   print(str(payment[i].id) + " "+ str(payment[i].value_paid)+" "+str(payment[i].car_owner_username)+" date: "+ str(payment[i].data_time))

"""# Εισαγωγές"""

import csv
payment_list=[]
for i in payment:
  cur=[]
  cur.append(i.id)
  cur.append(i.value_paid)
  cur.append(i.payment_way)
  cur.append(i.data_time)
  cur.append(i.points_used)
  cur.append(i.car_owner_username)
  cur.append(i.bank_id)
  payment_list.append(cur)


with open('/gdrive/My Drive/Colab Notebooks/payments.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in payment_list[100:]:
      wr.writerow(i)

pays_up_list=[]
for i in pays_up_relations:
  cur=[]
  cur.append(i.PaymentID)
  cur.append(i.ChargingID)
  pays_up_list.append(cur)
print(pays_up_list[0:200])

with open('/gdrive/My Drive/Colab Notebooks/pays_up.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in pays_up_list:
      wr.writerow(i)

energy_supplier_list=[]
for i in energy_supplier:
  cur=[]
  cur.append(i.id)
  cur.append(i.company_name)
  cur.append(i.is_user)
  cur.append(i.username)
  cur.append(i.hashed_password)
  cur.append(i.email)
  cur.append(i.phone)
  cur.append(i.whatamI)
  cur.append(i.sessionID)
  energy_supplier_list.append(cur)


with open('/gdrive/My Drive/Colab Notebooks/energy_supplier_list.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in energy_supplier_list:
      wr.writerow(i)


energy_supplier_user_list=[]
for i in energy_supplier:
  cur=[]
  cur.append(i.username)
  cur.append(i.password)

  energy_supplier_user_list.append(cur)

with open('/gdrive/My Drive/Colab Notebooks/energy_supplier_user_list.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in energy_supplier_user_list:
      wr.writerow(i)

car_manufacturers_list=[]
for i in car_manufacturers:
  cur=[]
  cur.append(i.id)
  cur.append(i.company_name)
  cur.append(i.is_user)
  cur.append(i.username)
  cur.append(i.hashed_password)
  cur.append(i.email)
  cur.append(i.phone)
  cur.append(i.whatamI)
  cur.append(i.sessionID)
  car_manufacturers_list.append(cur)

with open('/gdrive/My Drive/Colab Notebooks/car_manufacturers_list.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in car_manufacturers_list:
      wr.writerow(i)

car_manufacturers_user_list=[]
for i in car_manufacturers:
  cur=[]
  cur.append(i.username)
  cur.append(i.password)
  car_manufacturers_user_list.append(cur)

with open('/gdrive/My Drive/Colab Notebooks/car_manufacturers_user_list.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in car_manufacturers_user_list:
      wr.writerow(i)

car_owner_list=[]
for i in car_owners:
  cur=[]
  cur.append(i.username)
  cur.append(i.hashed_password)
  cur.append(i.email)
  cur.append(i.phone)
  cur.append(i.price_to_pay)
  cur.append(i.points)
  cur.append(i.sessionID)
  car_owner_list.append(cur)

with open('/gdrive/My Drive/Colab Notebooks/car_owner_list.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in car_owner_list:
      wr.writerow(i)

car_owner_user_list=[]
for i in car_owners:
  cur=[]
  cur.append(i.username)
  cur.append(i.password)
  car_owner_user_list.append(cur)
with open('/gdrive/My Drive/Colab Notebooks/car_owner_user_list.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in car_owner_user_list:
      wr.writerow(i)

bank_list = []
for i in banks:
  cur=[]
  cur.append(i.id)
  cur.append(i.name)
  bank_list.append(cur)
with open('/gdrive/My Drive/Colab Notebooks/bank_list.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in bank_list:
      wr.writerow(i)

station_list = []
for i in stations:
  cur=[]
  cur.append(i.ID)
  cur.append(i.operator)
  cur.append(i.euro_per_kWh)
  cur.append(i.payment_types)
  cur.append(i.is_active)
  cur.append(i.address_info)
  cur.append(i.postal_code)
  cur.append(i.country)
  station_list.append(cur)
with open('/gdrive/My Drive/Colab Notebooks/station_list.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in station_list:
      wr.writerow(i)

charging_positions_list = []
for i in charging_positions:
  cur=[]
  cur.append(i.name)
  cur.append(i.operator)
  cur.append(i.active)
  cur.append(i.taken)
  cur.append(i.stationID)
  cur.append(i.supplierID)
  charging_positions_list.append(cur)
with open('/gdrive/My Drive/Colab Notebooks/charging_positions_list.csv', 'w', newline='') as myfile:
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  for i in charging_positions_list:
    wr.writerow(i)

car_list = []
for i in cars:
  cur=[]
  cur.append(i.ID)
  cur.append(i.plates)
  cur.append(i.model)
  cur.append(i.usable_battery_size)
  cur.append(i.Car_Ownerusername)
  cur.append(i.Car_Manufacturercompany_name)
  car_list.append(cur)
with open('/gdrive/My Drive/Colab Notebooks/car_list.csv', 'w', newline='') as myfile:
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  for i in car_list:
    wr.writerow(i)

charger_type_list=[]
for i in charger_types:
  cur =[]
  cur.append(i.ID)
  cur.append(i.type_)
  cur.append(i.phases)
  cur.append(i.port)
  charger_type_list.append(cur)

with open('/gdrive/My Drive/Colab Notebooks/charger_type_list.csv', 'w', newline='') as myfile:
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  for i in charger_type_list:
    wr.writerow(i)

charging_events_list=[]
for i in charging_events:
  cur =[]
  cur.append(i.id)
  cur.append(i.connection_time)
  cur.append(i.disconnection_time)
  cur.append(i.done_charging_time)
  cur.append(i.kWh_delivered)
  cur.append(i.protocol)
  cur.append(i.battery_percent_begin)
  cur.append(i.battery_percent_end)
  cur.append(i.date)
  cur.append(i.charging_price)
  cur.append(i.still_owed)
  cur.append(i.total_km)
  cur.append(i.km_between_charges)
  cur.append(i.Car_Ownerusername)
  cur.append(i.car_id)
  cur.append(i.stationID)
  cur.append(i.position)
  cur.append(i.supplierID)

  charging_events_list.append(cur)

with open('/gdrive/My Drive/Colab Notebooks/charging_events_list.csv', 'w', newline='') as myfile:
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  for i in charging_events_list:
    wr.writerow(i)

has_relations_list=[]
for i in has_relations:
  cur=[]
  cur.append(i.Charger_TypeID)
  cur.append(i.CarID)
  has_relations_list.append(cur)
with open('/gdrive/My Drive/Colab Notebooks/has_relations_list.csv', 'w', newline='') as myfile:
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  for i in has_relations_list:
    wr.writerow(i)

supports_relations_list=[]
for i in supports_relations:
  cur=[]
  cur.append(i.Charger_TypeID)
  cur.append(i.StationID)
  supports_relations_list.append(cur)

with open('/gdrive/My Drive/Colab Notebooks/supports_relations_list.csv', 'w', newline='') as myfile:
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  for i in supports_relations_list:
    wr.writerow(i)

evaluations_list=[]
for i in evaluations:
  cur=[]
  cur.append(i.car_owner)
  cur.append(i.station_id)
  cur.append(i.evaluation)
  evaluations_list.append(cur)

with open('/gdrive/My Drive/Colab Notebooks/evaluations_list.csv', 'w', newline='') as myfile:
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  for i in evaluations_list:
    wr.writerow(i)

# class in_program_with:
#   monthly_charge=""
#   discount=""
#   Car_Ownerusername=""
#   Energy_SupplierID=""

in_program_with_relations_list=[]
for i in in_program_with_relations:
  cur=[]
  cur.append(i.monthly_charge)
  cur.append(i.discount)
  cur.append(i.Car_Ownerusername)
  cur.append(i.Energy_SupplierID)
  in_program_with_relations_list.append(cur)

with open('/gdrive/My Drive/Colab Notebooks/in_program_with_relations_list.csv', 'w', newline='') as myfile:
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  for i in in_program_with_relations_list:
    wr.writerow(i)

pip install passlib

from passlib.hash import sha512_crypt

pip install RandomUser

from randomuser import RandomUser
import csv
user_list = RandomUser.generate_users(1)
total=[]
total1 =[]
cur =[]
car =[]
for i in user_list:
  uname = i.get_username()
  cur.append(uname)
  car.append(uname)
  pas = i.get_password()
  car.append(pas)
  cur.append(sha512_crypt.encrypt(pas, rounds=1000))
  cur.append(i.get_email())
  cur.append(i.get_phone())
  cur.append(0)
print(cur)
print(car)
total.append(cur)
total1.append(car)
with open('/gdrive/My Drive/Colab Notebooks/admin_list.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in total:
      wr.writerow(i)

with open('/gdrive/My Drive/Colab Notebooks/admin_user_list.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in total1:
      wr.writerow(i)
