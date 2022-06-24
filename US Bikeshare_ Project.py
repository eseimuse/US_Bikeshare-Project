import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    
    city_list = ['chicago', 'new york city', 'washington']
    while True:
        city = input('What city do you wish to analyse, chicago, new york city or washington?\n').lower()
        if city in city_list:
            break
    else:
            print('Please enter a valid city')
        
        
    # get user input for month (all, january, february, ... , june)

    months_list = ['january', 'february', 'march', 'april', 'may', 'june']
    month_opted = input('Do you want to explore all or a specific month?\nEnter yes for all and anything else for specific month\n').lower()
    if month_opted == 'yes':
        month = 'all'
    else:
        while True:
            month = input('What month do you wish to analyse?\n').lower()
            if month in months_list:
                break
            else:
                print('Please enter a valid month')
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    day_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_opted= input('Do you want to explore all or a specific day?\nEnter yes for all and anything else for a specific day\n').lower()
    if day_opted == 'yes':
        day = 'all'
    else: 
        while True:
            day = input('What day of the week do you wish to analyse?\n').lower()
            if day in day_of_week:
                break
            else:
                print('Please enter a valid day of week')


    print('-'*40)
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
    #read csv file
    df = pd.read_csv(CITY_DATA[city])
    
    #create new columns for month, day of week and hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of week'] = df['Start Time'].dt.day_of_week
    df['Hour'] = df['Start Time'].dt.hour
    
    
    month_index = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
    if month != 'all':
        df = df.loc[df['month'] == month_index[month]]
    day_of_week_index = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}
    if day != 'all':
        df = df.loc[df['Day of week'] == day_of_week_index[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    highest_month = df['Month'].mode()
    print(highest_month)


    # display the most common day of week
    highest_Day_of_week = df['Day of week'].mode()
    print(highest_Day_of_week)

    # display the most common start hour
    highest_Hour = df['Hour'].mode()
    print(highest_Hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    highest_start_station = df['Start Station'].mode()
    print(highest_start_station)

    # display most commonly used end station
    highest_end_station = df['End Station'].mode()
    print(highest_end_station)

    # display most frequent combination of start station and end station trip
    df['Start-End'] = df['Start Station'] +" "+ df['End Station']                 
    highest_start_end = df['Start-End'].mode()
    print(highest_start_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print(Total_travel_time)

    # display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print(Mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    User_count = df['User Type'].value_counts()
    print(User_count)

    # Display counts of gender
    if  'Gender' in df.columns:
        Gender_count = df['Gender'].value_counts()
        print(Gender_count)
    else: 
        print('Gender statistics cannot be displayed as there is no data for gender')

    # Display earliest, most recent, and most common year of birth
    if  'Birth Year' in df.columns:
        Earliest_year_of_birth = df['Birth Year'].min()
        print('Earliest_year_of_birth') 
        Most_recent_year_of_birth = df['Birth Year'].max()
        print('Most_recent_year_of_birth')
        Most_common_year_of_birth = df['Birth Year'].mode()
        print(Most_common_year_of_birth)
    else:
        print('Birth year statistics cannot be displayed as there is no data for birth year')    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
   

def view_five_data(df):
    """Displays the first five rows of data and subsequent five rows of data."""
    
    view_data = input('Would you like to view the first five row of data?').lower()
    if view_data == 'yes':
            i = 0
            while 0 < 1:
                print(df.loc[i:i + 5])
                i+=5
                view_next = input('Do you want to view the next 5 rows?')
                if view_next != 'yes':
                    break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_five_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
