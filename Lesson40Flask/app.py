# bolilerplate for flask app
from flask import Flask, render_template, request

app = Flask(__name__)

# hardcoded news list
news_item =  {
    'title': 'Hezbollah strikes in Majdal Shams',
    'content': 'This is the best news you have ever heard',
    'img': 'https://i.abcnewsfe.com/a/99e4e04c-7f53-4804-9dac-c513a28ac66b/hezbollah-lebanon-rally-gty-jt-231010_1696955333183_hpMain_16x9.jpg?w=992'
}

news_item2 = {
    'title': 'Bibi is back to Israel',
    
    'content': 'Prime Minister Benjamin Netanyahu landed in Israel on Sunday afternoon, having returned early from his diplomatic trip to the US following the attack on Majdal Shams on Saturday, the Prime Ministers Office reported.',
    'img': 'https://static.timesofisrael.com/www/uploads/2023/10/bibimad-640x400.jpg'
}

news_item3 = {
    'title' : 'Security cabinet discusses response to Hezbollah attack',
    'content': 'Security cabinet discusses response to Hezbollah attack on Majdal Shams soccer field Funerals held for most of 12 kids killed in strike * Child still missing * US, Britain, France condemn attack * Druze community mourns as some call for Lebanon to ',
    'img': 'https://static.timesofisrael.com/www/uploads/2024/07/image-26-1024x640.jpg'
}
news_item4 = {
    'title' : 'Security cabinet discusses response to Hezbollah attack',
    'content': 'Security cabinet discusses response to Hezbollah attack on Majdal Shams soccer field Funerals held for most of 12 kids killed in strike * Child still missing * US, Britain, France condemn attack * Druze community mourns as some call for Lebanon to ',
    'img': 'https://static.timesofisrael.com/www/uploads/2024/07/image-26-1024x640.jpg'
}

news_list = [news_item,news_item2,news_item3, news_item4, news_item,news_item,news_item,news_item,news_item,news_item,]

#  in real life it will be something like that
# news_list_from_db = get_list_from_db()

days = ['Sunday', 'Friday', 'Saturday']

@app.route('/')
def welcome():
    return render_template('welcome.html', today = '2024-28-07', show_image = True, news_list = news_list)


@app.route('/showFavorityFlower')
def showFavorityFlower():
    
    return render_template('flowers.html', flower = 'lily', error = "wrong flower")


@app.route('/days')
def show_days():
    return render_template('days.html', days = days)    

@app.route('/days/<selected_day>')
def show_selected_day(selected_day):
    error = None
    if (selected_day not in days):
        error = 'Day not found'
    return render_template('days.html', days = days, selected_day = selected_day, error = error) 

@app.route('/addDay', methods = ['POST', 'GET'])
def addDay():
    error = None
    new_day = request.form['day']    
    if new_day not in days:
        days.append(new_day)
    else: # day already exists
        error = 'Day already exists'
    return render_template('days.html', days = days, error = error)
    






if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
    
    

# create  flask app 
# add route /showFavorityFlower
# in the app you should present your favorite flower
# <h1>My favorite flower is: {{flower}}</h1>    
# flower should be the parameter coming in reder_template
# if flower is rose the page should show a picture of a rose
# <img src = "https://www.classicroses.co.uk/media/catalog/product/cache/6e9e0330b981bee0eba0610998958c79/y/o/you_re_beautiful_bm_2019_2_1000px.jpg">