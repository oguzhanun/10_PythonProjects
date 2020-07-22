def maxProfit(prices) :
    
    if len(prices) == 1 :
        return 0
    elif len(prices) == 2 :
        if prices[1] - prices[0] < 0 :
            return 0
        else : 
            return prices[1] - prices[0]
    else :

        if prices[1] - prices[0] > 0 :
            pointer1 = True
        else :
            pointer1 = False
        
        pointer2 = pointer1

        yeniListe = list()
        
        yeniListe.append(prices[0])
       
        for i in range(2,len(prices)) :

            if (prices[i] - prices[i-1]) > 0 :
                pointer2 = True
            else:
                pointer2 = False

            if pointer1 == pointer2 :
                continue
            else :
                pointer1 = pointer2
                yeniListe.append(prices[i-1])
        
        # if pointer2 :
        yeniListe.append(prices[len(prices)-1])

        profit = 0

        print("yeniListe", yeniListe)

        if yeniListe[1] - yeniListe[0] > 0 :

            for i in range(len(yeniListe)) :

                if i % 2 == 1 :
                    profit = profit + yeniListe[i] - yeniListe[i-1]
            
            return profit

        else :
            
            for i in range(len(yeniListe)) :
                
                if i % 2 == 0 and i != 0:
                    profit = profit + yeniListe[i] - yeniListe[i-1]

            return profit


print(maxProfit([6,1,3,2,4,7]))