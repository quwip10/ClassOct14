#!/usr/bin/python3
# Exercise 12-1
# Page 255

class Knight():
    def __init__(self, search_name):
        knight_list = []
        raw_knight = None

        with open("../DATA/knights.txt") as knight_file:
            for line in knight_file:
                knight_list.append(line.strip().split(":"))

        for i in knight_list:
            if i[0] == search_name:
                raw_knight = i

        if raw_knight:
            self.name = raw_knight[0]
            self.title = raw_knight[1]
            self.favorite_color = raw_knight[2]
            self.quest = raw_knight[3]
            self.comment = raw_knight[4]
        else:
            raise ValueError

    def __str__(self):
        return("Name: {} {}\n"
               "Favorite Color: {}\n"
               "Quest: {}\n"
               "Comment: {}".format(
                            self.title, self.name,
                            self.favorite_color,
                            self.quest,
                            self.comment
                             ))
