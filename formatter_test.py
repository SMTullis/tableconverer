import re

import formatter

def test():
    usda_no = re.compile(".*?USDA# (\d{4})")
    dod_no = re.compile(".*?AC-(\d{4})")
    state = re.compile(".*?for the [\w\s]+?, (\w+)")
    effective_date = re.compile(".*?Effective Date: (\w+)")

    grade = re.compile("^.+?(?:WS-)(\d{1,2})")
    pay_rates = re.compile("(?:\s+?\d{1,2})? ([\d\.]+)\s+?([\d\.]+)\s+?([\d\.]+)\s+?([\d\.]+)\s+?([\d\.]+)\s+?")

    form = formatter.TableFormatter(
        usda_no,
        dod_no,
        state,
        effective_date,
        grade,
        pay_rates
    )

    data = [
        "1 16.48 17.15 17.85 18.52 19.21  18.11 18.87 19.64 20.38 21.13  25.18 26.21 27.28 28.33 29.38 ",
        "  2 17.85 18.57 19.31 20.05 20.80  19.62 20.43 21.24 22.06 22.87  26.56 27.68 28.77 29.90 30.96 ",
        "                                                           WS-16  42.09 43.84 45.57 47.36 49.10 ",
        "                                                           WS-18  44.60 46.47 48.34 50.16 52.02 ",
        "October 1, 2015, subject to the limitations contained in CPM 2019-12, dated 28 March 2019. Rates      ",
        "          for the Las Vegas, Nevada  (LV) Wage Area",
        "AC-0285R                 Defense Civilian Personnel Advisory Service   USDA# 0285",
        "              Chief                                           Effective Date: 11 November 2018"
    ]

    for entry in data:
        print(form.MatchLine(entry))

test()
