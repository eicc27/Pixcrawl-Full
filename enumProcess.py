import curses
stdscr = curses.initscr()
curses.curs_set(False)
MB = 1024 * 1024


def downloadBar0(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(0, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(0, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(0, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar1(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(1, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(1, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(1, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar2(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(2, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(2, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(2, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar3(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(3, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(3, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(3, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar4(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(4, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(4, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(4, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar5(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(5, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(5, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(5, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar6(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(6, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(6, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(6, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar7(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(7, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(7, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(7, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar8(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(8, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(8, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(8, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar9(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(9, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(9, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(9, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar10(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(10, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(10, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(10, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar11(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(11, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(11, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(11, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar12(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(12, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(12, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(12, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar13(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(13, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(13, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(13, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar14(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(14, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(14, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(14, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()


def downloadBar15(a, b, c):

    dd = a * b
    if dd > c:
        dd = c

    perc = dd / c
    percInStr = "%.2f%%" % (dd * 100 / c)
    for i in range(10):
        if perc > i / 10 and perc <= i + 1 / 10:
            stdscr.addstr(15, i + 1, '=')
    if perc > 0.9:
        stdscr.addstr(15, 10, '>')

    if c < MB:
        alldata = "%dKB" % (c / 1024)
    else:
        alldata = "%.2fMB" % (c / MB)
    if dd < MB:
        data = dd / 1024
        dataInStr = "%dKB" % data
    else:
        data = dd / MB
        dataInStr = "%.2fMB" % data

    stdscr.addstr(15, 12, percInStr + ' ' + dataInStr + '/' + alldata)
    stdscr.refresh()
