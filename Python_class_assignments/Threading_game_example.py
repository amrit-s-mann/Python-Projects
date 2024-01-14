from threading import Thread
from time import sleep

def start_game(prerequisites, delay):
    print("\nWaiting to start the game!\n")
    
    for thread in prerequisites:                    # Ensures all thread have completely run
        thread.join()
    
    sleep(delay)
    print("\nGame started!\n")

def load_assets(delay):
    sleep(delay)
    print("Assets loaded")

def load_player(delay):
    sleep(delay)
    print("Player loaded")

load_assets_thread = Thread(target = load_assets, args = (2, )) 
load_player_thread = Thread(target = load_player, args = (3, ))
# Note the usage of ',' in the thread arguement to make it a tuple

load_threads = [load_assets_thread, load_player_thread]
start_game_thread = Thread(target=start_game, args = (load_threads, 2))

load_player_thread.start()
load_assets_thread.start()
start_game_thread.start()
start_game_thread.join()
# Note the order of starting threads. We can't begin with 'start_game_thread' here.
