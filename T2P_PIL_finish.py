from PIL import Image, ImageDraw, ImageFont

# Settings
#W, H = (224, 224)

# Font 字型
#font = ImageFont.load_default("D://Users//xkllkx//Desktop//all_program//text_2_picture//Pixel.ttf")
font = ImageFont.truetype("D://Users//xkllkx//Desktop//all_program//text_2_picture//Silver.ttf", 24, encoding='utf-8')
font = ImageFont.truetype("Silver.ttf",60)
#font = ImageFont.load_default()


im = Image.open("f_w_model.jpg")
#im=Image.new("RGBA", (500,250),(248,247,216)) #生成空白頁

draw = ImageDraw.Draw(im)

def blood_lengh1_decrease(image,start_XY,end_XY,full_blood,current_blood):
    thick=2

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]) , (start_XY[0] , start_XY[1]+thick)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (66,62,63))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick) , (start_XY[0] , start_XY[1]+thick*2)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (65,77,67))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick*2) , (start_XY[0] , start_XY[1]+10)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (79,108,86))

def blood_lengh2_decrease(image,start_XY,end_XY,full_blood,current_blood):
    
    thick=2
    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]) , (start_XY[0] , start_XY[1]+thick)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (66,62,63))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick) , (start_XY[0] , start_XY[1]+thick*2)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (65,77,67))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick*2) , (start_XY[0] , start_XY[1]+8)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (79,108,86))

def blood_num(image,start_XY,full_blood,current_blood,font):
    ImageDraw.Draw(image).text((start_XY[0],start_XY[1]), f'{current_blood}/ {full_blood}' ,(71,68,53), font=font,align = "left")


player1_start_XY = [976,268] #XY #主角血條位置右
player1_end_XY = [751,268] #左

player2_start_XY = [403,63] #XY #對手血條位置右
player2_end_XY = [180,63] #左

num_start_XY = [868,279] #左上 #數字顯示

player1_full_blood = 20
player1_current_blood = 10

player2_full_blood = 20
player2_current_blood = 15

blood_lengh1_decrease(im,player1_start_XY,player1_end_XY,player1_full_blood,player1_current_blood)
blood_lengh2_decrease(im,player2_start_XY,player2_end_XY,player2_full_blood,player2_current_blood)

blood_num(im,num_start_XY,player1_full_blood,player1_current_blood,font)


im.save("f_w.png","png")
# im.show()