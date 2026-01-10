def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    
    def ft_repetition(i):
        if i > days:
            return ;
        print("Day ", i)
        ft_repetition(i+1)
    ft_repetition(1)
    print("Harvest time!")