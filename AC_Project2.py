#STOCK PORTFOLIO TRACKER:-

#Creating an empty Dictionary

n = int(input("Number of entries you wish to enter: "))
stockPortfolio = {}

#Input functions to store stock names and quantities.

for frequency in range(1, n+1):       
      stockName = input(f"Enter the name of Stock: ")
      stockQuantity = int(input("Enter the Quantity: "))
      stockPortfolio = {stockName : stockQuantity}
      print(stockPortfolio)


# Calculating Total Investments in Stocks
# Total_investment = (number of shares * current price of stock 1) + (number of shares * currect price of stock 2)...+ (number of shares * current price of stock (N))

sum = 0

for i in range(1, n+1): 
    stockName = input(f"Enter the name of Stock {i}: ")

    # Assuming the user will input the number of shares and current price for each stock
    
    number_of_shares = int(input(f"Enter number of shares you own for {stockName}:"))
    current_Price = int(input(f"Enter the current price of {stockName}: "))
    initial_investment = (number_of_shares * current_Price)
    print(f"Initial Investment in {stockName} = {initial_investment}")
    sum += initial_investment

Total_investment = sum
print(f"\n                Your Total Investment in Stocks = {Total_investment} \n")

#for viewing the Total Investment in a .txt file:

with open("Total_Investment.txt", "w") as file:
     file.write(f"Total Investment in Stocks = {Total_investment}\n")





