import time
import pandas as pd


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # use a while loop to ensure that the selection is not empty
    while True:
        # use a while loop to ensure the right input for the variable city
        while True:
            city = input('Please enter a city name from: chicago, new york city or washington: ')
            # Transform the input to a string in lower format to ensure compatibility with correct data
            city = str(city).lower()
            # check if the input is one of the correct city then break the loop or display an error message
            if city in CITY_DATA.keys():
                break
            else:
                print('Error: you did not type a correct city name:\ninput:"{}"\n'.format(city))
        print('-' * 20)

        # get user input for month (all, january, february, ... , june)
        # use a while loop to ensure the right input for the variable month
        while True:
            month = input('Please enter a month or type "all" if you would like to get all months:\n')
            # Transform the input to a string in lower format to ensure compatibility with correct data
            month = str(month).lower()
            # Create a list of month names
            months = ('all', 'january', 'february', 'march', 'april', 'may', 'june',
                      'july', 'august', 'september', 'october', 'november', 'december')
            # check if the input is one of the correct month name then break the loop or display an error message
            if month in months:
                break
            else:
                print('Error: you did not type a correct month name:\ninput:"{}"\n'.format(month))
        print('-' * 20)

        # get user input for day of week (all, monday, tuesday, ... sunday)
        # use a while loop to ensure the right input for the variable day
        while True:
            day = input('please enter a day name or type "all" if you would like to get all days of the week:\n')
            # Transform the input to a string in lower format to ensure compatibility with correct data
            day = str(day).lower()
            # Create a list of days name
            week_days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
            # check if the input is one of the correct day name then break the loop or display an error message
            if day in week_days:
                break
            else:
                print('Error: you did not type a correct day name:\ninput:"{}"\n'.format(day))
        print('-' * 20)
            
        if load_data(city, month, day).empty:
            print('There is no data in the selection, please choose a valid data with valid month name or day name')
            print('input= city:', city, ' month: ', month, 'day: ', day)
            print('You are required to choose a new dataset\n')
            print('*' * 40)
            prompt = input("--Please type a key to continue--\n")
        else:
            break

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # read the related csv file
    df_ = pd.read_csv(CITY_DATA[city])

    # transform the 'Start Time' column to a datetime data
    df_['Start Time'] = pd.to_datetime(df_['Start Time'])
    # extract the month name from the 'Start Time' column then create the new column month
    df_['month'] = df_['Start Time'].dt.month_name()
    # extract the day name from the 'Start Time' column then create the new column day
    df_['day'] = df_['Start Time'].dt.day_name()

    # if filters are required on month or day
    # filter on input month
    if month != 'all':
        # put in format title the month and day as those columns are in that format
        month = month.title()
        df_ = df_[df_['month'] == month]
    # filter on input day-"if" is used as it is possible that both month and day condition are true at the same time
    if day != 'all':
        # put in format title the month and day as those columns are in that format
        day = day.title()
        df_ = df_[df_['day'] == day]

    return df_


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    prompt = input("")
    # Check the computation time of the time_stats function
    start_time = time.time()
    
    # display the most common month
    print("The most common month in the selected data is:", df['month'].mode()[0])

    # display the most common day of week
    print("The most common day of week in the selected data is:", df['day'].mode()[0])

    # display the most common start hour
    # for that purpose, an extract of the hour from start time is required first
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour in the selected data is:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)
    prompt = input("--Please type a key to continue--\n")


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    prompt = input("")
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station in the selected data is:", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The most commonly used end station in the selected data is:", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    # for that purpose, we need to concatenate the start and end station
    df['start and end station'] = df['Start Station'] + ' -> ' + df['End Station']
    print("The most frequent combination of start station and end station trip in the selected data is:",
          df['start and end station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)
    prompt = input("--Please type a key to continue--\n")


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    prompt = input("")
    start_time = time.time()

    # display total travel time
    print("The total travel time in the selected data is: {} days".format(round(df['Trip Duration'].sum()/86400, 2)))
    # display mean travel time
    print("The total travel time in the selected data is: {} minutes".format(round(df['Trip Duration'].mean()/60, 2)))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)
    prompt = input("--Please type a key to continue--\n")


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    prompt = input("")
    start_time = time.time()

    # Display counts of user types
    print("Printing the count for types...")
    print("-" * 50, '\n')
    print(pd.DataFrame(df['User Type'].value_counts()))
    print("-" * 10)
    prompt = input("--Please type a key to continue--\n")

    # Display counts of gender
    try:
        print("Printing the count for gender...")
        print("-" * 50, '\n')
        print(pd.DataFrame(df['Gender'].value_counts()))
    except KeyError:
        print("There's no Gender column in the selected dataset ")
    prompt = input("--Please type a key to continue--\n")

    # Display earliest, most recent, and most common year of birth
    try:
        print("Printing the statistics for year of birth...")
        print("-" * 50, '\n')
        print("The earliest year of birth is: {}".format(int(df['Birth Year'].min())))
        print("The most recent year of birth is: {}".format(int(df['Birth Year'].max())))
        print("The most common year of birth is: {}".format(int(df['Birth Year'].mode())))
    except KeyError:
        print("There's no Birth Year column in the selected dataset ")
    print("-" * 30, '\n')
    print("\nThis took %s seconds." % (time.time() - start_time))

    prompt = input("--Please type a key to continue--\n")

    print('-' * 40)


def display_raw_data(df):
    counter = 0
    while True:
        raw_data = input('\nWould you like to see 5 lines of raw data? yes or no\n')
        if raw_data.lower() == 'yes':
            display = df.iloc[counter:counter+5]
            if display.empty:
                print('\nEnd of file reached, no more data to display\n')
                prompt = input("--Please type a key to continue--\n")
                break
            else:
                print(display)
            counter += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
