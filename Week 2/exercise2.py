friends = [["James", "Malaysia", "Malacca"], ["Goh", "Australia", "Brisbane"], ["Don", "Malaysia", "Pahang"], ["John", "Malaysia", "Kuala Lumpur"], ["Peter", "Malaysia", "Penang"], ["Alice", "USA", "New York"], ["Bob", "Canada", "Toronto"], ["Charlie", "UK", "London"], ["David", "Germany", "Berlin"], ["Eve", "France", "Paris"]]

def filterFriend(name='', home_country='', home_state=''):
    filtered_friends = []
    for friend in friends:
        if (name == '' or friend[0] == name) and (home_country == '' or friend[1] == home_country) and (home_state == '' or friend[2] == home_state):
            filtered_friends.append(friend)
    return filtered_friends

print(filterFriend(name='James'))