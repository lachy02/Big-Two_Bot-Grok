from itertools import combinations
deck_order = ['3D','3C','3H','3S','4D','4C','4H','4S','5D','5C', #deck order for game
  '5H','5S','6D','6C','6H','6S','7D','7C','7H','7S','8D',
  '8C','8H','8S','9D','9C','9H','9S','0D','0C','0H','0S','JD',
  'JC','JH','JS','QD','QC','QH','QS','KD','KC','KH','KS','AD',
  'AC','AH','AS','2D','2C','2H','2S']

face_order = ['3','4','5','6','7','8','9','0','J','Q','K','A','2'] #face order for game

def sort(card):                  #This function is called to sort cards
  for i in range(len(card)):
    minimum = i
    for j in range(i+1, len(card)):
      if deck_order.index(card[j]) < deck_order.index(card[minimum]):
        minimum = j
    card[minimum], card[i] = card[i], card[minimum]
    return card

def sort_face_order(card):                  #This function is called to sort cards based on face order only
  for i in range(len(card)):
    minimum = i
    for j in range(i+1, len(card)):
      if face_order.index(card[j]) < face_order.index(card[minimum]):
        minimum = j
    card[minimum], card[i] = card[i], card[minimum]
    return card

def sort_pair(card):                  #This function is called to sort pairs
  for i in range(len(card)):
    minimum = i
    for j in range(i+1, len(card)):
      if is_lower_pair(card[j],card[minimum]):
        minimum = j
    card[minimum], card[i] = card[i], card[minimum]
    return card

def sort_tri(card):                  #This function is called to sort tri
  for i in range(len(card)):
    minimum = i
    for j in range(i+1, len(card)):
      if is_lower_tri(card[j],card[minimum]):
        minimum = j
    card[minimum], card[i] = card[i], card[minimum]
    return card

def sort_straight(card):                  #This function is called to sort straight
  for i in range(len(card)):
    minimum = i
    for j in range(i+1, len(card)):
      if is_lower_straight(card[j],card[minimum]):
        minimum = j
    card[minimum], card[i] = card[i], card[minimum]
    return card

def sort_flush(card):                  #This function is called to sort flush
  for i in range(len(card)):
    minimum = i
    for j in range(i+1, len(card)):
      if is_lower_flush(card[j],card[minimum]):
        minimum = j
    card[minimum], card[i] = card[i], card[minimum]
    return card

def sort_full_house(card):                  #This function is called to sort full house
  for i in range(len(card)):
    minimum = i
    for j in range(i+1, len(card)):
      if is_lower_full_house(card[j],card[minimum]):
        minimum = j
    card[minimum], card[i] = card[i], card[minimum]
    return card

def sort_four_of_a_kind(card):                  #This function is called to sort four of a kind
  for i in range(len(card)):
    minimum = i
    for j in range(i+1, len(card)):
      if is_lower_four_of_a_kind(card[j],card[minimum]):
        minimum = j
    card[minimum], card[i] = card[i], card[minimum]
    return card

def sort_straight_flush(card):                  #This function is called to sort straight flush
  for i in range(len(card)):
    minimum = i
    for j in range(i+1, len(card)):
      if is_lower_straight_flush(card[j],card[minimum]):
        minimum = j
    card[minimum], card[i] = card[i], card[minimum]
    return card

#CHECKING IF COMBINATION IS CORRECT

def is_pair(card1, card2): #checking if pair
  if card1[0]== card2[0]:
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_tri(card1, card2, card3): #checking if tri
  if card1[0] == card2[0] == card3[0]:
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_straight(cards): #checking if straight
    allfaces = [f for f,s in cards]
    facetypes = set(allfaces)
    faces = sort_face_order(allfaces)
    if face_order.index(faces[-1]) - face_order.index(faces[0]) == 4 and len(facetypes) == 5:
        your_answer = True
    else:
        your_answer = False
    return your_answer

