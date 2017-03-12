import gym
import sys
import tty
import termios
from gym.envs.registration import register

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

inkey = _Getch()
#MACROS
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

#Key mapping
arrow_keys = {
        '\x1b[A' : UP,
        '\x1b[B' : DOWN,
        '\x1b[C' : RIGHT,
        '\x1b[D' : LEFT
        }

# register FrozenLake with is_slippery False
register(
        id = 'FrozenLake-v3',
        entry_point = 'gym.envs.toy_text:FrozenLakeEnv',
        kwargs = {'map_name' : '4x4', 'is_slippery':False}
)

env = gym.make('FrozenLake-v3')
env.render()#Show the initial board
while True:
    # Choose an action from keyboard
    key = inkey()
    if key not in arrow_keys.keys():
        print("Game aborted")
        break

    action =  arrow_keys[key]
    state, reward, done, info =env.step(action)
    env.render()# Show the board after action
    print("State: ", state, "Action: ",action,"Reward:", reward, "Info: " ,info)
    if done:
        print("Finished with reward", reward)
        break


'''
env = gym.make("FrozenLake-v0")
observation = env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space. 
'''
