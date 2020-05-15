# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where K ≠ 1.
# The Captain was given a separate room, and the rest were given one room per group.
# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of
# the tourists. The room numbers will appear K times per group except for the Captain's room.
# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of K and the room number list.
#
# Input Format
# The first line consists of an integer, K, the size of each group.
# The second line contains the unordered elements of the room number list.
#
# Constraints
# 1 < K < 1000
#
# Output Format
# Output the Captain's room number.

group_size = int(input())
fam_list = list(map(int, input().split()))
unique_fams = set(fam_list)

# From the discussion:
# Multiply the sum of unique numbers by group_size (as if every room number was repeated group_size times).
# Subtract the sum of given room numbers. The difference will be (group_size-1)*captains_room_number.
# Divide by (group_size-1) to get the captains room number
captains_room_number = ((sum(unique_fams) * group_size) - (sum(fam_list))) // (group_size - 1)
print(captains_room_number)