def is_flush(cards): #checking if flush
    allsuits = [s for f, s in cards]
    suits = set(allsuits)
    if len(suits) == 1:
        your_answer = True
    else:
        your_answer = False
    return your_answer

def is_full_house(cards): #checking if full house
    allfaces = [f for f,s in cards]
    faces = set(allfaces)
    if len(faces) != 2:
        your_answer = False
        return your_answer
    for f in faces:
        if allfaces.count(f) == 3:
            your_answer = True
            return your_answer
    else:
        return False

def is_four_of_a_kind(cards): #checking if four of a kind
    allfaces = [f for f,s in cards]
    faces = set(allfaces)
    if len(faces) != 2:
        your_answer = False
        return your_answer
    for f in faces:
        if allfaces.count(f) == 4:
            your_answer = True
            return your_answer

def is_straight_flush(cards): #checking if straight flush
    if is_flush(cards):
        if is_straight(cards):
            your_answer = True
            return your_answer
    else:
        your_answer = False
        return your_answer

#CHECKING FOR ALL POSSIBLE HAND COMBINATIONS

def all_pairs(hand): #checking for all possible combinations of pairs
  pairs = []
  p = combinations(hand,2)
  for i in list(p):
    if is_pair(i[0], i[1]):
      pairs.append(list(i))
  return pairs

def all_tri(hand): #checking for all possible combinations of tri
  tri = []
  p = combinations(hand,3)
  for i in list(p):
    if is_tri(i[0], i[1], i[2]):
      tri.append(list(i))
  return tri

def all_straight(hand): #checking al possible straights
  straight = []
  p = combinations(hand,5)
  for c in p:
    if is_straight(c):
      straight.append(list(c))
  return straight

def all_flush(hand): #checking all possible flushs
  flush = []
  p = combinations(hand,5)
  for c in p:
    if is_flush(c):
      flush.append(list(c))
  return flush

def all_full_house(hand): #checking all possible full houses
  full_house = []
  p = combinations(hand,5)
  for c in p:
    if is_full_house(c):
      full_house.append(list(c))
  return full_house

def all_four_of_a_kind(hand): #checking all possibl four of a kind
  four_of_a_kind = []
  p = combinations(hand,5)
  for c in p:
    if is_four_of_a_kind(c):
      four_of_a_kind.append(list(c))
  return four_of_a_kind

def all_straight_flush(hand): #checking all possible straight flushs
  straight_flush = []
  p = combinations(hand,5)
  for c in p:
    if is_straight_flush(c):
      straight_flush.append(list(c))
  return straight_flush

#CHECKING IN HAVING A COMBINATION OF THAT TYPE

def have_pair(hand): #checking if i have a pair
    hand = hand
    if len(all_pairs(hand)) != 0:
        your_answer = True
    else:
        your_answer = False
    return your_answer

def have_tri(hand): #checking if i have a tri
    if len(all_tri(hand)) != 0:
        your_answer = True
    else:
        your_answer = False
    return your_answer

def have_straight(hand): #checking if i have straight
    if len(all_straight(hand)) != 0:
        your_answer = True
    else:
        your_answer = False
    return your_answer

def have_flush(hand): #checking if i have flushes
    if len(all_flush(hand)) != 0:
        your_answer = True
    else:
        your_answer = False
    return your_answer

def have_full_house(hand): #checking if i have full houses
    if len(all_full_house(hand)) != 0:
        your_answer = True
    else:
        your_answer = False
    return your_answer

def have_four_of_a_kind(hand): #checking if i have four of a kind
    if len(all_four_of_a_kind(hand)) != 0:
        your_answer = True
    else:
        your_answer = False
    return your_answer

def have_straight_flush(hand): #checking if i have straight flush
    if len(all_straight_flush(hand)) != 0:
        your_answer = True
    else:
        your_answer = False
    return your_answer

