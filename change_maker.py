def make_change(amount, currency_list):
    my_change_list = []
    for coin in sorted(currency_list, reverse=True):
        coin_count = amount // coin
        my_change_list += [coin] * coin_count
        amount -= coin * coin_count
    return my_change_list

total_amount = 687

# Can use any currency denominations as long as they are specified
print(make_change(total_amount, currency_list=[50, 40, 25, 13, 10, 5, 1]))
