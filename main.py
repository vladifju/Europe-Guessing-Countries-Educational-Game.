import pandas
import turtle
FONT = ("Courier", 10, "bold")
FONT_SCORE = ("Courier", 20, "bold")
END_FONT = ("Courier", 30, "bold")

screen = turtle.Screen()
screen.setup(800,628)
screen.title("Europe Countries Game")
image = "europe.gif"
screen.addshape(image)
turtle.shape(image)

country_data = pandas.read_csv("europe_countries_data.csv")
countries = country_data["country"]
country_list = countries.tolist()

def show_country(answer):
    #turtle
    country_w = turtle.Turtle()
    country_w.penup()
    country_w.hideturtle()
    print(answer) #test 1
    country = country_data[countries == answer]
    x = int(country.x)
    y = int(country.y)
    print(x,y) #test 2
    country_w.goto(x=x,y=y)
    country_w.write(f"{answer}", font=FONT, align="center")

scoreboard_t = turtle.Turtle()

def scoreboard_write(score,turtle):
    turtle.clear()
    turtle.hideturtle()
    turtle.pu()
    turtle.goto(-400,100)
    turtle.write(f"Score: {score}", font=FONT_SCORE)

def scoreboard_win(turtle):
    turtle.goto(0,0)
    turtle.write("You've Guessed all The Countries!", font = END_FONT, align = "center")
    turtle.goto(0,-50)
    turtle.write("Congrats!!!", font = END_FONT, align = "center")

country_guess_list = []
guess_count = 0
game_is_on = True
while game_is_on:
    scoreboard_write(guess_count, scoreboard_t)
    answer_state = screen.textinput(title="Guess the Country",prompt="Whats's another country's name?").title()
    if answer_state == "Stop":
        game_is_on = False
    elif answer_state in country_list:
        if answer_state not in country_guess_list:
            show_country(answer_state)
            guess_count += 1
            country_guess_list.append(answer_state)
    if guess_count == 45:
        scoreboard_write(guess_count, scoreboard_t)
        scoreboard_win(scoreboard_t)
        break





turtle.mainloop()
