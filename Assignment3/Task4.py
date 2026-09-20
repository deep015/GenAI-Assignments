prices = [100, 250, 400, 1200, 50]

GST = lambda price: price + (0.18 * price)

price_With_gst = list(map(GST, prices))

print("Original prices:", prices)
print("Prices after GST:", price_With_gst)

