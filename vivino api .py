from typing import Text
from jsonpath_ng.parser import JsonPathParser
from numpy.lib.function_base import copy
import requests
import pandas as pd
import os
import time
import jsonpath
import json
import itertools
import os, shutil
import glob, os, shutil
from sanitize_filename import sanitize

def return_one(alist):
    if alist:
        return alist[0]
    else:
        return 'empty'

scraped_results = []
import numpy as np
pages = np.arange(1,2235, 1)
for x in pages:
    path = r'New folder'
    r = requests.get(
        "https://www.vivino.com/api/explore/explore",


        params = (
            ('country_code', 'US'),
            ('currency_code', 'USD'),
            ('grape_filter', 'varietal'),
            ('min_rating', '1'),
            ('order_by', ''),
            ('order', ''),
            ('page', str(x)),
            ('price_range_max', '500'),
            ('price_range_min', '10'),
            ('wine_type_ids^/[^/]', ['1', '2', '3', '4']),
        )
        
        ,
        
        headers = {
                'authority': 'www.vivino.com',
                'pragma': 'no-cache',
                'cache-control': 'no-cache',
                'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
                'accept': 'application/json',
                'x-requested-with': 'XMLHttpRequest',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
                'content-type': 'application/json',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1NFDLTaywNTUwUEuutA0NVksGEi5qBUDp9DTbssSizNSSxBy1_KIUW7X8pEpbtfKS6FigJJgyglDGEMpErdi2pAIA_yQcsg^%^3D^%^3D',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': 'first_time_visit=v9kHbNMswAfCTpvhZUncWZGoqsjv2^%^2FlO8^%^2F3ryXNgEjGm^%^2BtZGDRLn9Xll7cfR4vtZ9hD1MsaYH1O^%^2FBXoQiE4f20z1ipkDOPWDlw^%^3D^%^3D--6nhqa35cFGoZE8e7--^%^2Fp^%^2B62Ud7l^%^2BICTr3gjcL8lg^%^3D^%^3D; eeny_meeny_test_cro_2_v1=cYRbUDLUGYKnQDSBZuSOqd^%^2B3WqaQ0zHN90C^%^2FoJVG9MD0wLIhZLKYA5f1m3enOtgjp^%^2BAhZKhRfnHEPTH7Iow5Lg^%^3D^%^3D; __auc=bbaedda617b1c94dee0d8715750; _ga=GA1.2.792720468.1628272124; _hjid=81b8c426-748e-4305-b63e-ee9d00578920; _fbp=fb.1.1628272125863.956932232; _pin_unauth=dWlkPU16STVZbU00TVdVdFlqRTFNQzAwTlRGakxXSTNNamN0WXpRMk1UYzRZbVJpTmpWaw; _gid=GA1.2.408006668.1628456955; recently_viewed=y3rfcDQd3XnCx7QeiRN0WaIOusupEby5yIzu3AZonfLNRY0OTKCd0YsU11iX3WNRpSK5DQmdYopeXdu83^%^2B8V9wF1cZDVdz4V0KF0DdQkGcy0uEhhfdxdaDEXWWlwCnFXg7G5DIT8P2XgRNKTIjbrbZUt91APjQkVHi4oYho7VyqpKDoqkM^%^2F^%^2B5Zf2PL4Gx8IbTLObQg6eDUp^%^2Bimci6a5epld0GtAxgr^%^2F2BXXEqPq5l1q^%^2FNqP^%^2BYKn5qq8PuLKcqVE0zdfWN2bx31xfsLcT6ShHFFpEkcZQ0Np8LBvVaOyLR4YrguqynAgt6fQzwi1RhqYynHpwBhfxOjfLwzaCUvvOLXd7yh^%^2B03wvrTWXrABXpKj2msHTFuiRsmUoiAxXKMRN^%^2BJXR2lQDPJHOQpP3987XcweN^%^2FEIwIp90Zh^%^2FQXJeih66AAVgE6VcHmfbvekW6VT2YHmIv9NYw^%^3D--u32FBp0IhHCE8lXh--joUhOhilW^%^2Bv3V8DbD6Acnw^%^3D^%^3D; client_cache_key=Pi6UZa9Zb5^%^2BxtMwmM8W4GD^%^2BLJPaiT8pEprfNj02Aktg8MlaPKpSyUrKam^%^2FQS5Rr^%^2F^%^2BE7hVZF5yXT5pzVhmaKevFYLTyChUZ5LTfXTU5Xz6WclEfAFMDmcp8^%^2BVLvjShy^%^2BtnWbTBLXzXSqr--XNg91ngOMQiw^%^2BAfP--OZ6tRRtTLSg^%^2BwI^%^2BfK7VrJA^%^3D^%^3D; __asc=fe3db61217b397ee0ada00b345b; _hjIncludedInSessionSample=1; _hjAbsoluteSessionInProgress=0; _hp2_ses_props.3503103446=^%^7B^%^22ts^%^22^%^3A1628757245264^%^2C^%^22d^%^22^%^3A^%^22www.vivino.com^%^22^%^2C^%^22h^%^22^%^3A^%^22^%^2F^%^22^%^7D; t-ip=1; _tq_id.TV-8181459045-1.bb64=da83518ac43a7387.1628272126.0.1628757252..; _hp2_id.3503103446=^%^7B^%^22userId^%^22^%^3A^%^228417355197434239^%^22^%^2C^%^22pageviewId^%^22^%^3A^%^224608058409313074^%^22^%^2C^%^22sessionId^%^22^%^3A^%^221990790874286628^%^22^%^2C^%^22identity^%^22^%^3Anull^%^2C^%^22trackerVersion^%^22^%^3A^%^224.0^%^22^%^7D; _gat_vivinoTracker=1; cto_bundle=MxRm4l8lMkJ2cVltJTJGJTJGNjYya1U4c291elNwS29mamtnbFpjc3VjSklHRzNxb3pvZVBEdyUyQjJUcnpZZ2dpc00lMkJYRSUyRndGMUVDVzNQaW14TnFzMG0wS21wVFl1Y3hFTEdPMElCZlZKS01YdjlnbjdUMG9iZ2gxNnBwRiUyQmJhdThHbmlzZ0lnZ0RLeUN3SkM2T2d5OUhYRGtZek1xTTRVZyUzRCUzRA; tatari-cookie-test=75075821; tatari-session-cookie=b148474f-1d3d-41c5-19ce-4273b5746812; _ruby-web_session=kNuAwmsl3LvDHZp306oSU3XBGCDyDHxK3PbonSkH2SUXFQ3Vxq5e0v^%^2BxbIodhuOhFq8GMcRO^%^2FBgH^%^2BkcoDdNixz4RPpvKfcQsPKrHuHdG5MGCyEMnM31Gpyd9e^%^2B21Odd8IWUVG^%^2BdTyP5OVzWBjRigpgcl^%^2F777Zjg4tX68ZvkQpvqN7av^%^2BMu3ITW^%^2FXwkHrdhBkaYIq434EcBrV^%^2BEAcIcHLcwO^%^2FRWPU0iFlxrjLu7bHaMOcbMJtkq2cSiS^%^2BIMD1dvsQT1Obc7300r0G8bQ^%^2Fyjo1tcsjHwDAKZUu1aQqLM5L7cKrBevGxQuLruo5KMPfCxY0M70^%^2FASdNm8SvrY9DCxq7KlQQ0^%^2BOGqiZxhg1zVdyjudSI^%^2F9L2tyLnyqwULWMh6cEK2E2^%^2Bq62wccbroVqJUzbf25FKgip6dCTfJ1BThJUF5WihtHBBNOj^%^2B^%^2BByHpOQ6jMw6tvZchez^%^2BFVPSYprqIVn7soL1OiDzKtLXvTRnjnjYmevOWZcuYlNINXiC58FGCSSsxkB^%^2FNds1ZEJv7NZDDN2N0j4kCn7McZ2Krn9NEtc4F8RCLcPBwzfQdsvy^%^2Fsdnh^%^2FsCzdPP^%^2BGgpzhgcMW9bhl1qxAxQj2FZy4Lg9R7rCZ2YXeEItNhxHkn0Epnp^%^2F2UU7ONXPu2Mazhc^%^2BoryFJGRBCPktygIQvqXG7mBwx4tErUlyPPRX8UbwJySw35N7fZutDLdD7xvA^%^2BMQ7PipjKG0iBitZRV^%^2BSkN5apj^%^2FUVuZLVXc2gxE--ageC2g7hX3Sra^%^2FVV--SQ6F^%^2F2q8xh2Piwsz8JPpDg^%^3D^%^3D',
            }
         
    
                )

    print(x)
    print(r.status_code)
    results = []
    _DOWNLOAD_LABEL_SIZE = "bottle_medium"
    #wines_with_labels = [wine for wine in r.json()['explore_vintage']['matches'] if wine["vintage"]["image"]["variations"].get(_DOWNLOAD_LABEL_SIZE, None) is not None]
    #print(wines_with_labels)
    js = r.json()
    zong = jsonpath.jsonpath(js,'explore_vintage.matches.*')

    a = []
    for i in zong:
                       
        title = return_one(jsonpath.jsonpath(i,'$..vintage.name'))
        
        year = return_one(jsonpath.jsonpath(i,'$..vintage.year'))
        number = ("{}".format(year))
        
        price = return_one(jsonpath.jsonpath(i,'$..price.amount'))
                    
        img = return_one(jsonpath.jsonpath(i,'$..vintage.image.variations.bottle_medium'))
        if img == 'empty':
            img = return_one(jsonpath.jsonpath(i, '$..vintage.image.location'))
        
                      
        winery = return_one(jsonpath.jsonpath(i, '$..vintage.wine.winery.name'))
                      
        wine_Description = return_one(jsonpath.jsonpath(i, '$..vintage.wine.name'))
     
                

        import os

        # Directory
        directory = sanitize(title) 
        
        # Parent Directory path
        parent_dir = path

        # Path
        path2 = os.path.join(parent_dir, directory)

        # Create the directory
        
        try:
            os.makedirs(path2)
            print("Directory '% s' created" % directory)
        except FileExistsError:
                print("Directory " , path2 ,  " already exists") 


        import os.path

        save_path = path2



        man = os.path.join(save_path, "manufacturer.txt")         

        file1 = open(man, "wb")

        manufacture = sanitize(winery)
        
        file1.write(manufacture.encode("utf-8"))
    
        

    

        win = os.path.join(save_path, "wineDescription.txt")         

        file2 = open(win, "wb")

        st = sanitize(wine_Description + " " + number)
        

        file2.write(st.encode("utf-8"))
    
        
    
        pri = os.path.join(save_path, "price.txt")         

        file3 = open(pri, "wb")

        prices = price

        file3.write("{0}".format(prices).encode("utf-8"))

        
        

        IMG = os.path.join(save_path, directory +'.png')         

        file4 = open(IMG, "wb")

        

        file4.write(requests.get('http:'+img).content)

        

                
            
    
 