#CHECKING IF LOWER

def is_lower(card1, card2):     #This function is called to test if card is higher
  if deck_order.index(card1) < deck_order.index(card2):
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_lower_pair(pair1, pair2): #checking for lowest pair
  p1_c1 = deck_order.index(pair1[0])
  p1_c2 = deck_order.index(pair1[1])
  p2_c1 = deck_order.index(pair2[0])
  p2_c2 = deck_order.index(pair2[1])
  if max(p1_c1, p1_c2) < max(p2_c1, p2_c2):
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_lower_tri(tri1, tri2): #checking for lowest tri
  t1_c1 = deck_order.index(tri1[0])
  t1_c2 = deck_order.index(tri1[1])
  t1_c3 = deck_order.index(tri1[2])
  t2_c1 = deck_order.index(tri2[0])
  t2_c2 = deck_order.index(tri2[1])
  t2_c3 = deck_order.index(tri2[2])
  if max(t1_c1, t1_c2, t1_c3) < max(t2_c1, t2_c2, t2_c3):
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_lower_straight(first, second): #checking for lower straight
    faces_1 = sort(first)
    faces_2 = sort(second)
    if deck_order.index(faces_1[-1]) < deck_order.index(faces_2[-1]):
        your_answer = True
    else:
        your_answer = False
    return your_answer

def is_lower_flush(first, second): #checking for lower flush
    faces_1 = sort(first)
    faces_2 = sort(second)
    if deck_order.index(faces_1[-1]) < deck_order.index(faces_2[-1]):
        your_answer = True
    else:
        your_answer = False
    return your_answer

def is_lower_full_house(first, second): #checking for lower full house
  allfaces_1 = [f for f,s in first]
  faces_1 = set(allfaces_1)
  allfaces_2 = [f for f,s in second]
  faces_2 = set(allfaces_2)
  for f in faces_1:
    if allfaces_1.count(f) == 3:
      tri_1 = f
  for f in faces_2:
    if allfaces_2.count(f) == 3:
      tri_2 = f
  if face_order.index(tri_1) < face_order.index(tri_2):
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_lower_four_of_a_kind(first, second): #checking for lower four of a kind
  allfaces_1 = [f for f,s in first]
  faces_1 = set(allfaces_1)
  allfaces_2 = [f for f,s in second]
  faces_2 = set(allfaces_2)
  for f in faces_1:
    if allfaces_1.count(f) == 4:
      quad_1 = f
  for f in faces_2:
    if allfaces_2.count(f) == 4:
      quad_2 = f
  if face_order.index(quad_1) < face_order.index(quad_2):
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_lower_straight_flush(first, second): #checking for lower straight flush
    faces_1 = sort(first)
    faces_2 = sort(second)
    if deck_order.index(faces_1[-1]) < deck_order.index(faces_2[-1]):
        your_answer = True
    else:
        your_answer = False
    return your_answer

#CHECKING IF HIGHER

def is_higher(card1, card2):     #This function is called to test if card is higher
  if deck_order.index(card1) > deck_order.index(card2):
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_higher_pair(pair1, pair2):   #checking for highest pair
  p1_c1 = deck_order.index(pair1[0])
  p1_c2 = deck_order.index(pair1[1])
  p2_c1 = deck_order.index(pair2[0])
  p2_c2 = deck_order.index(pair2[1])
  if max(p1_c1, p1_c2) > max(p2_c1, p2_c2):
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_higher_tri(tri1, tri2):  #checking for highest tri
  t1_c1 = deck_order.index(tri1[0])
  t1_c2 = deck_order.index(tri1[1])
  t1_c3 = deck_order.index(tri1[2])
  t2_c1 = deck_order.index(tri2[0])
  t2_c2 = deck_order.index(tri2[1])
  t2_c3 = deck_order.index(tri2[2])
  if max(t1_c1, t1_c2, t1_c3) > max(t2_c1, t2_c2, t2_c3):
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_higher_straight(first, second): #checking for higher straight
    allfaces_1 = [f for f,s in first]
    setfaces_1 = set(allfaces_1)
    allfaces_2 = [f for f,s in first]
    setfaces_2 = set(allfaces_1)
    faces_1 = sort(first)
    faces_2 = sort(second)
    if setfaces_1 == setfaces_2:
        if deck_order.index(faces_1[-1]) > deck_order.index(faces_2[-1]):
            your_answer = True
        else:
            your_answer = False
        return your_answer
    if setfaces_1 > setfaces_2:
        your_answer = True
    else:
        your_answer = False
    return your_answer

