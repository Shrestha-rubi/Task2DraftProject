#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json, requests


#App id as signed up from openweathermap.org
APPID = 'b793a235076e755a4c7938d63c081d98'


#format of url when zipcode is given
def get_forecasturl_zipcode(zipcode):
    url = 'http://api.openweathermap.org/data/2.5/forecast?zip=%s&appid=%s' % (zipcode, APPID) 
    return  url


#format of url when city is given
def get_forecasturl_city(city):
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s' % (city, APPID)
    return url 


def main():


    #Allow the user to run the program multiple times
    while (True):


        #Ask the user for zip code or city
        user_input = input('Enter zip code or city: ')


        #Get the correct url based on input
        if user_input.isdecimal():
            url = get_forecasturl_zipcode(user_input)
        else :
            url = get_forecasturl_city(user_input)
        
        response = requests.get(url)


        #Check whether the connection was established
        try:
            response.raise_for_status()
            print('Connection was successful')
        except:
            print('Connection was not succesful')
            continue 


        weathers = json.loads(response.text)['list']
         
        #Display the weather informationi to the user
        print("Today's weather is " + weathers[0]['weather'][0]['description'])
        
        


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




