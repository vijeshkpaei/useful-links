import json
with open('error1.json') as json_file:
    data = json.load(json_file)
    for i in data:
        m=i
        for_region = data[m]['regions']
        filename = data[m]['filename']
        for regions in for_region:
            data_y = regions['shape_attributes']['all_points_y']
            data_x = regions['shape_attributes']['all_points_x']
            for allpoints_y in data_y:
                if allpoints_y > 273: # height
                    print(allpoints_y, " of ", filename)
            for allpoints_x in data_x:
                if allpoints_x > 424: # width
                    print(allpoints_x, " of ", filename)



