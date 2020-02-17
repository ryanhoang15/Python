
# First I created a Member class and created a class attribute for the total members, books out and videos out
class Member:
    # Creating a counter for the total number of members.
    total_mem = 0
    # Creating a list for the books that are checked out.
    bks_out = []
    # Creating a list for the videos being checked out.
    videos_out = []

    # I created the constructor and assign the parameter name. Not only that but I also create a list to keep track of what
    # members have checked out and adding the member count up by 1 for each new member
    def __init__(self, name):
        self.name = name
        self.list_media_of_mem = []
        Member.total_mem += 1

    # With the checkout method, I pass through the item which in this case may be the book title, author, and publisher or
    # or the video name, runtime, and author.
    def checkout(self, item):
        # Checks the condition to make sure the member cant checkout more than two books.
        if len(self.list_media_of_mem) < 2:
            # Making sure that the book hasn't been checked out and see if the object is a book.
            if item.check_out is False and isinstance(item, Book):
                # This adds that book to the list of that member.
                self.list_media_of_mem.append(item)
                # This adds that book name to the list of books checked out.
                self.bks_out.append(item)
                # Book is now checked out and set to true to prevent someone else from checking it out.
                item.check_out = True
                # Keeping record of current owner that has that item.
                item.owner = self.name
                # It prints out a statement saying who is the person that just checked it out.
                print(self.name, "has checked out:", item, "\n")

            # Making sure that the video hasn't checked out and to see if the object is a video
            elif item.check_out is False and isinstance(item, Video):
                # This adds the video name to the list of that member
                self.list_media_of_mem.append(item)
                # This adds video's name to the list of books checked out.
                self.videos_out.append(item)
                # Set that item that has been checked to true to prevent someone else from checking it out.
                item.check_out = True
                # Keeping record of current owner to has that item.
                item.owner = self.name
                # It prints out a statement saying who is the person that just checked it out.
                print(self.name, "has checked out:", item, "\n")

            # This is the final case where the person might have less than two books checked out BUT there is another person who has
            # the same book/video checked out therefore the print statement prints  a message saying the item can not be checked out.
            else:
                print("Sorry", self.name + ",", item, "is not available, checked out by", item.owner, "\n")

        # The message that is printed in the case that the person already has the maximum two items borrowed
        else:
            print(self.name, "reached the maximum number (2) of borrowed items, so can't check out:", item, "\n")

    # With the checkin method, I pass through the item (the book or the video) but in this case it is trying to return
    # an item that was previously checked out.
    def checkin(self, item):
        # The first thing that is checked for is if the item is in the self.list_media_of_mem, which is a list that contains all
        # the items that are checked out from all the members. This is to make sure no one tries to return a book that was never
        # checked out in the first place.
        if item not in self.list_media_of_mem:
            print("Sorry Can't Check in an item that was not checked out at first \n")

        # Checks if the item is a book and if the item IS found within the list, then the item is successfully returned. For the item to be fully returned, we
        # remove that item from the list bks_out (list of books checked out) as well as self.list_media_of_mem (list of media
        # from all the members). We also set item.check_out to false, set the item.owner to an empty string, and print a message.
        elif isinstance(item, Book):
            self.list_media_of_mem.remove(item)
            self.bks_out.remove(item)
            item.check_out = False
            item.owner = " "
            print(self.name, "checked in: ", item, "\n")

        # This is essentially the same as the code above except this is in the case that the item is a video instead of a book.
        # The item is still removed from the self.list_media_of_mem but instead of the list of checked out books, it is removed
        # from the videos_out list.
        else:
            self.list_media_of_mem.remove(item)
            self.videos_out.remove(item)
            item.check_out = False
            item.owner = " "
            print(self.name, "checked in: ", item, "\n")

    # This method is for in case you want to print out all the items that a specific person has checked out.
    def printCheckedOutItems(self):
        # Printing the checked out items of each member using polymorphism.
        print("Items checked out by", self.name, "\n")
        for item in self.list_media_of_mem:
            print("\t", item, "\n")


# This is the superclass.
class Media:
    # Counter for keeping track of total number of books.
    total_bks = 0
    # Counter for keeping track of total number of videos.
    total_videos = 0

    # This constructor has the instance attribute of the basic details a piece of media (book or video) might have which
    # include the title, author, and publisher. Within the constructor we also have whether the media is checked out and
    # the name of the owner.
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.check_out = False
        self.owner = " "


#  This is the Book subclass for media that will inherit some of the attributes from its parent class Media.
class Book(Media):

    # For this constructor I use the super function in order to refer to the parent class. From media it will take instance attributes
    # of the title, author, publisher BUT I added a new one for this specific class of num_pages. I keep a counter of how many books
    # there are and the counter was made in the class attribute of the Media class for the total books.
    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)
        self._num_pages = num_pages
        # adds to the total book count.
        Media.total_bks += 1

    # Overriding print() method to print out this statement.
    def __repr__(self):
        return "Book--> " + self.title + " written by " + self.author


# There is another subclass for Media, Video which will once again inherit some of the attributes from its parent class Media
class Video(Media):

    # Once again I use the super function to inherit some instance attributes from the parent class Media BUT instead of
    # adding the number of pages like it did for the book it add the run time of the video. Also like the Book subclass
    # I keep a counter of how many videos there are with the counter that was made in the class attribute of the Media class for the total videos.
    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher)
        self._rum_time = str(run_time)
        # add to the total video count.
        Media.total_videos += 1

    # Overriding print() method to print out this statement.
    def __repr__(self):
        return "Video-->" + self._rum_time + " mins video " + self.title + " created by " + self.author


# And finally  the function of displayStats that will print out some of the information and I  made sure to keep
# track of like the number of books checked out, total number of members, the total number of books, total number of videos
# and total number of videos checked out.
def displayStats():
    # line separation.
    print("\n", "*" * 42, "\n")
    print("Record of Library:\n")
    print("Total number of Books = ", Media.total_bks, "\n")
    print("Numbers of books checked out = ", len(Member.bks_out), "\n")
    print("Total number of videos = ", Media.total_videos, "\n")
    print("Numbers of videos checked out = ", len(Member.videos_out), "\n")
    print("Total number of members = ", Member.total_mem)
    print("\n", "*" * 70, "\n")
    print("The following items are checked out of the library:\n ")
    # This loop is displaying checked out book and by which member.
    for book_left in Member.bks_out:
        print(book_left, "checked out by", book_left.owner, "\n")
    # This loop is displaying checked out videos and by which member.
    for vid_left in Member.videos_out:
        print(vid_left, "checked out by", vid_left.owner, "\n")


# book1 = Book("Python for Beginners", "Unknown", "CBS", "40")
# book2 = Book("Python for Kids", "Jason R. Briggs", "NBC", "23")
# video1 = Video("Tom and Jerry", "W.Hannah, J.Barbara", "PBS", "30")
# Joe = Member("Joe smith")
# Jim = Member("Jim Stuart")
# Joe.checkout(book1)
# Joe.checkout(book2)
# Joe.printCheckedOutItems()
# Joe.checkout(video1)
# Joe.checkin(book1)
# Jim.checkout(book2)
# Joe.checkin(book2)
# Jim.checkout(video1)
# Jim.checkout(book1)
# displayStats()
