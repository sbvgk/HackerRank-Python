import request
import json
import xlsxwriter
import pandas

def write_to_excel(json1_object):
    my_fate=  xlsxwriter.Workbook('C:/Users/shiva/city_list2.xlsx')
    worksheet=my_fate.add_worksheet('sheet1')
    my_fate.close()
    id=[]
    name=[]
    country=[]
    coord=[]



    for x in json1_object:
        id.append(x['id'])
        name.append(x['name'])
        country.append(x['country'])
        coord.append(x['coord'])




    df1=pandas.DataFrame({'id':id,'name':name,'country':country,'coord':coord})

    df1.to_excel('C:/Users/shiva/city_list2.xlsx',index=False)
    


with open('C:/Users/shiva/city.list.json',encoding="utf8") as abc:
    data=json.load(abc)


    write_to_excel(data)

    