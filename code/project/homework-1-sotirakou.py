#Catherine Sotirakou
#04/11/1988
#"Homework 1"
#How old they are
year=input ("What year were you born?")
print(2017 - int(year))
age= 2017 - int(year)
#How many times their heart has beaten
#A human - 100 beats per minute
humanheart = (int(age)*525600 *100)
print("Your heart has beaten" , str(humanheart) , "times")
#How many times a blue whale's heart has beaten
#Blue whale - 10 beats per minute
bluewhale = (int(age)*525600 * 10 )
print("A blue whales heart has beaten", str(bluewhale) , "times")
#How many times a rabbit's hea * 10 rt has beaten
#A year has 525600 minutes and a bunny's heart bits 150 times per minute
rabbitheart = (int(age) *525600 *150 )
billionrabbit= (round(rabbitheart / 1000000000))
#print("A bunny's heart has beaten" , str(rabbitheart) ,"times")
#If the answer to (5) is more than a billion, say "XXX billion" instead of the very long raw number
if int(rabbitheart) > 1000000000:
 print( "A bunny's heart has beaten" , int(billionrabbit), "billion" , "times")
else:
  print ( "A bunny's heart has beaten" ,str(rabbitheart) , "times")
print("Isn't that fun?")
#How old they are in Venus years
#A year on Venus takes 225 Earth days.
venusyear= ((int(age) * 365) // 225)
print("You are", str(venusyear), "Venus years old")
#A year on Neptune lasts as long as about 165 years
neptuneyear=((int(age)*365 // 165))
print("You are", str(neptuneyear), "Neptune years old")
#Whether they are the same age as you, older or younger
myage=(2017 - int(1988))
compareage= abs(int(myage) - int(age))
print ("Our age difference is", int(compareage), "years")
#If older or younger, how many years difference
if int(age) > int(myage):
  print("Ha! You're older than me!")
elif int(age) < int(myage) :
  print("...Go away!!!")
elif int(age) == int(myage):
  print("Oh dear!Isn't that a perfect age?")
#If they were born in san even or odd year 
modulusyear= int(year) % 2
#print (int(modulusyear))
if int(modulusyear)==0:
  print ("You were born in an even year!")
elif int(modulusyear)==1:
  print ("You were born in an odd year!")
#How many times the Pittsburgh Steelers have won the Superbowl since their birth.
#NFL championships: 2009, 2006, 1980, 1979, 1976, 1975
if ( int(year)) <= 1975:
  print ( "The Pittsburgh Steelers have won the Superbowl 6 times since your birth.") 
elif ( int(year)) == 1976:
  print ("The Pittsburgh Steelers have won the Superbowl 5 times since your birth.")
elif (int(year)) <= 1979:
  print ("The Pittsburgh Steelers have won the Superbowl 4 times since your birth.")
elif (int(year)) == 1980:
  print ("The Pittsburgh Steelers have won the Superbowl 3 times since your birth.")
elif (int(year)) <= 2006:
  print ("The Pittsburgh Steelers have won the Superbowl 2 times since your birth.")
elif (int(year)) <= 2009:
  print ("The Pittsburgh Steelers have won the Superbowl 1 time since your birth.")
#Which US President was in office when they were born (1935 onward)
#    Franklin Delano Roosevelt, 1933-1945
#Harry S. Truman, 1945-1953
#Dwight David Eisenhower, 1953-1961
#John Fitzgerald Kennedy, 1961-1963
#Lyndon Baines Johnson, 1963-1969
#Richard Milhous Nixon, 1969-1974
#Gerald Rudolph Ford, 1974-1977
#James Earl Carter, Jr., 1977-1981
#Ronald Wilson Reagan, 1981-1989
#George Herbert Walker Bush, 1989-1993
#William Jefferson Clinton, 1993-2001
#George Walker Bush, 2001-2009
#Barack Hussein Obama, 2009-

if ( int(year)) <=1945:
  print ("Franklin Delano Roosevelt was in office when they were born")
elif (int(year)) <=1953:
  print ("Harry S. Truman was in office when they were born")
elif (int(year)) <= 1961:
  print ("Dwight David Eisenhower was in office when they were born")
elif (int(year)) <= 1963:
  print ("John Fitzgerald Kennedy was in office when they were born")
elif (int(year)) <= 1969:
  print ("Lyndon Baines Johnson was in office when they were born")
elif (int(year)) <=1974:
  print ("Richard Milhous Nixon was in office when they were born")
elif (int(year)) <= 1977:
  print ("Gerald Rudolph Ford was in office when they were born")
elif (int(year)) <= 1981:
  print ("James Earl Carter was in office when they were born")
elif (int(year)) <= 1989:
  print ("Ronald Wilson Reagan was in office when they were born")
elif (int(year)) <= 1993:
  print ("George Herbert Walker Bush was in office when they were born")
elif (int(year)) <= 2001:
  print ("William Jefferson Clinton was in office when they were born")
elif (int(year)) <= 2009:
  print ("George Walker Bush was in office when they were born")