def is_higher_flush(first, second): #checking for higher flush
    faces_1 = sort(first)
    faces_2 = sort(second)
    if deck_order.index(faces_1[-1]) > deck_order.index(faces_2[-1]):
        your_answer = True
    else:
        your_answer = False
    return your_answer

def is_higher_full_house(first, second): #checking for higher full house
  allfaces_1 = [f for f,s in first]
  faces_1 = set(allfaces_1)
  allfaces_2 = [f for f,s in second]
  faces_2 = set(allfaces_2)
  tri_1 = 0
  tri_2 = 0
  for f in faces_1:
    if allfaces_1.count(f) == 3:
      tri_1 = f
  for f in faces_2:
    if allfaces_2.count(f) == 3:
      tri_2 = f
  if face_order.index(tri_1) > face_order.index(tri_2):
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_higher_four_of_a_kind(first, second): #checking for higher four of a kind
  allfaces_1 = [f for f,s in first]
  faces_1 = set(allfaces_1)
  allfaces_2 = [f for f,s in second]
  faces_2 = set(allfaces_2)
  for f in faces_1:
    if allfaces_1.count(f) == 4:
      quad_1 = f
  for f in faces_2:
    if allfaces_2.count(f) == 4:
      quad_2 = f
  if face_order.index(quad_1) > face_order.index(quad_2):
    your_answer = True
  else:
    your_answer = False
  return your_answer

def is_higher_straight_flush(first, second): #checking for higher straight flush
    faces_1 = sort(first)
    faces_2 = sort(second)
    if deck_order.index(faces_1[-1]) > deck_order.index(faces_2[-1]):
        your_answer = True
    else:
        your_answer = False
    return your_answer

#CHANCE CALCULATIONS - STRATS

cards_not = [] #array of card that have not been played

def remove_cards(cards):  #removing cards from cards_not
    for i in cards:
        c = i[0]
        if c in cards_not:
            cards_not.remove(x)

#CARDS LEFT

def pairs_left(cards):  #calculating pairs left (sorted)
    p = all_pairs(cards)
    sort_pair(p)
    return p

def tri_left(cards): #calculating tri's left (sorted)
    p = all_tri(cards)
    sort_tri(p)
    return p

#BEST POSSIBLE CARD PLAYS

def best_pair(pairs_left, all_pairs): #check if i have the largest possible pair left
    my_pairs = sort_pair(all_pairs)
    if pairs_left[-1] == my_pairs[-1]:
        your_answer = True
    else:
        your_answer = False
    return your_answer

def best_tri(tri_left, all_tri): #checking if i have the highest tri
    may_tri = sort_tri(all_tri)
    if tri_left[-1] == my_tri[-1]:
        your_answer = True
    else:
        your_answer = False
    return your_answer

#CALCULATING PERCENTAGE

def single_chancebeat(play_card, cards_left): #percentage of cards beating every other card
    count = 0
    percentage = 1
    for c in cards_left:
        if is_lower(play_card, c) == True:
            count += 1
    if len(cards_left) != 0:
      percentage = int(count)/int(len(cards_left))
    return percentage

