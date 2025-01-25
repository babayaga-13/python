class Star_Cinema:
    hall_list = []
    
    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        for show in self.__show_list:
            if show[0] == id:
                print("Duplicate Show ID!!")
                return False
        self.__show_list.append((id, movie_name, time))
        seat_allocation = []
        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                row.append('F')
            seat_allocation.append(row)
        self.__seats[id] = seat_allocation
        return True

    def book_seats(self, id, positions):
        if id in self.__seats:
            n=0
            for row, col in positions:
                if not (0 <= row < self.__rows and 0 <= col < self.__cols):
                    print(f"Error: Seat ({row+1}, {col+1}) is out of range.")
                    continue
                if self.__seats[id][row][col] == 'B':
                    print(f"Error: Seat ({row+1}, {col+1}) is already booked.")
                    continue
                self.__seats[id][row][col] = 'B'
                n+=1
            print(f"{n} Seats successfully booked for Show ID '{id}'.")
        else:
            print("Invalid show ID!!!")

    def view_show_list(self):
        if not self.__show_list:
            print(f"No shows are currently running in Hall {self.__hall_no}.")
        else:
            print(f"Shows currently running in Hall {self.__hall_no}:")
            for id, movie_name, time in self.__show_list:
                print(f"  Movie Name: {movie_name}  ID: {id}  Starting Time: {time}\n")

    def view_available_seats(self, id):
        if id in self.__seats:
            print(f"Available seats for Show ID '{id}' in Hall {self.__hall_no}:\n")
            for i, row in enumerate(self.__seats[id]):
                row_display = "  ".join(row)
                print(f"Row {i+1}: {row_display}")
            print("\n'F' = Free, 'B' = Booked")
        else:
            print(f"Error: Invalid Show ID '{id}'.")


def main():
    hall = Hall(5, 5, 1010)
    while True:
        print("\n--------STAR CINEMA--------")
        print("1. Entry New Show")
        print("2. View Show List")
        print("3. View Available Seats")
        print("4. Book Seat")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_id = input("Enter Show ID: ")
            movie_name = input("Enter Movie Name: ")
            time = input("Enter Show Time: ")
            if hall.entry_show(show_id, movie_name, time):
                print(f"Show '{movie_name}' added successfully to Hall {hall._Hall__hall_no}.")
        elif choice == 2:
            hall.view_show_list()
        elif choice == 3:
            show_id = input("Enter Show ID: ")
            hall.view_available_seats(show_id)
        elif choice == 4:
            show_id = input("Enter Show ID: ")
            total = int(input("Number of tickets: "))
            positions = []
            for i in range(total):
                x, y = map(int, input(f"Enter seat position for ticket {i+1} (row col): ").split())
                x-=1
                y-=1
                positions.append((x, y))
            hall.book_seats(show_id, positions)
        elif choice == 5:
            print("Thank you for using STAR CINEMA!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
