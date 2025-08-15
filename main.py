#Copyright (c) 2025 Abhishek Sharma All Rights Reserved.
import random
import os 
print('WELCOME TO ROCK PAPER SCISSOR GAME..')
attempt =1
point_win = 10
point_lose = -5
point_on_start = 0
moves = {'r':'rock','p':'paper','s':'scissor'}
# for checking high score 
if not os.path.exists('High-score.txt'):
    with open('High-score.txt', 'w') as f:
        f.write('0')  # Default high score
with open('High-score.txt', 'r') as f:
    high_score = int(f.read())
print(f'🎯 High Score to Beat: {high_score}\n')
while(attempt<=10):
    inp = input(f'Attempt {attempt} :: Enter r for rock, Enter p for paper, Enter s for scissor : ')
    comp = random.choice(['r','p','s'])
    if inp not in ['r', 'p', 's']:
        print('\nEnter a valid input as mentioned\n')
    else:
        if(inp==comp):
            print("🤝 It's a draw!\n")
        else:
            if(inp=='r' and comp=='p')or\
                (inp=='p' and comp == 's')or\
                    (inp=='s' and comp=='r'):
                point_on_start += point_lose
                print(f'\nComputer : {moves.get(comp)} || You : {moves.get(inp)}')
                print(f'{moves.get(comp)} beats {moves.get(inp)}')
                print('❌ You LOSE!\n')

            else:
                point_on_start+=point_win
                print(f'\nComputer : {moves.get(comp)} || You : {moves.get(inp)}')
                print(f'{moves.get(inp)} beats {moves.get(comp)}')
                print('✅ You WIN!\n')
        attempt+=1       
                
score_after_loop_ends = point_on_start
if score_after_loop_ends > high_score:
    print(f'New High Score! Your Score: {score_after_loop_ends}')
    with open('High-score.txt', 'w') as f:
        f.write(str(score_after_loop_ends))
else:
    print(f'Your Score: {score_after_loop_ends} || High Score: {high_score}')

print('🎮 Game Over!')

print(f'Your Final Score: {score_after_loop_ends}')
