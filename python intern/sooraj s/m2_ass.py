
import pandas as pd
print("Enter No.of batsmen played")
No = int(input())
team1_batting = {}
print("Enter Name, runs scored, Balls faced, Sixers , Fours, Strike Rate respectively ")
for i in range (0 ,No):
  name = str(input("Name:"))
  score = []
  runs = int(input("Runs Scored:"))
  score.append(runs)

  ball_faced = int(input("Ball faced:"))
  score.append(ball_faced)

  six = int(input("Sixers:"))
  score.append(six)

  fours = int(input("Fours:"))
  score.append(fours)

  st_rate = float(input("Strike Rate"))
  score.append(st_rate)

  team1_batting[name] = score
#print(team1_batting)
df = pd.DataFrame(team1_batting , index= ['Runs','Balls_Faced' , 'Sixers','Fours','Strike_Rate'])
df1=df.transpose()
df1
print("Enter No.of batsmen played")
No = int(input())
team2_batting = {}
print("Enter Name, runs scored, Balls faced, Sixers , Fours, Strike Rate respectively ")
for i in range (0 ,No):
    name = str(input("Name:"))
    score = []
    runs = int(input("Runs Scored:"))
    score.append(runs)

    ball_faced = int(input("Ball faced:"))
    score.append(ball_faced)

    six = int(input("Sixers:"))
    score.append(six)

    score.append(fours)

    st_rate = float(input("Strike Rate"))
    score.append(st_rate)

    team2_batting[name] = score
df = pd.DataFrame(team2_batting , index= ['Runs','Balls_Faced' , 'Sixers','Fours','Strike_Rate'])
df1=df.transpose()
df1
print("Enter No. of bowlers bowled")
No1 = int(input())
team2_bowling = {}
print("Enter Name , wickets he had taken , balls bowled, runs given respectively ")
for i in range (0 ,No1):
  name = str(input("Name:"))
  score = []

  wickets = int(input("Wickets:"))
  score.append(wickets)

  ball_bowled = int(input("Balls Bowled:"))
  score.append(ball_bowled)

  runs_given = int(input("Runs Given"))
  score.append(runs_given)

  team2_bowling[name] = score ;

df = pd.DataFrame(team2_bowling , index= ['Wickets','Balls_Bowled' , 'Runs_Given'])
df1=df.transpose()
df1