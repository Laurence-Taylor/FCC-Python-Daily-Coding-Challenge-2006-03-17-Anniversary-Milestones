def get_milestone(years):
    if years < 1: return "Newlyweds"
    elif 1 <= years < 5: return "Paper"
    elif  5 <= years < 10: return "Wood"
    elif  10 <= years < 25: return "Tin"
    elif  25 <= years < 40: return "Silver"
    elif  40 <= years < 50: return "Ruby"
    elif  50 <= years < 60: return "Gold"
    elif  60 <= years < 70: return "Diamond"
    elif  70 <= years: return "Platinium"

    return years

if __name__ == '__main__':
    print(get_milestone(0))
    print('-----')
    print(get_milestone(1))