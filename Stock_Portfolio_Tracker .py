import pygame
import yfinance as yf
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stock Trading Simulator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Initial Player Data
balance = 100000  # Starting money
portfolio = {}
stocks = ["AAPL", "TSLA", "GOOGL", "AMZN", "MSFT"]

# Fetch stock prices
def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        return stock.history(period="1d")["Close"][0]
    except:
        return random.randint(50, 500)  # Random fallback price

# Main Game Loop
running = True
while running:
    screen.fill(WHITE)
    
    # Display balance
    balance_text = font.render(f"Balance: ${balance}", True, BLACK)
    screen.blit(balance_text, (20, 20))
    
    # Display stocks and prices
    y_offset = 80
    for stock in stocks:
        price = get_stock_price(stock)
        stock_text = font.render(f"{stock}: ${price:.2f}", True, BLACK)
        screen.blit(stock_text, (20, y_offset))
        y_offset += 40
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
