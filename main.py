import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# heuristic search
dp=[0]*1000
dp[1]=0
dp[2]=0
aa=[0]*1000
bb=[0]*1000
def get(x):
    limit=int((x+1)/2)
    for i in range(1,limit):
        rem=x-i
        if(aa[x]==0):
            aa[x]=i
        if(bb[x]==0):
            bb[x]=rem
        if(dp[rem]==0 and dp[i]==0):
            dp[x]=1
            aa[x]=i
            bb[x]=rem
for i in range(3,1000):
    get(i)
    # print(i," ",dp[i])

# UI ekhan theke
class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(
            text="                                                                     Welcome to Partitioning Game ",
            color='#7FFD4',
            font_size=25
        ))
        self.add_widget(Label(
            text="",
            color='#7FFD4',
            font_size=25
        ))

        self.add_widget(Label(
            text="Enter number of blocks: ",
            color='#7FFD4',
            font_size=25
        ))
        self.block = TextInput(font_size=25,multiline=False)
        self.add_widget(self.block)

        self.add_widget(Label(
            text="Opponent turn: ",
            color='#FFA500',
            font_size=25
        ))
        self.opponent = TextInput(font_size=25,multiline=False)
        self.add_widget(self.opponent)

        self.add_widget(Label(
            text="Your turn: ",
            color='#ADD8E6',
            font_size=25
        ))
        self.my = TextInput(
            font_size=25,
            multiline=False
        )
        self.add_widget(self.my)

        self.submit = Button(
            text="submit",
            font_size=25,
            background_color=(1, 0, 0, 1)
        )
        self.submit.bind(on_press=self.callback)
        self.add_widget(self.submit)

        self.greeting = Label(
            text="Your turn",
            font_size=25,
            color='#00FFCE'
        )
        self.add_widget(self.greeting)

        self.d="you"
        self.n="123"

    # submit korar por ekhane ashbe ->
    def callback(self, instance):
        block = int(self.block.text)
        if(self.n=="123"):
            self.n=self.block.text

        my = self.my.text
        oppo = self.opponent.text
        if(self.d=="you"):
            dd = int(self.n)
            if(dd==1 or dd==2):
                quit()
            a,b=list(map(int,my.split()))
            if(dp[a]==0 and dp[b]==0):
                d=max(a,b)
                self.n=str(d)
            if(dp[a]==1):
                self.n=str(a)
            else:
                self.n=str(b)
            dd = int(self.n)
            if(dd==1 or dd==2):
                self.opponent.text = "No turn left"
                self.greeting.text = "Computer Lost The Game!!"
            else:
                self.greeting.text = "Computer's turn"
        else:
            dd = int(self.n)
            if (dd==1 or dd==2):
                quit()
            if(dd==1 or dd==2):
                exit()

            a=aa[dd]
            b=bb[dd]

            self.opponent.text=str(a)+" "+str(b)
            a=max(a,b)
            self.n=str(a)
            dd = int(self.n)
            if(dd==1 or dd==2):
                self.my.text = "No turn left"
                self.greeting.text = "You Lost The Game!!"
            else:
                self.greeting.text = "Your turn"
                self.my.text = ""

        if(self.d=="you"):
            self.d="opponent"
        else:
            self.d="you"


class Partitioning_Game(App):
    def build(self):
        return MyGridLayout()

#run
Partitioning_Game().run()
