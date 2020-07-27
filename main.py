from time import sleep
from login_keys import *
from InstagramAPI import InstagramAPI

#returns a list of all followers
def getFollowers(api, user):
    followers = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id =''
        _ = api.getUserFollowers(user, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

#returns a list of all followings
def getFollowing(api, user):
    following = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id =''
        _ = api.getUserFollowings(user, maxid=next_max_id)
        following.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return following

#finds the snakes who aren't following you back
def getSnakes(followers, following):
    snakes = {}
    dictionary = {}
    print("finding snakes...\n")
    for follower in followers:
        dictionary[follower['username']] = follower['pk']
    for followed in following:
        if followed['username'] not in dictionary:
            print(followed['username'])
            snakes[followed['username']] = followed['pk']
    return snakes

def getRidOfThoseSnakes():
    api = InstagramAPI(USERNAME, PASS)
    api.login()
    user = api.username_id
    followers = getFollowers(api, user)
    following = getFollowing(api, user)
    snakes = getSnakes(followers, following)
    print("\nFollowers: " + str(len(followers)))
    print("Following: " + str(len(following)))
    print("Snakes: " + str(len(snakes)))

    #unfollows snakes
    '''
    while len(snakes) > 0:
        user = list(snakes.keys())[len(snakes)-1]
        api.unfollow(snakes[user])
        snakes.pop(user)
    print("done (:")
    '''

getRidOfThoseSnakes()