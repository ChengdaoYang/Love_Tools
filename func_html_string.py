def get_string(*args):
    for arg in args:
        arg.price(plot = True)
    main_string = """
    <html>
    <body>
    <h1>Summary</h1>
    <p>
    <font size=5 color="sky blue">"""

    for i in range(len(args)):
        main_string = main_string + args[i].ticker + \
                      '</font>\n<br /><br />\n<font size=4>' + \
                      'This is the summary of ' + args[i].ticker + \
                      '</font>\n<br />\n<font size=4>' + \
                      args[i].summary + \
                      '</font>\n<br /><br />\n<font size=4>' + \
                      'The latest prices of ' + args[i].ticker + ' are:' + \
                      '</font>\n<br />\n<font size=4>' + \
                      'Opening Price: ' + str(round(args[i].price(plot = True)['Open'].values[0],2)) + \
                      '</font>\n<br />\n<font size=4>' + \
                      'Closing Price: ' + str(round(args[i].price(plot = True)['Close'].values[0],2)) + \
                      '</font>\n<br />\n<font size=4>' + \
                      'Highest Price: ' + str(round(args[i].price(plot = True)['High'].values[0],2)) + \
                      '</font>\n<br />\n<font size=4>' + \
                      'Lowest Price: ' + str(round(args[i].price(plot = True)['Low'].values[0],2)) + \
                      '</font>\n<br /><br />\n<img class="' + \
                      args[i].ticker + \
                      '" src="cid:' + \
                      str(i) + \
                      '" width="60%">\n<br /><br />\n<font size=5 color="sky blue">'
    main_string = main_string + '\n</p>\n</div>\n</body>\n</html>\n'
    print(main_string)
    time.sleep(5)
    return main_string