def high_pair_left(cards_not, play_pair): #percentage change of my play beating every other play
    cards = sort(cards_not)
    high_cards = []
    low_cards = []
    percentage = 1
    for c in cards:
        if deck_order.index(x) > deck_order.index(play_card[0]) or deck_order.index(play_card[1]):
            high_cards.append(x)
        else:
            low_cards.append(x)
    if len(cards) != 0:
        percentage = len(high_cards)/len(cards)
    return percentage

def play(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):



  if is_start_of_round:  #calling to sort hand and append to cards not played
    sort(hand)
    for c in deck_order:
        cards_not.append(c) #apending items to cards_not for counting/cards left

#START OF ROUND PLAY PLAY_TO_BEAT = 0

  if len(play_to_beat) == 0:  #checking if start of round
    if is_start_of_round:
      play = ['3D']
    elif have_straight(hand):
        play = all_straight(hand)[0]
    elif have_pair(hand): # first round checking for pair below 7 (dont want to waste high cards)
        for x in all_pairs(hand):
            if is_lower_pair(x, ['7D','7D']):
                play = x
            else:
                play = [hand[0]]
    elif have_tri(hand): #first round checking for tri below 7 (dont want to waste high cards)
        for x in all_tri(hand):
            if is_lower_tri(x, ['7D','7D','7D']):
                play = x
            else:
                play = [hand[0]]
    else:
        play = [hand[0]]
    return play

#SINGE CARD PLAY

  if len(play_to_beat) == 1 and is_higher(hand[-1], play_to_beat[0]) == True: #checking if single card play
    if len(hand) == 2 and single_chancebeat(hand[-1], cards_not) > 0.7: #checking for two cards in hand, if play highest card
      play = [hand[-1]]
      return play
    elif hand_sizes[0] == 1 or hand_sizes[1] == 1 or hand_sizes[2] == 1 or hand_sizes[3] == 1:
      play = [hand[-1]]
      return play
    elif deck_order.index(play_to_beat[0]) > deck_order.index('QS') and len(hand) > 5:
      return []
    else:
      for x in hand:
        if is_higher(x, play_to_beat[0]):
            return [x]


#TWO CARD PLAY

  if len(play_to_beat) == 2: #checking if pair play
    for x in all_pairs(hand):
        if is_higher_pair(x, play_to_beat) and is_lower_pair(x, ['AD','AD']):
            return x
    else:
        return []

#THREE CARD PLAY

  if len(play_to_beat) == 3: #checking if tripple play
    for x in all_tri(hand):
        if is_higher_tri(x, play_to_beat) and is_lower_tri(x, ['KD','KD','KD']):
            return x
    else:
        return []

#FIVE CARD PLAY

  if len(play_to_beat) == 5: #checking if 5 card play
        if is_straight(play_to_beat):
            if have_straight(hand) and is_higher_straight(all_straight(hand)[-1], play_to_beat):
                for x in all_straight(hand):
                    if is_higher_straight(x, play_to_beat):
                        return x
            elif have_flush(hand):
                return all_flush(hand)[0]
            elif have_full_house(hand):
                return all_full_house(hand)[0]
            elif have_four_of_a_kind(hand):
                return all_four_of_a_kind(hand)[0]
            elif have_straight_flush(hand):
                return all_straight_flush(hand)[0]
            else:
                return []
        elif is_flush(play_to_beat):
            if have_flush(hand) and is_higher_flush(all_flush(hand)[-1], play_to_beat):
                for x in all_flush(hand):
                    if is_higher_flush(x, play_to_beat):
                        return x
            elif have_full_house(hand):
                return sort_full_house(all_full_house(hand))[0]
            elif have_four_of_a_kind(hand):
                return sort_four_of_a_kind(all_four_of_a_kind(hand))[0]
            elif have_straight_flush(hand):
                return sort_straight_flush(all_straight_flush(hand))[0]
            else:
                return []
        elif is_full_house(play_to_beat):
            if have_full_house(hand) and is_higher_full_house(all_full_house(hand)[-1], play_to_beat):
                for x in all_full_house(hand):
                    if is_higher_full_house(x, play_to_beat):
                        return x
            elif have_four_of_a_kind(hand):
                return sort_four_of_a_kind(all_four_of_a_kind(hand))[0]
            elif have_straight_flush(hand):
                return sort_straight_flush(all_straight_flush(hand))[0]
            else:
                return []
        elif is_four_of_a_kind(play_to_beat): #current play is four of a kind
            if have_four_of_a_kind(hand) and is_higher_four_of_a_kind(all_four_of_a_kind(hand)[-1], play_to_beat):
                for x in all_four_of_a_kind(hand):
                    if is_higher_four_of_a_kind(x, play_to_beat):
                        return x
            elif have_straight_flush(hand):
                return sort_straight_flush(all_straight_flush(hand))[0]
            else:
                return []
        elif is_straight_flush(play_to_beat): #current play is a straight flush
            if have_straight_flush(hand) and have_straight_flush(hand):
                for x in all_straight_flush(hand):
                    if is_higher_straight_flush(x, play_to_beat):
                        return x
            else:
                return []
        else:
          return []







