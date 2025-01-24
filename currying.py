def curry(f):
    def year(year):
        def month(month):
            def day(day):
                return f(year, month, day)
            return day
        return month
    return year