if __name__ == '__main__':

  # Write your own test cases for your `play` function here.
  # These can be run with the Run button and will not affect the tournament or marking.
  # Here's an example test case and testing code to kick you off.
  TESTS = [  # [ expected return value, inputs ]
  [['3D'], [['5D', '4D', '4H', '7D', '8D', '8H', '0D', '0C', 'JH', 'QC', 'QS', 'KH', '4S'], True, [], [[]], 0, [13, 13, 13, 13], [0, 0, 0, 0], 0]],

    [['5D'], [['5D', '5C', '5S', '7D', '8C', '8H', '8S', '9C', '9S', 'JD', 'KS', '2C', '2S'], False, ["3D"], [[]], 0, [13, 13, 13, 13], [0, 0, 0, 0], 0]],

    [['3'], [['4D', '5D', '6H', '7C', '7S', '8D', '8H', '9C', '0S', 'JH', 'KC', 'KS', 'AC'], False, ['3D', '7D', '0D', 'JD', 'QD'], [[]], 0, [13, 13, 13, 13], [0, 0, 0, 0], 0]],

    [['5D'], [['4D', '5C', '6S', '7D', '8C', '8H', '8S', '9C', '9S', 'JD', 'KS', '2C', '2S'], False, ["3D","4S","5S","6H","7D"], [[]], 0, [13, 13, 13, 13], [0, 0, 0, 0], 0]],

     [['5D'], [['4D', '5C', '6S', '7D', '8C', '8H', '8S', '9C', '9S', 'JD', 'KS', '2C', '2S'], False, ['3D', '4C', '5H', '6D', '7S'], [[]], 0, [13, 13, 13, 13], [0, 0, 0, 0], 0]],

    [[],[['3C', '3H', '5D', '6H', '7C', '8H', '9D', 'JS', 'QH', 'QS', 'KD', 'KS', 'AH'], False, ['9C', 'JD', 'QC', '0S', '8C'], [[[2, ['3D', '4C', '5H', '6D', '7S']], [3, ['9C', 'JD', 'QC', '0S', '8C']]]], 0, [13, 13, 8, 8], [-22, -12, 38, -4], 3]],

    # Add more tests here.
  ]

  # This runs the above test cases.
  for i, test in enumerate(TESTS):
    expected_return_value, inputs = test
    actual_return_value = play(*inputs)

    if actual_return_value == expected_return_value:
      print('PASSED {}/{}.'.format(i + 1, len(TESTS)))
    else:
      print('FAILED {}/{}.'.format(i + 1, len(TESTS)))
      print('    inputs:', repr(inputs))
      print('  expected:', repr(expected_return_value))
      print('    actual:', repr(actual_return_value))
